# Consiga la siguiente transformación:
# 12/31/20 ➡️ 31-12-2020
SEP = "-"
american_date = "12/31/20"
splitted_american_date = american_date.split("/")
day = splitted_american_date[1]
month = splitted_american_date[0]
year = "20" + splitted_american_date[2]
output_date = SEP.join([day, month, year])
print(output_date)
