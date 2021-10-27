sales=[13,3523,31,238]
sum=0
for sale in sales:
    sum+=sale
else:
    print(sum)

for i in range(10):
    print(i)
for i in range(10):
    print(i)
    if i ==3:
        break


shincho = { "Akun":173,"Bkun":165,"Ckun":181,"Dkun":177,"Ekun":171 }

print(shincho["Akun"])
print(shincho["Bkun"])
print(shincho["Ckun"])
print(shincho["Dkun"])
print(shincho["Ekun"])

shincho["Fkun"]=175
print(shincho)

del shincho["Akun"]
print(shincho)