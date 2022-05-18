# canyon-notifier
---

### Pre-requirements
- [redis server up and running](https://redis.io/docs/getting-started/installation/)
- [python 3.9+](https://www.python.org/downloads/)

### Local setup
```shell
$ git clone git@github.com:Eira/canyon-notifier.git
$ cd canyon-notifier
$ python3.9 -m venv venv
$ source venv/bin/activate
$ pip install -U poetry pip setuptools
$ poetry install
```

Create env file to override default config
```bash
cat > .env << EOF
redis_dsn=redis://user:pass@localhost:6379/1
EOF
```
# Logs configuration
```
в файле .env напишем
debug=true
в сеттингсах напишем
debug: bool = False
в ранере пишем
logging.basicConfig(level=logging.DEBUG if app_settings.debug else logging.INFO)
```


### Local run tests
```shell
$  poetry run pytest
```

### local run app
```
python -m app.update 
```

### lokal run flake
```
poetry run flake8 app/

```