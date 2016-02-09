#! /usr/bin/python

import hashlib

def main():
  baseString = "CO409CryptographyEngineeringRunsNowForItsSecondYear"
  i = 1
  
  difficulty = '0x000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
  compareValue = int(difficulty, 16)

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
  n.update(m.hexdigest())
  return n.hexdigest()



if __name__ == "__main__":
  main()
