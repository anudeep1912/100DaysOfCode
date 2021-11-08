#1. Create a greeting for your program.
print("Greetings, fellow Musicians!\n")
#2. Ask the user for the city that they grew up in.
city = input('What city you are born in?\n').capitalize()
#3. Ask the user for the name of a pet.
pet = input('What is the name of your pet?\n').capitalize()
#4. Combine the name of their city and pet and show them their band name.
result = city +" "+ pet
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/
print("Your band name is " + result +". Rock ON!")