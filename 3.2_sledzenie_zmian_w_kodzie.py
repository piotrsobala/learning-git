sklep_lista = {
    "Piekarnia" : ["Chleb", "Pączek", "Bułki"], 
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
    }

sklep = []
zakupy = []

print("Lista zakupów")
for sklep,zakupy in sklep_lista.items():
    print(f"Idę do {sklep} i kupuję tam {zakupy}")