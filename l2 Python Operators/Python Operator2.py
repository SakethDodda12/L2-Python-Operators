Amount =int(input("Please enter amount to withdraw :"))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10

print("Notes of 100", note1)
print("Notes of 50", note2)
print("Notes of 10", note3)