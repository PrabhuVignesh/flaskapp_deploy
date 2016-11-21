from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/countme/<input_str>')
def count_me(input_str):
  middle_str = "you have entered this '" + input_str +"' in URL"
  return middle_str


@app.route('/jql/<input_str>')
def count_me(input_str):
  jira = JIRA("http://jahsdsjdhf/jsbdj?jql=" +input_str+)
  middle_str = "you have entered this '" + input_str +"' in URL"
  return jira

if __name__ == '__main__':
  app.run()
