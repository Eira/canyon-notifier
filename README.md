# canyon-notifier
---
[![tests](https://github.com/Eira/canyon-notifier/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/Eira/canyon-notifier/actions/workflows/tests.yml)


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
$ poetry config virtualenvs.create false --local
$ poetry install
```

Create env file to override default config
```bash
cat > .env << EOF
throttling_time=10.0
debug=true
redis_dsn= redis://localhost:6379/1
amount_of_iterations=2
bot_token=5435048925:AAE0CdbhQL7baW-EZmtVZ0nbyNbEtCQWUcE
EOF
```

### Local run tests
```shell
$ pytest --cov=app
```

### Local run app
```
python -m app.catalog_updater
```

### Local run flake
```
poetry run flake8 app/
```
### Local run MyPy
```
poetry run mypy app/
```

### Telegram test bot name
```
CanyonNotifierTest
```

### Telegram test bot username
```
CanyonNotifierTestBot
```
### Telegram test bot token to access the HTTP API
```
5435048925:AAE0CdbhQL7baW-EZmtVZ0nbyNbEtCQWUcE
```
### Local run Telegram bot
```
python -m app.bot
```


### Check [production logs online](http://canyon.esemi.ru/)

```
Done! Congratulations on your new bot. You will find it at t.me/CanyonNotifierTestBot.
You can now add a description, about section and profile picture for your bot, see /help for a list of commands.
By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it.
Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:
5435048925:AAE0CdbhQL7baW-EZmtVZ0nbyNbEtCQWUcE
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```
