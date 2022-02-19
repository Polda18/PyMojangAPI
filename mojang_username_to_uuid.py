#!/usr/bin/env python3

# ------------------------------------------------------------------------------------
# Mojang API Python scripts made by CZghost/Polda18
# Script name: Mojang Status
#
# Usage: Simply run python3 mojang_username_to_uuid.py <username>
# ------------------------------------------------------------------------------------

# Import necessary libraries
#import json

from requests import get
from termcolor import colored as color

import sys
import uuid

# Create payload
def main():
    # Check given arguments (only 1 accepted, ignore rest)
    if(len(sys.argv) < 2):
        print("No argument given.")
        exit(1)
    
    # Fetch data
    username = sys.argv[1]
    request_url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = get(request_url)
    
    # Check response code
    if(response.status_code != 200):
        print(color("Invalid entry or profile doesn't exist", "red"))
        exit(2)
    
    # Deserialize response JSON
    response = response.json()
    
    # Fetch username and UUID
    username = response["name"]
    try:
        useruuid = uuid.UUID(response["id"])
    except:
        print(color('Retrieved UUID is invalid.', 'red'))       # Some error occured, retrieved UUID cannot be decoded
        exit(3)
    
    # Display data
    print("Username".ljust(20), end="UUID\n")
    #print("UUID")
    print("--------------------------------------------------------")
    print(username.ljust(20), end=f'{useruuid}\n')
    #print(useruuid)

# Run only if fetched through main payload
if __name__ == '__main__':
    main()
