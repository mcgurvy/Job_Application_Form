import re
import csv

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def collect_user_info():
    print("Welcome to the Job Application Form")
    
    name = input("Enter your full name: ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email format. Please try again.")
        email = input("Enter your email address: ")

    phone = input("Enter your phone number (10 digits): ")
    while not validate_phone(phone):
        print("Invalid phone number. Please enter exactly 10 digits.")
        phone = input("Enter your phone number: ")

    address = input("Enter your address: ")
    position = input("Position you are applying for: ")
    education = input("Enter your highest education: ")
    experience = input("Describe your work experience: ")
    skills = input("List your skills: ")
    references = input("List your references (comma-separated names): ")

    application_data = {
        'Name': name,
        'Email': email,
        'Phone': phone,
        'Address': address,
        'Position': position,
        'Education': education,
        'Experience': experience,
        'Skills': skills,
        'References': references
    }

    return application_data

def save_application_to_csv(data):
    with open('job_applications.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())
    print("Application data saved to 'job_applications.csv'.")

# Collect user info and save it to CSV
user_info = collect_user_info()
save_application_to_csv(user_info)
