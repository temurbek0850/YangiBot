from dotenv import load_dotenv
import os
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_FILE = os.getenv("DB_FILE")
BOT_ADMIN_FROM_ID = os.getenv("BOT_ADMIN_FROM_ID")