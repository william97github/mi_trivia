import random
import time

nombre = input("Ingrese su nombre: ")

iniciar = True
intentos = 1
while iniciar == True:

  puntaje = random.randint(1,10)
  correctos = 0

  rojo = "\033[31m"
  verde = "\033[32m"
  azul = "\033[34m"
  amarillo = "\033[33m"
  reset = "\033[39m"

  for x in range(5,0,-1):
    print(x)
    time.sleep(1)

  print(azul+"\n Hola ", nombre, " jugaremos a la trivia sobre las atracciones turisticas del Perú."+reset)




  print(azul+"\n Comensaras con ",puntaje,"vidas.\n Si llega a tener 0 vidas prederas el juego."+reset)

  time.sleep(3)

  if puntaje <=0 :
    repetir = input(rojo+"No cuenta con vidas para seguir en el juego. \n Ingrese (si) para volver a intentarlo."+reset).lower()
    if repetir != "si":
      iniciar == False
      intentos += 1
  else:
    print("\n ¿El Santuario Histórico de Machu Picchu, se encuentra en la región? \n A) Ica. \n B) Arequipa. \n C) Cusco. \n D) Puno.")
    respuesta1 = input("Escriba la alternativa que considere corecta: ")
    while respuesta1 not in ("a","A","b","B","c","C","d","D","r","R"):
      respuesta1 = input("\n vuelva intentarlo: ")
    if respuesta1 == "c" or respuesta1 == "C":
      correctos +=1
      puntaje*=random.randint(1,5)
      print(verde+"\n Correcto, puede pasar a la siguiente pregunta.\n Ahora cuenta con ",puntaje,"vidas."+reset)
    elif respuesta1 == "r" or respuesta1 == "R":
      puntaje*=random.randint(1,5)
      print("La respuesta es la alternativa C jajaja. \n Que suerte, puede pasar a la siguiente pregunta.\n Ahora cuenta con ",puntaje,"vidas.")
    elif respuesta1 == "a" or respuesta1 == "A":
      print("\n Ica, region cuyos atractivos turisticos son Lineas de Nazca, Reserva Nacional de Paracas e Islas Ballestas, Laguna Huacachina.")
      puntaje/=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")
    elif respuesta1 == "b" or respuesta1 == "B":
      print("\n Arequipa, region cuyos atractivos turisticos son Valle del Colca, Monasterio de Santa Catalina.")
      puntaje-=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")
    elif respuesta1 == "d" or respuesta1 == "D":
      print("\n Puno, region cuyos atractivos turisticos es el Lago Titicaca.")
      puntaje+=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")

  time.sleep(3)

  if puntaje <=0 :
    repetir = input(rojo+"No cuenta con vidas para seguir en el juego. \n Ingrese (si) para volver a intentarlo."+reset).lower()
    if repetir != "si":
      iniciar == False
      intentos += 1
  else:
    print("\n ¿La playa Las Pocitas es la playa más tranquila y hermosa de Perú, se encuentra en la región? \n A) Piura. \n B) Ancash. \n C) Lima. \n D) Loreto.")
    respuesta1 = input("Escriba la alternativa que considere corecta: ")
    while respuesta1 not in ("a","A","b","B","c","C","d","D","r","R"):
      respuesta1 = input("\n vuelva intentarlo: ")
    if respuesta1 == "a" or respuesta1 == "A":
      correctos +=1
      puntaje*=random.randint(1,5)
      print(verde+"\n Correcto, puede pasar a la siguiente pregunta.\n Ahora cuenta con ",puntaje,"vidas."+reset)
    elif respuesta1 == "r" or respuesta1 == "R":
      puntaje*=random.randint(1,5)
      print("La respuesta es la alternativa A jajaja. \n Que suerte, puede pasar a la siguiente pregunta.\n Ahora cuenta con ",puntaje,"vidas.")
    elif respuesta1 == "b" or respuesta1 == "b":
      print("\n Ancash, region cuyos atractivos turisticos son Las lagunas Llanganuco son dos espejos de aguas de color turquesa y celeste, Chavín de Huántar.")
      puntaje/=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")
    elif respuesta1 == "c" or respuesta1 == "c":
      print("\n Lima, region cuyos atractivos turisticos es la Huaca Pucllana es un antiguo centro ceremonial precolombino construido con adobes, cantos rodados y arena, el sitio arqueológico de Caral es considerado la ciudad más antigua de Perú")
      puntaje-=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")
    elif respuesta1 == "d" or respuesta1 == "D":
      print("\n Loreto, region cuyos atractivos turisticos es el El río amazonas es el río más largo y caudaloso de la tierra y una de las mayores reservas de agua dulce del planeta, Pacaya Samiria es la reserva más extensa de la Amazonia Peruana.")
      puntaje+=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")

  time.sleep(3)

  if puntaje <=0 :
    repetir = input(rojo+"No cuenta con vidas para seguir en el juego. \n Ingrese (si) para volver a intentarlo."+reset).lower()
    if repetir != "si":
      iniciar == False
      intentos += 1
  else:
    print("\n ¿Los Baños del Inca es un balneario de aguas termo medicinales que posee propiedades curativas, se encuentra en la región? \n A) Arequipa. \n B) Tumbes. \n C) Trujillo. \n D) Cajamarca.")
    respuesta1 = input("Escriba la alternativa que considere corecta: ")
    while respuesta1 not in ("a","A","b","B","c","C","d","D","r","R"):
      respuesta1 = input("\n vuelva intentarlo: ")
    if respuesta1 == "d" or respuesta1 == "D":
      correctos +=1
      puntaje*=random.randint(1,5)
      print(verde+"\n Correcto, acaba de culminar la trivia.\n Ahora cuenta con ",puntaje,"vidas."+reset)
    elif respuesta1 == "r" or respuesta1 == "R":
      puntaje*=random.randint(1,5)
      print("La respuesta es la alternativa D jajaja. \n Que suerte, puede pasar a la siguiente pregunta.\n Ahora cuenta con ",puntaje,"vidas.")
    elif respuesta1 == "a" or respuesta1 == "A":
      print("\n Arequipa, region cuyos atractivos turisticos es el Valle del Colca es un extenso valle de tierras fértiles que bordea el río Colca.")
      puntaje/=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")
    elif respuesta1 == "b" or respuesta1 == "B":
      print("\n Tumbes, region cuyos atractivos turisticos son Los Manglares de Tumbes que es un área protegida que abarca una porción de la eco región del golfo de Guayaquil, Punta Sal un hermoso balneario que está ubicado en la provincia de Contralmirante Villar.")
      puntaje-=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")
    elif respuesta1 == "c" or respuesta1 == "C":
      print("\n Trujillo, region cuyos atractivos turisticos es Chan Chan es la ciudad de adobe más grande de América y la segunda del mundo, Huanchaco es un histórico balneario que está ubicado en el distrito de Huanchaco.")
      puntaje+=random.randint(1,5)
      print("\n Ahora cuenta con ",puntaje," vidas.")

      print("\n\n Respondio correctamente ",correctos,"preguntas. \n En ",intentos," intentos.")

    res = input(amarillo+"\n Ingrese R para ver las respuestas y tereminar el juego o cualquier teclado para tvolver a intentarlo: "+reset)

    if res == "r" or res == "R":
      print(amarillo+"Pregunta 1: C \n Pregunta 2: A \n Pregunta 3: D \n Gracias por jugar mi trivia!!!"+reset)
      iniciar == False
    else:
      print(amarillo+"\n Gracias por jugar mi trivia!!!"+reset)
      iniciar == False
