import datetime
import re
from datetime import date
from beautifultable import BeautifulTable
import csv


class User:
    def __init__(self, firstname, lastname, gender, city, address, mobile_phone_number, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.city = city
        self.address = address
        self.mobile_phone_number = mobile_phone_number
        self.username = username
        self.password = password

    @staticmethod
    def is_valid_firstname(firstname):
        if not firstname:
            print("The first name field cannot be empty.")
            return False

        if any([char for char in firstname if not char.isalpha()]):
            print("First name should only contain letters.")
            return False

        return True

    @staticmethod
    def is_valid_lastname(lastname):
        if not lastname:
            print("The last name field cannot be empty.")
            return False

        if any([char for char in lastname if not char.isalpha()]):
            print("Last name should only contain letters.")
            return False

        return True

    @staticmethod
    def is_valid_gender(gender):
        if gender not in ["male", "female"]:
            print("Gender can only be male or female.")
            return False

        return True

    @staticmethod
    def is_valid_country(country):
        if not country:
            print("The country field cannot be empty.")
            return False

        return True

    @staticmethod
    def is_valid_state(state):
        if not state:
            print("The state field cannot be empty.")
            return False

        return True

    @staticmethod
    def is_valid_city(city):
        if not city:
            print("The city field cannot be empty.")
            return False

        return True

    @staticmethod
    def is_valid_address(address):
        if not address:
            print("The address field cannot be empty.")
            return False

        return True

    @staticmethod
    def is_valid_age(age):
        if not age.isdigit():
            print("Age must be numerical.")
            return

        if int(age) < 18:
            print("Age cannot be less than 18.")
            return False

        if int(age) > 120:
            print("Age cannot be more than 120.")
            return False

        return True

    @staticmethod
    def is_valid_mobile_phone_number(mobile_phone_number):
        if not mobile_phone_number.isdigit():
            print("Mobile phone number should only contain digits.")
            return False

        if len(mobile_phone_number) != 11:
            print("Mobile phone number must be 11 digits.")
            return False

        if mobile_phone_number[:4] not in ["0912", "0990", "0919", "0935"]:
            print("Mobile phone number must start with prefixes 0912 or 0990 or 0919 or 0935.")
            return False

        return True

    @staticmethod
    def is_valid_landline_phone_number(landline_phone_number):
        if not landline_phone_number.isdigit():
            print("Landline phone number should only contain digits.")
            return False

        if len(landline_phone_number) != 11:
            print("Landline phone number must be 11 digits.")
            return False

        if not landline_phone_number.startswith("071"):
            print("Landline phone number must start with prefix 071.")
            return False

        return True

    @staticmethod
    def is_valid_email(email):
        return re.match("^[^@]+@[^@]+\\.[^@]+$", email)

    @staticmethod
    def is_valid_initial_balance(initial_balance):
        if not initial_balance.isdigit():
            print("Initial balance must be numerical.")
            return

        if int(initial_balance) < 200000:
            print("Initial balance should not be less than 200,000.")
            return False

        return True

    @staticmethod
    def is_valid_balance(balance):
        if not balance.isdigit():
            print("Initial balance must be numerical.")
            return

        if int(balance) < 20000:
            print("Balance should not be less than 20,000.")
            return False

        return True


class Admin(User):
    admins = []
    id_counter = 1

    def __init__(self, *args):
        super().__init__(firstname=args[0], lastname=args[1], gender=args[2], city=args[4], address=args[5],
                         mobile_phone_number=args[6], username=args[7], password=args[8])
        self.state = args[3]

        if len(args) == 9:
            self.id = f"M00{Admin.id_counter}"
            Admin.id_counter += 1
        else:
            self.id = args[9]
            Admin.id_counter = max(Admin.id_counter, int(self.id[3:]) + 1)

    @staticmethod
    def is_valid_username(username):
        if len(username) < 10:
            print("Password must contain at least 10 characters.")
            return False

        if not any([char for char in username if 48 <= ord(char) <= 57]):
            print("Password must contain at least one digit.")
            return False

        if not any([char for char in username if 65 <= ord(char) <= 90]):
            print("Password must contain at least one uppercase letter.")
            return False

        if not any([char for char in username if 97 <= ord(char) <= 122]):
            print("Password must contain at least one lowercase letter.")
            return False

        if not any([char for char in username if char in "[@_!#$%^&*()<>?}{~:]"]):
            print("Password must contain at least one special character.")
            return False

        return True

    @staticmethod
    def is_valid_password(password):
        if len(password) < 10:
            print("Password must contain at least 10 characters.")
            return False

        if not any([char for char in password if 48 <= ord(char) <= 57]):
            print("Password must contain at least one digit.")
            return False

        if not any([char for char in password if 65 <= ord(char) <= 90]):
            print("Password must contain at least one uppercase letter.")
            return False

        if not any([char for char in password if 97 <= ord(char) <= 122]):
            print("Password must contain at least one lowercase letter.")
            return False

        if not any([char for char in password if char in "[@_!#$%^&*()<>?}{~:]"]):
            print("Password must contain at least one special character.")
            return False

        return True

    @staticmethod
    def is_unique_username(username):
        for admin in Admin.admins:
            if admin.username == username:
                return False
        return True

    @staticmethod
    def search_by_username(username):
        for admin in Admin.admins:
            if admin.username == username:
                return admin
        return None

    @staticmethod
    def add_admin():
        if len(Admin.admins) == 3:
            print("The capacity of the admins list is full.")
            return

        print("1. Single Line")
        print("2. Question And Answer")

        option = input("Enter the data entry method: ").strip()

        if option != "1" and option != "2":
            print("The entered option is incorrect.")
            return

        if option == "1":
            data = input(
                "Enter first name, last name, gender, state, city, address, mobile phone number, username, password in one line seperated with ','\n").strip()
            data = re.sub("\s*,\s*", ",", data).split(",")

            if len(data) != 9:
                print("The number of entries should be 9.")
                return

            firstname, lastname, gender, state, city, address, mobile_phone_number, username, password = data

        else:

            firstname = input("Enter first name: ").strip()
            lastname = input("Enter last name: ").strip()
            gender = input("Enter gender(male/female): ").strip().lower()
            state = input("Enter state: ").strip()
            city = input("Enter city: ").strip()
            address = input("Enter address: ").strip()
            mobile_phone_number = input("Enter mobile phone number: ").strip()
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()

        if not User.is_valid_firstname(firstname):
            print("The entered first name is not valid.")
            return

        if not User.is_valid_lastname(lastname):
            print("The entered last name is not valid.")
            return

        if not User.is_valid_gender(gender):
            print("The entered gender is not valid.")
            return

        if not User.is_valid_state(state):
            print("The entered state is not valid.")
            return

        if not User.is_valid_city(city):
            print("The entered city in not valid.")
            return

        if not User.is_valid_address(address):
            print("The entered address is not valid.")
            return

        if not User.is_valid_mobile_phone_number(mobile_phone_number):
            print("The entered mobile phone number is not valid.")
            return

        if not Admin.is_valid_username(username):
            print("The entered username is not valid.")
            return

        if not Admin.is_unique_username(username):
            print("The entered username is already taken.")
            return

        if not Admin.is_valid_password(password):
            print("The entered password is not valid.")
            return

        admin = Admin(firstname, lastname, gender, state, city, address, mobile_phone_number, username, password)
        Admin.admins.append(admin)
        print("The admin added to the admins list successfully.")

    @staticmethod
    def remove_admin():
        username = input("Enter username: ").strip()
        admin = Admin.search_by_username(username)

        if not admin:
            print("There is no admin with this username.")
            return

        Admin.admins.remove(admin)
        print("The admin removed from the users list successfully.")

    @staticmethod
    def update_admin():
        admin_username = input("Enter username: ").strip()
        admin = Admin.search_by_username(admin_username)

        if not admin:
            print("There is no admin with this id.")
            return

        print("1. Single Line")
        print("2. Question And Answer")

        option = input("Enter the data entry method: ").strip()

        if option != "1" and option != "2":
            print("The entered option is incorrect.")
            return

        if option == "1":
            data = input(
                "Enter new first name, new last name, new gender, new state, new city, new address, new mobile phone number, new username, new password in one line seperated with ','\n").strip()
            data = re.sub("\s*,\s*", ",", data).split(",")

            if len(data) != 9:
                print("The number of entries should be 9.")
                return

            firstname, lastname, gender, state, city, address, mobile_phone_number, username, password = data

        else:
            firstname = input("Enter new first name: ").strip()
            lastname = input("Enter new last name: ").strip()
            gender = input("Enter new gender(male/female): ").strip().lower()
            state = input("Enter new state: ").strip()
            city = input("Enter new city: ").strip()
            address = input("Enter new address: ").strip()
            mobile_phone_number = input("Enter new mobile phone number: ").strip()
            username = input("Enter new username: ").strip()
            password = input("Enter new password: ").strip()

        if not User.is_valid_firstname(firstname):
            print("The entered first name is not valid.")
            return

        if not User.is_valid_lastname(lastname):
            print("The entered last name is not valid.")
            return

        if not User.is_valid_gender(gender):
            print("The entered gender is not valid.")
            return

        if not User.is_valid_state(state):
            print("The entered state is not valid.")
            return

        if not User.is_valid_city(city):
            print("The entered city in not valid.")
            return

        if not User.is_valid_address(address):
            print("The entered address is not valid.")
            return

        if not User.is_valid_mobile_phone_number(mobile_phone_number):
            print("The entered mobile phone number is not valid.")
            return

        if not Admin.is_valid_username(username):
            print("The entered username is not valid.")
            return

        if not Admin.is_unique_username(username):
            print("The entered username is already taken.")
            return

        if not Admin.is_valid_password(password):
            print("The entered password is not valid.")
            return

        admin.firstname = firstname
        admin.lastname = lastname
        admin.gender = gender
        admin.state = state
        admin.city = city
        admin.address = address
        admin.mobile_phone_number = mobile_phone_number
        admin.username = username
        admin.password = password
        print("The admin information updated successfully.")

    @staticmethod
    def add_user():
        print("1. Single Line")
        print("2. Question And Answer")

        option = input("Enter the data entry method: ").strip()

        if option != "1" and option != "2":
            print("The entered option is incorrect.")
            return

        if option == "1":
            data = input(
                "Enter first name, last name, gender, country, city, address, age, landline phone number, mobile phone number, email, username, password, initial balance in one line seperated with ','\n").strip()
            data = re.sub("\s*,\s*", ",", data).split(",")

            if len(data) != 13:
                print("The number of entries should be 13.")
                return

            firstname, lastname, gender, country, city, address, age, landline_phone_number, mobile_phone_number, email, username, password, initial_balance = data

        else:
            firstname = input("Enter first name: ").strip()
            lastname = input("Enter last name: ").strip()
            gender = input("Enter gender(male/female): ").strip().lower()
            country = input("Enter country: ").strip()
            city = input("Enter city: ").strip()
            address = input("Enter address: ").strip()
            age = input("Enter age: ").strip()
            landline_phone_number = input("Enter landline phone number: ").strip()
            mobile_phone_number = input("Enter mobile phone number: ").strip()
            email = input("Enter email: ").strip()
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            initial_balance = input("Enter initial balance: ").strip()

        if not User.is_valid_firstname(firstname):
            print("The entered first name is not valid.")
            return

        if not User.is_valid_lastname(lastname):
            print("The entered last name is not valid.")
            return

        if not User.is_valid_gender(gender):
            print("The entered gender is not valid.")
            return

        if not User.is_valid_country(country):
            print("The entered country is not valid.")
            return

        if not User.is_valid_city(city):
            print("The entered city in not valid.")
            return

        if not User.is_valid_address(address):
            print("The entered address is not valid.")
            return

        if not User.is_valid_age(age):
            print("The entered age is not valid.")
            return

        if not User.is_valid_landline_phone_number(landline_phone_number):
            print("The entered landline phone number is not valid.")
            return

        if not User.is_valid_mobile_phone_number(mobile_phone_number):
            print("The entered mobile phone number is not valid.")
            return

        if not User.is_valid_email(email):
            print("The entered email is not valid.")
            return

        if not RegularUser.is_valid_username(username):
            print("The entered username is not valid.")
            return

        if not RegularUser.is_unique_username(username):
            print("The entered username is already taken.")
            return

        if not RegularUser.is_valid_password(password):
            print("The entered password is not valid.")
            return

        if not User.is_valid_initial_balance(initial_balance):
            print("The entered initial balance is not valid.")
            return

        user = RegularUser(firstname, lastname, gender, country, city, address, int(age),
                           landline_phone_number, mobile_phone_number, email, username, password, int(initial_balance))
        RegularUser.users.append(user)
        print("The user added to the users list successfully.")

    @staticmethod
    def remove_user():
        username = input("Enter username: ").strip()
        user = RegularUser.search_by_username(username)

        if not user:
            print("There is no user with this username.")
            return

        RegularUser.users.remove(user)
        print("The user removed from the users list successfully.")

    @staticmethod
    def update_user():
        username = input("Enter username: ").strip()
        user = RegularUser.search_by_username(username)

        if not user:
            print("There is no user with this username.")
            return

        print("1. Single Line")
        print("2. Question And Answer")

        option = input("Enter the data entry method: ").strip()

        if option != "1" and option != "2":
            print("The entered option is incorrect.")
            return

        if option == "1":
            data = input(
                "Enter new first name, new last name, new gender, new country, new city, new address, new age, new landline phone number, new mobile phone number, new email, new username, new password, new balance in one line seperated with ','\n").strip()
            data = re.sub("\s*,\s*", ",", data).split(",")

            if len(data) != 13:
                print("The number of entries should be 13.")
                return

            firstname, lastname, gender, country, city, address, age, landline_phone_number, mobile_phone_number, email, username, password, balance = data

        else:
            firstname = input("Enter new first name: ").strip()
            lastname = input("Enter new last name: ").strip()
            gender = input("Enter new gender(male/female): ").strip().lower()
            country = input("Enter new country: ").strip()
            city = input("Enter new city: ").strip()
            address = input("Enter new address: ").strip()
            age = input("Enter new age: ").strip()
            landline_phone_number = input("Enter new landline phone number: ").strip()
            mobile_phone_number = input("Enter new mobile phone number: ").strip()
            email = input("Enter new email: ").strip()
            username = input("Enter new username: ").strip()
            password = input("Enter new password: ").strip()
            balance = input("Enter new balance: ").strip()

        if not User.is_valid_firstname(firstname):
            print("The entered first name is not valid.")
            return

        if not User.is_valid_lastname(lastname):
            print("The entered last name is not valid.")
            return

        if not User.is_valid_gender(gender):
            print("The entered gender is not valid.")
            return

        if not User.is_valid_country(country):
            print("The entered country is not valid.")
            return

        if not User.is_valid_city(city):
            print("The entered city in not valid.")
            return

        if not User.is_valid_address(address):
            print("The entered address is not valid.")
            return

        if not User.is_valid_age(age):
            print("The entered age is not valid.")
            return

        if not User.is_valid_landline_phone_number(landline_phone_number):
            print("The entered landline phone number is not valid.")
            return

        if not User.is_valid_mobile_phone_number(mobile_phone_number):
            print("The entered mobile phone number is not valid.")
            return

        if not User.is_valid_email(email):
            print("The entered email is not valid.")
            return

        if not RegularUser.is_valid_username(username):
            print("The entered username is not valid.")
            return

        if not RegularUser.is_unique_username(username):
            print("The entered username is already taken.")
            return

        if not RegularUser.is_valid_password(password):
            print("The entered password is not valid.")
            return

        if not User.is_valid_balance(balance):
            print("The entered balance is not valid.")
            return

        user.firstname = firstname
        user.lastname = lastname
        user.gender = gender
        user.country = country
        user.city = city
        user.address = address
        user.age = int(age)
        user.landline_phone_number = landline_phone_number
        user.mobile_phone_number = mobile_phone_number
        user.email = email
        user.username = username
        user.password = password
        user.balance = int(balance)
        print("The user information updated successfully.")

    @staticmethod
    def record_user():
        print("1. Record By First Name")
        print("2. Record By Last Name")
        print("3. Record By Gender")
        print("4. Record By City")
        print("5. Record By Country")
        print("6. Record By Age")

        option = input("Enter your option number: ").strip()

        print()

        if option not in ["1", "2", "3", "4", "5", "6"]:
            print("The entered option number is not valid.")
            return

        if option == "1":
            RegularUser.users.sort(key=lambda user: user.firstname)

        elif option == "2":
            RegularUser.users.sort(key=lambda user: user.lastname)

        elif option == "3":
            RegularUser.users.sort(key=lambda user: user.gender)

        elif option == "4":
            RegularUser.users.sort(key=lambda user: user.city)

        elif option == "5":
            RegularUser.users.sort(key=lambda user: user.country)

        else:
            RegularUser.users.sort(key=lambda user: user.age)

        RegularUser.display()

        save = input("Do you want to save records in file? (y/n)\n").strip()

        if save == "y":
            attrs = ["firstname", "lastname", "gender", "city", "country", "age"]
            attr = attrs[int(option) - 1]
            file_name = f"users-{attr}.csv"
            RegularUser.save_to_file(file_name)
            print(f"The records were successfully saved to file {file_name}.")

    @staticmethod
    def search_user_by_username():
        username = input("Enter username: ").strip()

        user = RegularUser.search_by_username(username)

        if not user:
            print("There is no user with this username.")
            return

        user.print_info()

    @staticmethod
    def search_user_by_phone_number():
        mobile_phone_number = input("Enter mobile phone number: ").strip()

        user = RegularUser.search_by_mobile_phone_number(mobile_phone_number)

        if not user:
            print("There is no user with this mobile phone number.")
            return

        user.print_info()

    @staticmethod
    def search_user():
        print("1. Search By Username")
        print("2. Search By Mobile Phone Number")

        option = input("Enter your option number: ").strip()

        print()

        if option == "1":
            Admin.search_user_by_username()
        elif option == "2":
            Admin.search_user_by_phone_number()
        else:
            print("The entered option number is not valid.")

    @staticmethod
    def login(username, password):
        for admin in Admin.admins:
            if admin.username == username and admin.password == password:
                admin.menu()
                return

        print("Username or password is not valid.")

    @staticmethod
    def register_multiple_user_by_file():
        file_name = input("Enter file path: ").strip()

        try:
            with open(file_name, "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 13:
                        firstname, lastname, gender, country, city, address, age, landline_phone_number, mobile_phone_number, email, username, password, initial_balance = row

                        if not User.is_valid_firstname(firstname):
                            continue

                        if not User.is_valid_lastname(lastname):
                            continue

                        if not User.is_valid_gender(gender):
                            continue

                        if not User.is_valid_country(country):
                            continue

                        if not User.is_valid_city(city):
                            continue

                        if not User.is_valid_address(address):
                            continue

                        if not User.is_valid_age(age):
                            continue

                        if not User.is_valid_landline_phone_number(landline_phone_number):
                            continue

                        if not User.is_valid_mobile_phone_number(mobile_phone_number):
                            continue

                        if not User.is_valid_email(email):
                            continue

                        if not RegularUser.is_valid_username(username):
                            continue

                        if not RegularUser.is_unique_username(username):
                            continue

                        if not RegularUser.is_valid_password(password):
                            continue

                        if not User.is_valid_initial_balance(initial_balance):
                            continue

                        user = RegularUser(firstname, lastname, gender, country, city,
                                           address, int(age), landline_phone_number, mobile_phone_number, email,
                                           username, password,
                                           int(initial_balance))
                        RegularUser.users.append(user)

            print("The file information about users has been successfully added.")

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def save_admins():
        try:
            with open("admins.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for admin in Admin.admins:
                    writer.writerow(list(vars(admin).values()))

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def load_admins():
        try:
            with open("admins.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    firstname, lastname, gender, city, address, mobile_phone_number, username, password, state, admin_id = row
                    admin = Admin(firstname, lastname, gender, state, city, address, mobile_phone_number, username,
                                  password, admin_id)
                    Admin.admins.append(admin)

        except Exception as e:
            if type(e) != FileNotFoundError:
                print("ERROR:", e)

    def menu(self):
        print(f"\nWellcome {self.firstname} {self.lastname}\n")

        while True:
            print("1. Add An Admin")
            print("2. Remove An Admin")
            print("3. Update An Admin Information")
            print("4. Add An User")
            print("5. Remove An User")
            print("6. Update An User Information")
            print("7. Recording Users")
            print("8. Search Users")
            print("9. Register Multiple Admin By Using File")
            print("10. Exit")

            option = input("Enter your option number: ").strip()

            if option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
                print("The entered option number is not valid.")
                continue

            if option != "10":
                password = input("Enter your password: ").strip()

                if password != self.password:
                    print("The entered password is not valid.")
                    continue

            print()

            if option == "1":
                Admin.add_admin()
            elif option == "2":
                Admin.remove_admin()
            elif option == "3":
                Admin.update_admin()
            elif option == "4":
                Admin.add_user()
            elif option == "5":
                Admin.remove_user()
            elif option == "6":
                Admin.update_user()
            elif option == "7":
                Admin.record_user()
            elif option == "8":
                Admin.search_user()
            elif option == "9":
                Admin.register_multiple_user_by_file()
            elif option == "10":
                break

            print()

            Admin.save_admins()
            RegularUser.save_users()


class RegularUser(User):
    users = []
    account_number_counter = 1000000000000

    def __init__(self, *args):
        super().__init__(firstname=args[0], lastname=args[1], gender=args[2], city=args[4], address=args[5],
                         mobile_phone_number=args[8], username=args[10], password=args[11])
        self.country = args[3]
        self.age = args[6]
        self.landline_phone_number = args[7]
        self.email = args[9]
        self.balance = args[12]

        if len(args) == 15:
            self.registration_date = args[13]
            self.account_number = args[14]
            RegularUser.account_number_counter = max(RegularUser.account_number_counter, self.account_number + 1)
        else:
            self.registration_date = date.today()
            self.account_number = RegularUser.account_number_counter
            RegularUser.account_number_counter += 1

    @staticmethod
    def is_valid_username(username):
        if len(username) < 8:
            print("Username must contain at least 10 characters.")
            return False

        if not any([char for char in username if 48 <= ord(char) <= 57]):
            print("Username must contain at least one digit.")
            return False

        if not any([char for char in username if 65 <= ord(char) <= 90]):
            print("Username must contain at least one uppercase letter.")
            return False

        if not any([char for char in username if 97 <= ord(char) <= 122]):
            print("Username must contain at least one lowercase letter.")
            return False

        if not any([char for char in username if char in "[@_!#$%^&*()<>?}{~:]"]):
            print("Username must contain at least one special character.")
            return False

        return True

    @staticmethod
    def is_valid_password(password):
        if len(password) < 8:
            print("Password must contain at least 10 characters.")
            return False

        if not any([char for char in password if 48 <= ord(char) <= 57]):
            print("Password must contain at least one digit.")
            return False

        if not any([char for char in password if 65 <= ord(char) <= 90]):
            print("Password must contain at least one uppercase letter.")
            return False

        if not any([char for char in password if 97 <= ord(char) <= 122]):
            print("Password must contain at least one lowercase letter.")
            return False

        if not any([char for char in password if char in "[@_!#$%^&*()<>?}{~:]"]):
            print("Password must contain at least one special character.")
            return False

        return True

    @staticmethod
    def is_unique_username(username):
        for user in RegularUser.users:
            if user.username == username:
                return False
        return True

    @staticmethod
    def search_by_account_number(account_number):
        for user in RegularUser.users:
            if user.account_number == account_number:
                return user
        return None

    @staticmethod
    def search_by_username(username):
        for user in RegularUser.users:
            if user.username == username:
                return user
        return None

    @staticmethod
    def search_by_mobile_phone_number(mobile_phone_number):
        for user in RegularUser.users:
            if user.mobile_phone_number == mobile_phone_number:
                return user
        return None

    @staticmethod
    def display():
        if not RegularUser.users:
            print("The users list is empty.")
            return

        table = BeautifulTable(maxwidth=400)
        attrs = list(vars(RegularUser.users[0]).keys())

        for user in RegularUser.users:
            table.rows.append(list(vars(user).values()))

        table.columns.header = attrs
        print(table)

    @staticmethod
    def save_to_file(file_name):
        try:
            with open(file_name, "w", newline="") as file:
                writer = csv.writer(file)
                for user in RegularUser.users:
                    data = [str(value) for value in list(vars(user).values())]
                    writer.writerow(data)

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def login(username, password):
        for user in RegularUser.users:
            if user.username == username and user.password == password:
                user.menu()
                return

        print("Username or password is not valid.")

    @staticmethod
    def save_users():
        try:
            with open("users.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for user in RegularUser.users:
                    writer.writerow(list(vars(user).values()))

        except Exception as e:
            print("ERROR:", e)

    @staticmethod
    def load_users():
        try:
            with open("users.csv", "r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    firstname, lastname, gender, city, address, mobile_phone_number, username, password, country, age, landline_phone_number, email, balance, registration_date, account_number = row
                    user = RegularUser(firstname, lastname, gender, country, city, address, int(age),
                                       landline_phone_number, mobile_phone_number, email, username, password,
                                       int(balance),
                                       registration_date,
                                       int(account_number))
                    RegularUser.users.append(user)

        except Exception as e:
            if type(e) != FileNotFoundError:
                print("ERROR:", e)

    def save_log(self, *args):
        try:
            with open("logs.log", "a") as file:
                data = f"{self.username},{','.join(args)},{datetime.datetime.now()}\n"
                file.write(data)

        except Exception as e:
            print("ERROR:", e)

    def menu(self):
        print(f"\nWellcome {self.firstname} {self.lastname}\n")

        self.save_log("login")

        while True:
            print("1. Print Information")
            print("2. Update Information")
            print("3. Transfer Money")
            print("4. Exit")

            option = input("Enter your option number: ").strip()

            print()

            if option == "1":
                self.print_info()
            elif option == "2":
                self.change_info()
            elif option == "3":
                self.transfer_money()
            elif option == "4":
                self.save_log("logout")
                break
            else:
                print("The entered option number is not valid.")

            print()

            Admin.save_admins()
            RegularUser.save_users()

    def print_info(self):
        print("First Name:", self.firstname)
        print("Last Name:", self.lastname)
        print("Gender:", self.gender)
        print("Country:", self.country)
        print("City:", self.city)
        print("Address:", self.address)
        print("Age:", self.age)
        print("Landline Phone Number:", self.landline_phone_number)
        print("Mobile Phone Number:", self.mobile_phone_number)
        print("Email: ", self.email)
        print("Registration Date:", self.registration_date)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
        print("Username:", self.username)
        print("Password:", self.password)

    def change_info(self):
        print("1. Update Password")
        print("2. Update Landline Phone Number")
        print("3. Update Mobile Phone Number")
        print("4. Update Address")
        print("5. Update Email")

        option = input("Enter your option number: ").strip()

        print()

        if option == "1":
            self.update_password()
        elif option == "2":
            self.update_landline_phone_number()
        elif option == "3":
            self.update_mobile_phone_number()
        elif option == "4":
            self.update_address()
        elif option == "5":
            self.update_email()
        else:
            print("The entered option number is not valid.")

        print()

    def update_password(self):
        new_password = input("Enter new password: ").strip()

        print()

        if RegularUser.is_valid_password(new_password):
            self.password = new_password
            print("The password updated successfully.")
        else:
            print("The entered password is not valid.")

        print()

    def update_landline_phone_number(self):
        new_landline_phone_number = input("Enter new landline phone number: ").strip()

        print()

        if User.is_valid_landline_phone_number(new_landline_phone_number):
            self.landline_phone_number = new_landline_phone_number
            print("The landline phone number updated successfully.")
        else:
            print("The entered landline phone number is not valid.")

        print()

    def update_mobile_phone_number(self):
        new_mobile_phone_number = input("Enter new mobile phone number: ").strip()

        print()

        if User.is_valid_mobile_phone_number(new_mobile_phone_number):
            self.mobile_phone_number = new_mobile_phone_number
            print("The mobile phone number updated successfully.")
        else:
            print("The entered mobile phone number is not valid.")

        print()

    def update_address(self):
        new_address = input("Enter new address: ").strip()

        print()

        if new_address:
            self.address = new_address
            print("The address updated successfully.")
        else:
            print("The entered address is not valid.")

        print()

    def update_email(self):
        new_email = input("Enter new email: ").strip()

        print()

        if User.is_valid_email(new_email):
            self.email = new_email
            print("The email updated successfully.")
        else:
            print("The entered email is not valid.")

        print()

    def transfer_money(self):
        amount = input("Enter the amount: ").strip()
        destination_account_number = input("Enter the destination account number: ").strip()

        print()

        if not amount.isdigit() or int(amount) <= 0:
            print("The entered amount is not valid.")
            return

        amount = int(amount)

        if self.balance - amount < 20000:
            print("The account balance is insufficient.")
            return

        if not destination_account_number.isdigit():
            print("The destination account number is not valid.")
            return

        destination_account_number = int(destination_account_number)
        destination = RegularUser.search_by_account_number(destination_account_number)

        if not destination:
            print("The destination account number is not valid.")
            return

        self.balance -= amount
        destination.balance += amount

        self.save_log("transfer money", destination.firstname + " " + destination.lastname,
                      str(destination.account_number),
                      str(amount))

        print()
        print("Successful Transaction")
        print("Source Account Number:", self.account_number)
        print("Destination Account Number:", destination.account_number)
        print("Destination Account Holder:", destination.firstname + " " + destination.lastname)
        print("Amount:", amount)
        print()


def register_menu():
    print("1. Register As Admin")
    print("2. Register As User")

    option = input("Enter your option number: ").strip()

    print()

    if option == "1":
        Admin.add_admin()
    elif option == "2":
        Admin.add_user()
    else:
        print("The entered option number is not valid.")

    print()


def login_menu():
    print("1. Login As Admin")
    print("2. Login As User")

    option = input("Enter your option number: ").strip()

    print()

    if option == "1":
        login_admin()
    elif option == "2":
        login_user()
    else:
        print("The entered option number is not valid.")

    print()


def login_admin():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    Admin.login(username, password)


def login_user():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    RegularUser.login(username, password)


def main():
    Admin.load_admins()
    RegularUser.load_users()

    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        option = input("Enter your option number: ").strip()

        print()

        if option == "1":
            register_menu()
        elif option == "2":
            login_menu()
        elif option == "3":
            break
        else:
            print("The entered option number is not valid.")

        print()

        Admin.save_admins()
        RegularUser.save_users()


if __name__ == '__main__':
    main()
