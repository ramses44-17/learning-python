def make_album(artist_name:str, album_title:str, song_number=None):
    """Create a dictionary representing a music album."""
    album_maked = {
        'album_title':album_title.title(),
        'artist_name': artist_name.title()
    }
    if song_number:
        album_maked["song_number"] = song_number
    return album_maked


albums = [make_album("djimy mbaya", "mafuta", 3),
make_album("ninho", "ISPAC"),
make_album("daniel banam","profondeur",10)
]

for album in albums:
    print(f"l'album {album.get("album_title")} de l'artiste {album.get("artist_name")} était top.")
    if(album.get("song_number")):
        print(f"cette album de  {album.get("artist_name")} avait {album.get("song_number")} chansons\n")


