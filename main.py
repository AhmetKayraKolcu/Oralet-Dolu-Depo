meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap"
            "ROFL - bir şakaya karşılık cevap"
            "SHEESH - onaylamamak"
            "CREEPY - korkunç"
            "AGGRO - agresifleşmek/sinirlenmek"
            }
            
            
word = input("anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!):")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(word,"kelimesinin anlamı",meme_dict[word])
else:
    print(word,"kelimesinin anlamı bulunamadı")
