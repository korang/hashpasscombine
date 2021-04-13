# hashpasscombine

Parse and match values from a NTLM hash dump to cracked passwords from Hashcat
  
Total re-write.  I am storing the orginal hash dump file and the cracked hash file in a dictionary object now.

You need to verify your hash dump file from DC is in the format name\\domain:hash format.

The output from hashcat in hash:pass format.

USAGE:  python combine.py "originaldumphashfile" "hashcatcrackedhashfile"

Output from script will be in user:pass format.

TODO:

1) ~~Accept input to write out results to file.~~
2) Figure out why the output is in reverse order (if it matters)


