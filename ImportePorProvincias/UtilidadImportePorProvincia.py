class UtilidadImportePorProvincia:
    def __init__(self):
        self.dfResult = 0

    # Imported methods
    from .calcularImportePorProvincia import calcular
    from .crearTablaImportePorProvincia import crear

    def crearTablaProvinciaImporte(self):
        self.calcular()
        self.crear()

    def printHeadTablaProvinciaImporte(self):
        self.dfResult.head()
