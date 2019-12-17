from flask import Flask
From .config import DevConfig

# Initializing application
app = Flask(__name__)

from app import views