import random
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server, config
from unicodedata import decimal


# Contains all the User Accounts
AccountList = []

# Contains all the Names of Bank Accounts
name_list = []

# Contains all the Bank Accounts
BankList = []

# Contains all the Payee Accounts
PayeeList = []

# Contains all the Names of the Payee Accounts
PayeeList_name = []

# Calculate the total sum for interest rate
FullAmount = 0


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
                        <a href="?app=transfer_page" class="nav-link">
                             <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-right-square" viewBox="0 0 16 16">
  <path fill-rule="evenodd" d="M15 2a1 1 0 0 0-1-1H2a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1zM0 2a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2zm4.5 5.5a.5.5 0 0 0 0 1h5.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 1 0-.708.708L10.293 7.5z"/>
</svg>
                            Transfer</a>
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

# THIS IS THE BANK CURRENCY
XPBank = 1000000

# this is global variables for profile page
profile_name = ""
profile_date_of_birth = 0
profile_email = ""
profile_number = 0

# this is global variables for account page
account_name = ""
account_number = 0
pin_number = 0
account_money = 0
UID = 0

# this is global variables for payee page
person_name = ""
person_number = 0
person_email = ""


class LoginAccount:
    fullname = None
    username = None
    dob = None
    email = None
    phone_number = None
    password = None

    def __init__(self, fullname, username, dob, email, phone_number, password):
        self.fullname = fullname
        self.username = username
        self.dob = dob
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def __str__(self):
        return f"{self.fullname} {self.username} {self.dob} {self.email} {self.phone_number} {self.password}"

    @classmethod
    def change_email(cls, replace_email):
        cls.email = replace_email
        return cls.email

    @classmethod
    def change_phone_number(cls, replace_number):
        cls.phone_number = replace_number
        return cls.phone_number

    @classmethod
    def change_name(cls, replace_username):
        cls.username = replace_username
        return cls.username

    @classmethod
    def change_date_of_birth(cls, replace_data_of_birth):
        cls.dob = replace_data_of_birth
        return cls.dob

class BankAccount:
    BankName = None
    BankNumber = None
    BankCode = None
    BankBalance = decimal
    uniqueCode = None

    def __init__(self, bank_name, bank_number, bank_code, bank_balance, unique):
        self.BankName = bank_name
        self.BankNumber = bank_number
        self.BankCode = bank_code
        self.BankBalance = bank_balance
        self.uniqueCode = unique

    def __str__(self):
        return f"{self.BankName}, {self.BankNumber}, {self.BankCode}, {self.BankBalance}"

class PayeeAccount:
    PayeeName = None
    PayeeNumber = None
    PayeeEmail = None

    def __init__(self, payee_name, payee_number, payee_email):
        self.PayeeName = payee_name
        self.PayeeNumber = payee_number
        self.PayeeEmail = payee_email

    def __str__(self):
        return f"{self.PayeeName}, {self.PayeeNumber}, {self.PayeeEmail}"

# This is the back button that allows you to take the user into different pages
def back_button(link):
    put_html(f"""<a href={link} class="btn btn-primary">Back</a>""")

# This is the login where the user can log their account with their data from the file
@config(theme="dark")
def user_login():
    clear()
    put_html("<h1>Login</h1>")

    put_buttons(["ResetPassword", "Register"], onclick=[password_reset_page, user_signup]).style("text-align:center;")

    data = input_group("", [
        input("Enter username: ", name="name", required=True),
        input("Enter password: ", name="password", required=True, type=PASSWORD)], cancelable=True)

    username = data["name"]
    password = data["password"]

    # use a loop here so it keeps checking if the data is correct and if not then will send the user back with security stuff

    for row in open("data_file.txt", "r").readlines():
        data = row.split()

        if username == data[1] and password == data[5]:
            global profile_name
            global profile_date_of_birth
            global profile_email
            global profile_number

            profile_name = data[0]
            profile_date_of_birth = data[2]
            profile_email = data[3]
            profile_number = data[4]

            account = LoginAccount(data[0], data[1], data[2], data[3], data[4], data[5])
            AccountList.append(account)

            toast("You now have logged in :)")
            home_page()

    else:
        toast("incorrect data, please refresh the page")
        user_login()

main_account = user_login

# This is where the user can sign up and add their data onto the database
@config(theme="dark")
def user_signup():
    clear()
    back_button("?app=login")
    put_html("<h1>Sign Up</h1>")

    put_html("<h3>When doing your Signing up, Make sure to use no spaces when inputting your name. </h3>").style(
        "text-align:center;")

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

    put_code(signup_data)

    if " " in signup_data["FullName"]:  # this checks if there is a space in the Fullname
        toast("please dont put spaces in the full name")
        user_signup()

    if len(signup_data["password"]) <= 4:  # this checks if the password is too small
        toast("your password is too small")
        user_signup()

    if "@" not in signup_data["email_address"]:  # This checks if there is the At symbol in the email address
        toast("please put @ in your email address")
        user_signup()

    # This gets the data from the input group into variables
    fullname = signup_data["FullName"]
    username = signup_data["username"]
    dob = signup_data["DOF"]
    email_address = signup_data["email_address"]
    phone_number = signup_data["phone_number"]
    password = signup_data["password"]

    # This Created the Class object for the class
    account = LoginAccount(fullname, username, dob, email_address, phone_number, password)

    # This opens the Data_file.txt which will write data onto the text file which would then get read by the login
    login_file = open("data_file.txt", "a")
    login_file.write(f"{account}\n")
    login_file.close()

    toast(f"Your account has been created :D")

    user_login()

# This allows the user to create the bank account
def create_bank():
    clear()
    back_button("?app=create")
    put_html("<h1>Create Page</h1>")

    create_data = input_group("Please input your data", [
        input("what would you like to call your bank account", name="account", required=True),
        input("Please enter your 6 digit pin code so you can have protection", name="pin", required=True),
        input("How much money would you like to put into your account?", name="money", type= NUMBER, required=True)
    ])

    if len(create_data["pin"]) == 6:
        toast("we will now create your account")

        global account_name
        global account_number
        global pin_number
        global account_money
        global UID

        account_name = create_data["account"]
        account_number = random.randint(100000, 999999)
        UID = random.randint(0, 100)
        pin_number = create_data["pin"]
        account_money = create_data["money"]
        BankList.append(BankAccount(account_name, account_number, pin_number, account_money, UID))

        name_list.append(str(account_name))

        put_html(f"""    <div class="py-3 text-center container ">
<div class="card mx-auto" style="width: 25rem;">
  <div class="card-body">
   <h5 class="card-title">--------Current data--------</h5>
   <h6 class="card-subtitle mb-2 text-body-secondary">here you can see what we have created for you</h6>
     <ul class="list-group list-group-flush">
  <p class="card-text">Account Name : {account_name}</p>
    <p class="card-text">Personal Name : {profile_name}</p>
    <p class="card-text">Account Number : {account_number}</p>
    <p class="card-text">PIN : {pin_number}</p>
    <p class="card-text">Balance : {account_money}</p>
  </ul>
  </div>
  <h5 class="card-title">------------------------------</h5>
</div>
</div>""")
    else:
        toast("please input 6 Digit")
        home_page()

    options = actions("Does this look good for your account?", ['Yes', 'No'])

    if options == "Yes":
        toast("you now have a bank account!")
        home_page()
    else:
        toast("Sorry for the issue")
        create_bank()

# This allows the user to create the payee account
@config(theme="dark")
def create_payee():
    clear()
    back_button("?app=payment_page")
    put_html("<h1>Create Payee</h1>")

    create_person = input_group("Please input your data", [
        input("What should we call your new friend?", name="person_name", required=True),
        input("What is their phone number?", name="person_number", required=True),
        input("What is their email?", name="person_email", required=True)
    ])

    global person_name
    global person_number
    global person_email

    person_name = create_person["person_name"]
    person_number = create_person["person_number"]
    person_email = create_person["person_email"]
    PayeeList.append(PayeeAccount(person_name, person_number, person_email))

    put_html(f"""<div class="py-3 text-center container ">
    <div class="card mx-auto" style="width: 25rem;">
      <div class="card-body">
       <h5 class="card-title">--------Current data--------</h5>
       <h6 class="card-subtitle mb-2 text-body-secondary">here you can see what we have created for you</h6>
         <ul class="list-group list-group-flush">
         <p class="card-text">Person Name : {person_name}</p>
        <p class="card-text">Person Number : {person_number}</p>
        <p class="card-text">Person Email : {person_email}</p>
      </ul>
      </div>
      <h5 class="card-title">------------------------------</h5>
    </div>
    </div>""")

    options = actions("Does this look good for your new payee?", ['Yes', 'No'])

    if options == "Yes":
        payment_page()
    else:
        toast("Sorry for the issue, please delete if you are unhappy")

# This is where the user can select accounts and create them for data
@config(theme="dark")
def home_page():
    clear()

    back_button("?app=product")
    put_html(navbar)
    put_html("<h1>Home Page</h1>")

    put_html("<h3>This is where you can create your Bank account</h3>")

    put_html("<h4>When you have created your account, select no to not make, to see your account</h4>")

    options = actions("would you like to create an bank account", ['Yes', 'No'])

    if options == "Yes":
        create_bank()

    elif not BankList:
        toast("you need to create an bank account to see the data")
        home_page()

    else:
        for account in BankList:
                put_html(f"""<div class="py-3 text-center container ">
        <div class="card mx-auto" style="width: 25rem;">
          <div class="card-body">
            <h5 class="card-title">Bank Name : #{account.BankName}</h5>
             <ul class="list-group list-group-flush">
            <li class="list-group-item">Account Number: {account.BankNumber}</li>
            <li class="list-group-item"> Account Code: {account.BankCode}</li>
            <li class="list-group-item">Balance: {account.BankBalance}</li>
          </ul>
          </div>
        </div>
        </div>
        """)

# This is the profile page which will output the users information and will have function to change
@config(theme="dark")
def profile_page():
    clear()
    back_button("?app=home")
    put_html(navbar)
    put_html("<h1>Profile</h1>")

    for data in AccountList:
        if data.fullname == profile_name:
            put_html(f""" <div class="container mt-5">
                <div class="form-floating">
                    <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com" value="{data.username}">
                    <label for="floatingInput">Name</label>
                </div>
                <!-- this input is invalid -->
                <div class="form-floating">
                    <input type="date" class="form-control is-invalid" id="floatingDOB" value="{data.dob}" >
                    <label for="floatingDOB">Data of birth</label>
                </div>
                <div class="form-floating">
                    <input type="email" class="form-control" id="floatingEmail" placeholder="Password" value="{data.email}">
                    <label for="floatingEmail">Email Address</label>
                </div>
                <div class="form-floating">
                    <input type="number" class="form-control" id="floatingNumber" placeholder="Password" value="{data.phone_number}">
                    <label for="floatingNumber">Mobile Number</label>
                </div>
            </div>
            """)

    update = actions('Would you like to update your Profile??', ['Yes Please', 'No Thanks'], )

    if update == 'Yes Please':
        update_page()

# This is the product page where the user can select loans for their account depending on their needs
@config(theme="dark")
def product_page():
    clear()
    back_button("?app=transfer_page")
    put_html(navbar)
    put_html("<h1>Product Page</h1>")


    options = actions("would you like an loan out?", ['Yes', 'No'])

    if options == "Yes":

        if not name_list:
            toast("please create an bank account")
            home_page()

        loan_data = input_group('Add user', [
            slider("How much money would you like to take out?", value=(XPBank / 2), name='borrowed_money', min_value=0,
                   max_value=XPBank),
            input('How much time do you need to pay for this?', type=NUMBER, name='years', required=True),
            select("Which account would you like to transfer money from?", options=name_list, name='name'),
        ])

        put_code(loan_data)

        # Gets the data into the variables to calculate
        money_taken = loan_data["borrowed_money"]
        amount_years = loan_data["years"]
        bank_name = loan_data["name"]

        month_money = (((money_taken * 6) / amount_years) / 12)

        print(month_money)

        put_html(f"""<div class="py-3 text-center container ">
                <div class="card mx-auto" style="width: 25rem;">
                  <div class="card-body">
                    <h5 class="card-title">Here is your current Loan</h5>
                  </ul>
                  </div>
                   <ul class="list-group list-group-flush">
                    <li class="list-group-item">So you want to take out: {money_taken} pounds</li>
                    <li class="list-group-item"> You will pay it back in: {amount_years} years</li>
                    <li class="list-group-item"> The current interest Rate is %6</li>
                    <li class="list-group-item"> Therefore, month payment will be {month_money}</li>
                    <li class="list-group-item">You have chosen {bank_name} as ur main bank account</li>
                  </ul>
                </div>
                </div>""")

        final = actions("Is this ok for you?", ['Yes', 'No'])

        if final == "Yes":
            for data in BankList:
                    data.BankBalance += money_taken
                    toast(f"you now have {data.BankBalance} in your bank account")
                    home_page()

        else:
            toast("That is fine")
            home_page()

    else:
        toast("That is fine")
        home_page()

# This allows the user to work on adding or replacing new data for the profile page by using class subroutines
def update_page():
    clear()
    back_button("?app=profile")
    put_html("<h1>Update Profile</h1>")

    option = select("What would you like to update?",  # options for the user to choose from
                    options=["Username", "Data of birth", "Email address", "Phone number"])

    # This allows the user to change the data of their account, mostly their profile but also their data class account
    for data in AccountList:
        if data.fullname == profile_name:

            if option == "Email address":
                new_email = input("What do you want ur new email to be?", type=TEXT)
                data.email = data.change_email(new_email)
                toast("your info will be updated")
                toast(data.email)

            elif option == "Phone number":
                new_phone_number = input("What would you like to input for your phone number", type=NUMBER)
                data.phone_number = data.change_phone_number(new_phone_number)

            elif option == "Data of birth":
                new_date_of_birth = input("what would you like to input for your date of birth", type=DATE)
                data.dob = data.change_date_of_birth(new_date_of_birth)

            elif option == "Username":
                new_username = input("what would you like your new username to be", type=TEXT)
                data.username = data.change_name(new_username)
            else:
                toast("ERROR")

# This is their payment method where the user can select different payee for user to give money
@config(theme="dark")
def payment_page():
    clear()
    back_button("?app=profile")
    put_html(navbar)
    put_html("<h1>Payee Page</h1>")

    put_html("<h3>This is where you can create your Payee account</h3>")

    put_html("<h4>When you have created your Payee, select no to not make, to see your Payee</h4>")

    options = actions("would you like to create a payee person", ['Yes', 'No'])


    if options == "Yes":
        create_payee()
    else:
        if not PayeeList: # Checks if the list is empty
            toast("Please create an Payee Person to see your list")
            payment_page()
        else:
            for account in PayeeList: # If the list is not Empty then it will output the data from the class
                put_html(f"""<div class="card">
                            <div class="card-body">
                               <h5 class="card-title">Person Name : {account.PayeeName}</h5>
                               <ul class="list-group list-group-flush">
                              <li class="list-group-item">Person Number : {account.PayeeEmail}</li>
                              <li class="list-group-item">Person Email : {account.PayeeNumber}]</li>
                            </ul>
                            </div>""")

# This is the page where the user can reset their password by giving their emails
@config(theme="dark")
def password_reset_page():
    clear()
    back_button("?app=login")
    put_html("<h1>Password Reset Page</h1>")

    old_email = input("Please enter your old email address so we can reset ur password:")

    for row in open("data_file.txt", "r").readlines():
        item = row.split()

        if item[3] == old_email:
            put_html(
                "<h1>I am happy to say that the system has found your email so please look at it to change your password</h1>")
        else:
            put_html("ERROR")

# This is the page where the user can transfer their money to the Payee account
@config(theme="dark")
def transfer_page():
    clear()
    back_button("?app=payment_page")
    put_html(navbar)
    put_html("<h1>Transfer Page Page</h1>")


    put_html("<h3>This is where you can get loans to get some money</h3>")

    put_html("<h4>You will be able to select which accounts gets the money<h4>")

    # This uses two lists to get the data, depending on what the user has chosen in the action menu

    if not BankList and not PayeeList:
        toast("Please create an account and payee to transfer your money")

    for data in BankList:

        for data2 in PayeeList:

            options = actions("Would you like like to transfer money from your bank account to one of your payee?",
                              ['Yes', 'No'])

            if options == "Yes":
                if not name_list: # Checks if there is any accounts, if there isn't any then it will take user back
                    toast("please create an account")
                    transfer_page()

                else:
                    name = select("Which account would you like to transfer money from?", name_list)

                    if data.BankName == name: # Checks if the name is the same in the Bank list
                        put_html(f"""<div class="card" style="width: 20rem;">
                                                          <div class="card-body">
                                                            <h5 class="card-title">Current data</h5>
                                                            <h6 class="card-subtitle mb-2 text-body-secondary">Here is your account</h6>
                                                            <p class="card-text">Account Name : {data.BankName}</p>
                                                            <p class="card-text">Account Number : {data.BankNumber}</p>
                                                            <p class="card-text">PIN : {data.BankCode}</p>
                                                            <p class="card-text">Balance : {data.BankBalance}</p>
                                                          </div>
                                                        </div>""").style("text-align:center;")

                for i in PayeeList:
                    PayeeList_name.append(str(i.PayeeName)) # Puts all the data from the Payee into the list for the select function

                if not PayeeList_name:  # Checks if there is any Payee accounts, if there isn't any then it will take user back
                    toast("Please create an Payee")
                    transfer_page()
                else:
                    payee = select("which payee would you like to send it to?", PayeeList_name)

                    if data2.PayeeName == payee: # Checks if the name is the same in the Payee list
                        put_html(f"""<div class="card" style="width: 20rem;">
                                                                              <div class="card-body">
                                                                                <h5 class="card-title">Current data</h5>
                                                                                <h6 class="card-subtitle mb-2 text-body-secondary">Here is the Payee Account</h6>
                                                                                <p class="card-text">Payee Name : {data2.PayeeName}</p>
                                                                                <p class="card-text">Payee Number : {data2.PayeeNumber}</p>
                                                                                <p class="card-text">Payee Email : {data2.PayeeEmail}</p>
                                                                              </div>
                                                                            </div>""").style("text-align:center;")



                options2 = slider("how much would you like to give to your payee?", value=(int(data.BankBalance) / 2), min_value=0,
                                  max_value=data.BankBalance) # Lists the amount of money from the specific bank money

                last_option = actions("Do you want to make this transaction???",["yes","no"])

                if last_option == "yes":
                    data.BankBalance = data.BankBalance - options2

                    put_html(f"""<div class="card" style="width: 20rem;">
                                                                            <div class="card-body">
                                                                              <h5 class="card-title">Current data</h5>
                                                                              <h6 class="card-subtitle mb-2 text-body-secondary">Here is your account after the transaction</h6>
                                                                              <p class="card-text">Balance : {data.BankBalance}</p>
                                                                            </div>
                                                                          </div>""").style("text-align:center;")
                else:
                    toast("sorry for wasting your time")
                    transfer_page()

            if options == "no":
                home_page()

# This is the welcome hub where the user will start the journey of either signing in the account or logging in
@config(theme="dark")
def welcome_page():
    clear()
    put_html("<h1>Welcome Page</h1>").style("text-align:center;")

    put_html(
        "<h3>Welcome to the XP App welcome page, this is where you will be able to find the login and sign up button to get access to our page, Just look before this text</h3>").style(
        "text-align:center;")

    put_buttons(["Register", "Login"], onclick=[user_signup, user_login]).style("text-align:center;")

    put_html("<h1>About</h1>").style("text-align:center;")

    put_html(
        """<h3>This is one of the top most used bank system created by the famous malik. Its an unique piece of art that he has made. Very simple to create an account,
        and very easy to create payee account to allow you to transfer your money.
        
        The best thing is that you can even create money within the system with a single click in our system, Find out more in the XP bank Premium pass
        </h3>""").style(
        "text-align:center;")

    put_html("<h1>Products</h1>").style("text-align:center;")

    put_html(
        """<h3>TIn the near future, we will plan to expand the XP bank to the limit by working together with other bank to allow an proper and fair way to work with your money
        and see what the best options such at looking at loans, mortgages, saving and investment with the help of other banks</h3>""").style(
        "text-align:center;")

# This is the route section for the program
if __name__ == '__main__':
    routes = {
        "welcome_page": welcome_page,
        "login": user_login,
        "signup": user_signup,
        "home": home_page,
        "profile": profile_page,
        "product": product_page,
        "payment_page": payment_page,
        "password_reset": password_reset_page,
        "transfer_page": transfer_page
    }
    start_server(routes, port=5000, debug=True)
