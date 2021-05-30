import random
from unittest.main import main


class User:
    def __init__(self, email, password, confirmPassword):
        self.email = email
        self.password = password
        self.confirmPassword = confirmPassword
        
    users = []

    def createUser(email, password, confirmPassword):
        """
        This method creates a new user
        """
        newUser = User(email, password, confirmPassword)
        return newUser
        
    def saveUser(email, password):
        """
        This method saves user
        """
        newUser=[email, password]
        User.users.append(newUser)
    
    def loginMessage():
        """
        This method diplays to user upon successful login
        """
        print("Login successful")
        
    @classmethod
    def displayUsers(self):
        for user in self.users:
            return user
        
    
    @classmethod
    def deleteUsers(self):
        User.users.remove(self) 
        
        

class Credentials:
    def __init__(self, username, password):
        """
        This is a credentials constructor 
        """
        self.username = username
        self.password = password

    credentials = []
    
    def createNewCredentials(self, username, password):
        """
        This method creates new credentials
        """
        newCredentials = Credentials(username, password)
        return newCredentials
    
    def save_credentials(self, username, password):
        """
        This methods saves credentials
        """
        Credentials.credentials.append(self)
        
    def display_credentials(self,credentials):
        for credential in credentials:
            print(credential.username+" - "+credential.password)   
    
    def check_existance(self, email):
        """
        This is a method to check the existatnce of data
        """
        if Credentials.credentials:
            for credential in Credentials.credentials:
                if credential.email == email:
                    return True
            print("Details in the account provided doesn't exist")
        else:
            print("No saved data yet")
    
    def deleteCredential(accountName):
        """
        This method will delete user credentials
        """
        for credential in Credentials.credentials:
            if credential.username == accountName:
                Credentials.credentials.remove(credential)
            
            
   
def main():
    while True:    
        # print("*"*50)
        options = input("Hey there, what's  your name? ")
        login_options = input(f"How can I help you {options}. Kindly select option using the following short codes:\n cc - Create account.\n lg - Login")
        # print("*"*50)
        if login_options == 'cc':
            username = input("Enter username / email address: \n")
            
            passwordoption = input(
                "Choose password option: \n 1. Enter password\n2. Use autogenerated password\n")
            
            if passwordoption == "1":                
                password = input("Enter password: \n")
                
                confirmPassword = input("Confirm password: \n")
                
                if password == confirmPassword:
                    print("Welcome to password locker. Login")
                    User.createUser(username,password,confirmPassword)
                    User.saveUser(username, password)
                    print(f"Account created successfully with {username} as username")
                    print("\n")
                                                   
                                    
            elif passwordoption == "2":
                password1 = random.randint(10000, 90000)
                User.saveUser(username, password1)
            print(f"Account created successfully with user {username}.\n")
            print("Password is ")
            print(password1)
                # break
            
        else:
            print("Invalid input")
                
        print("*"*50)
        print("Welcome to password locker. Login\n")
        print("Enter your username: \n")
        login_username = input()
        print("\n")
        
        print("Enter your password: \n")
        login_password = input()
        print(User.users)
        for credential in User.users:
            if credential[0] == login_username and credential[1] == int(login_password):
                prompt_selection = input("Kindly select the option you would like to do using number:\n 1. Store already existing account credentials.\n 2. Create new account credentials.\n 3. View account credentials and passwords. \n 4. Delete account details.")
                            
                if prompt_selection == "1":
                    for user in User.users:
                        Credentials.save_credentials(username, password)
                    print(f"Your credentials {user} have been save successfully.")
                
                elif prompt_selection == "2":
                    newAccount = input("Enter your username: \n")
                    
                    newPassword = input("Enter your password: \n")
                    Credentials.createNewCredentials(newAccount, newPassword)
                    Credentials.save_credentials(newAccount, newPassword)
                    break
                
                elif prompt_selection == "3":
                    Credentials.display_credentials(Credentials.credentials)
                
                elif prompt_selection == "4":
                    accountName = input("Enter username of the credential to delete: \n")
                    Credentials.deleteCredential(accountName)
                    print(f"Credential with username {accountName} deleted successfully")
                
                else:
                    print("Invalid selection")
            else:
                print("Incorrect username or password")
                break
       
        
if __name__ == '__main__':
    main()
