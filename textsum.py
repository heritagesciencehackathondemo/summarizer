import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim.summarization import keywords
from flask import Flask
app = Flask(__name__)

@app.route('/<text>')
def hello_world(text):
    return keywords(text)
