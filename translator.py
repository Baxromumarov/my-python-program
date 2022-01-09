from googletrans import Translator
savol = input("Tilni tanlang(en/ru): ")
if savol=='en':
	matn_uz = input("Matnni kiriting: ")
	tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
	tarjima = tarjimon.translate(matn_uz)
	print(tarjima.text)
if savol == "ru":
	matn_ru = input("Matnni kiriting: ")
	tarjimon = Translator()
	tarjima_ru = tarjimon.translate(matn_ru, dest='ru')
	print(tarjima_ru.text)