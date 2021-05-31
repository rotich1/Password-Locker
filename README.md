# PASSWORD LOCKER
### Author Kiptoo Rotich
## Description
This is a python application that allows users to save their account credentials so they can retrieve them whenever they need of forget them.
## Installation
1. Clone the project to your local machine. Use this [Link](https://github.com/rotich1/Password-Locker)
2. Change directory to the project folder.
3. If you have the pre-requisites you can run the application.
## Pre-requisites
You need to have Python3.8
To install python3.8 in terminal, run the following commands.
apt-get install python3.8
apt-get install pip3

## Running the application
1. Cd to the project folder using terminal and run ./Main.py to run the app.
 
| Behaviour                            |      Input                       |                                         Output |
| ------------------------------------ | :-------------:                  | ---------------------------------------------: |
| Select cc                            | Provide username, password and 
                                        confirm password. 
                                        Choose option 
                                        1 enter own password and option 
                                        2 for system generated password   | If success, login input is displayed, 
                                                                            else if passwords does not match, application prints 'Passwords does not match'               |
| Provide login credentials 
    i.e username and password          | username and password            | 1. Store already existing account credentials. 
                                                                            1. Create new account credentials. 3. View account credentials and passwords.  4. Delete account details. 5. Exit                                 |
|Select 1                              |username and password             |Credentials saved successfully                    |
