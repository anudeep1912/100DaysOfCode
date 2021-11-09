#Write your code below this line 👇
name_1 = input("Please enter your name.").lower()
name_2 = input("please enter your partners name.").lower()
count_1 = name_1.count("t") + name_1.count("r") + name_1.count("u") + name_1.count("e") 
count_2 = name_2.count("t") + name_2.count("r") + name_2.count("u") + name_2.count("e")

count = count_1 * 10 + count_2
if count <= 10 or count >= 90:
  print(f"Your score is {count}, you go together like coke and mentos.")
elif count >= 50 or count <= 60:
  print(f"Your score is {count}, you are alright together.")
else:
  print(f"Your score is {count}")