# Logs configuration
```
в файле .env напишем
debug=true
в сеттингсах напишем
debug: bool = False
в ранере пишем
logging.basicConfig(level=logging.DEBUG if app_settings.debug else logging.INFO)
```

# about telegram bot
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


### Check [production logs online](http://canyon.esemi.ru/)