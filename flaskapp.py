from flask import Flask
from jira import JIRA
import requests
app = Flask(__name__)

@app.route('/testme')
def get_auth():
	jira_session = requests.session()

	try:
		jira_session.post('https://104.198.10.59', auth=("prabhukumar", "Apple@123"), verify=False)
	except:
		print('Unable to connect or authenticate with JIRA server.')
	print("i am in......")
	url = 'https://104.198.10.59/rest/api/2/search?jql=project=SLBAG'
	results = jira_session.get(url)
	project_data = results.json()
	return project_data

@app.route('/')
def hello_world():
  projects = "jira.projects()"
  return projects

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
