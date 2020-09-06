# Schedule telegram bot

Telegram bot for delivering university schedule to students


### Contents

- [Start the bot](#start-the-bot)
- [Useful commands](#useful-commands)
- [Installation](#installation)
- [About us](#about-us)


## Start the bot


Start bot from CLI:
```bash
python3 Bot.py
```

[Up](#schedule-telegram-bot)


## Useful commands


For managing db in manual control you can go 2 ways:



Create db file:
```bash
python3 RunManager.py --manager=Db --action=upAllMigrations
```


Drop db file:
```bash
python3 RunManager.py -—manager=Db —-action=dropDb
```


Drop dp and fill with test data:
```bash
python3 RunManager.py --manager=Db --action=resetDb 
```

[Up](#schedule-telegram-bot)


## Installation


Install correct version of telebot
```bash
sudo python3 -m pip install PyTelegramBotAPI==2.2.3
```


telebot startup manual:

```bash
telebot/__init__.py:816 
    rename all dacorators from @util.async to @util.async_dec for example
telebot/util.py:141 
    rename function from async() to async_dec()
```

[Up](#schedule-telegram-bot)


## About us

- Telegram - [@grit4in](https://t.me/grit4in) and [@kekmarakek](https://t.me/kekmarakek)
- Website - [Oleg Gritchin](https://oleg.gritchin.ru) [Lamedev](https://lamedev.ru)

[Up](#schedule-telegram-bot)
