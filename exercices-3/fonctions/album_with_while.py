def make_album(artist_name:str, album_title:str, song_number=None):
    album_maked = {
        'album_title':album_title.title(),
        'artist_name': artist_name.title()
    }
    if song_number:
        album_maked["song_number"] = song_number
    return album_maked


albums = []

exit = True

while exit:
    print("Veuillez entrer correctement les informations de votre albums favorite\n")
    album_title = input("Entrez le titre de l'album: ")
    artist_name = input("Entrez le nom de l'artiste: ")
    make_albumed = make_album(artist_name, album_title)
    song_number = input("Entrez le nombre de chansons de l'album (optionnel): ")
    if song_number.isdigit():
        make_albumed = make_album(artist_name, album_title, int(song_number))
    albums.append(make_albumed)
    print(f"Album enregistré: {len(albums)}\n")
    quitter = input("Voulez-vous ajouter un autre album? (oui/non): ")
    if quitter.lower() == 'non':
        exit = False

print("\nVos albums favoris enregistrés sont:\n")
index = 1
for album in albums:
    print(f"{index}. {album.get('album_title')}', {album.get('artist_name')}'")
    if album.get("song_number"):
        print(f"   Nombre de chansons: {album.get('song_number')}")
    index += 1
