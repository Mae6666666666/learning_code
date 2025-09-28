

def testSwitch(lang: str):
    match lang:
        case  "JavaScript":
            print("You can become a web developer.")
        case "Python":
            print("You can become a Data Scientist")
        case "php":
            print("You can become a backend developer")
        case "Solidity":
            print("You can become a Blockchain developer")
        case "Java":
            print("You can become a mobile app developer")
        case _:
            print("The language doesn't matter, what matters is solving problems.")

# testSwitch("php")

from enum import Enum

class Location(Enum):
    Outside = "outside"
    Inside = "inside"


class Genre(Enum):
    Classic = 0
    Indie = 1
    Rock = 2
    Alternative = 3
    Electronic = 4

gorillaz = Genre.Electronic

match gorillaz:
    case Genre.Rock:
        print("is rock")
    case Genre.Electronic:
        print("is electronic")
    case _:
        print("The language doesn't matter, what matters is solving problems.")
 # scope stuff
# test01 = 56
# print(test01)
#
#
# def test():
#     test00 = "hello"
#
# test()
#
# while True:
#     test00 = "world"
#
#
# print(test00)

user_name = "Mae"

match user_name:
    case "Kim":
        print("Hello Kim!")
    case "Abe":
        print("Hey Abe!")
    case "Mae":
        print("Hi Mae!")
    case _:
        print("Unknown user")

value = 32

match value:
    case n if 0 <= n <= 10:
        print("Between 0 and 10")
    case n if 11 <= n <= 20:
        print("Between 11 and 20")
    case n if 21 <= n <= 50:
        print("Between 21 and 50")
    case _:
        print("Out of range")
        
        
        
daft_punk_data_dic = {
	"artist": {
		"id": "27",
		"name": "Daft Punk",
		"picture": "https://api.deezer.com/artist/27/image",
		"picture_big": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/500x500-000000-80-0-0.jpg",
		"picture_medium": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/250x250-000000-80-0-0.jpg",
		"picture_small": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/56x56-000000-80-0-0.jpg",
		"picture_xl": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/1000x1000-000000-80-0-0.jpg",
		"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
		"type": "artist"
	},
	"available": True,
	"contributors": [
		{
			"id": 27,
			"link": "https://www.deezer.com/artist/27",
			"name": "Daft Punk",
			"picture": "https://api.deezer.com/artist/27/image",
			"picture_big": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/500x500-000000-80-0-0.jpg",
			"picture_medium": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/250x250-000000-80-0-0.jpg",
			"picture_small": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/56x56-000000-80-0-0.jpg",
			"picture_xl": "https://cdn-images.dzcdn.net/images/artist/638e69b9caaf9f9f3f8826febea7b543/1000x1000-000000-80-0-0.jpg",
			"radio": True,
			"role": "Main",
			"share": "https://www.deezer.com/artist/27?utm_source=deezer&utm_content=artist-27&utm_term=0_1759057449&utm_medium=web",
			"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
			"type": "artist"
		}
	],
	"cover": "https://api.deezer.com/album/302127/image",
	"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
	"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
	"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
	"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
	"duration": 3662,
	"explicit_content_cover": 0,
	"explicit_content_lyrics": 7,
	"explicit_lyrics": False,
	"fans": 314972,
	"genre_id": 113,
	"genres": {
		"data": [
			{
				"id": 113,
				"name": "Dance",
				"picture": "https://api.deezer.com/genre/113/image",
				"type": "genre"
			}
		]
	},
	"id": "302127",
	"label": "Daft Life Ltd./ADA France",
	"link": "https://www.deezer.com/album/302127",
	"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
	"nb_tracks": 14,
	"record_type": "album",
	"release_date": "2001-03-07",
	"share": "https://www.deezer.com/album/302127?utm_source=deezer&utm_content=album-302127&utm_term=0_1759057449&utm_medium=web",
	"title": "Discovery",
	"tracklist": "https://api.deezer.com/album/302127/tracks",
	"tracks": {
		"data": [
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "320",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135553",
				"link": "https://www.deezer.com/track/3135553",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/f/8/c/0/f8c5dc3837912dba37c9a1ab3170cc3f.mp3?hdnea=exp=1759058349~acl=/api/1/1/f/8/c/0/f8c5dc3837912dba37c9a1ab3170cc3f.mp3*~data=user_id=0,application_id=42~hmac=8799530cc03df12f7db854b813211a88afecf8927c0b6a2b932c92226ddab33a",
				"rank": "882844",
				"readable": True,
				"title": "One More Time",
				"title_short": "One More Time",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "212",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 6,
				"explicit_lyrics": False,
				"id": "3135554",
				"link": "https://www.deezer.com/track/3135554",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/6/9/9/0/699d41611cf0280f0a55c8ba4a372c14.mp3?hdnea=exp=1759058349~acl=/api/1/1/6/9/9/0/699d41611cf0280f0a55c8ba4a372c14.mp3*~data=user_id=0,application_id=42~hmac=fe071d8e765a749fe4fe2c8c861e31fef9a59f089bcaa135d2d59787449b35cc",
				"rank": "737762",
				"readable": True,
				"title": "Aerodynamic",
				"title_short": "Aerodynamic",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "301",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135555",
				"link": "https://www.deezer.com/track/3135555",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/9/e/9/0/9e9f1086d844a1e5eef43ba230c508a9.mp3?hdnea=exp=1759058349~acl=/api/1/1/9/e/9/0/9e9f1086d844a1e5eef43ba230c508a9.mp3*~data=user_id=0,application_id=42~hmac=2e6cde6c60ef112074fe1ac11a5d1684ca38f83205314ea40801d45fb6c12220",
				"rank": "707364",
				"readable": True,
				"title": "Digital Love",
				"title_short": "Digital Love",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "226",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135556",
				"link": "https://www.deezer.com/track/3135556",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/c/4/d/0/c4d7dbe3524ba59d2ad06d8cccd2484f.mp3?hdnea=exp=1759058349~acl=/api/1/1/c/4/d/0/c4d7dbe3524ba59d2ad06d8cccd2484f.mp3*~data=user_id=0,application_id=42~hmac=b478718af8185242842d0960a38d2aee158ef4525248e6cba4a82954e76519f8",
				"rank": "806178",
				"readable": True,
				"title": "Harder, Better, Faster, Stronger",
				"title_short": "Harder, Better, Faster, Stronger",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "211",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135557",
				"link": "https://www.deezer.com/track/3135557",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/1/f/6/0/1f65f58dc3cfa276ac6a1ee6f2ffac20.mp3?hdnea=exp=1759058349~acl=/api/1/1/1/f/6/0/1f65f58dc3cfa276ac6a1ee6f2ffac20.mp3*~data=user_id=0,application_id=42~hmac=fbf883cbfda130a8e53016737686c923e651ad44c4ce9fda91beb043d08b158b",
				"rank": "595844",
				"readable": True,
				"title": "Crescendolls",
				"title_short": "Crescendolls",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "104",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 6,
				"explicit_lyrics": False,
				"id": "3135558",
				"link": "https://www.deezer.com/track/3135558",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/c/0/6/0/c063dbb3b8f2af8dac3e88950f2e38b0.mp3?hdnea=exp=1759058349~acl=/api/1/1/c/0/6/0/c063dbb3b8f2af8dac3e88950f2e38b0.mp3*~data=user_id=0,application_id=42~hmac=c58498fc898e28bbf188b6c15cc84964443068be10693689c4299ab1ad91e5fc",
				"rank": "529366",
				"readable": True,
				"title": "Nightvision",
				"title_short": "Nightvision",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "237",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135559",
				"link": "https://www.deezer.com/track/3135559",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/1/b/c/0/1bc57c07bfaf6a265e06ce9574390e0e.mp3?hdnea=exp=1759058349~acl=/api/1/1/1/b/c/0/1bc57c07bfaf6a265e06ce9574390e0e.mp3*~data=user_id=0,application_id=42~hmac=4f1b8d2364503b18e21c0f3e55f2a3ba38d11cffd157625d1523660674f5f616",
				"rank": "568112",
				"readable": True,
				"title": "Superheroes",
				"title_short": "Superheroes",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "201",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135560",
				"link": "https://www.deezer.com/track/3135560",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/e/e/a/0/eea4fd9467e697d503998dff44ceeaa3.mp3?hdnea=exp=1759058349~acl=/api/1/1/e/e/a/0/eea4fd9467e697d503998dff44ceeaa3.mp3*~data=user_id=0,application_id=42~hmac=681be5682974a99332c2f01742cb309db0218d7a3fae5b6a497856a24c8e8128",
				"rank": "565141",
				"readable": True,
				"title": "High Life",
				"title_short": "High Life",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "232",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 6,
				"explicit_lyrics": False,
				"id": "3135561",
				"link": "https://www.deezer.com/track/3135561",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/c/f/f/0/cff7c95e11ba9f6ac3ff0401a81df4f5.mp3?hdnea=exp=1759058349~acl=/api/1/1/c/f/f/0/cff7c95e11ba9f6ac3ff0401a81df4f5.mp3*~data=user_id=0,application_id=42~hmac=697f57d1f7178178ba9d652147dab8e3b1d0f07ada1d19c4b7f8240771431a77",
				"rank": "764640",
				"readable": True,
				"title": "Something About Us",
				"title_short": "Something About Us",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "227",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135562",
				"link": "https://www.deezer.com/track/3135562",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/b/c/9/0/bc95bc4a6fdcf3e9b1672229f679eea1.mp3?hdnea=exp=1759058349~acl=/api/1/1/b/c/9/0/bc95bc4a6fdcf3e9b1672229f679eea1.mp3*~data=user_id=0,application_id=42~hmac=f6b9a63b4fb647040bcc4c1d68d04aba871280a9481d4a4eeeefd6dce256c4eb",
				"rank": "674182",
				"readable": True,
				"title": "Voyager",
				"title_short": "Voyager",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "345",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135563",
				"link": "https://www.deezer.com/track/3135563",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/6/4/5/0/6456b666c0b1d4537e34d71e5cbd098c.mp3?hdnea=exp=1759058349~acl=/api/1/1/6/4/5/0/6456b666c0b1d4537e34d71e5cbd098c.mp3*~data=user_id=0,application_id=42~hmac=6e2d8991f9aa826cb885302727487788965ec25062966b4928b7b8ce523964fc",
				"rank": "928445",
				"readable": True,
				"title": "Veridis Quo",
				"title_short": "Veridis Quo",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "206",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135564",
				"link": "https://www.deezer.com/track/3135564",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/4/1/3/0/413592fd246163564e5416fb72f8c831.mp3?hdnea=exp=1759058349~acl=/api/1/1/4/1/3/0/413592fd246163564e5416fb72f8c831.mp3*~data=user_id=0,application_id=42~hmac=4ad8dfc9c25207aeb41f65076c4c7d95627156aff41df1bcb776e59e027c6270",
				"rank": "510426",
				"readable": True,
				"title": "Short Circuit",
				"title_short": "Short Circuit",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "240",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135565",
				"link": "https://www.deezer.com/track/3135565",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/b/c/5/0/bc5ffa003d9ccf020a633083738c6ae4.mp3?hdnea=exp=1759058349~acl=/api/1/1/b/c/5/0/bc5ffa003d9ccf020a633083738c6ae4.mp3*~data=user_id=0,application_id=42~hmac=715e7327463c2de4d11e9da92a4f8de0f0147143b8c7860c95e3cdd840c88551",
				"rank": "624865",
				"readable": True,
				"title": "Face to Face",
				"title_short": "Face to Face",
				"title_version": "",
				"type": "track"
			},
			{
				"album": {
					"cover": "https://api.deezer.com/album/302127/image",
					"cover_big": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/500x500-000000-80-0-0.jpg",
					"cover_medium": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/250x250-000000-80-0-0.jpg",
					"cover_small": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/56x56-000000-80-0-0.jpg",
					"cover_xl": "https://cdn-images.dzcdn.net/images/cover/5718f7c81c27e0b2417e2a4c45224f8a/1000x1000-000000-80-0-0.jpg",
					"id": "302127",
					"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
					"title": "Discovery",
					"tracklist": "https://api.deezer.com/album/302127/tracks",
					"type": "album"
				},
				"artist": {
					"id": "27",
					"name": "Daft Punk",
					"tracklist": "https://api.deezer.com/artist/27/top?limit=50",
					"type": "artist"
				},
				"duration": "600",
				"explicit_content_cover": 0,
				"explicit_content_lyrics": 0,
				"explicit_lyrics": False,
				"id": "3135566",
				"link": "https://www.deezer.com/track/3135566",
				"md5_image": "5718f7c81c27e0b2417e2a4c45224f8a",
				"preview": "https://cdnt-preview.dzcdn.net/api/1/1/8/f/e/0/8fe6827c48cc62fb82fe8e741b0534f4.mp3?hdnea=exp=1759058349~acl=/api/1/1/8/f/e/0/8fe6827c48cc62fb82fe8e741b0534f4.mp3*~data=user_id=0,application_id=42~hmac=c22b829f328b439eb8fabaccfb16651a449e1cc74e918c3644354f639096bef0",
				"rank": "581722",
				"readable": True,
				"title": "Too Long",
				"title_short": "Too Long",
				"title_version": "",
				"type": "track"
			}
		]
	},
	"type": "album",
	"upc": "724384960650"
}


# print(daft_punk_data_dic["artist"]["name"])
# print(daft_punk_data_dic["tracks"]["data"][0]["explicit_content_lyrics"])

my_str = "ttvolume"
result = my_str.startswith("vol")

print(result)

from random import sample

my_number_list  = [1,2,3,4,4,5,6,6,7,78,8,9]
my_letter_list = ["t", "y", "u", "i", "o", "p"]
my_word_list = ["big", "small", "Mae"]
my_dic_list = [
	{"key1": 2},
	{"key3": "word 2"},
{"key5": "word 17"},
{"key66": "word 66666"},
]

results = sample(my_dic_list, 3)
print(results)