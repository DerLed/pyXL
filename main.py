from tkinter import *
import string
import certificate

from openpyxl import load_workbook

root = Tk()
root.title('openXL')


my_workbook = load_workbook('C:/Копия журнал верификации лист 09Г2С - копия.xlsx')
my_worksheet = my_workbook.active
print(my_worksheet.max_row)

thickness = 10
count = 0
column_template = [2, 4, 5, 6, 7, 8]
my_list = []

for my_row in range(5, my_worksheet.max_row):
    if not my_worksheet['A' + str(my_row)].value:
        break
    me_row = my_worksheet[my_row]
    super_list = [x.value for x in me_row]
    my_list.append(super_list)


for x in column_template:
    my_list[0][x] = None

for x in my_list[0]:
    print(x)


h = 'Лист г/к  8*1500*6000'
y = h.split('Лист г/к')
h = h[8:-10].strip()


# print(h)
# print(my_worksheet.cell(row = 6, column = column_s).value, end=' ---  ')
# for x in range(6, my_worksheet.max_row):
#     if not my_worksheet['M' + str(x)].value:
#         break
#     print(my_worksheet['M' + str(x)].value.split())


# root.mainloop()
bob = certificate.Certificate(my_list[0])
print(bob.thickness)
print(bob.metal_grade)

"""
{
  "melting_number": "?",
  "certificate_number": "?",
  "date_of_certificate": "?",
  "metal_grade": "?",
  "thickness": "?"
}
"""
