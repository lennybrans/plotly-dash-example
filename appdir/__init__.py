import os
# session and request can be used to determine the user
from flask import Flask, session, request
from dash import Dash
from dash_auth import BasicAuth
from dotenv import load_dotenv

from . import layout
from . import callbacks

load_dotenv()

server = Flask(__name__)
server.secret_key = os.getenv('SECRET_KEY')

app = Dash(__name__, server=server)
auth = BasicAuth(app)

app.layout = layout.layout
