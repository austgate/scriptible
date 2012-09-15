import nltk

from collections import defaultdict


class Extraction:
    
    def extract_nep(self, text):
        '''
           Function extracts the entities from the text
           @param text stream of text to be parsed
           @return set of nodes and their entities
        '''
        nep = []
        try:
            for sent in nltk.sent_tokenize(text):
                for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))): 
                    if hasattr(chunk, 'node'):
                        rnep = ' '.join(c[0] for c in chunk.leaves())
                        nep.append(self._clean_node(chunk.node)+'::'+rnep)
        except Exception:
            print "Exception raised in the parsing ", Exception[0]
        
        return nep
    
    def extract_count(self, orig_term):
        ''' 
           Function to return a count of the number of times a term exists in text
           @param orig_set the original set of terms and their node type
           @return dictionary of terms and counts
        '''
        term_count = defaultdict(int)
        
        for v in orig_term:
            node,term = v.split('::')
            term_count[term]+= 1
        
        return term_count
    
    
    def extract_author (self, termlist):
        book = []
        for v in termlist:
            term, node = v.split('::')
            if term == "http://xmlns.com/foaf/0.1/name":
                book.append(node)
        return book
    
    def extract_book (self, termlist):
        book = []
        for v in termlist:
            term, node = v.split('::')
            print term
            if term == "http://purl.org/dc/elements/1.1/title":
                book.append(node)
        return book
    
    def _clean_node (self, node):
        
        if node == "PERSON":
            return node.replace("PERSON", "foaf:name")
        elif node == "ORGANIZATION":
            return node.replace("ORGANIZATION", "dc:title")
        elif node == "GPE":
            return node.replace("GPE", "dc:title")