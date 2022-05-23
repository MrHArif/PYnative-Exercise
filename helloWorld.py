

#variables

#strings
fname = "bro"
lname = "code"
print(fname.find("r"))
print(fname.find("R")) #this produces an error
print(fname.upper())
print(fname + " " + lname)
print(fname.isalpha())
print(fname.isdigit())
print(fname.count("o"))
print(fname)
print(fname * 3)

#converting varibale to a string
age = 21
age += 1
print("your age is " + str(age))

#Print functions, handy
print(type(str(age)))