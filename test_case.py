import unittest
from question2_lib import Goodreadsquotes
 
class TestGoodReads(unittest.TestCase):
    #Testcase can to check if authentication fails for empty useremail and password
    def test_authentication_empty_input(self):
        goodreads = Goodreadsquotes()
        testOutput=goodreads.authenticate("","")
        assert testOutput==False
     
    #Testcase to authenticate a valid user
    def test_authentication_valid_input(self):
        goodreads = Goodreadsquotes()
        testOutput=goodreads.authenticate("radhikalaiselvan@gmail.com","tempPassword123")
        assert testOutput==True
        
    #Testcase to fail authentication for invalid user
    def test_authentication_invalid_input(self):
        goodreads = Goodreadsquotes()
        testOutput=goodreads.authenticate("radhn@gmail.com","temp23")
        assert testOutput==False
     
    #Testcases to check if there are exactly 10 quotes
    def test_quotes_count(self):
        goodreads = Goodreadsquotes()
        length=len(goodreads.get_Top_10_quotes())
        assert length==10
    
        
if __name__ == '__main__':
   unittest.main()