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











# weather_c = {
#     # "Monday": 12,
#     # "Tuesday": 14,
#     # "Wednesday": 15,
#     # "Thursday": 14,
#     # "Friday": 21,
#     # "Saturday": 22,
#     # "Sunday": 24,
#     "day" : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
#     "temperature" : [12, 14, 15, 14, 21, 22, 24]
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# # weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items()}
# #
# # print(weather_f)
#
#
# import pandas
# data_frame = pandas.DataFrame(weather_c)
# # print(data_frame)
#
# for (index, row) in data_frame.iterrows():
#     print(row)
#     # print(f"day : {day}, temperature : {temp}")










import tkinter
# from playground import add

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=250, height=150)
window.config(padx=50, pady=20)

# # Label
# my_label = tkinter.Label(text="Im a label", font=("Arial", 24))
# my_label.grid(column=0, row=0)
# # my_label.pack()
#
# # total_sum = add(1, 2, 3, 4, 5)
# # my_second_label = tkinter.Label(text=str(total_sum), font=("Arial", 24))
# # my_second_label = tkinter.Label(text="text111", font=("Arial", 24))
# # my_second_label.pack()
# #
# # my_second_label["text"] = "text2"
# # my_second_label.config(text="text2")
#
#
# # Button
# def button_clicked(args):
#     user_input = input.get()
#     print(f"{args}!!!")
#     my_label["text"] = f"{user_input}!!!"
#
#
# # Entry
# input = tkinter.Entry()
# input.grid(column=3, row=2)
# # input.pack()
#
# button = tkinter.Button(text="Click!", command=lambda: button_clicked("test"))
# # button = tkinter.Button(text="Click!", command=lambda: input_get)
# button.grid(column=1, row=1)
# # button.pack()
#
# button2 = tkinter.Button(text="Button 2")
# button2.grid(column=2, row=0)


def miles_to_km():
    res = round(float(miles_input.get()) * 1.609, 2)
    km_result_label.config(text=f"{res}")


miles_input = tkinter.Entry()
miles_input.grid(row=0, column=1)


miles_label = tkinter.Label(text="Miles", font=("Arial", 20))
miles_label.config(padx=5, pady=5)
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 20))
equal_label.grid(row=1, column=0)

km_result_label = tkinter.Label(text="0", font=("Arial", 20))
km_result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=("Arial", 20))
km_label.grid(row=1, column=2)

convert_button = tkinter.Button(text="Calculate", command=lambda:miles_to_km())
convert_button.grid(row=2, column=1)






window.mainloop()




























