import threading 
from threading import*
import time

store={} #'store' is the dictionary in which we store data

def create(key,value,timeout=0):
    if key in store:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(store)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32:
                    store[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#for read operation
            
def read(key):
    if key not in store:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=store[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation

def delete(key):
    if key not in store:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=store[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del store[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del store[key]
            print("key is successfully deleted")

#for modify operation 

def modify(key,value):
    b=store[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in store:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                store[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in store:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            store[key]=l
