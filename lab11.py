import pandas as pd
import json
#1
data = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]
#2
updatedData = []
info = {}
for element in data:
    if(type(element)==int):
        info["info"] = element
    elif(type(element)==str):
        info["name"] = element
    elif(type(element) == float):
        info['employee_hr'] = element
    else:
        pass
    if(len(info)==3):
        updatedData.append(info)
        info = {}
        
df = pd.DataFrame(updatedData)
#3
df.drop_duplicates(subset = "info", keep = "first", inplace = True)
#4
df["employee_rate"] = df["employee_hr"] * 1.3
list = json.loads(df.to_json(orient = 'records'))

underpaid_salaries = []
i = 0
for i in range(len(list)):
    #5
    if list[i].get("employee_rate") >= 28.15 and list[i].get("employee_rate") <= 30.65:
        underpaid_salaries.append(list[i])
#6
def newRaise(wage):
    if(wage >= 22.0 and wage < 24.0):
        return wage * 1.05
    elif(wage >= 24.0 and wage < 26.0):
        return wage * 1.04
    elif(wage >= 26.0 and wage < 28.0):
        return wage * 1.03
    else:
        return wage * 1.02

df['raise'] = df["employee_hr"].map(newRaise)
company_raises = json.loads(df[["name",'raise']].to_json(orient = 'records'))

#7
print("\n\tMain list: ")
json_string = json.dumps(list, indent = 4)
print(json_string)
print("\n\tUnderpaid Salaires: ")
json_paid = json.dumps(underpaid_salaries, indent = 4)
print(json_paid)
print("\n\tRaises: ")
json_raise = json.dumps(company_raises, indent = 4)
print(json_raise)