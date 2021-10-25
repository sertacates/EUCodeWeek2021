#Kullanıcının istenilen girdileri doğru veri tipinde gireceği varsayılmıştır.
print(*"Sayı Tahmin Oyunu")
alt = int(input("Tahmin oyunu için alt sınır:"))
ust = int(input("Tahmin oyunu için üst sınır:"))
print(alt,"-",ust,"sayı aralığında aklınızdan bir sayı tutunuz!")
tahmin=1
orta=int((alt+ust)/2)
bulunduMu=False
while abs(alt-ust)>=1:
    print("Tuttuğunuz sayının",orta,"sayısına göre durumu nedir?")
    print("(e)şit (b)üyük (k)üçük")
    cevap=input("Cevabınız:")
    if cevap=="b":
        alt = orta
        orta = int((alt+ust)/2)
        tahmin+=1
    elif cevap=="k":
        ust = orta
        orta = int((alt+ust)/2)
        tahmin+=1
    elif cevap=="e":
        bulunduMu=True
        break
    else:
        print("Hatalı girdi!")
if bulunduMu:
    print("Sayınızın",orta,"olduğunu",tahmin,"defada buldum!")
else:
    print("Aklınızda tuttuğunuz sayıyı bulamadım!",tahmin,"defa denedim ama verdiğiniz cevaplar doğrultusunda sayınızı tahmin edemedim!")
