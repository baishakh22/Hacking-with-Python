from pwn import *
import sys

if len(sys.argv) != 2:
	print("Ivalid arguments!")
	print(">> {} <sha256sum>".format(sys.argv[0]))
	exit()

wanted_hash = sys.argv[1]
password_file = "file_list.txt"
attempts = 0


# log.progress which get imported from the pwntools module. 
with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:			# log can use to print out status messages during exploitation.
	with open(password_file, "r", encoding='latin-1') as password_list:
		for password in password_list:
			password = password.strip("\n").encode('latin-1')  						# Clean up the file and all word will be in new line
			password_hash = sha256sumhex(password)
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
			if password_hash == wanted_hash:
				p.success("Password hash found after {} attempts! Hash value for '{}' is: {}".format(attempts, password.decode('latin-1'), password_hash))
				exit()
			attempts += 1
		p.failure("Password has not found!")