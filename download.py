'''
  Functions to download the Gutenberg index and specified texts
  
  '''
import zipfile, os
from urllib2 import urlopen, URLError

def download(text=None, identifier=None): 
    '''
       Function to get the index if text is none. 
       @param text if this is none, we assume that index is being downloaded
    '''

    if text is None:
        _download_index()
    else:
        _download_text(text,identifier)

def _download_index():
    '''
       Function to download the index archive
       '''
    try:
        archiveresponse = urlopen('http://www.gutenberg.org/feeds/catalog.rdf.zip')
        with open(os.path.basename("catalog.rdf.zip"), "wb") as archive_file:
            archive_file.write(archiveresponse.read())
    except URLError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code

def _extract_index (archive):
    '''
        Function to extract the archive. Extracts to current directory.
        Perhaps this shoudl be changed. 
        @param archive - name of the archive
    '''
    try:
        zf = zipfile.ZipFile(archive)
        zf.extract("catalog.rdf")
    except KeyError:
        print KeyError

        
def _download_text(title, identifier):
    '''
      Gutenberg appears to blocking scripts reading them. 
      Internet Archive appears to have the texts on it so using this for now
      @param title title from the catalogue
      @param identifier the text id from the catalogue
    '''
    try:
        if identifier is None or title is None:
            raise Exception("Must have an identifier or text to download a stream" )
        
        #archive.org stream appears to be first 18 characrters - gutenberg id - gut/
        url = 'http://archive.org/stream/'+title[:18].lower().replace(' ', '')+identifier+'gut/'+identifier+'.txt'
        fileresponse = urlopen(url)
        contents = fileresponse.read()
        if contents:
            f = open('../data'+identifier + '.txt', 'wb')
            f.write(contents)
            f.close()
    except Exception:
        print Exception