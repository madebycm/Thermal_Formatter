#!/usr/bin/python
# Filename: Thermal_Formatter.py

import textwrap
wrap = textwrap.TextWrapper(width=32)

from Adafruit_Thermal import *

# Mock method, replace with Adafruit_Thermal class
# class printer:
#   def setSize(self,size):
#     pass
#   def println(self,line):
#     print wrap.fill(line)
#   def setDefault(self):
#     pass

# printer = printer()

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

def processAndPrint(text):

  #@todo
  # determine width of medium and big text
  allowed = ['s','b','br']

  i = 1
  for line in text:
    if line[0] not in allowed:
      print 'Invalid property: %s [line %d]' % (line[0], i)
      invalid = True
      break
    else: 
      invalid = False
      i += 1

  if not invalid:
    for line in text:
      prop = line[0]
      try: 
        line = line[1]
      except:
        pass
      # text sizing
      if prop in ['small','s']:
        printer.setSize('S')
        printer.println(line)
      elif prop in ['medium','m']:
        printer.setSize('M')
        printer.println(line)
      elif prop in ['big','b']:
        printer.setSize('B')
        printer.println(line)
      # other visual elements
      elif prop == 'br':
        print '-' * 32
      else:
        pass

      printer.setDefault()
