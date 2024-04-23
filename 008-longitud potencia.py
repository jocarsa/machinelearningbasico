from PIL import Image,ImageFilter

imagen = Image.open("josevicente.jpg")
escalado = imagen.resize((512,512))
grises = escalado.convert("L")
bordes = grises.filter(ImageFilter.FIND_EDGES)
blancoynegro = bordes.point(lambda x:0 if x < 50 else 255,'1')
pixeles = blancoynegro.load()
anchurabloque = 2
longitud = pow(2,pow(anchurabloque,2))

