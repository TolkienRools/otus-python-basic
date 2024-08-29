import os

DB_URL = os.environ.get('DATABASE_URI', 'sqlite:///test.db')
# "postgresql+psycopg://user:password@localhost:5432/time_management"
DB_ECHO = False