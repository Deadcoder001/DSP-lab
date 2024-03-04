from collections import OrderedDict  
dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])

dic1.update({"D": '400'})
print(dic1)

dic1.move_to_end("D", last=False)
  

print ("Resultant Dictionary :")
print(dic1)
