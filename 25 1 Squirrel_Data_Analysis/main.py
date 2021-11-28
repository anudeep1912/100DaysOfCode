"""Combs through the Squirrel data in central park in NY and gives count of a
particular color in csv format """

import pandas

squirrel_data = pandas.read_csv("Central_Park_Squirrel_Census.csv")
gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
    "Fur Color": ["Gray", "Black", "Red"],
    "Count": [gray_squirrel_count, black_squirrel_count, red_squirrel_count]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")
