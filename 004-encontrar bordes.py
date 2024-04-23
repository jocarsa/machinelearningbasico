from PIL import Image,ImageFilter

imagen = Image.open("josevicente.jpg")
escalado = imagen.resize((512,512))
grises = escalado.convert("L")
bordes = grises.filter(ImageFilter.FIND_EDGES)
bordes.show()
