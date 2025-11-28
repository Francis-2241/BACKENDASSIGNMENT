# name = "Isaiah Isaac"
# print(name)

# decimal = 3.14
# print(decimal)

# boolean = True
# print(boolean)

# integer = 42
# print(integer)

# num1 = 100
# num2 = 50
# sum = num1 + num2
# print(sum)

# num1 = 100
# num2 = 50
# sub = num1 - num2
# print(sub)

# num1 = 100
# num2 = 50
# sum = num1 > num2
# print(sum)

# students_name = ["Jeffery", "Francis", "Isaiah"]
# print(students_name)

# fruit_name = ["Mango","Apple","Orange"]
# print(fruit_name[2])

# car = {
#     "color": "Red",
#     "Model": "Toyota",
#     "Year": 2020
# }
# print(car)
 #  CLASS 3
# age = 14
# if age >=18:
#     print("You are eligible to vote")
# else:
#     print("Your are not eligible to vote")

# score = 90
# if score>= 80:
#     print("Grade: A")
# elif score>= 60:
#     print("Grade: B")
# else :
#     print("Grade: C")


# list = ["Apple","Banana","Orange","Cherry"]

# for list in ["Apple","Banana","Orange","Cherry"]:
#    print(list)
# count = 0
# while count < 5:
#   print("Count is",count)
#   count += 1

# correct_password = "backend123"
# attempts = 0

# while attempts < 5:
#     password = input("Enter your password:")
#     print("login successful")
#     break
# else:
#     print("Wrong password")
#     attempts += 1
# if attempts == 5:
#     print("Account Blocked: Too many attempts")       

# CLASS 4 - FUNCTION

# def send_email():
#    print("Hello Isaiah!, We wil be having class tomorrow")

# send_email()   


#try:
 #  number = int(input("Enter a number: "))
  # result = 10/ number
   #print("Result:", result)

#except ZeroDivisionError:
 #  print("You cannot divide by zero!")



#try:
  # number = int(input("Enter a number: "))
   #result = 10/ number
   #print("Result:", result)

#except ZeroDivisionError:
 #  print("You cannot divide by zero!")

#except ValueError:
 #  print("Please enter a valid number.")

users = {"covenant": "1234"}

try:
   username = input("Enter username:")
   password = input("Enter password:")

   if users[username] == password:
      print("Login successful")
   else:
         print("Wrong password")

except KeyError:
   print("username not found")
 
