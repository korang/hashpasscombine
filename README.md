# hashpasscombine

Parse and match values from a NTLM hash dump to cracked passwords from Hashcat
  
Total re-write.  I am storing the orginal has dump file and the cracked hash file in a dictionary object now.

You need to verify your hash dump file from DC is in the format name\\domain:hash format.

The output from hashcat in hash:pass format.

USAGE:  python combine.py <originaldumphashfile> <hashcatcrackedhashfile>


