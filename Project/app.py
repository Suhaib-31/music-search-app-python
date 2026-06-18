import requests

print("🎵 Music Search App")
print("-" * 30)

song_name = input("Enter Song Name: ")

url = f"https://itunes.apple.com/search?term={song_name}&limit=5"

try:
    response = requests.get(url)
    data = response.json()

    results = data["results"]

    if len(results) == 0:
        print("No songs found!")

    else:
        print("\n===== Search Results =====\n")

        for index, song in enumerate(results, start=1):

            print(f"Song #{index}")
            print(f"Track Name : {song.get('trackName', 'N/A')}")
            print(f"Artist     : {song.get('artistName', 'N/A')}")
            print(f"Album      : {song.get('collectionName', 'N/A')}")
            print(f"Release    : {song.get('releaseDate', 'N/A')[:10]}")
            print(f"Preview    : {song.get('previewUrl', 'N/A')}")
            print("-" * 50)

except Exception as e:
    print("Error:", e)