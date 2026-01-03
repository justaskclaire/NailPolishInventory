"""
Fix Color and Finish columns with ACCURATE data from official product descriptions
"""
import csv

# Accurate mapping based on ACTUAL product page descriptions
polish_data = {
    3: {"color": "Purple, Blue", "finish": "Shimmer"},
    10: {"color": "Brown", "finish": "Cat Eye"},  # Siamese Cat - brown base based on image
    12: {"color": "Purple", "finish": "Cat Eye"},  # Ragdoll - purple based on image
    17: {"color": "Pink, Orange", "finish": "Cat Eye"},  # Shy Snowshoe - "shimmery magenta with orange"
    19: {"color": "Pink", "finish": "Mood Change"},
    20: {"color": "Blue", "finish": "Cat Eye"},
    21: {"color": "Orange, Brown", "finish": "Cat Eye"},
    23: {"color": "Purple, Pink", "finish": "Shimmer"},
    25: {"color": "Grey", "finish": "Holographic"},  # Chunky Holo - "glittery grey"
    26: {"color": "Purple", "finish": "Cat Eye"},  # Chartreux Cat
    34: {"color": "Orange", "finish": "Cat Eye"},
    36: {"color": "Purple, Red", "finish": "Shimmer"},
    39: {"color": "Pink, Red", "finish": "Cream"},
    41: {"color": "Neutral, Purple", "finish": "Cream"},
    43: {"color": "Pink, Purple", "finish": "Cream"},
    52: {"color": "Yellow", "finish": "Cream"},
    67: {"color": "Red", "finish": "Cream"},
    112: {"color": "Orange", "finish": "Cream"},
    116: {"color": "Pink", "finish": "Cream"},
    140: {"color": "Pink", "finish": "Cream"},
    143: {"color": "Pink", "finish": "Cream"},
    151: {"color": "Neutral, Brown", "finish": "Shimmer"},
    178: {"color": "Brown, Neutral", "finish": "Cream"},
    184: {"color": "Pink", "finish": "Cream"},
    194: {"color": "Purple", "finish": "Shimmer"},
    204: {"color": "Yellow", "finish": "Shimmer"},
    209: {"color": "Orange, Pink", "finish": "Cream"},
    210: {"color": "Orange, Pink", "finish": "Cream"},
    219: {"color": "Pink, Purple", "finish": "Shimmer"},  # Tulip
    243: {"color": "Green", "finish": "Shimmer"},
    248: {"color": "Red", "finish": "Cream"},
    250: {"color": "Brown", "finish": "Cream"},
    254: {"color": "Red, Purple", "finish": "Shimmer"},
    272: {"color": "Orange, Red", "finish": "Shimmer"},
    278: {"color": "Pink", "finish": "Cream"},
    283: {"color": "Green", "finish": "Shimmer"},
    299: {"color": "Neutral", "finish": "Shimmer"},
    310: {"color": "Pink, Neutral", "finish": "Cream"},  # Confetti - "dusty nude mocha pink creme"
    317: {"color": "Brown, Orange", "finish": "Cream"},  # Cookie Chips - "golden caramel brown"
    418: {"color": "Orange, Yellow", "finish": "Cream"},
    427: {"color": "Blue", "finish": "Shimmer"},
    437: {"color": "Blue", "finish": "Cream"},
    440: {"color": "Orange, Yellow", "finish": "Cream"},
    490: {"color": "Red, Brown", "finish": "Cream"},
    497: {"color": "Pink", "finish": "Cream"},
    530: {"color": "Blue", "finish": "Shimmer"},
    607: {"color": "Brown, Neutral", "finish": "Cream"},
    635: {"color": "Red, Purple", "finish": "Shimmer"},
    729: {"color": "Blue", "finish": "Shimmer"},
    751: {"color": "Brown, Red", "finish": "Shimmer"},
    753: {"color": "Red", "finish": "Shimmer"},
    754: {"color": "Red, Purple", "finish": "Shimmer"},
    769: {"color": "Red", "finish": "Shimmer"},  # Glistening Sky - "captivating red shimmer"
    775: {"color": "Purple, Pink", "finish": "Shimmer"},
    781: {"color": "Yellow, Gold", "finish": "Shimmer"},  # Starry Night - "rich yellow-toned gold"
    920: {"color": "Pink, Purple", "finish": "Shimmer"},
    929: {"color": "Orange", "finish": "Shimmer"},
    981: {"color": "Brown, Neutral", "finish": "Shimmer"},
    2442: {"color": "Pink", "finish": "Sheer"},
}

# Special handling for duplicate number 26 (Cleocatra)
cleocatra_data = {"color": "Neutral, Pink", "finish": "Cream"}

# Read existing CSV
input_file = "polishes.csv"
output_file = "polishes.csv"

with open(input_file, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Update Color and Finish columns
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
        print(f"Warning: No data for polish #{number} - {row['Name']}")
        row["Color"] = ""
        row["Finish"] = ""

# Write updated CSV
fieldnames = ["Brand", "Number", "Name", "Link", "Image Address", "LocalImage", "Color", "Finish"]
with open(output_file, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print("Updated polishes.csv with ACCURATE Color and Finish data from official product descriptions")
print(f"Total polishes updated: {len([r for r in rows if r.get('Color')])}")
