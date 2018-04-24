## 3. Read the File Into a String ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_lis = names.split('\n')
nested_list =[]
for rows in names_lis :
    nest=rows.split(",")
    nested_list.append(nest)
print(nested_list[0:5])

    


## 6. Convert Numerical Values ##

#print(nested_list[0:5])
numerical_list=[]
for rows in nested_list :
    name = rows[0]
    num = float(rows[1])
    new_list =[name,num]
    numerical_list.append(new_list)
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater=[]
for rows in numerical_list :
    if rows[1] >=1000 :
       thousand_or_greater.append(rows[0])
print(thousand_or_greater)