### Install
```console
$ git clone https://sohje@bitbucket.org/sohje/__flask_psg.git
```

### Production env -> postgresql://localhost/testing
```console
$ export APP_SETTINGS='config.ProductionConfig'
$ python app.py
```

### Dev env -> sqlite://testing.db
```console
$ export APP_SETTINGS='config.ProductionConfig'
$ python app.py
```

### unittest
```console
$ python test.py
```
