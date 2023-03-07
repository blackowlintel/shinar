import requests
import json
import sys
import re
import datetime
from colorama import Fore, Back, Style

#MANDATORY ASCII ART MOMENT

print(Fore.BLUE + "      _      _         _  _         ")
print(Fore.BLUE + " ___ | |__  / | _ __  | || |   _ __ ")
print(Fore.BLUE + "/ __|| '_ \ | || '_ \ | || |_ | '__|")
print(Fore.BLUE + "\__ \| | | || || | | ||__   _|| |   ")
print(Fore.BLUE + "|___/|_| |_||_||_| |_|   |_|  |_|   ")
print(" ")                      
print(Fore.RED + "+-++-+ +-++-++-++-++-++-++-++-+ +-++-++-++-++-++-++-++-++-++-")
print(Fore.RED + "|B||l||a||c||k||o||w||l| |i||n||t||e||l||l||i||g||e||n||c||e|")
print(Fore.RED + "+-++-+ +-++-++-++-++-++-++-++-+ +-++-++-++-++-++-++-++-++-++-")
print(Fore.GREEN + "Written by m4v3r1ck and 3stkh" + Style.RESET_ALL) 

# Get email address from user input
if len(sys.argv) != 2:
    print("Please provide an email argument for execution.")
    sys.exit(1)
email = sys.argv[1]

# validate the email using regular expressions
if not re.match(r"^\S+@\S+\.\S+$", email):
    print("Invalid email address provided.")
    sys.exit(1)


# Construct API URL with email parameter
url = f"https://www.duolingo.com/2017-06-30/users?email={email}"

# Make request to API and get response
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

# Check response status code
if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

# Get JSON content from response
json_content = json.loads(response.content)

# Replacing None Values
for key in json_content:
    if json_content[key] is None:
        json_content[key] = ""


# Define the headers for the user table
user_headers = ["ID", "Username", "Name", "Location", "Email Verified", "Has Facebook ID", "Has Google ID", "Profile Country", "Creation Date"]


# Define the headers for the courses table
course_headers = ["Title", "XP", "Crowns", "From Language"]

# Printing tables
print(" ")
print(" ")
print(Fore.GREEN + "User Information")
print(" ")
# Print the user table headers
print(Fore.BLUE + "{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*user_headers) + Style.RESET_ALL)

# Print a line of dashes under the user table headers
print("-" * 180)

# Iterate through the users and print the required fields in a table format
for user in json_content['users']:
    user_id = user.get('id', '')
    username = user.get('username', '')
    name = user.get('name', '')
    location = user.get('location', '')
    email_verified = user.get('emailVerified', '')
    has_facebook_id = user.get('hasFacebookId', '')
    has_google_id = user.get('hasGoogleId', '')
    profile_country = user.get('profileCountry', '')
    creation_date = datetime.datetime.fromtimestamp(user.get('creationDate', '')).strftime('%d-%m-%Y')

    # Replace None values with empty string
    user_data = [user_id, username, name, location, email_verified, has_facebook_id, has_google_id, profile_country, creation_date]
    user_data = [" " if value is None else value for value in user_data]

    print("{:<10} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(*user_data))
    print("-" * 180)

    print(" ")
    # get and print the picture URL
    
    user_picture = json_content['users'][0]['picture']
    print(Fore.RED + "User Picture URL:")
    print(" ")
    print(Fore.YELLOW + "http:"+f"{user_picture}"+"/xxlarge")
    print(" ")
    print(" ")
    print(Fore.GREEN + "Courses Info")
    print(" ")

    # Print the courses table headers
    print(Fore.BLUE + "{:<20} {:<10} {:<10} {:<20}".format(*course_headers) + Style.RESET_ALL)
    # Print a line of dashes under the courses table headers
    print("-" * 60)

    # Iterate through the courses and print the required fields in a table format
    for course in user['courses']:
        title = course.get('title', '')
        xp = course.get('xp', '')
        crowns = course.get('crowns', '')
        from_lang = course.get('fromLanguage', '')

        # Replace any None values with empty strings
        course_info = [title, xp, crowns, from_lang]
        for i in range(len(course_info)):
            if course_info[i] is None:
                course_info[i] = ''

        print("{:<20} {:<10} {:<10} {:<20}".format(*course_info))

    # Print a line of dashes between users
    print("-" * 60)



