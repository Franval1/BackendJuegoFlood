import random
from cola import Cola


class Flood:
    """
    Clase para administrar un tablero de N colores.
    """

    def __init__(self, alto, ancho):
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        tablero = []
        for n in range(alto):
            fila = []
            for i in range(ancho):
                fila.append(1)
            tablero.append(fila)

        self.tablero = tablero
        self.colores = None
        self.alto = alto
        self.ancho = ancho




    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        colores = []
        cont = 0
        while cont != (n_colores):
            colores.append(cont)
            cont += 1
   
        for fila in range(len(self.tablero)):
            for i in range(len(self.tablero[fila])):
                color = random.choice(colores)
                self.tablero[fila][i] = color
        self.colores = colores

    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        # Parte 1: Cambiar el `raise` por tu código...
        if fil == len(self.tablero):
            return self.tablero[fil - 1][col]
        elif col == len(self.tablero[0]):
            return self.tablero[fil][col -1]
        return self.tablero[fil][col]




    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        return self.colores


    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        filas = len(self.tablero)
        columnas = len(self.tablero[0])
        return (filas, columnas)


    def cambiar_color(self, color_nuevo):
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        color = self.tablero[0][0]            
        self.pintar_casillero(0, 0, color_nuevo, color)


    def pintar_casillero(self, fila, columna, color_nuevo, color):
        if (fila >= len(self.tablero)) or (columna >= len(self.tablero[0])):
            return
        if fila < 0 or columna < 0:
            return
        if self.tablero[fila][columna] != color:
            return     
        if color_nuevo == color:
            return   
        self.tablero[fila][columna] = color_nuevo

        self.pintar_casillero(fila + 1, columna, color_nuevo, color)
        self.pintar_casillero(fila - 1, columna, color_nuevo, color)
        self.pintar_casillero(fila, columna + 1, color_nuevo, color)
        self.pintar_casillero(fila, columna - 1, color_nuevo, color)
    




    def obtener_flood(self, fila, columna, color):

        celdas = []
        return self._obtener_flood(fila, columna, color, celdas)



    def _obtener_flood(self, fila, columna, color, celdas):
        """obtiene el tamaño del flood actual dado su color"""
        tamano_flood = 0
        if (fila >= len(self.tablero)) or (columna >= len(self.tablero[0])):
            return tamano_flood
        if (fila < 0 or columna < 0) or (self.tablero[fila][columna] != color):
            return tamano_flood
        if (fila, columna) in celdas:
            return tamano_flood
        if self.tablero[fila][columna] == color:
            tamano_flood +=1
            celdas.append((fila, columna))
            t1 = self._obtener_flood(fila + 1, columna, color, celdas)
            t2 = self._obtener_flood(fila - 1, columna, color, celdas)
            t3 = self._obtener_flood(fila, columna + 1, color, celdas)
            t4 = self._obtener_flood(fila, columna - 1, color, celdas)
        return  tamano_flood + t1 + t2 + t3 + t4


    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        clon = Flood(self.alto, self.ancho)
        clon.tablero = []
        for fila in self.tablero:
            clon.tablero.append(fila[:])
        clon.colores = self.colores
        return clon
    

    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        color_comparar = self.tablero[0][0]
        for f in range(len(self.tablero)):
            for c in self.tablero[f]:
                color_columna = c
                if color_comparar != color_columna:
                    return False
        return True
                
