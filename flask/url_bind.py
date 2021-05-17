from flask import *

app = Flask(__name__)

@app.route('/root')
def root():
  return "You are the root!"

@app.route('/guest')
def guest():
  return "You are the guest!"

@app.route('/super')
def super():
  return "You are super!"

@app.route('/')
def main():
  return "You are on the main page, try going to /root or /users/guest."

@app.route('/users/<user>')
def redirect_to(user):
  if user == 'guest':
    return redirect(url_for('guest'))
  if user == 'super':
    return redirect(url_for('super'))
  if user == 'root':
    return redirect(url_for('root'))

if __name__ == '__main__':
  app.run()
