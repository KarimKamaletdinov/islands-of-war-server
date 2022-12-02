from app import app
from os import environ
from db import init, execute


init(dict(environ))
execute('CREATE TABLE test (id INTEGER, name VARCHAR)')
app.run()
