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
import base64
import json

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
    request_url = f"https://sessionserver.mojang.com/session/minecraft/profile/{requestuuid}"
    
    # Fetch data and check response code
    response = get(request_url)
    if(response.status_code != 200):
        print(color('User profile not found', 'red'))                   # Error, profile not found
        exit(3)
    
    # Deseialize response JSON
    response = response.json()
    
    # Display retrieved UUID
    try:
        useruuid = uuid.UUID(response['id'])
    except:
        print(color('Couldn\'t decode retrieved UUID.', 'red'))         # Some error occured, retrieved UUID cannot be decoded
        exit(4)
    
    # Get username and properties data
    username = response['name']
    properties = response['properties']
    
    # Display username and UUID data
    print("Username".ljust(20), end='')
    print("UUID")
    print("--------------------------------------------------------")
    print(username.ljust(20), end='')
    print(useruuid, end='\n\n')
    
    # Show textures prefix
    texture_prefix = "http://textures.minecraft.net/texture/"
    print(f"Texture hash URL prefix: {texture_prefix}")
    print("\tIf given response is in parenthesis, there is default value", end='\n\n')
    
    # Display textures data
    for row in properties:
        # Decode textures data object
        decoded_object = json.loads(base64.b64decode(row['value']))['textures']
        
        # Determine skin and cape properties
        skin_texture = '(Default)'
        skin_type = '(Unknown)'
        cape_texture = '(None)'
        if 'SKIN' in decoded_object.keys():
            # Skin texture data found
            skin_texture = decoded_object['SKIN']['url'].replace(texture_prefix, '')
            
            # Check metadata
            if 'metadata' in decoded_object['SKIN'].keys():
                skin_type = 'Alex'
            else:
                skin_type = 'Steve'
        
        if 'CAPE' in decoded_object.keys():
            # Cape texture data found
            cape_texture = decoded_object['CAPE']['url'].replace(texture_prefix, '')
        
        # Display skin and cape data
        print(f"Skin type  : {skin_type}")
        print(f"Skin hash  : {skin_texture}")
        print(f"Cape hash  : {cape_texture}")

# Run only if fetched through main payload
if __name__ == '__main__':
    main()
