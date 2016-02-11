#! /usr/bin/python

import hashlib

def main():
  baseString = "CO409CryptographyEngineeringRunsNowForItsSecondYear"
  i = 1
  
  #set the difficulty as 6 zeroes followed by alls fs. We need
  #to get less than or equal to this value to start with 6 zeroes.
  difficulty = '0x000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'

  #convert above hex string to an integer (base 16 to base 10)
  comparevalue = int(difficulty, 16)

  while(True):
    toHash = baseString + str(i)
    hashed = doubleSHA256Hash(toHash)
    if (int(hashed, 16) <= compareValue):
      print 'Done. String: ' + toHash  
      print 'Hash: ' + hashed
      return
    i = i + 1
 

def doubleSHA256Hash(toHash):
  m = hashlib.sha256()
  m.update(toHash)
  n = hashlib.sha256()

  #hash the string and output byte form (digest) 
  n.update(m.digest())

  #hash these bytes but return the hex for comparison
  return n.hexdigest()



if __name__ == "__main__":
  main()
