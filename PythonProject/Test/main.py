# with open("./file1.txt") as content_file1:
#     list_file1 = content_file1.readlines()
# with open("./file2.txt") as content_file2:
#     list_file2 = content_file2.readlines()
#
# result = [int(num) for num in list_file1 if num in list_file2 and num != '']
#
#
#
# # Write your code above 👆
# print(result)











weather_c = {
    # "Monday": 12,
    # "Tuesday": 14,
    # "Wednesday": 15,
    # "Thursday": 14,
    # "Friday": 21,
    # "Saturday": 22,
    # "Sunday": 24,
    "day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "temperature" : [12, 14, 15, 14, 21, 22, 24]
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:
# weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
#
# print(weather_f)


import pandas
data_frame = pandas.DataFrame(weather_c)
# print(data_frame)

for (index, row) in data_frame.iterrows():
    print(row)
    # print(f"day : {day}, temperature : {temp}")