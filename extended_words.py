import sys,re,collections
array=[]                                                                                                                        
sent=[]
rgx = re.compile("((?::|;|=|<)(?:-)?(?:\)|D|P|p|3))")
single_char = {"b":"bee","B":"bee", "c":"see","C":"see","d":"the","D":"the","k":"okey","K":"okey","m":"am","M":"am","qs":"question","Qs":"question","r":"are","R":"are","s":"ass","S":"ass","u":"you","U":"you","v":"we","V":"we","x":"times", "X":"times","y":"why","Y":"why"}

def compute(string,pos,temp):
  if pos>=len(string):
     array.append(temp);
     return
  if pos==len(string)-1:
    array.append(temp+string[pos])
    return 
  if string[pos]!=string[pos+1]:
    compute(string,pos+1,temp+string[pos])
  else: 
    compute(string,pos+2,temp+string[pos]+string[pos+1])
    compute(string,pos+2,temp+string[pos]) 
  return  
#fp=open(sys.argv[1],'r')
#lines=fp.readlines()
for line in sys.stdin:
  lis=line.split()
  emotions = rgx.findall(line)
  for j in range(len(lis)):
    if lis[j] in single_char:
        lis[j] = single_char[lis[j]]
    if lis[j] in emotions:
        lis[j] = '{emotion}'

    coun=1
    string="" 
    for k in range(1,len(lis[j]),1):
      if lis[j][k]==lis[j][k-1]:
        coun=coun+1
      else: 
        if coun>=2:
          string=string+lis[j][k-1]+lis[j][k-1]
        else: 
          string=string+lis[j][k-1]
        coun=1
    if coun>=2:
      string=string+lis[j][len(lis[j])-1]+lis[j][len(lis[j])-1]
    else: 
      string=string+lis[j][len(lis[j])-1]
    compute(string,0,"")
    if(len(array)==1):
       n = 0
#       temp1=lis[j]+lis[j]+"\\"+temp1
       temp1= lis[j]+"/"+lis[j]
    else:
      temp1="/".join(array)
      temp1=lis[j]+'/'+lis[j]+"/"+temp1
#    sent += [temp1]
#    print temp1        
    del(array[:])
    sent += [temp1+'$']
#    print sent

  output = ' ^'.join(sent)
  sys.stdout.write('^'+output+'\n')
  del(sent[:])
