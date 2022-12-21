# weather_data_csv = []
# with open("./weather_data.csv") as weather_data:
#     weather_data_csv = weather_data.readlines()

# import csv
#
# temperatures = []
# with open("./weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(int(row[1]))

import pandas

# read csv
data = pandas.read_csv("./weather_data.csv")

# # convert to dictionary
# data_dict = data.to_dict()
# print(data_dict)
#
# # convert to list
# # average using mean()
# temp_list = data["temp"].tolist()
# avg_temp = round(sum(temp_list) / len(temp_list), 2)
# print(f"Average temp is {avg_temp}")
# print(f"Average temp using pandas is {round(data['temp'].mean(), 2)}")
#
# # pandas max()
# print(f"Max temperature using pandas : {data['temp'].max()}")
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])

# Get row data which had the highest temperature
# print(data[data.temp == data['temp'].max()])


# print(data[data.day == "Monday"].temp * 9/5 + 32)


data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [88, 99, 100]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./csv_from_pandas.csv")