import openpyxl
from openpyxl.chart import BarChart, Reference
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(10):
	sheet.append([i])
values = Reference(sheet, min_col=1, min_row=1,
				max_col=1, max_row=10)
chart = BarChart()
chart.add_data(values)
chart.title = "Experience vs Salary of 10 people"
chart.x_axis.title = "Experience"
chart.y_axis.title = "Salary"
sheet.add_chart(chart, "C2")
wb.save("sample.xlsx")
