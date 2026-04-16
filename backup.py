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


now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
filename = f"config_{now}.txt"

try:
    with ConnectHandler(**ios_device) as net_connect:
        print("Fetching configuration...")
        config_data = net_connect.send_command('show running-config')
        
        with open(filename, 'w') as f:
            f.write(config_data)
            
    print(f"Backup successful! Saved to: {filename}")

except Exception as e:
    print(f"Failed: {e}")
