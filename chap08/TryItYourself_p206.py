#8-6

def city_country(city, country):
	print(f'"{city.title()}, {country.title()}"')

city_country('cape town', 'south africa')
city_country('sydney', 'australia')
city_country('berlin', 'germany')

#8-7
def make_album(artist_name, album_title, number_of_songs = None):
	person = {'artist' : artist_name.title(), 'album_name' : album_title.title(), 'songs': number_of_songs }
	return person

	if number_of_songs:
		album = f" {artist_name}, {album_title}, {number_of_songs}"
	else:
		album = f" {artist_name}, {album_title}"


album = make_album('Hollow Coves', 'Moments', 11)
print(album)
album = make_album('nf', 'the search', 20)
print(album)
album = make_album('dean', 'a place we knew', 12)
print(album)

#8-8
def make_album(artist_name, album_title, number_of_songs = None):
	person = {'artist' : artist_name.title(), 'album_name' : album_title.title(), 'songs': number_of_songs }
	return person

while True:
	print("\nEnter an artist and album title: ")
	print("\nEnter 'done' to exit any time")

	artist_name = input("Artist name: " )
	if artist_name == 'done':
		break
	album_title = input("Album title: " )
	if album_title == 'done':
		break
	album = make_album(artist_name, album_title)
	print(f" Artist: {artist_name} \nAlbum: {album_title}")



