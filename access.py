#here are the commands to demonstrate how to access and perform operations on a main file

import code as p 
#importing the main file("code" is the name of the file I have used) as a library 


p.create("Naveen",400)
p.create("chauhan",39,3600) 
p.read("Naveen")
p.read("Chauhan")
p.create("Naveen",60)
#it returns an ERROR since the key_name already exists in the database



p.modify("Naveen",60)
#it replaces the initial value of the respective key with new value 

 
p.delete("Naveen")
#it deletes the respective key and its value from the database(memory is also freed)

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

