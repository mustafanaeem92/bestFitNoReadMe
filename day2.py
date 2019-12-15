# i = 1
# while i <= 6:
#     print(i)
#     i = i + 1
# print("Done")

# secret_no = 10
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_no:
#         print("You won")
#         break
# else:
#     print("You Failed")

# command = ""
# started = True
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if started:
#             print("Car already Started")
#         else:
#             started = True
#             print('Car started...')
#
#     elif command == "stop":
#         if not started:
#                 print("Car is already stopped!")
#             else:
#                 started = False
#                 print("Car stopped....")
#     elif command == "help":
#         print("""
#         Start > to Start the Car
#         Stop > to Stop the Car
#         quit > to quit""")
#     elif command == "quit":
#         break
#     else:
#         print("I do'nt understand")

# for item in range(1, 11, 3):
#     print(item)
# items =[10, 20, 30, 40]
# total = 0
# for price in items:
#     total += price
#     print(f"Total: {total}")

# for x in range(4):
#     for y in range (3):
#         print(f'({x},{y})')

# number = [1, 1, 1, 1, 5]
# for x in number:
#     print('x' * x)

# numbers = [3, 5, 2, 8, 12, 4]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

#numbers = [2, 8, 4, 6, 9,]
#numbers.append(21)
#numbers.insert(3,7)
#numbers.remove(4)
#numbers.clear()
#numbers.pop()
#numbers.index(2)
#numbers.sort()
#numbers.reverse()
# numbers2= numbers.copy()
# numbers.append(12)
# print(numbers)

#tuples
#numbers = (1, 2, 3)
#print(numbers[1])

# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print

#Dictionaries

# customer = {
#     "name": "Bilal Batook",
#     "age": 23,
#     "is_verified": True
# }
# customer["Birth_date"] = "Dec 22 1996"
# print(customer["Birth_date"])

# phone = input("Phone")
# digits_mapping = {
#     "1": "One",
#     "2": "two",
#     "3": "three",
#     "4": "four"
#
# }
# output = ""
# for no in phone:
#     output = digits_mapping.get(no,"!")
#     print(output)

#Emoji_coverter

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": ":-)",
#     ":(": ":-("
# }
# output = ""
# for word in words:
#     output += emojis.get(word, word)
# print(output)

#Functions

# def greet_user():
#     print('Hi There')
#     print('Welcome Abroad')
#
#
# print("Start")
# greet_user()
# print("finished")

# def greet_user(f_name, l_name):
#     print(f"Hi {f_name}, {l_name}")
#     print('Welcome Abroad')
#
#
# print("Start")
# greet_user("Bilal","Batook")
# print("finished")

#Key_Argument

# def greet_user(f_name, l_name):
#     print(f"Hi {f_name} {l_name}")
#     print('Welcome Abroad')
#
#
# print("Start")
# greet_user(l_name="Batook", f_name="Bilal")
# print("finished")

def square(number):
    return number * number


result = square(4)
print(result)