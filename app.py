import os

from sqlalchemy import (create_engine, MetaData,
    Table, Column, Integer, Text, String, DateTime)
from flask import Flask, request, jsonify, g

from mock_session import session_info_retriever
app = Flask(__name__)

# config.DevelopmentConfig -> sqlite://testing.db
# config.ProductionConfig -> postgresql://localhost/testing
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

engine = create_engine(app.config['DATABASE_URI'], convert_unicode=True)
metadata = MetaData(bind=engine)
users = Table('users', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', Text),
    Column('sex', Text),
    Column('birthday', DateTime),
    Column('city', Text),
    Column('country', Text),
    Column('ethnicity', Text)
)

error_sess_obj = {'status': 'error', 'Message': 'Invalid session'}
error_data_obj = {'status': 'error', 'Message': 'Invalid data'}

def init_db():
    from mock_users import users_list

    db = get_db()
    db.execute('DROP TABLE IF EXISTS users;')
    metadata.create_all()
    db.execute(users.insert(), users_list)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = engine.connect()
    return db

@app.before_request
def before_request():
    g.db = get_db()

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# initialize db
@app.before_first_request
def init_me():
    init_db()

# retrieve user profile
@app.route('/api/v1/profiles/<user_id>', methods=['GET'])
def return_profile(user_id):
    # validate user session
    session = request.cookies.get('session') or request.args.get('session')
    session_info = session_info_retriever(session)
    if session_info['data']['session_exists'] == False: # check session
        return jsonify(error_sess_obj)

    st = users.select().where(users.c.user_id == user_id)
    result = g.db.execute(st).fetchone()
    return jsonify(result) if result is not None else jsonify({})

# update profile
@app.route('/api/v1/profiles/self', methods=['PUT', 'PATCH'])
def change_profile():
    session = request.cookies.get('session') or request.args.get('session')
    session_info = session_info_retriever(session)
    data = request.get_json()
    if session_info['data']['session_exists'] == False: # check session
        return jsonify(error_sess_obj)
    elif not data:
        return jsonify(error_data_obj)

    user_id = session_info['data']['session_data']['user_id']
    # todo: validate json body before exec
    # todo: patch/put (update/modify entries)
    st = users.update().where(users.c.user_id == user_id).values(request.get_json())
    try:
        g.db.execute(st)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e), 'data': request.get_json()})
    return jsonify({'status': 'OK'})

if __name__ == '__main__':
    app.run()
