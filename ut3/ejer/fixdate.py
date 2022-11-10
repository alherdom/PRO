# Consiga la siguiente transformación:
# 12/31/20 ➡️ 31-12-2020

input_date = "12/31/20"
day = input_date[:2]
month = input_date[3:5]
year = "20" + input_date[6:9]
output_date = '-'.join([day,month,year])
print(output_date)
