#Dated : 12 Dec 2014
#Author : Laksh Arora
#Site : www.laksharora.com
#Description : Retrieve backers information from kickstarter project
import re
import csv
import os
import urllib
with open('prjurl.csv', 'rb') as csvfile:
    c = 1
    spamreader = csv.reader(csvfile, delimiter=',')
    row=spamreader.next()
   #c=0
    for row in spamreader:
      c += 1
      if c > 3607:

        print  row[0], ',', row[1]
        url = row[1]+'/backers'
        print 'printing url= '
        print url
        site = urllib.urlopen(url)
        data = site.read()
        fn='kshtmlsource/'+'f'+row[0]+'.txt'
        if not os.path.exists(os.path.dirname(fn)):
          os.makedirs(os.path.dirname(fn))
        #print fn
        file = open(fn,"wb") #open file in binary mode
        file.writelines(data)
        file.close()
        fhand = open(fn,"rb")
        ocsvfn='b'+row[0]+'.csv'
        #print ocsvfn
        pn = 'ksbackers/'+ocsvfn
        if not os.path.exists(os.path.dirname(pn)):
          os.makedirs(os.path.dirname(pn))
        csvfile1=open(pn, 'w')
        for line in fhand:
             s=''
             line = line.rstrip()
             if line == '': continue
             m = re.search('<a href="/profile/(.*)">(.+?)</a>', line)
             if m:
                 found1=m.group(1)
                 found = m.group(2)
                 if re.match('<img(.*)', found):continue
                 s=found1+','+found+','
                 a4=fhand.next()
                 a4=fhand.next()
                 a4=a4.rstrip()
                 if a4 == '<p class="location">':
                   a1=fhand.next()
                   a=fhand.next()
                   a=a.rstrip()
                   s=s+a+','
                   a4=fhand.next()
                   a4=fhand.next()
                   a4=a4.rstrip()
                 else :
                   s=s+','
                 if a4== '<p class="backings">':
                    a2=fhand.next()
                    a3=fhand.next();
                    word = a3.split()
                    if word[0] == 'Backed':
                       s=s+word[1]
                    #else:
                 s=s+'\n'
                 print 's= ',s
                 csvfile1.write(s)
        csvfile1.close()
        fhand.close()

csvfile.close()

