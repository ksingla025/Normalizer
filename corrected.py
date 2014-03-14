#!/usr/bin/python

import re,sys,commands

dic=[]
rgx = re.compile("((?::|;|=|<)(?:-)?(?:\)|D|P|p|3))")
single_char = {"b":"bee","B":"bee", "c":"see","C":"see", "d":"the", "D":"the","k":"okey","K":"okey","m":"am","M":"am","qs":"question","Qs":"question","r":"are","R":"are", "s":"ass", "S":"ass","u":"you","U":"you", "v":"we","V":"we","x":"times", "X":"times","y":"why", "Y":"why"}

dictionary = open("big.txt",'r')
for line in dictionary:
        line=line.strip()
        dic += [line]
for line in sys.stdin:
        sent=[]
        line = re.sub('[\^$]', '', line)
#       print line
        words=line.split()
#       print words
        for word in words:
                candidates=word.split('/')
                for candidate in candidates:
#                       print candidate
                        if candidate in dic:
                                candidates[0]= candidate
    
                sent +=[candidates[0]]
#               print sent
        sys.stdout.write(" ".join(sent)+'\n')
    
