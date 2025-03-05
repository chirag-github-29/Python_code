import pandas as pd

df=  pd.read_csv("movies.csv")

if 'ratings' not in df.columns:
    raise KeyError("The 'ratings' column is missing. Check the CSV file for the correct column name.")

# Convert ratings to numeric (handle errors and missing values)
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce').fillna(0)

# User input for preferred movie
user_input = input("Enter a movie you like: ")
liked_movie_data = df[df['title'].str.lower() == user_input.lower()]

# Check if the movie exists in the dataset
if liked_movie_data.empty:
    print("Movie not found in dataset. Try another one.")
else:
    director = liked_movie_data.iloc[0]['director']
    genre = liked_movie_data.iloc[0]['genre']
    
    # Fetch top 2 movies by the same director
    director_matches = (
        df[df['director'] == director]
        .sort_values(by='ratings', ascending=False)
        .head(2)
    )
    
    # Fetch top 3 movies from the same genre but different director
    genre_matches = (
        df[(df['genre'] == genre) & (df['director'] != director)]
        .sort_values(by='ratings', ascending=False)
        .head(3)
    )
    
    # Combine and display recommendations
    recommendations = pd.concat([director_matches, genre_matches]).drop_duplicates()
    print("\nRecommended Movies:\n")
    for _, row in recommendations.iterrows():
        print(f"Title: {row['title']}\nOverview: {row['overview']}\nRating: {row['ratings']}\n")
