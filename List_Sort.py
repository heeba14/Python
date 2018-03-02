name_list=[{"first_name":"Ruzeena","last_name":"Bashir","address":["abc","jandk"]},
{"first_name":"Heeba","last_name":"Kawoosa","address":["def","Delhi"]},
{"first_name":"Rumaya","last_name":"Rashid","address":["ghi","Banglore"]}]


for i,r in enumerate(sorted(name_list, key=lambda r: r['address'][1])):
    print (i,r)

#OR
''' for c, value in enumerate(new_list, 1):
        print(c, value) '''












