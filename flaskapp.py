from flask import Flask
from jira import JIRA
app = Flask(__name__)

options = {
    'server': 'http://104.198.10.59/'}
jira = JIRA(options)


@app.route('/')
def hello_world():
  return projects = jira.projects()

@app.route('/countme/<input_str>')
def count_me(input_str):
  middle_str = "you have entered this '" + input_str +"' in URL"
  return middle_str


@app.route('/auth/<input_str>')
def auth(input_str):
  middle_str = "you have entered this '" + input_str +"' in URL"
  return middle_str

@app.route('/basicauth/<username>/<password>')
def basic_auth(username,password):
  authed_jira = JIRA(basic_auth=('vishalkumar2', '$Jira1353'))
  return middle_str

@app.route('/hardlogin')
def hard_auth():
  authed_jira = JIRA(basic_auth=('vishalkumar2', '$Jira1353'))
  return middle_str


if __name__ == '__main__':
  app.run()
