'''
NAME:HARIHARAN P
DATE:09/05/2022
'''

nameoffile = input("Input the Filename: ")
extention = nameoffile.split(".")
extention=extention[-1]
if str(extention)=='py':
    extention='python'
print ("\n The extension of the file is : " + str(extention))