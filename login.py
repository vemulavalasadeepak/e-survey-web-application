from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Mock user data for demonstration purposes
users = {'username': 'password', 'testuser': 'testpassword'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login, redirect to a success page
        return redirect(url_for('success', username=username))
    else:
        # Failed login, redirect back to the login page
        return redirect(url_for('index'))

@app.route('/success/<username>')
def success(username):
    return f'Welcome, {username}!'

if __name__ == '__main__':
    app.run(debug=True)
