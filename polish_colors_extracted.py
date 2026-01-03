# Polish Colors and Finishes Extracted from Official DND Descriptions
# Format: List of dictionaries to support duplicate polish numbers
# Each entry: {"number": polish_number, "name": "polish name", "color": "color from description", "finish": "finish type"}

polish_colors = [
    # From official product descriptions - completed
    {"number": 427, "name": "Air Of Mint", "color": "Mint", "finish": "Shimmer"},  # "A unique pastel mint with grey undertones"
    {"number": 729, "name": "Ambrosia", "color": "Blue", "finish": "Shimmer"},  # "A dark pearly midnight blue"
    {"number": 112, "name": "Apple Cider", "color": "Orange", "finish": "Cream"},  # "A dusty orange tinted with peach undertones"
    {"number": 283, "name": "Army Green", "color": "Green", "finish": "Shimmer"},  # "deep olive green with warm undertones"
    {"number": 272, "name": "Autumn Blaze", "color": "Red", "finish": "Shimmer"},  # "muted cinnamon brownish-red"
    {"number": 497, "name": "Baby Girl", "color": "Pink", "finish": "Cream"},  # "A classic mid-tone pink with warm undertones"
    {"number": 143, "name": "Banana Crepe", "color": "Pink", "finish": "Cream"},  # "An apricot pink with hints of orange"
    {"number": 52, "name": "Biscuits N' Honey", "color": "Yellow", "finish": "Cream"},  # "light golden beige créme"
    {"number": 23, "name": "Blossom Orchid", "color": "Magenta", "finish": "Shimmer"},  # "A deep and sultry version of the classic hot magenta"
    {"number": 437, "name": "Blue De France", "color": "Blue", "finish": "Cream"},  # "A subtle jelly like deep blue"
    {"number": 530, "name": "Blue Lake", "color": "Blue", "finish": "Shimmer"},  # "An elegant Cinderella-style sky blue"
    {"number": 3, "name": "Blue Violet", "color": "Purple", "finish": "Shimmer"},  # "A fun and vibrant royal purple with blue undertones"
    {"number": 116, "name": "Blushing Face", "color": "Pink", "finish": "Cream"},  # "A popping pink with warm undertones"
    {"number": 775, "name": "Boo'd Up", "color": "Burgundy", "finish": "Shimmer"},  # "A cozy burgundy shimmer"
    {"number": 635, "name": "Burgandy Mist", "color": "Burgundy", "finish": "Shimmer"},  # "A mysterious and sophisticated deep burgundy with blue undertones"
    {"number": 418, "name": "Butternut Squash", "color": "Brown", "finish": "Cream"},  # "A coco brown nude fitting for all skin color"
    {"number": 278, "name": "California Grace", "color": "Pink", "finish": "Cream"},  # "A flirty rosy pink with blue undertones"
    {"number": 151, "name": "Castles In Spain", "color": "Grey", "finish": "Shimmer"},  # "cool oyster grey-beige"
    {"number": 2442, "name": "Catch Me Sheering", "color": "Mauve", "finish": "Sheer"},  # "A sheer toasted mauve"
    {"number": 250, "name": "Cedar Brown", "color": "Brown", "finish": "Cream"},  # "muted umber brown"
    {"number": 26, "name": "Chartreux Cat", "color": "Purple", "finish": "Cat Eye"},  # Chartreux Cat - "chic red-violet cat eye"
    {"number": 751, "name": "Cherry Mocha", "color": "Brown", "finish": "Shimmer"},  # "A deep sultry cherry purple brown"
    {"number": 248, "name": "Cherry On Top", "color": "Red", "finish": "Cream"},  # "bright cherry red with warm undertones"
    {"number": 981, "name": "Chestnut Cassette", "color": "Brown", "finish": "Shimmer"},  # "pastel medium-toned brown shade" (cool light brown)
    {"number": 20, "name": "Chubby Himalayan", "color": "Blue", "finish": "Cat Eye"},  # Chubby Himalayan - "royal blue cat eye"
    {"number": 184, "name": "Clean Pallet", "color": "Pink", "finish": "Cream"},  # "light watermelon pink" (flamingo pink)
    {"number": 194, "name": "Clique-Bait", "color": "Purple", "finish": "Shimmer"},  # "bright pastel purple" (lavender)
    {"number": 310, "name": "Confetti", "color": "Pink", "finish": "Cream"},  # "A dusty nude mocha pink creme"
    {"number": 317, "name": "Cookie Chips", "color": "Brown", "finish": "Cream"},  # "A golden caramel brown neutral"
    {"number": 209, "name": "Coral Breeze", "color": "Orange", "finish": "Cream"},  # "soft peachy orange" (bright coral orange)
    {"number": 43, "name": "Dark Salmon", "color": "Purple", "finish": "Cream"},  # "steely blue cool-toned purple"
    {"number": 299, "name": "Dream World", "color": "Mauve", "finish": "Shimmer"},  # "milky nude mauve creme"
    {"number": 67, "name": "Fire Engine Red", "color": "Red", "finish": "Cream"},  # "bright and shiny classic red"
    {"number": 178, "name": "Fawn Over Me", "color": "Taupe", "finish": "Cream"},  # "warm taupe with orange undertones"
    {"number": 39, "name": "Fire Brick", "color": "Pink", "finish": "Cream"},  # "deep pink with classic red undertones"
    {"number": 34, "name": "Fur-st Place", "color": "Orange", "finish": "Cat Eye"},  # Daydream - "fanciful golden cat eye with its prismatic flakes"
    {"number": 769, "name": "Glistening Sky", "color": "Red", "finish": "Shimmer"},  # "deep ruby red with gold-toned glitter"
    {"number": 607, "name": "Hazelnut", "color": "Mauve", "finish": "Cream"},  # "cool-toned deep and dusty mauve"
    {"number": 243, "name": "Imperial Jade", "color": "Green", "finish": "Shimmer"},  # "bright neutral green"
    {"number": 140, "name": "Little Piggy", "color": "Pink", "finish": "Cream"},  # "bright bubblegum pink"
    {"number": 920, "name": "Magenta Aura", "color": "Magenta", "finish": "Shimmer"},  # "hot magenta shade accented by silver and pink glitter"
    {"number": 204, "name": "Marigold", "color": "Yellow", "finish": "Shimmer"},  # "soft gold yellow"
    {"number": 19, "name": "Bridal Pink", "color": "Pink", "finish": "Mood Change"},  # "Bridal Pink To Brighter Pink"
    {"number": 440, "name": "Papaya Whip", "color": "Beige", "finish": "Cream"},  # "warm beige nude"
    {"number": 490, "name": "Redwood City", "color": "Red", "finish": "Cream"},  # "rust-toned brownish red with hints of pink"
    {"number": 753, "name": "Scarlett Dreams", "color": "Burgundy", "finish": "Shimmer"},  # "rich sangria dream burgundy"
    {"number": 781, "name": "Starry Night", "color": "Gold", "finish": "Shimmer"},  # "rich yellow-toned gold with decadent shimmer"
    {"number": 210, "name": "Sunkissed Coral", "color": "Coral", "finish": "Cream"},  # "milky bright coral"
    {"number": 254, "name": "Vampire Kiss", "color": "Purple", "finish": "Shimmer"},  # "dark wine purple"
    {"number": 754, "name": "Winter Berry", "color": "Maroon", "finish": "Shimmer"},  # "winter berry maroon red"
    {"number": 36, "name": "Sultry Gem", "color": "Red", "finish": "Shimmer"},  # "deep, dark red glitter"
    {"number": 41, "name": "With GRAYce", "color": "Taupe", "finish": "Cream"},  # "light taupe créme with cool undertones"
    {"number": 25, "name": "Chunky Holo", "color": "Silver", "finish": "Holographic"},  # "holographic glitter with chunky holographic sparkles"
    {"number": 929, "name": "Orange Aura", "color": "Orange", "finish": "Shimmer"},  # "warm orange shade with iridescent glitter"
    {"number": 219, "name": "Tulip", "color": "Pink", "finish": "Shimmer"},  # "rose gold pink holographic" (DC Mermaid)
    {"number": 21, "name": "Japanese Bobtail", "color": "Orange", "finish": "Cat Eye"},  # Japanese Bobtail - "vibrant, sunkissed tiger orange"
    {"number": 17, "name": "Shy Snowshoe", "color": "Magenta", "finish": "Cat Eye"},  # Shy Snowshoe - "shimmery magenta with orange cat eye"
    {"number": 12, "name": "Ragdoll", "color": "Unknown", "finish": "Cat Eye"},  # Ragdoll - No explicit color description, generic Cat Eye text
    {"number": 10, "name": "Siamese Cat", "color": "Unknown", "finish": "Cat Eye"},  # Siamese Cat - No explicit color description, generic Cat Eye text
    {"number": 26, "name": "Cleocatra", "color": "Red", "finish": "Cream"},  # Cleocatra (9D Cat Eye Creamy) - "A purr-suasive shade of red"
]

# Notes on extraction:
# - Changed from dictionary to list format to support duplicate polish numbers
# - The company reuses polish numbers (e.g., #26 for both Chartreux Cat and Cleocatra)
# - Colors extracted ONLY from official product descriptions
# - "Unknown" marked for Cat Eye polishes #10 and #12 that lack explicit color descriptions
# - Finish types identified from URL patterns (dc-cat-eyes, mood-change, etc.)
# - Common color names used as specified
# - No "Multicolor" entries as instructed
