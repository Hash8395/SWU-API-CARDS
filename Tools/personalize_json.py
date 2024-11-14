import json

# Chemin vers le fichier JSON d'origine et le fichier de sortie
input_file = "cards_data_shd.json"
output_file = "cards_data_shd_modified.json"

# Charger le fichier JSON
with open(input_file, "r") as f:
    data = json.load(f)

# Supprimer les clés des cartes dans la liste "data"
for card in data["data"]:
    keys_to_remove = ["Artist", "VariantType", "MarketPrice", "FoilPrice", "FrontArt", "BackArt"]
    for key in keys_to_remove:
        card.pop(key, None)  # Suppression de la clé si elle existe

# Trier les cartes par numéro
data["data"].sort(key=lambda x: int(x["Number"]))

# Sauvegarder le fichier modifié
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print("Fichier JSON modifié, trié et sauvegardé avec succès !")