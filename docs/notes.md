# Logs configuration
```
в файле .env напишем
debug=true
в сеттингсах напишем
debug: bool = False
в ранере пишем
logging.basicConfig(level=logging.DEBUG if app_settings.debug else logging.INFO)
```