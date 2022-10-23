# untuk mendapat nilai A nilai rata rata harus 90 - 100
# untuk mendapat nilai B nilai rata rata harus 80 - 89
# untuk mendapat nilai C nilai rata rata harus 70 - 79
# untuk mendapat nilai D nilai rata rata harus 60 - 69
# untuk mendapat nilai E nilai rata rata kurang dari 60

# matematika
# english
# b Indo
# pkn
# biologi
# fisika

nilaimath  = int(input('Matematika: '))
nilaieng  = int(input('English: '))
nilaibindo  = int(input('Bahasa Indonesia: '))
nilaipkn = int(input('PKN: '))
nilaibio  = int(input('Biologi: '))
nilaifis  = int(input('Fisika: '))
rata2 = int((nilaimath + nilaibindo + nilaieng + nilaipkn + nilaibio + nilaifis) / 6)
print('Rata-rata =', rata2)
if(rata2 >= 90 and rata2 <= 100): #jika rata-rata 90-100 maka mendapat nilai A
 print(f'Rata-rata {rata2} mendapat A') 
elif(rata2 >= 80 and rata2 <= 89): #jika rata-rata 80-89 maka mendapat nilai B
 print(f'Rata-rata {rata2} mendapat B') 
elif(rata2 >= 70 and rata2 <= 79): #jika rata-rata 70-79 maka mendapat nilai C
 print(f'Rata-rata {rata2} mendapat C') 
elif(rata2 >= 60 and rata2 <= 69): #jika rata-rata 60-69 maka mendapat nilai D
 print(f'Rata-rata {rata2} mendapat D') 
elif(rata2 < 60): #jika rata-rata kurang dari 60 mendapat nilai E
 print(f'Rata-rata {rata2} mendapat E') 
else:
    print("Tidak dalam jangkauan")