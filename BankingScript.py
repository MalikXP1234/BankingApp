
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server, config

email_list = []

navbar = """<div class="fixed-bottom">
   <nav class="navbar-dark bg-dark">

        <div class="container-fluid">

                <ul class="nav justify-content-center">
                    <li class="">

                    </li>
                    <li class="">
                        <a href="?app=home" class="nav-link">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-house-door" viewBox="0 0 16 16">
  <path d="M8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4.5a.5.5 0 0 0 .5-.5v-4h2v4a.5.5 0 0 0 .5.5H14a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293zM2.5 14V7.707l5.5-5.5 5.5 5.5V14H10v-4a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v4z"/>
</svg>
                            Home</a>
                    </li>
                    <li class="">
                        <a href="?app=profile" class="nav-link">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-fill" viewBox="0 0 16 16">
  <path d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
</svg>
                            Profile</a>
                    </li>
                    <li class="">
                        <a href="?app=payment_page" class="nav-link">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-bank" viewBox="0 0 16 16">
  <path d="m8 0 6.61 3h.89a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.5.5H15v7a.5.5 0 0 1 .485.38l.5 2a.498.498 0 0 1-.485.62H.5a.498.498 0 0 1-.485-.62l.5-2A.5.5 0 0 1 1 13V6H.5a.5.5 0 0 1-.5-.5v-2A.5.5 0 0 1 .5 3h.89zM3.777 3h8.447L8 1zM2 6v7h1V6zm2 0v7h2.5V6zm3.5 0v7h1V6zm2 0v7H12V6zM13 6v7h1V6zm2-1V4H1v1zm-.39 9H1.39l-.25 1h13.72z"/>
</svg>
                            Payment</a>
                    </li>
                    <li class="">
                        <a href="?app=product" class="nav-link">
                              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-boxes" viewBox="0 0 16 16">
  <path d="M7.752.066a.5.5 0 0 1 .496 0l3.75 2.143a.5.5 0 0 1 .252.434v3.995l3.498 2A.5.5 0 0 1 16 9.07v4.286a.5.5 0 0 1-.252.434l-3.75 2.143a.5.5 0 0 1-.496 0l-3.502-2-3.502 2.001a.5.5 0 0 1-.496 0l-3.75-2.143A.5.5 0 0 1 0 13.357V9.071a.5.5 0 0 1 .252-.434L3.75 6.638V2.643a.5.5 0 0 1 .252-.434zM4.25 7.504 1.508 9.071l2.742 1.567 2.742-1.567zM7.5 9.933l-2.75 1.571v3.134l2.75-1.571zm1 3.134 2.75 1.571v-3.134L8.5 9.933zm.508-3.996 2.742 1.567 2.742-1.567-2.742-1.567zm2.242-2.433V3.504L8.5 5.076V8.21zM7.5 8.21V5.076L4.75 3.504v3.134zM5.258 2.643 8 4.21l2.742-1.567L8 1.076zM15 9.933l-2.75 1.571v3.134L15 13.067zM3.75 14.638v-3.134L1 9.933v3.134z"/>
</svg>
                            Product</a>
                    </li>
                </ul>

        </div>

    </nav>
  </div>"""

card = """<div class="py-3 text-center container ">
<div class="card mx-auto" style="width: 25rem;">
  <div class="card-body">
    <h5 class="card-title">[ACCOUNT NAME]</h5>
     <ul class="list-group list-group-flush">
    <li class="list-group-item">Account Number: [NUMBER]</li>
    <li class="list-group-item"> Account Code: [CODE]</li>
    <li class="list-group-item">Balance: [BALANCE]</li>
  </ul>
  </div>
  <a href="#" class="btn btn-primary">Select this Account</a>
</div>
</div>
"""

# This is the back button that allows you to take the user into different pages
def back_button(link):
    put_html(f"""<a href={link} class="btn btn-primary">Back</a>""")

# This is the login where the user can log their account with their data from the file
def user_login():
    clear()
    put_html("<h1>Login</h1>")

    put_buttons(["ResetPassword", "Register"], onclick=[password_reset_page, user_signup]).style("text-align:center;")

    data = input_group("", [
        input("Enter username: ", name="name", required=True),
        input("Enter password: ", name="password", required=True, type=PASSWORD)], cancelable=True)

    if len(data["password"]) > 5 > 10:
        username = data["name"]
        password = data["password"]

        toast(f"Welcome {username} and your password is {password}")
        home_page()
    else:
        toast("sorry your password should be bigger than 5 but smaller than 8")

# This is where the user can sign up and add their data onto the database
def user_signup():
    clear()
    back_button("?app=login")
    put_html("<h1>Sign Up</h1>")

    signup_data = input_group('Add user', [
        input('username', type=TEXT, name='username', required=True),
        input('password', type=PASSWORD, name='password', required=True),
        actions('', [
            {'label': 'Save', 'value': 'save'},
            {'label': 'Save and add next', 'value': 'save_and_continue'},
        ], name='action', help_text='actions'),
    ])

    # this would then be used to input into a text file. After that it will create the class item here of the object then put that in the code on the text file, then it would read and put it in the class

    put_code(signup_data)

# This is when the user can log out if they want to
def user_logout():
    clear()
    put_html("<h1>Logout</h1>")

# This is where the user can select accounts and create them for data
@config(theme="dark")
def home_page():
    clear()

    back_button("?app=product")
    put_html(navbar)
    put_html("<h1>Home Page</h1>")

    put_html("""<div class="card">
        <div class="card-body">
            <div class="d-grid gap-2">
                <a href="" class="btn btn-warning">Live chat</a>
            </div>
        </div>
    </div>""")

    i = 5

    for i in range(5):
        put_html(card)

# This is the profile page which will output the users infomation and will have function to change
@config(theme="dark")
def profile_page():
    clear()
    back_button("?app=home")
    put_html(navbar)
    put_html("<h1>Profile</h1>")

    put_html(""" <div class="container mt-5">

    <div class="form-floating">

        <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" value="Even Micheal Jr">
        <label for="floatingInput">Name</label>
    </div>
    <!-- this input is invalid -->
    <div class="form-floating">
        <input type="date" class="form-control is-invalid" id="floatingDOB">
        <label for="floatingDOB">Data of birth</label>
    </div>
    <div class="form-floating">
        <input type="text" class="form-control" id="floatingAddress" placeholder="Password" value="NE4TQE">
        <label for="floatingAddress">Address</label>
    </div>
    <div class="form-floating">
        <input type="Text" class="form-control is-invalid" id="floatingStreet" placeholder="Password" value="">
        <label for="floatingStreet">Street</label>
    </div>
    <div class="form-floating">
        <input type="text" class="form-control" id="floatingCountry" placeholder="Password" value="United Kingdom">
        <label for="floatingCountry">Country</label>
    </div>
    <div class="form-floating">
        <input type="email" class="form-control" id="floatingEmail" placeholder="Password" value="Evens12@gmail.com">
        <label for="floatingEmail">Email Address</label>
    </div>
    <div class="form-floating">
        <input type="number" class="form-control" id="floatingNumber" placeholder="Password" value="07973433245">
        <label for="floatingNumber">Mobile Number</label>
    </div>

</div>
""")

# This is the product page where the user can select loans for their account depending on their needs
@config(theme="dark")
def product_page():
    clear()
    back_button("?app=payment_page")
    put_html(navbar)
    put_html("<h1>Product Page</h1>")

    i = 5

    for i in range(5):
        put_html("""<div class="py-3 text-center container ">
<div class="card mx-auto" style="width: 25rem;">
  <div class="card-body">
    <h5 class="card-title">[LOAN NAME]</h5>
  </ul>
  </div>
  <a href="#" class="btn btn-primary">Select this LOAN/a>
</div>
</div>""")

# This is their payment method where the user can select different payee for user to give money
@config(theme="dark")
def payment_page():
    clear()

    back_button("?app=profile")

    put_html(navbar)

    put_html("<h1>Payment Page</h1>")
    put_html("<h2>Select Payee</h2>")

    i = 5

    for i in range(5):
        put_html("""<div class="card">
      <div class="card-body">
         <h5 class="card-title">[PAYEE NAME]</h5>
         <ul class="list-group list-group-flush">
        <li class="list-group-item">[PAYEE EMAIL]</li>
        <li class="list-group-item">[PAYEE NUMBER]</li>
      </ul>
      </div>
       <a href="#" class="btn btn-primary">Select this Payee</a>
    </div>""")

    # another action input to ask user to input like account or pin or anything like that or create an custom pin or account number from class

# This is the page where the user can reset their password by giving their emails
@config(theme="dark")
def password_reset_page():
    clear()
    back_button("?app=login")
    put_html("<h1>Password Reset Page</h1>")

    old_email = input("Please enter your old email address so we can reset ur password:")

    for email in email_list:
        if email == old_email:
            put_text("I am happy to say that we have found your email address and gave your new code")

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