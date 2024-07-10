"""  Create a dictionary and take input from the user and return the meaning of the word
 from the dictionary """

dict={"Array":"Array is a collection of similar data type" ,"HAPPINESS":"love yourself not others" , "SADNES": "love othes then you never get happier life"}
print("enter following word for meaning\n",dict.keys())
#word=input()
word = input("enter the word :") #input function ()bricate behave like print statement so we can print anything without write print() function
w=word.capitalize()          #input function me ().capitalice use karne se only 1st word pr effect padta hain
print( "\t", dict[w])




