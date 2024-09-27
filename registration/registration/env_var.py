from dotenv import find_dotenv, load_dotenv

from .utils import required_env_var

load_dotenv(find_dotenv())



# DJANGO
SECRET_KEY = required_env_var("SECRET_KEY")

# DB
DB_NAME = required_env_var("DB_NAME_1")
DB_USERNAME = required_env_var("DB_USERNAME")
DB_PASSWORD = required_env_var("DB_PASSWORD")
DB_HOST = required_env_var("DB_HOST")
DB_PORT = required_env_var("DB_PORT")