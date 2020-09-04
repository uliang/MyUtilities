
ITERATOR_LEN = -1 
OVERFLOW = 2147483647


class _Chunker :
    """
    Yields lists of length buffer from iterator. Each yield returns the first buffer-1 items,
    the next yield, the next buffer-1 items. The final yield returns the remaining items 
    in the iterator. 

    Set buffer to -1 to buffer the entire iterator into a single list and return that. 
    """
    def __init__(self, iterator, buffer:int) :
        self._iterator = iterator 
        self._buffer = buffer

    def __call__(self) : 
        chunk = []
        for i, item in enumerate(self._iterator): 
            if i == OVERFLOW: 
                raise OverflowError("Too many items!")
            
            chunk.append(item) 
            
            if (i+1) % self._buffer == 0 and self._buffer != ITERATOR_LEN: 
                yield chunk
                chunk = [] 
        yield chunk

def Chunker (iterator, buffer) :
    return _Chunker(iterator, buffer)()