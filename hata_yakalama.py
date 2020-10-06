try: # code'u bu blokun icinde yaziyoruz
    sayi1=input("Sayi 1 : ")
    sayi2=input("Sayi 2 : ")
    topla=int(sayi1+sayi2)
    print(topla)
except (ValueError,ZeroDivisionError) : # Hatalari buradan yaziyoruz
    print("Valueerror veya ZerodivisionError hatasi var. ")
finally: # Mutlaka calismasi gereken kodlar burada yaziliyor
    print("Bu code calisir. ")

def ters(x):
    if (type(x)!= str):
        raise ValueError("Bu bir string degildir. ") # hata firlatdik
    else:
         return  x[::-1]

print(ters(4))