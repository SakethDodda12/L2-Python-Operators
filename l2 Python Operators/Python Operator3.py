print("Enter marks for the subjects:")
 
english = int(input("Marks for english:"))
math = int(input("Marks for math:"))
science = int(input("Marks for science:"))
spanish = int(input("Marks for spanish:"))

sum = english+math+science+spanish
print("The sum of all your subjects is ", sum)

perc = (sum/400)*100
print("Your overall percentage is ", perc)
