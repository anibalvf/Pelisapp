class Pelicula():

    # Constructor
    def __init__(self,titulo,calidad,url_imagen):
        self.titulo = titulo
        self.calidad = calidad
        self.url_imagen =url_imagen
        self.getEnlaceTorrent()


    def getEnlaceTorrent(self):
        prefijoTorrent="https://pctfenix.com/uploads/t/"

        enlace = self.url_imagen.split("/")

    
        if "thumbs" in enlace:

            self.enlace_torrent = prefijoTorrent+enlace[6][:-4]+".torrent"
        else:
            self.enlace_torrent=prefijoTorrent+enlace[5][:-4]+".torrent"

        




    