nilai = int(input('Enter any number: '))

#jika nilai 90-100 maka mendapat nilai A
#jika nilai 80-89 maka mendapat nilai B
#jika nilai 70-79 maka mendapat nilai C
#jika nilai 60-69 maka mendapat nilai D
#jika nilai kurang dari 60 mendapat nilai F


if(nilai >= 90 and nilai <= 100): #jika nilai 90-100 maka mendapat nilai A
 print(f'nilai {nilai} mendapat A') 
elif(nilai >= 80 and nilai < 90):
    print(f'nilai {nilai} mendapat B') 
elif(nilai >= 70 and nilai < 80):
    print(f'nilai {nilai} mendapat C') 
elif(nilai >= 60 and nilai < 70):
    print(f'nilai {nilai} mendapat D') 
elif(nilai <60 ):
    print(f'nilai {nilai} mendapat F') 
else: 
    print('Tidak dalam rentang')