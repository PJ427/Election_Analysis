counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
#    print(county, voters)

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])

#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not in the list of counties.")

#for county in counties_dict.keys():
#    print(county)

#for i in range(len(counties)):
#    print(counties[i])

#for voters in counties_dict.values():
#    print(voters)

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")