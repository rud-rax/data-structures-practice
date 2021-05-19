
import unittest
import hashtable2 as ht2

class TestHashtableMethods(unittest.TestCase):
    
    def test_create_hashtable1(self): 
        length, probing = map(int,input("ENTER THE LENGTH AND PROBING OF THE HASH TABLE --> ").rstrip().split())
        hashtable = ht2.HashTable(length,probing)
        self.assertEqual(hashtable,ht2.HashTable(length,probing))
        
    def test_create_hashtable2(self): 
        length, probing = 10 , 1
        hashtable = ht2.HashTable(length,probing)
        self.assertEqual(hashtable,ht2.HashTable(length,probing))

    def test_create_hashtable3(self): 
        length, probing = 10,2
        hashtable = ht2.HashTable(length,probing)
        self.assertEqual(hashtable,ht2.HashTable(length,probing))

    # def insert_hashtable_test1(self):
    #     length, probing = map(int,input("ENTER THE LENGTH AND PROBING OF THE HASH TABLE --> ").rstrip().split())
    #     hashtable = ht2.Hashtable(length,probing)
    #     self.assertEqual(hashtable,ht2.Hashtable(length,probing))
    #     test_data = [
    #         [9900,"rud"],
    #         [9999,"keo"],
    #         [2222,"fui"],
    #         [9821,"lily"],
    #         [2345,"pecko"]
    #     ]

    #     for key,name in test_data:
    #         hashtable.insert(key,name)
        
    #     for key,name in test_data:
            


    #     self.assertEqual(hashtable, )

           
if __name__ == "__main__":
    unittest.main()
