from PIL import Image

imagen = Image.open("josevicente.jpg")
escalado = imagen.resize((512,512))
escalado.show()
