


recommendations = {
    "movies": ["Inception", "Interstellar", "Avatar", "The Dark Knight"],
    "books": ["Atomic Habits", "Rich Dad Poor Dad", "The Alchemist"],
    "music": ["Shape of You", "Blinding Lights", "Perfect"],
    "sports": ["Cricket", "Football", "Badminton"],
    "technology": ["AI", "Machine Learning", "Data Science"]
}


user_interest = input("Enter your interest (movies, books, music, sports, technology): ").lower()


if user_interest in recommendations:
    print("\nRecommended Items:")
    for item in recommendations[user_interest]:
        print("-", item)
else:
    print("\nSorry! No recommendations available for that interest.")
