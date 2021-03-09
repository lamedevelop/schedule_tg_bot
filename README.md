# Schedule telegram bot

Telegram bot for delivering university schedule to students


<a href="https://github.com/badges/shields/graphs/contributors" alt="Contributors">
        <img src="https://img.shields.io/badge/python-v3-green" /></a>

### Contents

- [Start the bot](#start-the-bot)
    - [Quickstart](#quickstart)
    - [Docker](#docker-deploy)
    - [Cmd](#cmd)
- [Useful commands](#useful-commands)
- [Installation](#installation)
- [About us](#about-us)


## Startup guide

### Docker deploy

```bash
# Full project
docker-compose up -d --build

# Only app service
docker-compose run -d --service-ports app

# Only database service
docker-compose run -d --service-ports mariadb
```

Running db separately from app is useful for testing. 
You can run bot locally from cli, change it and then 
simply reload without container rebuilding.

Command to run bot from cli:
```bash
python3 Bot.py
```

### Manual deploy

##### Step 1 - Install requirements
Install requirements from file
```bash
sudo python3 -m pip install -r Requirements.txt
```

##### Step 2 - Fix config
Firstly manually edit Configs/tgConfig.py. You need to fill it with your bot token and server ip (port already specified but you also can personalize it for your case).

Also you can provide your monitoring bot token and chat id (destination where you want to receive monitoring notifications). As chat id you can write your telegram id or your custom chat id (standard group chat).

##### Step 3 - Configure db and get certificates for webhooks

Just run Scripts/quickstart.sh.
```bash
chmod +x ./Scripts/quickstart.sh
./Script/quickstart.sh
``` 
Important thing is that when you will be asked to enter "Common Name" - enter your server ip.

##### Step 4 - Run daemon

Copy schedulebot.service to the /etc/systemd/system for bot demonisation and then run commands to run the bot.
```bash
# Copy daemon file
cp Scripts/schedulebot.service /etc/systemd/system/

# Add new daemon
systemctl daemon-reload
enable schedulebot
systemctl start schedulebot

# Check status of daemon
systemctl status schedulebot.service
```

[Up](#schedule-telegram-bot)


## Useful commands

Use RunManager.py and run methods of any manager manually.

Here are some commands for manual calling DbManager functions.

Db interactions:

```bash
# Set all migrations to up state 
python3 RunManager.py --manager=Db --action=upAllMigrations

# Set all migrations to down state 
python3 RunManager.py --manager=Db --action=downAllMigrations

# Drop db
python3 RunManager.py -—manager=Db —-action=dropDb

# Drop dp, create new one and fill with test data
python3 RunManager.py --manager=Db --action=resetDb 
```


Command to run db_interact.py script. You can change action of the script 
inside of it's main function in the db_interact.py file.
```bash
python3 RunManager.py --script=db_interact
```

Crons running:

```bash
# Install crons from config (also updates already existing crons)
python3 RunManager.py --manager=Cron --action=install

# Disable all crons
python3 RunManager.py --manager=Cron --action=disable

# Enable all crons
python3 RunManager.py --manager=Cron --action=enable

# Removes crontab (delete all crons)
python3 RunManager.py --manager=Cron --action=erase
```

[Up](#schedule-telegram-bot)


## About us

- Telegram - [@grit4in](https://t.me/grit4in) and [@kekmarakek](https://t.me/kekmarakek)
- Website - [Oleg Gritchin](https://oleg.gritchin.ru) [Lamedev](https://lamedev.ru)

[Up](#schedule-telegram-bot)