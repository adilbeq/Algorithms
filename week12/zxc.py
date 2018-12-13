import hashlib, sys
m = hashlib.md5()
hash = ""
hash_file = input("What is the file name in which the hash resides?  ")
wordlist = input("What is your wordlist?  (Enter the file name)  ")
try:
	hashdocument = open(hash_file,"r")
except IOError:
	print ("Invalid file.")
	raw_input()
	sys.exit()
else:
	hash = hashdocument.readline()
	hash = hash.replace("\n","")
	
try:
	wordlistfile = open(wordlist,"r")
except IOError:
	print ("Invalid file.")
	raw_input()
	sys.exit()
else:
	pass
for line in wordlistfile:
	m = hashlib.md5()
	line = line.replace("\n","")
	m.update(line)
	word_hash = m.hexdigest()
	if word_hash==hash:
		print ("Collision!  The word corresponding to the given hash is")
		raw_input()
		sys.exit()

print ("The hash given does not correspond to any supplied word in the wordlist.")
input()
sys.exit()
