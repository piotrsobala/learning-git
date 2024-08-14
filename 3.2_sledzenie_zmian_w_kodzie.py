sklep_lista = {
    "Piekarnia" : ["Chleb", "Pączek", "Bułki"], 
    "Warzywniak" : ["Marchew", "Seler", "Rukola"]
    }

sklep = []
zakupy = []

print("Lista zakupów")
res = {key: [ele.upper() for ele in sklep_lista[key] ] for key in sklep_lista }
for key,ele in res.items():
    print(f"Idę do {key} i kupuję tam {ele}")

produkty = sum(sklep_lista.values(), [])
print(f"W sumie kupuję {len(produkty)} produktów.")


