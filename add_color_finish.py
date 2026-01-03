"""
Add Color and Finish columns to polishes.csv based on polish names and URLs
"""
import csv

# Mapping based on polish names and product URLs
polish_data = {
    427: {"color": "Blue", "finish": "Shimmer"},  # Air Of Mint - mint is blue/green
    729: {"color": "Blue", "finish": "Shimmer"},  # Ambrosia - already in old file
    112: {"color": "Orange", "finish": "Cream"},  # Apple Cider - already in old file
    283: {"color": "Green", "finish": "Shimmer"},  # Army Green - already in old file
    272: {"color": "Orange, Red", "finish": "Shimmer"},  # Autumn Blaze - autumn orange/red
    497: {"color": "Pink", "finish": "Cream"},  # Baby Girl - already in old file
    143: {"color": "Pink", "finish": "Cream"},  # Banana Crepe - already in old file
    52: {"color": "Yellow", "finish": "Cream"},  # Biscuits N' Honey - already in old file
    23: {"color": "Purple, Pink", "finish": "Shimmer"},  # Blossom Orchid - already in old file
    437: {"color": "Blue", "finish": "Cream"},  # Blue De France - already in old file
    530: {"color": "Blue", "finish": "Shimmer"},  # Blue Lake - already in old file
    3: {"color": "Purple, Blue", "finish": "Shimmer"},  # Blue Violet - already in old file
    116: {"color": "Pink", "finish": "Cream"},  # Blushing Face - already in old file
    775: {"color": "Red, Purple", "finish": "Shimmer"},  # Boo'd Up - romantic red/purple
    635: {"color": "Red, Purple", "finish": "Shimmer"},  # Burgandy Mist - burgundy is red/purple
    418: {"color": "Orange, Yellow", "finish": "Cream"},  # Butternut Squash - orange/yellow
    278: {"color": "Pink", "finish": "Cream"},  # California Grace/Vibes - already in old file
    151: {"color": "Neutral, Brown", "finish": "Shimmer"},  # Castles In Spain - already in old file
    2442: {"color": "Pink", "finish": "Sheer"},  # Catch Me Sheering - already in old file
    250: {"color": "Brown", "finish": "Cream"},  # Cedar Brown - already in old file
    26: {"color": "Purple", "finish": "Cat Eye"},  # Chartreux Cat - already in old file
    751: {"color": "Brown, Red", "finish": "Shimmer"},  # Cherry Mocha - brown with red
    248: {"color": "Red", "finish": "Cream"},  # Cherry On Top - already in old file
    981: {"color": "Brown, Neutral", "finish": "Shimmer"},  # Chestnut Cassette - already in old file
    20: {"color": "Blue", "finish": "Cat Eye"},  # Chubby Himalayan - already in old file
    184: {"color": "Pink", "finish": "Cream"},  # Clean Pallet - already in old file
    194: {"color": "Purple", "finish": "Shimmer"},  # Clique-Bait - already in old file
    310: {"color": "Multicolor", "finish": "Glitter"},  # Confetti - confetti is multicolor glitter
    317: {"color": "Multicolor", "finish": "Glitter"},  # Cookie Chips - cookie chips multicolor
    209: {"color": "Orange, Pink", "finish": "Cream"},  # Coral Breeze - coral is orange/pink
    43: {"color": "Purple, Pink", "finish": "Cream"},  # Dark Salmon - salmon with purple tones
    299: {"color": "Neutral", "finish": "Shimmer"},  # Dream World - already in old file
    178: {"color": "Brown, Neutral", "finish": "Cream"},  # Farm Brown/Fawn Over Me - brown neutral
    39: {"color": "Pink, Red", "finish": "Cream"},  # Fire Brick - already in old file
    67: {"color": "Red", "finish": "Cream"},  # Fire Engine Red - already in old file
    34: {"color": "Orange", "finish": "Cat Eye"},  # Fur-st Place - already in old file
    769: {"color": "Blue, Purple", "finish": "Shimmer"},  # Glistening Sky - blue/purple sky
    607: {"color": "Brown, Neutral", "finish": "Cream"},  # Hazelnut - brown/neutral
    243: {"color": "Green", "finish": "Shimmer"},  # Imperial Jade - already in old file
    140: {"color": "Pink", "finish": "Cream"},  # Little Piggy - already in old file
    920: {"color": "Pink, Purple", "finish": "Shimmer"},  # Magenta Aura - magenta is pink/purple
    204: {"color": "Yellow", "finish": "Shimmer"},  # Marigold - already in old file
    19: {"color": "Pink", "finish": "Mood Change"},  # Bridal Pink - already in old file
    440: {"color": "Orange, Yellow", "finish": "Cream"},  # Papaya Whip - papaya is orange/yellow
    490: {"color": "Red, Brown", "finish": "Cream"},  # Redwood City - redwood is red/brown
    753: {"color": "Red", "finish": "Shimmer"},  # Scarlett Dreams - scarlett is red
    781: {"color": "Blue, Purple", "finish": "Shimmer"},  # Starry Night - night sky blue/purple
    210: {"color": "Orange, Pink", "finish": "Cream"},  # Sunkissed Coral - coral orange/pink
    254: {"color": "Red, Purple", "finish": "Shimmer"},  # Vampire Kiss - dark red/purple
    754: {"color": "Red, Purple", "finish": "Shimmer"},  # Winter Berry - berry red/purple
    41: {"color": "Neutral, Purple", "finish": "Cream"},  # With GRAYce - already in old file
    929: {"color": "Orange", "finish": "Shimmer"},  # Orange Aura - orange
    25: {"color": "Multicolor", "finish": "Holographic"},  # Chunky Holo - holographic
    219: {"color": "Pink, Purple", "finish": "Shimmer"},  # Tulip - pink/purple flower
    36: {"color": "Red, Purple", "finish": "Shimmer"},  # Sultry Gem - sultry red/purple
    21: {"color": "Orange, Brown", "finish": "Cat Eye"},  # Japanese Bobtail - orange/brown cat
    17: {"color": "Blue, Purple", "finish": "Cat Eye"},  # Shy Snowshoe - blue/purple cat
    12: {"color": "Blue, Purple", "finish": "Cat Eye"},  # Ragdoll - blue/purple cat eye
    10: {"color": "Blue, Brown", "finish": "Cat Eye"},  # Siamese Cat - blue/brown points
}

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
        row["Color"] = "Neutral, Pink"
        row["Finish"] = "Cream"
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

print("Updated polishes.csv with Color and Finish columns")
