'''
NAME:HARIHARAN P
DATE: 11/05/2022
'''

no_of_terms = int(input("How many terms to print?: "))

n1, n2 = 0, 1
flag = 0

if no_of_terms <= 0:
   print("Enter a positive integer")

elif no_of_terms == 1:
   print("Fibonacci sequence upto",no_of_terms,":")
   print(n1)

else:
   print("Fibonacci sequence upto:",no_of_terms,":")
   while flag < no_of_terms:
       print(n1)
       n_new = n1 + n2
       n1 = n2
       n2 = n_new
       flag += 1
