import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 3063880))
    API_HASH = os.environ.get("API_HASH", "e0f71a9affe6526b56ab254c0bea9b1b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6093948774:AAFD1194xZaIWH-AT6CY6T2tK30yodz9axs")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Captcha-Bot")
    GROUP_CHAT_ID = int(os.environ.get("GROUP_CHAT_ID", -1001665155031))
