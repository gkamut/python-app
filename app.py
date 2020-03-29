from datetime import datetime
import socket

def get_Host_name_IP():
   try:
      host_name = socket.gethostname()
      host_ip = socket.gethostbyname(host_name)
      print("Hostname: ", host_name)
      print("IP: ", host_ip)
   except:
      print("Unable to get Hostname and IP")

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
get_Host_name_IP()
