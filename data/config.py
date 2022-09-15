# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")
adm = config["settings"]["admin_id"]
if "," in adm:
    adm = adm.split(",")
else:
    if len(adm) >= 1:
        adm = [adm]
    else:
        adm = []
        print("***** Вы не указали админ ID *****")

bot_version = "2.9"
bot_description = f"<b>♻ Bot создал @satanasat</b>\n" \
                  f"<b>⚜ Bot Version:</b> <code>{bot_version}</code>\n" \
                  f"<b>🔗 Support:</b> <a href='https://github.com/Cicadadenis/'><b>Click me</b></a>"
