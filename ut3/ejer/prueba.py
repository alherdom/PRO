pdata = {
    'Tokyo':38140000, 'Delhi': 26454000, 'Shangai': 24484000, 'Mumbai':21357000
}
avg_data = {}
total_population = sum(pdata.values())
for city, population in pdata.items():   
    percent_population = (population / total_population) *100
    avg_data[city] = round(percent_population,3)
print(avg_data)
