#list comprehension

list_1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list_2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
k=[i for i in range(2,15) if(i%2==0)]
g=[i for i in range(2,15) if(i%2!=0)]
print(k,g)