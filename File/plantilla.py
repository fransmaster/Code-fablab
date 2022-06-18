import csv
with open('plantilla.csv','w') as file:
	writer=csv.writer(file)
	writer.writerow(['curtois','portero'])