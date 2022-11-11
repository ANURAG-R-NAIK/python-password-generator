#here we will generate a random password of the length given by the user.

import string  #this is used ffor accessing the string functions for the password characters
import random  #this will help us randomply pick up the characters from the string library


s1 = string.ascii_lowercase  # this consists of all the lower case alphabets

s2 = string.ascii_uppercase   # this consists of all the upper case alphabets


s3 = string.digits   # this consists of all the digits from 0-9


s4 = string.punctuation  # this consists of all the punctuation symbols



plen=int(input("enter the length of the password in integer form ")) #ask the user for password length
           
s=[]
s.extend(list(s1))  #all thses will concatnate the listss inside our empty list
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
#print(s) # this was a sorted list
random.shuffle(s)  #this will select random elements from the list s

print("Your Password Is:")

print("".join(s[0:plen]))  #this will take the elements satisfying the length of password
                            #then join all the characters using join fuunction without any seperator as we want to 
                        #concatenate them
                        
#you can also make a  sample using random.sample and do the .join function