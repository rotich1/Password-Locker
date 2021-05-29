
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
        
    def saveUser(self):
        """
        This method saves user
        """
        User.users.append(self)
    
    def loginMessage(self):
        """
        This method diplays to user upon successful login
        """
        print("Login successful")
        
    @classmethod
    def displayUsers(display):
        return display.users
        
    
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
            
            
            
    def main():
        while True:            
            options = input("Hey there, what's  your name? ")
            prompt_selection = input(f"How can I help you {options}. \nKindly select the option you would like to do using number:\n 1. Store already existing account credentials.\n 2. Create new account credentials.\n 3. View account credentials and passwords. \n 4. Delete account details.")
