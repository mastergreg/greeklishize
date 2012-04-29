#!/usr/bin/env python
# -*- coding: utf-8
#
#* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
# File Name : greeklishize.py
# Creation Date : 29-04-2012
# Last Modified : Sun 29 Apr 2012 01:53:03 PM EEST
# Created By : Greg Liras <gregliras@gmail.com>
#_._._._._._._._._._._._._._._._._._._._._.*/
from string import maketrans,translate

def main():
    while 1:
        try:
            text = raw_input()
            text = text.decode('utf-8')
            text = text.encode('iso-8859-7', 'replace')
            from_chars = u'áâãäåæçèéêëìíîïðñóòôõö÷øùÜÝÞßúÀüýûàþÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÓÔÕÖ×ØÙ¶¸¹ºÚ¼¾Û¿'.encode('latin1')
            to_chars =  u'abgdezh8iklmn3oprsstufxywaehiiiouuuwABGDEZH8IKLMNJOPRSTYFXCWAEHIIOUUW'.encode('latin1')
            trantab = maketrans( from_chars, to_chars )
            #trantab = dict((ord(a), b) for a, b in zip(from_chars, to_chars))
            text = translate( text, trantab )
            print text
        except EOFError:
            exit(0)

if __name__=="__main__":
    main()

