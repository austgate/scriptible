'''
   Function to diff two texts 
'''

import difflib
#from difflib_data import *

#use ndiff since it is made for text
class differenceText:
    
    def __init__(self, a,b):
        if a is None or b is None:
            raise Exception('Path needs a string')
        
        self.a = a
        self.b = b

    def diff_text(self, tofile=False):
        '''
           Function takes to streams and then diffs them. 
           If tofile  is set to True, then writes to file, otherwise prints the stream out
        '''
        
        diff = difflib.ndiff(self.a, self.b) #a & b are text streams
         
        if tofile is True:
            self.diff_file_write(a+'_diff.txt', '\n'.join(list(diff)))
        else:
            return '\n'.join(diff)
            
            
    def diff_file_write(self, filename, difftext):
        '''
           Writes out to the file system. 
           Open needs to write appendably
        '''
        fileh = open(filename, 'wb+')
        fileh.write(difftext)
        fileh.close()
        
    def find_index (self, textstr, substr):
        return textstr.index(substr)