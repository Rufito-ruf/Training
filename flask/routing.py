from flask import Flask
app = Flask(__name__)

@app.route('/home')
def home():
  return 'Welcome!'

@app.route('/home/<username>')
def home_username(username):
  return 'Welcome, ' + username + '!'

@app.route('/home/<username>/<int:salary>')
def home_salary(username, salary):
  return "You are " + username + " and your salary is " + str(salary) + "."

if __name__ == '__main__':
  app.run()

