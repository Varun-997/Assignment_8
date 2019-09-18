data = input("Enter binary data that has to be transmitted\t")     #Inputting binary string
count=0
for i in data:    
    if i == '1':
        count+=1   # if even parity
if (count%2) == 0:
   data = data + '1'    #add 1 at the end
else:
    data = data + '0'   #add 0 for odd
print('Parity bit data:', data)   
data = data.replace('010', '0100')
data = data + '0101'
print("Transmitting data: ",data)
