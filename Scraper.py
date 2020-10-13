from bs4 import BeautifulSoup
import requests
from Pelicula import Pelicula

# Peticion a la pagina
r = requests.get("https://pctfenix.com/descargar-peliculas/hd/")

# Se guarda en la variable soup todo el contenido de la pagina 
soup = BeautifulSoup(r.text, 'html.parser')

# Primer filtro para quedarnos solo con los divs de peliculas usando el class name movie-item en la variable divs
divs = soup.find_all('div',class_='movie-item')

#lista para almacenar las peliculas
lista_peliculas = []

# Una vez tenemos los divs de peliculas los recorremos y filtramos
for i in divs:

    # Aqui obtenemos tanto el titulo como la calidad de las distintas peliculas
    titulos=i.find('div',class_='title-in')
    titulo=titulos.h6.a.text
    calidad =titulos.strong.text

    # Aqui obtenemos el enlace de la caratula de la pelicula
    imagenes = i.find('div',class_='mv-img')
    imagen=imagenes.img['src']

    #creamos el objeto pelicula y lo añadimos a la lista
    pe = Pelicula(titulo,calidad,imagen)
    lista_peliculas.append(pe)
 
 
for p in lista_peliculas:
   print(p.titulo) 
   print(p.enlace_torrent)

    
        



