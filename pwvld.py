import re, sys
s=input("Enter password to be validated:")
if len(s) < 8 :
	print("Weak password")
	sys.exit()
if re.search(r'[a-z]', s) :
	if re.search(r'[A-Z]', s) :
		if re.search(r'[0-9]', s) :
			print("Strong password")
			sys.exit()
print("Weak password")
	
