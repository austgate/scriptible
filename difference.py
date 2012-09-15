'''
   Function to diff two texts 
'''

import difflib
from difflib_data import *

#use ndiff since it is made for text
class Difference:

    def diff_text(self, a, b, tofile=False):
        '''
           Function takes to streams and then diffs them. 
           If tofile  is set to True, then writes to file, otherwise prints the stream out
        '''
        if a is None or b is None:
            raise Exception('Path needs a string')
        diff = difflib.ndiff(a, b) #a & b are text streams
        
        if tofile is True:
            self.diff_file_write(a+'_diff.txt', '\n'.join(list(diff)))
        else:
            print '\n'.join(list(diff))
            
            
    def diff_file_write(self, filename, difftext):
        '''
           Writes out to the file system. 
           Open needs to write appendably
        '''
        fileh = open(filename, 'wb+')
        fileh.write(difftext)
        fileh.close()