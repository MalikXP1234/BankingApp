
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server

put_text("XP BANKING SYSTEM")






# This is the route section for the program
if __name__ == '__main__':
    routes = {
        "login": user_login,
        "signup": user_signup,
        "logout": user_logout,
        "home": home_page,
        "profile": profile_page,
        "product": product_page,
        "payment_page": payment_page,
        "password_reset": password_reset_page
    }
    start_server(routes, port=5000, debug=True)