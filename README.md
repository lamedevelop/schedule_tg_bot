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


Drop dp and fill with test data:
```bash
python3 CliRunInterface.py --manager=Db --action=resetDb 
```


Install correct version of telebot
```bash
sudo python3 -m pip install PyTelegramBotAPI==2.2.3
```
