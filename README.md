# Send Email for Valid Email Addresses

Simple python program that validates the email addresses and send emails while log the invalid emails

## Getting started:
##### (eg. in any Linux distribution, you can follow a similar process in another os also.)

1. Create a project root directory in your local machine
```bash
mkdir <project_name> 
```
2. Clone the project in this <project_name> directory (you can use ssh also)
   
3. Create your virtual environment, activate that environment and install all the requirements
```bash
pip install -r requirements.txt
``` 
4. collect all static files (if run for the first time it creates the assests folder in <project_name> directory)
```bash
django-admin collectstatic
```
5. Create `env.py` inside `<project_name/`. Copy from `env.example.py` for the first time and update settings as your requirements.

6. To run program 
```bash
python3 send_email.py
```
7. To run test cases
```bash 
python3 test_cases.py
```
