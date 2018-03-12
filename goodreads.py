#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:42:29 2017

@author: radhikakalaiselvan
"""


from robobrowser import RoboBrowser
from bs4 import BeautifulSoup
import requests

class Goodreadsquotes: 
    
    def authenticate(self,user_email,password):
        # Get the signup form and set the values
        browser = RoboBrowser()
        browser.open('http://www.goodreads.com')
        signup_form = browser.get_form(id='sign_in')
        signup_form['user[email]'].value = user_email
        signup_form['user[password]'].value = password
        #submit the signup form
        browser.submit_form(signup_form)
        p=browser.parsed()
        #p is the page after submitting the form, if the returned file has 'My Books' only if the user is authenticated
        page=str(p)
        if "My Books" not in page:
            print("Login failed !")
            return False
        else:
            print("Login success !")
            return True
    
    def get_Top_10_quotes(self):
        quotes_top_10=[]
        #Goodreads doesnt authenticate user to get the quotes. So a simple get of the url will get the page. No need to send cookies.
        response=requests.get("https://www.goodreads.com/quotes/search?utf8=%E2%9C%93&q=Mark+Twain&commit=Search")
        #The response html is parsed and quotes and authors are stored in an array
        quotes=[""]
        authors=[""]
        soup=BeautifulSoup(response.content,"lxml")
        for tag in soup.findAll('div',{ "class" : "quoteText" }):
            quotes.append(tag.contents[0].strip())
            authors.append(tag.find('a').get_text())
        count=0
        #Filtering the quotes of Mark Twain and incrementing the count.
        for i in range(len(quotes)):
            if(count<10):
                if(authors[i]=="Mark Twain"):
                    count+=1
                    quotes_top_10.append(quotes[i])
            else:
                    break
        return quotes_top_10
            
     
   
    
            
    

