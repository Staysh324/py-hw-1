# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).


long = int (input("введите количество долек в длинне: "))
width = int (input("введите количество долек в ширине: "))
slices = int (input("введите количество отламываемых долек: "))
allslices = long*width
if  (slices >= long) and (slices < allslices) and (slices % long == 0):
        print ("yes")
elif (slices >= width) and (slices < allslices) and (slices % width == 0):
       print ("yes")
else:
        print ("no") 
    
