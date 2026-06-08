print("=== Recommendation System ===")

items = {
    "movies": ["3 Idiots", "Dangal", "Taare Zameen Par", "12th Fail"],
    "books" : ["Rich Dad Poor Dad", "The School of Life", "Atomic Habits"],
    "products" : ["Laptops", "Headphones", "Smartphones"],
    "music" : ["Arijit Singh", "Lofi beats", "Anuv Jain"],
}

def recommend(category) :
    if category in items: 
        print("\nRecommend",category, ":" )
        for i in items[category]:
            print("-", i)
    else: 
        print("No recommendations found for this category.")

while True:
    print("\nCategories: movies / books / products / music / exit")
    user = input("Enter your preference: ").lower()

    if user == "exit":
        print("Thank you for using recommendation system")
        break

    recommend(user)