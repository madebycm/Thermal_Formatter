#!/usr/bin/python

# Filename: Thermal_Formatter.py
# Author: madebycm
# Url: http://madebycm.no

import textwrap
wrap = textwrap.TextWrapper(width=32,break_long_words=True)

from Adafruit_Thermal import *

try:
  printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
except:
  
  # Mock method so we can test code when printer is off-line
  class printer:
    def setSize(self,size):
      pass
    def println(self,line):
      print wrap.fill(line)
    def setDefault(self):
      pass
    def justify(self,pos):
      pass
    def feed(self,length):
      pass

  printer = printer()

class Thermal_Formatter:
  def processAndPrint(self,text):

    # @todo
    # determine width of medium and big text
    sizes = ['s','m','l','br']
    alignments = ['c','r']

    allowed = sizes + alignments

    i = 1
    for line in text:
      prop = line[0].split(':') # split regardless
      # check if we have an aligment
      try:
        if prop[1] and prop[1] not in alignments:
          print 'Invalid alignment: %s [line %d]' % (prop[1], i)
          invalid = True
          break
      except:
        pass
      if str(prop[0]).lower() not in allowed:
        print 'Invalid property: %s [line %d]' % (prop[0], i)
        invalid = True
        break
      else: 
        invalid = False
        i += 1

    if not invalid:
      for line in text:
        props = line[0].split(':')
        size = str(props[0]).lower()
        try:
          alignment = str(props[1]).lower()
        except:
          alignment = False
        try: 
          line = wrap.fill(line[1])
        except:
          pass

        # text sizing
        if size in ['small','s']:
          printer.setSize('S')

        elif size in ['medium','m']:
          printer.setSize('M')

        elif size in ['large','l']:
          printer.setSize('L')

        # alignments
        if alignment in ['c', 'center']:
          printer.justify('C')

        elif alignment in ['r','right']:
          printer.justify('R')

        # other visual elements
        if size == 'br':
          line = '-' * 32 # linebreak

        else:
          pass

        # print
        printer.println(line)
        # 'n clear
        printer.setDefault()

    printer.feed(4)
