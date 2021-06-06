"""
Classes que ajuden a implementar les etapes d'un joc.
"""

class Etapa(object):

    def executa_iteracio(self):
        """
        Actualitza l'estat de l'etapa, gestiona esdeveniments i dibuixa l'estat.

        Es crida a cada iteració del bucle principal.
        """
        return

class Joc(object):

    def executa(self):
        """
        Executa el bucle principal del joc.

        A cada iteració crida al mètode executa_iteració de l'etapa
        que estigui activa .
        """
        final = False
        self.inicialitza()
        while not final:
            final = self.etapa.executa_iteracio()
            self.sincronitza()
        self.acaba()

    def inicialitza(self):
        """
        Inicialitza el bucle principal.

        Es crida abans de començar la iteració del bucle principal.
        """
        return

    def sincronitza(self):
        """
        Sincronitza la visualització i el retard en el pas del temps.

        Es crida al final de cada iteració del bucle principal.
        """
        return

    def acaba(self):
        """
        Acaba el bucle principal.

        Es crida un cop acabat el bucle principal.
        """
        return
