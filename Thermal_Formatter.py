#!/usr/bin/python
# Filename: Thermal_Formatter.py

import textwrap
wrap = textwrap.TextWrapper(width=32)

def hehe():
  print "hehe"

def MINGO():
  print "BINGO"

# Mock method, replace with Adafruit_Thermal class
class printer:
  def setSize(self,size):
    pass
  def println(self,line):
    print wrap.fill(line)

printer = printer()

def processAndPrint(text):

  #@todo
  # determine width of medium and big text
  allowed = ['s','b','br']

  i = 1
  for line in output:
    if line[0] not in allowed:
      print 'Invalid property: %s [line %d]' % (line[0], i)
      invalid = True
      break
    else: 
      invalid = False
      i += 1

  if not invalid:
    for line in output:
      prop = line[0]
      try: 
        line = line[1]
      except:
        pass
      if prop == 'small' or prop == 's':
        printer.setSize('S')
        printer.println(line)
      elif prop == 'medium' or prop == 'm':
        printer.setSize('M')
        printer.println(line)
      elif prop == 'big' or prop == 'b':
        printer.setSize('B')
        printer.println(line)
      elif prop == 'br':
        print '-' * 32
      else:
        pass

output = [
    ['s',   'Hello my son, how are you doing today?']
  , ['b',   'But as the pleasing continues this is my very long message.']
  , ['br']
]

processAndPrint(output)