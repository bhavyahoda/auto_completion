import requests 
data=requests.get("https://raw.githubusercontent.com/coding-blocks-archives/ML-Noida-2019-June-Two/master/datasets/speeches/speech.txt")


data=data.text 
#this is  extract the things from response object coz by requests.get we get a response object



data[0:500]


# "hello hello helli helly helli hello"#this is a sample data 
# #This thing below is transition table 
# X.      y.       freq
# "hell"  'o'      3
# "ello"  ' '      2
# "hell"  'i'      2
# "hell"   'y'     1
# #the above table is not complete it is just telling how we have to write 
# #these above lines mean that if hell is input then o is output and this word is in my data once till now 
# #now imagine if a user types the word hell then since the word hello appears 3 times
# #hence we will output that since it has the maximum probabiloty


def generateTransition(data,k=4):
    T={}
    
    for i in range(len(data)-k):
        X=data[i:i+k]
        y=data[i+k]#output 
        
        if T.get(X) is None:#if input state is not there in the dictionary 
            T[X]={}#new dictionary 
            T[X][y]=1
        else:
            if T[X].get(y) is None:#if u already have input in dictionary but the output is not there 
                T[X][y]=1
            else:
                T[X][y]+=1#++ does not work in python
                #if u have both input and output in dict just increment the frequency
    return T



s="hello hello helli helly helli hello"
T=generateTransition(s)


T['hell']#means if i write hell then what is my probability of choosing 


#now let us work with original data 
T1=generateTransition(data.lower())#converting everthing to lower case 

input="country"
possible_chars=list(T1[input[-4:]].keys())
possible_freq=list(T1[input[-4:]].values())#generates all possible characters 
probabs=[ele/sum(possible_freq) for ele in possible_freq]
#input[-4:] means try
print(possible_chars)
print(probabs)

import numpy as np
pred=np.random.choice(possible_chars,p=probabs)

input+=pred

for i in range(300):
    possible_chars=list(T1[input[-4:]].keys())
    possible_freq=list(T1[input[-4:]].values())#generates all possible characters 
    probabs=[ele/sum(possible_freq) for ele in possible_freq]
    pred=np.random.choice(possible_chars,p=probabs)
    input+=pred


print(input)