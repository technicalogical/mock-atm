# mock-atm
This is a mockup of an atm login screen for a coding project at work.  It is a bit of a mess, was supposed to include both a frontend and backend framework.  I failed in my attempts to bring my Python Flask authentication together with my React frontend.

Requirements: python3, pip, pipenv

Clone the files, and open in your editor and also a terminal window.  In terminal we will start our virtual environment with:

$ pipenv shell

Then we need to export our app name:

$ export FLASK_APP=project
$ export FLASK_DEBUG=1

Now run the flask with the following command:

$ flask run

If you have issues at this point, you will need to run:

$ pipenv install flask flask_sqlalchemy flask_login

Then run $ flask run

You should be able to navigate to http://localhost:5000 to access the app.  It is missing the coloring on the balance, and I was hell-bent on getting authentication to work, but I couldn't figure out how to authenticate with only a password.


Use the account number in both fields.

List of accounts:
23416
82352
65275
31038

There is a working version of React in there, but it's pretty much just create-react-app basics.
