# IMPORT IMDB LIBRARY
import imdb

# TOTAL RESULTS COUNTER
number=1

# OBJECT IMDB
ia = imdb.IMDb()

# SERCH INPUT LINE
search = ia.search_movie(title=input("Search: "))

print("\nResults found: \n")

# PRINT THE RESULTS
for i in search:
    print(f"{number}. {i}")
    number=number + 1

number=number - 1

# TOTAL RESULTS FOUND 
print(f"\nTotal results: {number}")



