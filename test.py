import paramiko
import time

# Define your network device details
host = '192.168.10.100'
username = 'vayu'
password = 'vayu'

# Establish an SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=username, password=password, allow_agent=False, look_for_keys=False)

# Send configuration commands
commands = [
    'conf t',
    'interface loopback0',
    'ip address 1.1.1.1 255.255.255.0',
    'no shutdown',
    'end'
]

for command in commands:
    ssh.send(command + '\n')
    time.sleep(1)  # Allow time for the device to process the command

# Close the SSH connection
ssh.close()
