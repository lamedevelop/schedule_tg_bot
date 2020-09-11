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

* Use RunManager.py and run methods of DbManager manually
* Use RunManager.py with db_interact.py script

Here are some commands for manual calling DbManager functions.

Db interactions:

```bash
# Create db file
python3 RunManager.py --manager=Db --action=upAllMigrations

# Drop db file
python3 RunManager.py -—manager=Db —-action=dropDb

Drop dp and fill with test data
python3 RunManager.py --manager=Db --action=resetDb 
```


Here is single command to run db_interact.py script. You can change action of the script insine of it's main function in the db_interact.py file.
```bash
python3 RunManager.py --script=db_interact
```


Cron running:

```bash
# Install crons from config (also updates already existing crons)
python3 RunManager.py --manager=Cron --action=installCrons

# Disable all crons
python3 RunManager.py --manager=Cron --action=disableCrontab

# Enable all crons
python3 RunManager.py --manager=Cron --action=enableCrontab

# Removes crontab (delete all crons)
python3 RunManager.py --manager=Cron --action=removeCrontab
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
