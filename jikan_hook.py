from jikanpy import Jikan

jikan = Jikan()

def pull_img (char_id):
	character_images = jikan.character(extension ='pictures', id = char_id)
	return character_images['image']

print(pull_img(11))