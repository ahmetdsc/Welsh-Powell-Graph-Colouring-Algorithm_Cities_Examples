#This software was written by Ahmet Disci.
#Welch ve Powel Algoritması

#FONKSİYONLARIM
#Matrisleri yazdırdıgım fonksiyon
def yazdır():
    for i in range(8):
            print(sehirler[i][1], end="\t")
            print(matris[i])

def komsuKontrol(sehir,renk):#komşuların renklerini kontrol ettiğim fonksiyon
    for i in range(8):
        if matris[sehir][i] == 1:
            if sehirler[i][3] == renk:
                return 0
    return 1

def boya(sehir,renk):#şehirleri boyadığım fonksiyon
    sehirler[sehir][3]=renk#istenilen renge boyadığım fonksiyon


#Matrisleri olusturdugum  yer . bağlantılıysa"1"  bağlantılı değilse "0"
matris = ([0,1,1,1,0,0,0,0],[1,0,1,0,1,0,0,0],[1,1,0,1,1,0,0,0],[1,0,1,0,1,0,1,1],[0,1,1,1,0,1,1,0],[0,0,0,0,1,0,1,0]
,[0,0,0,1,1,1,0,1],[0,0,0,1,0,0,1,0])

print("Program Başlatıldı.")
print("Şehirler ve Komsuluk Matrisi")

#şehir kodları,isimleri,dereceleri,renk kodları
sehirler=[0,"Afyonk.",0,0],[1,"Kütahya",0,0],[2,"Uşak   ",0,0],[3,"Denizli",0,0],[4,"Manisa ",0,0],[5,"İzmir  ",0,0],[6,"Aydın  ",0,0],[7,"Muğla  ",0,0]

#renk kodları 0=null 1=yeşil, 2=kırmızı , 3=beyaz ,4 siyah
# 3 renk yaparsam boyanmıyordu siyah ekledim
yazdır()
enYuksekDerece = 0  # En yüksek dereceyi buluyorum

print()#boşluk için
for i in range(8):#Sehirlerin derecelerini buluyorum
    derece=0
    for j in range(8):
        if matris[i][j]==1:
            derece=derece+1
    sehirler[i][2]=derece
    if derece>enYuksekDerece:
        enYuksekDerece=derece

for i in range(8):#Sehirlerin derecelerini yazdırıyorum
    print(sehirler[i][1], end="\t dereceleri=")
    print(sehirler[i][2])

print()#Boşluk bırakmak için
while enYuksekDerece>0:
    for i in range(8):#şehirleri döndürüyoruz
        if enYuksekDerece==sehirler[i][2]:#dereceleri yüksekten şehirden küçük şehire doğru sırayla boyuyoruz
            if komsuKontrol(i,1)==1:#yeşile boyama kontrol
                boya(i,1)
                print(sehirler[i][1] + " şehrini yeşile boyadım")

            elif komsuKontrol(i,2)==1:#kırmızıya boyama kontrol
                boya(i,2)
                print(sehirler[i][1] + " şehrini kırmızıya boyadım")

            elif komsuKontrol(i,3)==1:#beyaza boyama kontrol
                boya(i,3)
                print(sehirler[i][1] + " şehrini beyaza boyadım")

            elif komsuKontrol(i,4)==1:#siyaha boyama kontrol
                boya(i,4)
                print(sehirler[i][1] + " şehrini siyaha boyadım")
            else:
                print("Lütfen daha fazla renk ekleyiniz.Şehirleri boyayamıyorum.")
    enYuksekDerece=enYuksekDerece-1

print("Program başarıyla tamamlandı.Test edebilirsiniz.")