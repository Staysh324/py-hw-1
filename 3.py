# Вы пользуетесь общественным транспортом? Вероятно, 
# вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным 
# номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется 
# написать программу, которая проверяет счастливость билета.

number = int (input ("введите номер билета: "))
first = number//1000
second = number%1000
sumfirstnum = 0
sumsecondnum = 0
while first > 0:
    sumfirstnum += first % 10
    first //= 10
while second > 0:
    sumsecondnum += second % 10
    second //= 10
if sumsecondnum == sumfirstnum:
    print (f"билет счастливый")
else:
    print (f"билет не счастливый")