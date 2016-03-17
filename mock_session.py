import random
def session_info_retriever(data):
    mock_session_info = {
        'data': {
            'session_exists': False,
            'session_data': {}
        },
        'metadata': {}
    }
    if data:
        mock_session_info['data']['session_exists'] = True
        mock_session_info['data']['session_data']['session_id'] = data
        mock_session_info['data']['session_data']['user_id'] = data

    return mock_session_info
