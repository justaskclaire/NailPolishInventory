# Comprehensive Polish Color and Finish Mapping
# Based on official DND Gel product descriptions from dndgel.com
# Format: Number -> {"Color": "Color1, Color2", "Finish": "FinishType"}

polish_mapping = {
    3: {"Color": "Purple, Blue", "Finish": "Shimmer"},  # Blue Violet - "fun and vibrant royal purple with blue undertones"
    10: {"Color": "Blue, Brown", "Finish": "Cat Eye"},  # 5D Siamese Cat - Cat eye formula
    12: {"Color": "Blue, Purple", "Finish": "Cat Eye"},  # 5D Ragdoll - Cat eye formula
    17: {"Color": "Pink, Orange", "Finish": "Cat Eye"},  # Shy Snowshoe - "shimmery magenta with orange cat eye"
    19: {"Color": "Pink", "Finish": "Mood Change"},  # Bridal Pink - "Bridal Pink To Brighter Pink"
    20: {"Color": "Blue", "Finish": "Cat Eye"},  # Chubby Himalayan - "royal blue cat eye"
    21: {"Color": "Orange", "Finish": "Cat Eye"},  # Japanese Bobtail - "vibrant, sunkissed tiger orange"
    23: {"Color": "Purple, Pink", "Finish": "Shimmer"},  # Blossom Orchid - "deep and sultry version of the classic hot magenta"
    25: {"Color": "Grey", "Finish": "Holographic"},  # Chunky Holo - "holographic glitter with chunky holographic sparkles" (FIXED from "Multicolor")
    26: {"Color": "Purple", "Finish": "Cat Eye"},  # Chartreux Cat - "chic red-violet cat eye"
    26: {"Color": "Red", "Finish": "Cat Eye"},  # Cleocatra - "purr-suasive shade of red" (Note: Duplicate number)
    34: {"Color": "Gold", "Finish": "Cat Eye"},  # Fur-st Place - "fanciful golden cat eye with prismatic flakes"
    36: {"Color": "Red", "Finish": "Glitter"},  # Sultry Gem - "deep, dark red glitter"
    39: {"Color": "Pink, Red", "Finish": "Cream"},  # Fire Brick - "deep pink with classic red undertones"
    41: {"Color": "Neutral, Purple", "Finish": "Cream"},  # With Grayce - "light beige with purple undertones...light taupe créme with cool undertones"
    43: {"Color": "Purple", "Finish": "Cream"},  # Dark Salmon - "sophisticated steely blue cool-toned purple"
    52: {"Color": "Yellow", "Finish": "Cream"},  # Biscuits N' Honey - "light golden beige créme"
    67: {"Color": "Red", "Finish": "Shimmer"},  # Fire Engine Red - "bright and shiny classic red"
    112: {"Color": "Orange", "Finish": "Cream"},  # Apple Cider - "dusty orange tinted with peach undertones"
    116: {"Color": "Pink", "Finish": "Cream"},  # Blushing Face - "popping pink with warm undertones"
    140: {"Color": "Pink", "Finish": "Cream"},  # Little Piggy - "bright bubblegum pink"
    143: {"Color": "Pink, Orange", "Finish": "Cream"},  # Banana Crepe - "apricot pink with hints of orange"
    151: {"Color": "Neutral, Brown", "Finish": "Shimmer"},  # Castles In Spain - "cool oyster grey-beige"
    178: {"Color": "Brown, Orange", "Finish": "Cream"},  # Fawn Over Me - "light taupe with orange undertones"
    184: {"Color": "Pink", "Finish": "Cream"},  # Clean Pallet - "light watermelon pink" (flamingo pink)
    194: {"Color": "Purple", "Finish": "Shimmer"},  # Clique-Bait - "bright pastel purple" (lavender)
    204: {"Color": "Yellow", "Finish": "Cream"},  # Marigold - "soft gold yellow"
    209: {"Color": "Orange, Pink", "Finish": "Cream"},  # Coral Breeze - "soft peachy orange" (bright coral orange)
    210: {"Color": "Orange, Pink", "Finish": "Cream"},  # Sunkissed Coral - "coral orange"
    219: {"Color": "Pink, Gold", "Finish": "Holographic"},  # Tulip - "rose gold pink holographic"
    243: {"Color": "Green", "Finish": "Cream"},  # Imperial Jade - "bright neutral green"
    248: {"Color": "Red", "Finish": "Cream"},  # Cherry On Top - "bright cherry red with warm undertones"
    250: {"Color": "Brown", "Finish": "Cream"},  # Cedar Brown - "muted umber brown"
    254: {"Color": "Red, Purple", "Finish": "Sheer"},  # Vampire's Kiss - "dark red-violet...dark wine purple"
    272: {"Color": "Orange, Red", "Finish": "Shimmer"},  # Autumn Blaze - "muted cinnamon brownish-red"
    278: {"Color": "Pink", "Finish": "Cream"},  # California Grace - "flirty rosy pink with blue undertones"
    283: {"Color": "Green", "Finish": "Shimmer"},  # Army Green - "deep olive green with warm undertones"
    299: {"Color": "Purple, Pink", "Finish": "Cream"},  # Dream World - "milky nude mauve creme"
    310: {"Color": "Pink, Neutral", "Finish": "Cream"},  # Confetti - "dusty nude mocha pink creme" (FIXED from "Multicolor")
    317: {"Color": "Brown, Orange", "Finish": "Cream"},  # Cookie Chips - "golden caramel brown neutral" (FIXED from "Multicolor")
    418: {"Color": "Brown, Neutral", "Finish": "Cream"},  # Butternut Squash - "coco brown nude fitting for all skin color"
    427: {"Color": "Blue, Green", "Finish": "Shimmer"},  # Air Of Mint - "unique pastel mint with grey undertones"
    437: {"Color": "Blue", "Finish": "Cream"},  # Blue De France - "subtle jelly like deep blue"
    440: {"Color": "Neutral", "Finish": "Cream"},  # Papaya Whip - "warm beige nude"
    490: {"Color": "Red, Brown, Pink", "Finish": "Cream"},  # Redwood City - "rust-toned brownish red with hints of pink"
    497: {"Color": "Pink", "Finish": "Cream"},  # Baby Girl - "classic mid-tone pink with warm undertones"
    530: {"Color": "Blue", "Finish": "Shimmer"},  # Blue Lake - "elegant Cinderella-style sky blue"
    607: {"Color": "Purple", "Finish": "Cream"},  # Hazelnut - "cool-toned deep and dusty mauve"
    635: {"Color": "Red, Purple", "Finish": "Shimmer"},  # Burgundy Mist - "mysterious and sophisticated deep burgundy with blue undertones"
    729: {"Color": "Blue", "Finish": "Shimmer"},  # Ambrosia - "dark pearly midnight blue"
    751: {"Color": "Red, Purple, Brown", "Finish": "Shimmer"},  # Cherry Mocha - "deep sultry cherry purple brown"
    753: {"Color": "Red, Purple", "Finish": "Cream"},  # Scarlett Dreams - "rich sangria dream burgundy"
    754: {"Color": "Red", "Finish": "Cream"},  # Winter Berry - "winter berry maroon red"
    769: {"Color": "Red", "Finish": "Glitter"},  # Glistening Sky - "deep ruby red with gold-toned glitter"
    775: {"Color": "Red, Purple", "Finish": "Shimmer"},  # Boo'd Up - "cozy burgundy shimmer"
    781: {"Color": "Gold", "Finish": "Shimmer"},  # Starry Night - "rich yellow-toned gold with decadent shimmer"
    920: {"Color": "Pink", "Finish": "Glitter"},  # Magenta Aura - "hot magenta shade accented by silver and pink glitter"
    929: {"Color": "Orange", "Finish": "Glitter"},  # Orange Aura - "warm orange shade with iridescent glitter"
    981: {"Color": "Brown, Neutral", "Finish": "Shimmer"},  # Chestnut Cassette - "pastel medium-toned brown shade"
    2442: {"Color": "Purple, Pink", "Finish": "Sheer"},  # Catch Me Sheering - "sheer toasted mauve"
}

# Print summary
if __name__ == "__main__":
    print("Polish Color and Finish Mapping Summary")
    print("="*50)
    print(f"Total polishes mapped: {len(polish_mapping)}")
    print("\nFinish type distribution:")
    
    finish_types = {}
    for polish_data in polish_mapping.values():
        finish = polish_data["Finish"]
        finish_types[finish] = finish_types.get(finish, 0) + 1
    
    for finish, count in sorted(finish_types.items()):
        print(f"  {finish}: {count}")
    
    print("\nKey corrections made:")
    print("  - #25 Chunky Holo: Changed from 'Multicolor' to 'Grey/Holographic'")
    print("  - #310 Confetti: Changed from 'Multicolor' to 'Pink, Neutral/Cream'")
    print("  - #317 Cookie Chips: Changed from 'Multicolor' to 'Brown, Orange/Cream'")
    
    print("\nNote: Polish #26 has two entries (Chartreux Cat and Cleocatra)")
    print("\nSample entries:")
    for num in [25, 310, 317, 751, 920]:
        if num in polish_mapping:
            print(f"  #{num}: Color={polish_mapping[num]['Color']}, Finish={polish_mapping[num]['Finish']}")
