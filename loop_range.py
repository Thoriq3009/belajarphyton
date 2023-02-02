#for i in range(5):
    #print(i)

#loop di mulai dari 1 sebanyak 10

#for i in range(1, 5):
    #print(i)
#for i in range (2,11,2):
   # print(i)

#fruits = ['apple', 'banana', 'cherry']
#for i in range(len(fruits)):
    #print(i, fruits[i])

#for i in range(1,101):
 #   if i % 2 == 0 :
 #       print(f'{i}, Genap')
  #  else:
   #     print(f'{i}, Ganjil')

for i in range(1,101):
   if (i % 3 == 0 and i % 5 > 0) :
      print(f'{i}, Boom')
   elif (i % 5 == 0 and i % 3 > 0):
        print(f'{i}, Door')
   elif (i % 5 == 0 and i % 3 == 0):
      print(f'{i}, Joss')
