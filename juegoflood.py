from flood import Flood
from pila import Pila
from cola import Cola


class JuegoFlood:
    """
    Clase para administrar un Flood, junto con sus estados y acciones
    """

    def __init__(self, alto, ancho, n_colores):
        """
        Genera un nuevo JuegoFlood, el cual tiene un Flood y otros
        atributos para realizar las distintas acciones del juego.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla del Flood.
            n_colores: Cantidad maxima de colores a incluir en la grilla.
        """
        self.flood = Flood(alto, ancho)
        self.flood.mezclar_tablero(n_colores)
        self.mejor_n_movimientos, _ = self._calcular_movimientos()
        self.n_movimientos = 0
        self.pasos_solucion = Cola()
        self.estados = Pila()
        self.estado_rehacer = Pila()
        self.clon = self.flood.clonar
        # Parte 3: Agregar atributos a la clase...


    def cambiar_color(self, color):
        """
        Realiza la acción para seleccionar un color en el Flood, sumando a la
        cantidad de movimientos realizados y manejando las estructuras para
        deshacer y rehacer

        Argumentos:
            color (int): Nuevo color a seleccionar
        """


        self.n_movimientos += 1
        self.clon = self.flood.clonar()        
        self.estados.apilar(self.clon)
        self.flood.cambiar_color(color) 


        if not self.pasos_solucion.esta_vacia() and self.pasos_solucion.ver_frente() == color:
            self.pasos_solucion.desencolar()


        else:
            self.pasos_solucion = Cola()


    def deshacer(self):
        """
        Deshace el ultimo movimiento realizado si existen pasos previos,
        manejando las estructuras para deshacer y rehacer.
        """
        if not self.estados.esta_vacia():
            estado = self.estados.desapilar()
            self.flood.tablero = estado.tablero
            self.estado_rehacer.apilar(estado)
            self.n_movimientos -= 1
        else:
            return


        
        self.pasos_solucion = Cola()


    def rehacer(self):
        """
        Rehace el movimiento que fue deshecho si existe, manejando las
        estructuras para deshacer y rehacer.
        """
        if not self.estado_rehacer.esta_vacia():
            estado_rehacer = self.estado_rehacer.desapilar()
            self.flood.tablero = estado_rehacer.tablero
            self.estados.apilar(estado_rehacer)
            self.n_movimientos += 1
        self.pasos_solucion = Cola()


    def _calcular_movimientos(self):
        """
        Realiza una solución de pasos contra el Flood actual (en una Cola)
        y devuelve la cantidad de movimientos que llevó a esa solución.

        COMPLETAR CON EL CRITERIO DEL ALGORITMO DE SOLUCIÓN.
        utiliza una comparacion de opciones y toma cual de esas opciones de colores
        es la que mas casillas del flood completa hasta terminar el juego.

        Devuelve:
            int: Cantidad de movimientos que llevó a la solución encontrada.
            Cola: Pasos utilizados para llegar a dicha solución
        """


        solucion = Cola()
        pasos = 0
        tablero_prueba = self.flood.clonar()

        while not tablero_prueba.esta_completado():
            opciones = {}
            agrega_al_flood = 0
            eleccion = 0
            tamano_inicial = tablero_prueba.obtener_flood(0,0,tablero_prueba.tablero[0][0])

            for i in tablero_prueba.colores:
                if i == tablero_prueba.tablero[0][0]:
                    continue
                tablero = tablero_prueba.clonar()
                tablero.cambiar_color(i)
                tamano_final = tablero.obtener_flood(0,0,tablero.tablero[0][0])
                cant_agregada = tamano_final - tamano_inicial
                opciones[i] = cant_agregada
                

            for clave, valor in opciones.items():
                if   valor > agrega_al_flood:
                    eleccion = clave
                    agrega_al_flood = valor
            tablero_prueba.cambiar_color(eleccion)
            pasos += 1
            solucion.encolar(eleccion)
        
        return pasos, solucion



                



    def hay_proximo_paso(self):
        """
        Devuelve un booleano indicando si hay una solución calculada
        """
        return not self.pasos_solucion.esta_vacia()


    def proximo_paso(self):
        """
        Si hay una solución calculada, devuelve el próximo paso.
        Caso contrario devuelve ValueError

        Devuelve:
            Color del próximo paso de la solución
        """
        return self.pasos_solucion.ver_frente()


    def calcular_nueva_solucion(self):
        """
        Calcula una secuencia de pasos que solucionan el estado actual
        del flood, de tal forma que se pueda llamar al método `proximo_paso()`
        """
        _, self.pasos_solucion = self._calcular_movimientos()


    def dimensiones(self):
        return self.flood.dimensiones()


    def obtener_color(self, fil, col):
        return self.flood.obtener_color(fil, col)
        


    def obtener_posibles_colores(self):
        return self.flood.obtener_posibles_colores()


    def esta_completado(self):
        return self.flood.esta_completado()
