#!/usr/bin/env python3

# ------------------------------------------------------------------------------------
# Mojang API Python scripts made by CZghost/Polda18
# Script name: Mojang Status
#
# Usage: Simply run python3 mojang_uuid_to_username_history.py <uuid>
# ------------------------------------------------------------------------------------

# Import necessary libraries
import json

from requests import get
from termcolor import colored as color

import sys
import uuid
import time

# Create payload
def main():
    # Check given arguments (only 1 accepted, ignore rest)
    if(len(sys.argv) < 2):
        print("No argument given.")
        exit(1)
    
    # Validate UUID format and convert it to the correct display format
    useruuid = sys.argv[1]
    try:
        useruuid = uuid.UUID(useruuid)
    except:
        print(color('Invalid entry. Try again.', 'red'))                # Error, invalid entry
        exit(2)
    
    # Convert UUID to variant without dashes for data fetch
    requestuuid = str(useruuid).replace('-', '')
    request_url = f"https://api.mojang.com/user/profiles/{requestuuid}/names"
    
    # Fetch data and check response code
    response = get(request_url)
    if(response.status_code != 200):
        print(color('User profile not found', 'red'))                   # Error, profile not found
        exit(3)
    
    # Deserialize response JSON
    response = response.json()
    
    # Display data
    print(f"UUID: {useruuid}", end='\n\n')
    print('Username'.ljust(30), end='Change Timestamp\n')
    #print('Change Timestamp')
    print('-------------------------------------------------------------------')
    for row in response:
        print(row['name'].ljust(30), end='')
        if 'changedToAt' in row.keys():
            ts = row['changedToAt']//1000                               # Convert milliseconds into seconds
            ts = time.strftime("%dth %B %Y %H:%M:%S", time.gmtime(ts))  # Convert UNIX timestamp to readable date&time format in UTC timezone
            print(f"{ts} UTC")
            # Credit: Iselink, Sasi
        else:
            print('n/a')                                                # No timestamp found

# Run only if fetched through main payload
if __name__ == '__main__':
    main()
