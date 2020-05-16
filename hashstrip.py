#!/bin/python3
import os
import sys

#Strips the hashes from the unshadow file and creates a file for hashcat

print("*" * 25)
print("Hashstrip by Laurence Curling")
print("*" * 25)
print("\n" * 3)

f = open("shadow.txt", "r")

for x in f:
	s = x.split(":")
	for line in s:
		if line.startswith("$"):
			with open("result.txt", "a") as result:
				result.write(line + "\n")
				print(line)
f.close()
		
os.system("john --wordlist=/usr/share/wordlists/rockyou.txt result.txt")
exit()	
