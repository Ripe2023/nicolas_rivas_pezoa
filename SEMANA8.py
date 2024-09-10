class Nodo:
    def __init__(self, paciente):
        self.paciente = paciente
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, paciente):
        self.raiz = self._insertar(self.raiz, paciente)

    def _insertar(self, raiz, paciente):
        if raiz is None:
            return Nodo(paciente)
        if paciente.id < raiz.paciente.id:
            raiz.izquierdo = self._insertar(raiz.izquierdo, paciente)
        elif paciente.id > raiz.paciente.id:
            raiz.derecho = self._insertar(raiz.derecho, paciente)
        return raiz

    def buscar(self, id_paciente):
        return self._buscar(self.raiz, id_paciente)

    def _buscar(self, raiz, id_paciente):
        if raiz is None or raiz.paciente.id == id_paciente:
            return raiz
        if id_paciente < raiz.paciente.id:
            return self._buscar(raiz.izquierdo, id_paciente)
        return self._buscar(raiz.derecho, id_paciente)

    # Implementar otras operaciones según sea necesario
