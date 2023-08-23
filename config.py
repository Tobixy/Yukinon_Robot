from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

BOT_TOKEN = environ.get("BOT_TOKEN")
API_ID = int(environ.get("API_ID"))
API_HASH = environ.get("API_HASH")
SUDO_USERS_ID = environ.get("SUDO_USERS_ID")
LOG_GROUP_ID = environ.get("LOG_GROUP_ID")
MONGO_URL = environ.get("mongodb+srv://Shivam10:rLh2OeAtAbtn2L1B@cluster0.m7nxa0j.mongodb.net/?retryWrites=true&w=majority")
BASE_DB = MONGO_URL
ARQ_API_URL = environ.get("ARQ_API_URL")
ARQ_API_KEY = environ.get("ARQ_API_KEY")
F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")
OWNER_ID = int(environ.get("OWNER_ID", "5715764478"))
