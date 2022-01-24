#python program to get IP adress
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is"+hostname)
print("your computer IP adress is: "+ IPAddr)