#!/usr/bin/env python3

# ------------------------------------------------------------------------------------
# Mojang API Python scripts made by CZghost/Polda18
# Script name: Mojang Status
#
# Usage: Simply run python3 mojang_status.py
# ------------------------------------------------------------------------------------

# Import necessary libraries
#import json

from requests import get
from termcolor import colored as color

# Create payload
def main():
    # This is new response
    print("This service was closed down by Mojang, due to incorrect responses.")
    print("Status check was made for a legacy system that is currently not up to date.")

# For historical reasons, I decided to rename the old code - it is not used anywhere
def old_main():
    # Fetch data
    request_url = "https://status.mojang.com/check"
    response = get(request_url)
    
    # Check response code
    if(response.status_code != 200):
        print(color("Couldn't check status", "red"))        # Error, status couldn't be checked
        exit(1)
    
    # Deserialize response JSON
    response = response.json()
    
    # Fetch all servers from list
    for row in response:
        for key, value in row.items():
            server = key
            colorcode = value
            
            # Decode color codes
            if(colorcode == 'red'):
                status = 'down'
            elif(colorcode == 'yellow'):
                status = 'partially down'
            elif(colorcode == 'green'):
                status = 'fully operational'
            else:
                status = 'status not available'
            
            # If color code is anything else than traffic light colors, display white
            if(colorcode != 'red' and colorcode != 'yellow' and colorcode != 'green'):
                colorcode = 'white'
            
            # Display server status
            print(f"API Server `{server}`".ljust(50), end=f"status `{color(status, colorcode)}`\n")
            #print(f"status `{color(status, colorcode)}`")

# Run only if fetched through main payload
if __name__ == "__main__":
    main()
