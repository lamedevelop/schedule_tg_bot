# schedule_tg_bot
Telegram bot for delivering university schedule to students

# Useful commands

Start bot from CLI:
```bash
python3 Bot.py
```


Create db file:
```bash
python3 CliRunInterface.py --manager=Db --action=upAllMigrations
```


Drop db file:
```bash
python3 CliRunInterface.py -—manager=Db —-action=dropDb
```


Drop dp and fill with test data:
```bash
python3 CliRunInterface.py --manager=Db --action=resetDb 
```


Install correct version of telebot
```bash
sudo python3 -m pip install PyTelegramBotAPI==2.2.3
```


telebot startup manual:

```
telebot/__init__.py:816 rename all dacorators from @util.async to @util.async_dec for example
and in telebot/util.py:141 rename function from async() to async_dec()
```
