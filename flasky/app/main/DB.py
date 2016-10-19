import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

app.secret_key = "my precious"

@app.route('/')
def home():
	return render_template('home.html')
@app.route('/Login')
	facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': 'email'}
)

@app.route('/Introduction')
def Introduction():
	return render_template('Introduction.html')
@app.route('/Administrator/')
def Administrator():
    return render_template('Adminlog.html')
    return render_template('Administrator.html')
@app.route('/loginAsAdmin')
def loginAsAdmin():
	return render_template('googlelogin.py', error = error)
 

@app.route('/addAsAdmin')
def addAsAdmin():
    return ("""<title>Additional information.</title><h1><p align="center">Adding Information.</p></h1><body><p>The administrator gives additional information about Panma; adding names and contacts of those who are doing the maintenance.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using POST.'
    else:
        return 'You are probably using GET.'


@app.route('/viewAsAdmin')
def viewAsAdmin():
    return ("""<title>Admin View.</title><h1><p align="center">Administrator View.</p></h1><body><p>The administrator is able to view all the progress at Panma therefore supervising and controlling all that happens.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using POST.'
    else:
        return 'You are probably using GET.'


@app.route('/updateAsAdmin')
def updateAsAdmin():
    return ("""<title>Admin Update.</title><h1><p align="center">Administrator Updating.</p></h1><body><p>The Admin updates Panma by rejecting, approving and adding comments to maintenance records.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using POST.'
    else:
        return 'You are probably using GET.'

@app.route('/logoutAsAdmin')
def logoutAsAdmin():
	session.pop('logged_in', None)
	flash('You were just logged out')
	return redirect(url_for('Introduction'))

@app.route('/loginAsStaff')
def loginAsStaff():
    return ("""<title>Staff Login.</title><h1><p align="center">Staff Log In.</p></h1><body><p>User logs in as a staff member.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using POST.'
    else:
        return 'You are probably using GET.'
    return ("""<form>Staff Name:<br><input type="text" name="Username"><br>Staff Password:<br><input type="password" name="Password"><br><input type="submit"></form>""")

@app.route('/viewAsStaff')
def viewAsStaff():
    return ("""<title>Staff info.</title><h1><p align="center">Staff Information.</p></h1><body><p>Staff can view their progress and pending, started or completed tasks.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using POST.'
    else:
        return 'You are probably using GET.'


@app.route('/updateAsStaff')
def updateAsStaff():
    return ("""<title>Staff Update.</title><h1><p align="center">Staff Update Information.</p></h1><body><p>The Staff can update whether or not they have completed a certain task.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using POST.'
    else:
        return 'You are probably using GET.'

@app.route('/logoutAsStaff')
def logoutAsStaff():
    return ("""<title>Staff Logout.</title><h1><p align="center">Staff Log Out.</p></h1><body><p>The Staff can log out as staff and leave.</p></body></html>""")
    return 'You are probably using %s' % request.method
    if request.method == 'POST':
        return 'You are using post'
    else:
        return 'You are probably using GET'




if __name__ == "__main__":
    app.run(debug=True)




