import sys
import telnetlib

if len(sys.argv) != 4:
  raise ValueError('Please pass HOST, USER and PASS arguments')

host, user, password = sys.argv[1:]

tn = telnetlib.Telnet(host)
tn.read_until(b"login: ")

tn.write(user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

tn.write(b"reboot\n")
tn.write(b"exit\n")

print (tn.read_all().decode( 'ascii' ))