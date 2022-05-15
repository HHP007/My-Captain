'''
Name:Hariharan P
Date:15/05/2022
'''
def most_frequent(string):
    freq = dict()
    for key in string:
        freq[key] = freq.get(key, 0) + 1
    freq_rev = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    for (key, value) in freq_rev:
        print(key,"=", value) 
    
string = input("enter the word: \n")
most_frequent(string)