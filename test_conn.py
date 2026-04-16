from netmiko import ConnectHandler
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

ios_device = {
    'device_type': os.getenv('DEVICE_TYPE'),
    'host': os.getenv('HOST'),
    'username': os.getenv('USER'),
    'password': os.getenv('PASS'),
    'port': int(os.getenv('PORT', 22)), 
}

print(f"Connecting to CISCO Sandbox via {ios_device['host']}...")

try:
    with ConnectHandler(**ios_device) as net_connect:
        print("Connected successfully!")
        
        output = net_connect.send_command('show install active summary')
        print("Device Output:")
        print(output)
        
except Exception as e:
    print(f"Connection failed: {e}")
