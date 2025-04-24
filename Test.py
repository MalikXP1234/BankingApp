import random
from itertools import count

from pywebio.input import *
from pywebio.output import *
from pywebio import start_server, config

def logged_in():
    clear()
    put_html("<h1>logged_in</h1>")


def user_signup():
    clear()
    put_html("<h1>Sign Up</h1>")

    put_html("<h3>When doing your Signing up, Make sure to use no spaces when inputting your name. </h3>").style("text-align:center;")

    put_html("<h3>please use (- or _ ) instead of spaces  </h3>").style("text-align:center;")



    signup_data = input_group('Add user', [
        input('Full Name', type=TEXT, name='FullName', required=True),
        input('username', type=TEXT, name='username', required=True),
        input('Date of birth', type=DATE, name='DOF', required=True),
        input('email address', type=TEXT, name='email_address', required=True),
        input('phone number', type=NUMBER, name='phone_number', required=True),
        input('password', type=TEXT, name='password', required=True),
        actions('', [
            {'label': 'Save', 'value': 'save'},
        ], name='action', help_text='actions'),
    ])




if __name__ == '__main__':
    routes = {
        "signup": user_signup,
    }
    start_server(routes, port=5000, debug=True)