# hashpasscombine

Parse and match values from a NTLM hash dump to cracked passwords from Hashcat
  
Total re-write.  I am storing the orginal hash dump file and the cracked hash file in a dictionary object now.

You need to verify your hash dump file from DC is in the format name\\domain:hash format.

The output from hashcat in hash:pass format.

USAGE:  python3 hashpasscombine.py "originaldumphashfile" "hashcatcrackedhashfile" ( -o "outputfile")

Output from script will be in user:pass format.

EXAMPLE:

In the Example folder there are examples to see. The MIMIKATZ files are example dumps from my lab Domain Controller. The formattedfile.txt shows the format the orignal file shoudl be in to be processed. The examplecrackfile.txt show output form hashcat. Exampleoutput.txt shows what combine.py will gave as the output. The command I used to create the exampleout.txt was:
	python3 hashpasscombine.py formattedfile.txt examplecrackfile.txt -o exampleoutput.txt

TODO:

1) ~~Accept input to write out results to file.~~
2) Figure out why the output is in reverse order (if it matters)


