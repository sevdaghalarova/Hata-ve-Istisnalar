# Bu listenin içindeki stringlerden içinde sadece rakam bulunanları ekrana yazdırın.

# #
# #
liste=["345","sadas","324a","14","kemal"]
for eleman in liste:
     try:
        eleman=int(eleman)
        print(eleman)
     except:
         pass



