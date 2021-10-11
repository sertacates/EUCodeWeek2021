import tkinter.scrolledtext
def onIslemler(cumle):
    
    # Tüm büyük harfler küçük harflere çevriliyor
    cumle = cumle.lower()

    # Özel işaretler, noklama işaretleri ve rakamlar kaldırılıyor
    for karakter in cumle:
        if not(karakter in "abcçdefgğhıijklmnoöprsştuüvyz "): # boşluk kalsın
                cumle = cumle.replace(karakter,"")

    # Etkisiz Kelimeler (Stop Words) Çıkartılıyor
    with open("etkisizKelimeler.txt", "rt", encoding="utf-8") as dosyaEtkisizKelimeler:
        etkisizKelimeListesi = dosyaEtkisizKelimeler.readlines()
        cumleListe = cumle.split(" ")
        for cumleninKelimesi in cumleListe:
            for kelime in etkisizKelimeListesi:
                if cumleninKelimesi in kelime:
                    while cumleninKelimesi in cumleListe:
                        cumleListe.remove(cumleninKelimesi)
        cumle = ""
        cumle = ' '.join(map(str, cumleListe))

    return str(cumle)

# Bu fonksiyon Grafik Arayüzü oluşturuyor
def sohbetEkraniniOlustur():

    def cevabiAl(basilanTus):
        # Kullanıcı tarafından girilen veri okunuyor.
        kullanicininGirdigiCevap = girdiEkrani.get().strip()
        # Kullanıcı başka bir cevap girebilmesi için ekran soru kutusu boşaltılıyor.
        girdiEkrani.delete(0, tkinter.END)

        # Kullanıcı boş ekranda ENTER'a basmamışsa yazışma ekranının renkleri düzenlenip cevap döndürülüyor.
        if kullanicininGirdigiCevap:
            sohbetEkrani.config(state=tkinter.NORMAL)
            sohbetEkrani.tag_config("kullanicininAdininRengi", foreground="#000000")
            sohbetEkrani.tag_config("kullanicininCevabininRengi", foreground="#666666")
            sohbetEkrani.tag_config("uyariEkraniRengi", foreground="#CC0000", justify="center")
            sohbetEkrani.tag_config("sisteminAdininRengi", foreground="#000000")
            sohbetEkrani.tag_config("sisteminCevabininRengi", foreground="#999999")

            # Girilen cevap ön işlemlerden geçiriliyor.
            kullanicininGirdigiCevap = onIslemler(kullanicininGirdigiCevap)

            # Kullanıcının girdiği cevap yazışma ekranına yazdırılıyor.
            sohbetEkrani.insert(tkinter.END, "\nBilmeceye verdiğiniz cevap: ","kullanicininAdininRengi")
            sohbetEkrani.insert(tkinter.END, kullanicininGirdigiCevap + " (Ön işlemden geçirildi!)" + "\n", "kullanicininCevabininRengi")

            # Girilen cevaba göre uyarı döndürülüyor.
            dur = False
            if kullanicininGirdigiCevap=="mum":
                uyariMesaji = "Tebrikler, bildiniz!"
                print("Katılımınız için teşekkür ederiz. Oyun bitmiştir.")
                dur = True
            elif kullanicininGirdigiCevap=="insan":
                uyariMesaji = "Nesne olarak düşünün!"
            else:
                uyariMesaji = "Tekrar deneyiniz!"
            sohbetEkrani.insert(tkinter.END, uyariMesaji , "sisteminAdininRengi")
            if dur:
                print("Bilmece bilindiği için sistem durduruluyor.")
                ekran.destroy()
                print("Sistem durduruldu!")
                return
                
        
        # Yazışmalar arttıkça ekran yukarı doğru aşağıdaki satır ile kaydırılmış olur.
        # Yani ekranda son yazılanlar görününür, yazışma geçmişine kaydırma çubuğu ile ulaşılabilir.
        sohbetEkrani.see(tkinter.END)

    # Yazışma Ekranı oluşturuluyor.
    ekran = tkinter.Tk()
    ekran.title("İzmir Fen Lisesi - EU Code Week Activities - Bilmece Soran Sohbet Robotu")
    ekran.geometry("1024x768")
    ekran.resizable(width=False, height=False)
    ekran.configure(background="#999999")
    sohbetEkrani = tkinter.scrolledtext.ScrolledText(ekran, bd=0, bg="#FFFFCC", width="1004", height="688", font="System",wrap=tkinter.WORD)
    sohbetEkrani.place(x=10, y=70, width=1004, height=598)
    etiket1 = tkinter.Label(ekran, bd=0, bg="#FFFFFF", text="Bilmece Soran Sohbet Robotu BİLRO'ya hoş geldiniz.\nBİLRO aşağıdaki kutucuktan cevap kabul edecektir. Kabul edilen cevabınız analiz edilip anlaşılmaya çalışılacaktır. Anlaşılan cevabınıza göre BİLRO size mesaj yazacaktır.", relief=tkinter.FLAT, justify= "center")
    etiket1.place(x=10, y=10, width=1004, height=50)
    etiket2 = tkinter.Label(ekran, bd=0, bg="#CC9999", text="Cevabınızı aşağıdaki kutucuğa yazdıktan sonra ENTER tuşuna basınız ve bekleyiniz!", relief=tkinter.FLAT, justify= "center")
    etiket2.place(x=10, y=688, width=1004, height=30)
    girdiEkrani = tkinter.Entry(ekran, bd=0, bg="#FFFF33", font="Terminal", justify="center")
    girdiEkrani.place(x=10, y=718, width=1004, height=30)

    # Kullanıcıya bilmeceyi sor!
    sohbetEkrani.insert(tkinter.END, "\nBilmeceniz: \"","kullanicininAdininRengi")
    sohbetEkrani.insert(tkinter.END, "Gençken uzundum ve yaşlandıkça kısaldım, bil bakalım ben neyim?\"" + "\n", "kullanicininCevabininRengi")

    # Kullanıcının yazışmaya başlaması için soru kutusu etkinleştirilir.
    girdiEkrani.focus()
    # Soru yazılıp ENTER tuşuna basıldığında cevap üretme fonksiyonu çağrılır.
    girdiEkrani.bind("<Return>", cevabiAl)
    # Yazışma pencerenin X (kapat) düğmesine basılana kadar devam ettirilir.
    ekran.mainloop()

print("Bilmece Soran Sohbet Robotuna Hoşgeldiniz!")
sohbetEkraniniOlustur()