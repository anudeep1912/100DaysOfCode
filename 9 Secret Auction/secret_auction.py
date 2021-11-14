from os import system, name
from art import logo


print(logo)
print("Welcome to the Secret auction!")
bids = {}
flag = True
while flag:
    name = input("Please enter your name: ")
    bid = float(input("Please Place your Bid: "))
    if name in bids.keys():
        print("The name is already taken. Please choose a different name")
    else:
        bids[name] = bid
    rerun = input("Do u want to place another bid. (yes or no): ")
    if rerun == 'no':
        flag = False

v = list(bids.values())
k = list(bids.keys())
print(f"The max bid is by {k[v.index(max(v))]} for {max(v)}")