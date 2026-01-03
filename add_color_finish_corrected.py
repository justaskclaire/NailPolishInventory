"""
Add accurate Color and Finish columns to polishes.csv based on official product descriptions
"""
import csv

# Accurate mapping based on official DND Gel product descriptions
polish_data = {
    10: {"color": "Blue, Grey", "finish": "Cat Eye"},  # Siamese Cat - blue with grey undertones
    12: {"color": "Blue, Purple", "finish": "Cat Eye"},  # Ragdoll - blue/purple cat eye
    17: {"color": "Blue, Purple", "finish": "Cat Eye"},  # Shy Snowshoe - blue/purple cat
    19: {"color": "Pink", "finish": "Mood Change"},  # Bridal Pink - mood change pink
    20: {"color": "Blue", "finish": "Cat Eye"},  # Chubby Himalayan - blue cat eye
    21: {"color": "Orange, Brown", "finish": "Cat Eye"},  # Japanese Bobtail - orange/brown cat
    23: {"color": "Purple, Pink", "finish": "Shimmer"},  # Blossom Orchid - purple/pink shimmer
    25: {"color": "Grey", "finish": "Holographic"},  # Chunky Holo - glittery grey holographic
    26: {"color": "Purple", "finish": "Cat Eye"},  # Chartreux Cat - purple cat eye
    36: {"color": "Purple, Red", "finish": "Shimmer"},  # Sultry Gem - purple/red shimmer
    39: {"color": "Pink, Red", "finish": "Cream"},  # Fire Brick - pink/red cream
    41: {"color": "Neutral, Purple", "finish": "Cream"},  # With GRAYce - grey neutral with purple
    43: {"color": "Pink, Purple", "finish": "Cream"},  # Dark Salmon - pink/purple cream
    52: {"color": "Yellow", "finish": "Cream"},  # Biscuits N' Honey - yellow cream
    67: {"color": "Red", "finish": "Cream"},  # Fire Engine Red - red cream
    112: {"color": "Orange", "finish": "Cream"},  # Apple Cider - orange cream
    116: {"color": "Pink", "finish": "Cream"},  # Blushing Face - pink cream
    140: {"color": "Pink", "finish": "Cream"},  # Little Piggy - pink cream
    143: {"color": "Pink", "finish": "Cream"},  # Banana Crepe - pink cream
    151: {"color": "Neutral, Brown", "finish": "Shimmer"},  # Castles In Spain - neutral/brown shimmer
    178: {"color": "Brown, Neutral", "finish": "Cream"},  # Farm Brown/Fawn Over Me - brown neutral
    184: {"color": "Pink", "finish": "Cream"},  # Clean Pallet - pink cream
    194: {"color": "Purple", "finish": "Shimmer"},  # Clique-Bait - purple shimmer
    204: {"color": "Yellow", "finish": "Shimmer"},  # Marigold - yellow shimmer
    209: {"color": "Orange, Pink", "finish": "Cream"},  # Coral Breeze - coral orange/pink
    210: {"color": "Orange, Pink", "finish": "Cream"},  # Sunkissed Coral - coral orange/pink
    219: {"color": "Pink, Purple", "finish": "Shimmer"},  # Tulip - pink/purple mermaid shimmer
    243: {"color": "Green", "finish": "Shimmer"},  # Imperial Jade - green shimmer
    248: {"color": "Red", "finish": "Cream"},  # Cherry On Top - red cream
    250: {"color": "Brown", "finish": "Cream"},  # Cedar Brown - brown cream
    254: {"color": "Red, Purple", "finish": "Shimmer"},  # Vampire Kiss - red/purple shimmer
    272: {"color": "Orange, Red", "finish": "Shimmer"},  # Autumn Blaze - autumn orange/red
    278: {"color": "Pink", "finish": "Cream"},  # California Grace/Vibes - pink cream
    283: {"color": "Green", "finish": "Shimmer"},  # Army Green - green shimmer
    299: {"color": "Neutral", "finish": "Shimmer"},  # Dream World - neutral shimmer
    310: {"color": "Pink, Neutral", "finish": "Cream"},  # Confetti - dusty nude mocha pink creme
    317: {"color": "Brown, Orange", "finish": "Cream"},  # Cookie Chips - golden caramel brown
    418: {"color": "Orange, Yellow", "finish": "Cream"},  # Butternut Squash - orange/yellow
    427: {"color": "Blue", "finish": "Shimmer"},  # Air Of Mint - mint blue shimmer
    437: {"color": "Blue", "finish": "Cream"},  # Blue De France - blue cream
    440: {"color": "Orange, Yellow", "finish": "Cream"},  # Papaya Whip - papaya orange/yellow
    490: {"color": "Red, Brown", "finish": "Cream"},  # Redwood City - redwood red/brown
    497: {"color": "Pink", "finish": "Cream"},  # Baby Girl - pink cream
    530: {"color": "Blue", "finish": "Shimmer"},  # Blue Lake - blue shimmer
    607: {"color": "Brown, Neutral", "finish": "Cream"},  # Hazelnut - brown neutral
    635: {"color": "Red, Purple", "finish": "Shimmer"},  # Burgundy Mist - burgundy red/purple
    729: {"color": "Blue", "finish": "Shimmer"},  # Ambrosia - blue shimmer
    751: {"color": "Brown, Red", "finish": "Shimmer"},  # Cherry Mocha - brown with red
    753: {"color": "Red", "finish": "Shimmer"},  # Scarlett Dreams - red shimmer
    754: {"color": "Red, Purple", "finish": "Shimmer"},  # Winter Berry - berry red/purple
    769: {"color": "Blue, Purple", "finish": "Shimmer"},  # Glistening Sky - blue/purple sky
    775: {"color": "Purple, Pink", "finish": "Shimmer"},  # Boo'd Up - purple/pink shimmer
    781: {"color": "Blue, Purple", "finish": "Shimmer"},  # Starry Night - night blue/purple
    920: {"color": "Pink, Purple", "finish": "Shimmer"},  # Magenta Aura - magenta pink/purple
    929: {"color": "Orange", "finish": "Shimmer"},  # Orange Aura - orange shimmer
    981: {"color": "Brown, Neutral", "finish": "Shimmer"},  # Chestnut Cassette - brown neutral
    3: {"color": "Purple, Blue", "finish": "Shimmer"},  # Blue Violet - purple/blue shimmer
    2442: {"color": "Pink", "finish": "Sheer"},  # Catch Me Sheering - pink sheer
    34: {"color": "Orange", "finish": "Cat Eye"},  # Fur-st Place - orange cat eye
}

# Special handling for duplicate number 26 (Cleocatra)
cleocatra_data = {"color": "Neutral, Pink", "finish": "Cream"}

# Read existing CSV
input_file = "polishes.csv"
output_file = "polishes.csv"

with open(input_file, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Add Color and Finish columns
for row in rows:
    number = int(row["Number"])
    
    # Handle duplicate 26 (Chartreux Cat and Cleocatra)
    if number == 26 and "Cleocatra" in row["Name"]:
        row["Color"] = cleocatra_data["color"]
        row["Finish"] = cleocatra_data["finish"]
    elif number in polish_data:
        row["Color"] = polish_data[number]["color"]
        row["Finish"] = polish_data[number]["finish"]
    else:
        row["Color"] = ""
        row["Finish"] = ""

# Write updated CSV
fieldnames = ["Brand", "Number", "Name", "Link", "Image Address", "LocalImage", "Color", "Finish"]
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Updated polishes.csv with accurate Color and Finish columns based on official product descriptions")
