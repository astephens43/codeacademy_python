# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update_damages(list1):
  lista = []
  for item in list1:    
    if item[-1] == ("M"):
      new_itemM = (float(item[:-1]) * int(1000000))
      lista.append(new_itemM)
    elif item[-1] == ("B"):
      new_itemB = (float(item[:-1]) * int(1000000000))
      lista.append(new_itemB)
    else:
      new_itemC = item
      lista.append(new_itemC)
  return lista       
  


damages2 = (update_damages(damages)) 

# test function by updating damages


# 2 
# Create a Table


def convert_list_to_tuple(list1, KeyName):
  one = list([KeyName] * len(list1))
  two = (zip(one, list1))
  KeyName = list(two)
  return KeyName

Name = (convert_list_to_tuple(names, "Name"))
Month = (convert_list_to_tuple(months, "Month"))
Year = (convert_list_to_tuple(years, "Year"))
Max = (convert_list_to_tuple(max_sustained_winds, "Max Sustained Wind"))
Area = (convert_list_to_tuple(areas_affected, "Areas Affected"))
Damages = (convert_list_to_tuple(damages2, "Damage"))
Deaths = (convert_list_to_tuple(deaths, "Deaths"))

trial = (names, months, years, max_sustained_winds, areas_affected, damages2, deaths )
trial2 = ("Name", "Month", "Year","Max Sustained Wind", "Areas Affected", "Damage", "Deaths" )

def dictionary_of_lists(list1, list2, list3, list4, list5, list6, list7,):
  values = {}
  for i in (range(len(list1))):
    out = ({"Name": list1[i], \
    "Month": list2[i],\
    "Year": list3[i], \
    "Max Sustained wind": list4[i], \
    "Areas Affected": list5[i], \
    "Damage": list6[i], \
    "Deaths": list7[i]})
    values[list1[i]] = out
  return values
# Create and view the hurricanes dictionary
huricanes_dict = dictionary_of_lists(names, months, years, max_sustained_winds, areas_affected, damages2, deaths )


    


# 3
# Organizing by Year
year_by_year = sorted(set(years))
#print(year_by_year)
#print(huricanes_dict)
#print(huricanes_dict.values())




# create a new dictionary of hurricanes with year and key
hurricanes_by_year = {key:value for key, value in zip(year_by_year, [])}
for item in huricanes_dict.values():
    current_year = item["Year"]
    current_case = item
    hurricanes_by_year.setdefault(current_year, []).append(current_case)
    
#print(hurricanes_by_year)

#print(len(hurricanes_by_year.keys())) 
#print(len(hurricanes_by_year.values()))   

# 4
# Counting Damaged Areas
areas_affected_flat = []
for sublist in areas_affected:
    for item in sublist:
        areas_affected_flat.append(item)
#print(areas_affected_flat) 

dedup_areas = set(areas_affected_flat)
frequency_of_area = {key:value for key, value in zip(dedup_areas, "" )}
for item in dedup_areas:
  score = areas_affected_flat.count(item)
  frequency_of_area[item] = score 
# create dictionary of areas to store the number of hurricanes involved in
#print(frequency_of_area)

# 5 
# Calculating Maximum Hurricane Count
def max_count(diction):
  max_value = max(diction.values())  # maximum value
  max_keys = [k for k, v in diction.items() if v == max_value]
  return (max_keys, max_value)
# find most frequently affected area and the number of hurricanes involved in
#print(max_count(frequency_of_area))

# 6
# Calculating the Deadliest Hurricane
def max_value_item(diction1, item):
  interim = {}
  for record in diction1.values():
      temp_name = record["Name"]
      temp_value = record[item]
      if type (temp_value) == str:
          temp_value = 0
      one = (temp_name, temp_value)
      interim.update({one}) 
  out = max_count(interim)
  return out



 
# find highest mortality hurricane and the number of deaths
print(max_value_item(huricanes_dict, "Deaths"))
#print(huricanes_dict["Mitch"])
# 7
# Rating Hurricanes by Mortality
def huricanes_by_rating(diction, key):
  rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  for record in diction.values():
    x = record[key]
    for i in range(len(mortality_scale.keys())):
      if x <= mortality_scale[i]:
        rating[i].append(record)
  return rating 
    
huricanes_by_mortality = huricanes_by_rating(huricanes_dict, "Deaths")

# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage
print(max_value_item(huricanes_dict, "Damage"))
# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
#damage_scale = {0: 0,
 #               1: 100000000,
   #             2: 1000000000,
    #            3: 10000000000,
     #           4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def huricanes_by_damage_rating(diction, key):
  rating = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  for record in diction.values():
    if type (record[key]) == str:
      x = 0
    else:
      x = record[key]
    for i in range(len(damage_scale.keys())):
      if x <= damage_scale[i]:
        rating[i].append(record)
  return rating 

print(huricanes_by_damage_rating(huricanes_dict, "Damage"))
