### Install
```console
$ git clone https://github.com/sohje/__flask_psgr.git
```

### Production env -> postgresql://localhost/testing
```console
$ export APP_SETTINGS='config.ProductionConfig'
$ python app.py
```

### Dev env -> sqlite://testing.db
```console
$ export APP_SETTINGS='config.DevelopmentConfig'
$ python app.py
```

### unittest
```console
$ python test.py
```
