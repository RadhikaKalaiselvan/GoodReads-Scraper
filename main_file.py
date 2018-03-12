
from question2_lib import Goodreadsquotes 

class Caller:
     if __name__ == '__main__':
        #Get the user input
        user_email = input("Enter user email for goodreads.com: ")
        user_password=input("Enter password for goodreads.com: ")
        if user_email=="" or user_password=="":
            print("Kinldy enter valid username and password")
        else:
                
                obj=Goodreadsquotes()
                #Authenticate user
                if(obj.authenticate(user_email,user_password)):
                    # get the top 10 posts
                    top_10_q=obj.get_Top_10_quotes()
                    #write the top 10 posts to output file
                    with open("Top_10_Mark_Twain_Quotes.txt","wb") as file :
                        for q in top_10_q:
                            file.write(q.encode(encoding='utf-8'))
                    file.close
                    print("Open file Top_10_Mark_Twain_Quotes.txt to check output")
                else:
                    #If not authenticated print Error
                    print("AUTHENTICATION ERROR")