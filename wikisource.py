from urllib2 import urlopen, URLError
import os, re


'''
       Function to download the index archive
'''
title = "De_Cive"
try:
    
    archiveresponse = urlopen('http://en.wikisource.org/w/index.php?action=raw&title='+ title)
    with open(os.path.basename(title+".txt"), "wb") as archive_file:
        archive_file.write(archiveresponse.read())
except URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
except Exception, fe:
    print 'Exception', fe
#need to parse wiki text - need to find [[]] as this is for urls    
txtf = open(os.path.basename(title+".txt"), "rb").read()

urls =re.findall('\[\[/.*\]\]', txtf, re.IGNORECASE) #all we need is the urlds
for links in urls:
    links = links.replace('[[','').replace(']]','')
    if not links.startswith('/'):
        continue
    else:
        for g in links.split('|'):
            if g.startswith('/'):
                try:
                    print 'http://en.wikisource.org/wiki/'+title+g.replace(' ', '_')+'?action=raw'
                    response = urlopen('http://en.wikisource.org/wiki/'+title+g.replace(' ', '_')+'?action=raw')
                    with open(os.path.basename(g.replace(' ', '_')+".txt"), "wb") as archive:
                        try:
                            archive.write(response.read())
                        except Exception, e:
                            print e 
                except URLError, e:
                    if hasattr(e, 'reason'):
                        print 'We failed to reach a server.'
                        print 'Reason: ', e.reason
                    elif hasattr(e, 'code'):
                        print 'The server couldn\'t fulfill the request.'
                        print 'Error code: ', e.code  