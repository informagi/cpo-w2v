#!/usr/bin/python

import sys, getopt
from IPython.lib import passwd

def main(argv):
   mypwd = 'copd';
   try:
      opts, args = getopt.getopt(argv,"hp:",["pwd="])
   except getopt.GetoptError:
      print('pwd.py -p password')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -p <password>')
         sys.exit()
      elif opt in ("-p", "--pwd"):
         mypwd = arg
   print("'{}'".format(passwd(mypwd)))
         
if __name__ == "__main__":
   main(sys.argv[1:])
