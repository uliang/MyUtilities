from unittest import TestCase 
from src.chunker import Chunker 

class TestChunker(TestCase) : 
    def test_chunker_yields_list_with_buffered_size(self) : 
        chunks = Chunker(range(5), 3)
        chunk = next(chunks)
        
        self.assertEqual(len(chunk), 3)
        self.assertListEqual(chunk, [0,1,2])
        
        next_chunk = next(chunks)

        self.assertListEqual(next_chunk, [3,4])

    def test_setting_neg1_on_buffer_yields_entire_list(self) : 
        chunks = Chunker(range(5), -1)
        chunk = next(chunks)

        self.assertListEqual(chunk, [0,1,2,3,4])