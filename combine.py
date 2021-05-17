#!/usr/bin/python

import os
import sys
import argparse

# Define Dictionary objects.
orighashdict = {}
crackedhashdict = {}

# Initialize DICT counters
origcount = 1
crackedhashcount = 1

parser = argparse.ArgumentParser(description="Parse and match values from a NTLM hash dump to cracked passwords from Hashcat")
parser.add_argument("Input_Hash_File", help="The dump file you pulled from the DC in name\\domain:hash format")
parser.add_argument("Cracked_Hash_File", help="The output from hashcat in hash:pass format")
parser.add_argument("-o", "--output", type=str, help="Output results to the specified file. Default is STDOUT.")

arguments = parser.parse_args()
orighashfile = arguments.Input_Hash_File
crackedhashfile = arguments.Cracked_Hash_File

# Filename of prepared hash file from dump. Should be username:ntlm2 hash.
# Import original hash file into dictionary object.
with open(orighashfile, "r") as origin:
    for line in origin:
        # Set NAME as key and HASH as value.
        (val1, val2) = line.rstrip('\n').split(':')
        orighashdict[origcount] = val1,val2
        origcount = origcount + 1

# Import cracked Hash file into dictionary object.
with open(crackedhashfile, "r") as hashf:
    for line in hashf:
        # Set HASH as key and cracked password as value.
        (val1, val2) = line.rstrip('\n').split(':')
        crackedhashdict[crackedhashcount] = val1,val2
        crackedhashcount = crackedhashcount +1

#set keys for dictionary compare.
#k1 = set(orighashdict.keys())
#k2 = set(crackedhashdict.keys())

orighashcount = len(orighashdict)
crackedcount = len(crackedhashdict)
print (orighashcount)
print (crackedcount)
#print (orighashdict)

for 
# Find keys(hashes) that match in both files.
#common_keys = set(k1).intersection(set(k2))

for key in common_keys:
    if orighashdict[key] != crackedhashdict[key]:
        if arguments.output:
            out_file = arguments.output
            print("[+] Writing output to file " + out_file + "for user: " + orighashdict[key])
            outputstream = open(out_file, "a+")
            outputstream.writelines(orighashdict[key] + ":" + crackedhashdict[key] + "\n")
            outputstream.close()
        else:
            # Print user:pass to screen
            print (orighashdict[key] + ":" + crackedhashdict[key])
