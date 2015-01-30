
# coding: utf-8

# In[2]:

def convert(input, source, target):
        if (source == "0123456789") & (target == "01"): #converting decimal to binary
            return bin(int(input))[2:]
        if (source == "01") & (target == "0123456789"): #converting binary to decimal
            return int(input, 2)
        if (source == "0123456789") & (target == "0123456789ABCDEF"): #converting decimal to hexadecimal
            return hex(int(input))[2:]
        if (source == "0123456789ABCDEF") & (target == "0123456789"): #converting hexadecimal to decimal
            return int(input, 16)
        if (source == "0123456789ABCDEF") & (target == "abcdefghijklmnopqrstuvwxyz"): #converting hexadecimal to alphabet
            return input.decode("hex")
        if (source == "0123456789ABCDEF") & (target == "01"): #converting hexadecimal to binary 
            return bin(input, 16)[2:]
        if (source == "01") & (target == "0123456789ABCDEF"): #converting binary to hexadecimal
            return hex(int(input, 2))[2:]
        if (source == "abcdefghijklmnopqrstuvwxyz") & (target == "0123456789ABCDEF"): #converting alphabet to hexadecimal
            hexValList = []
            for i in input:
                hexVal = hex(ord(i))[2:]
                if len(hexVal) ==1:
                    hexVal = '0'+hexVal
                hexValList.append(hexVal)
            return reduce(lambda x,y:x+y, hexValList)    


# In[5]:

print convert("73766970", "0123456789ABCDEF","abcdefghijklmnopqrstuvwxyz")
print convert("11", "01","0123456789")
print convert("0000010010001101", "01","0123456789ABCDEF")


# In[ ]:



