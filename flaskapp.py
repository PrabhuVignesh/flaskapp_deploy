from flask import Flask
from jira import JIRA
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/countme/<input_str>')
def count_me(input_str):
  middle_str = "you have entered this '" + input_str +"' in URL"
  return middle_str


@app.route('/auth')
def auth(input_str):
  middle_str = "you have entered this '" + input_str +"' in URL"
  return middle_str

@app.route('/basicauth')
def basic_auth(input_str):
  authed_jira = JIRA(basic_auth=('vishalkumar2', '$Jira1353'))
  return middle_str



if __name__ == '__main__':
  app.run()
