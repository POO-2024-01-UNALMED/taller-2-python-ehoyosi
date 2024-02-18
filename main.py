class Asiento:
     
    def __init__(self, color, precio, registro ):
        
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):

        if (color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco") :
            
            self.color = color
                       
class Motor:
    
    def __init__(self,numeroCilindros, tipo, registro):
        
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self,registro):
        
        self.registro = registro
        
    def asignarTipo(self, tipo):
        if (tipo == "gasolina" or tipo == "electrico"):
            self.tipo = tipo
            
class Auto:
    
    cantidadCreados = 0
    def __init__(self, modelo, precio, marca, motor, registro, asientos,):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.asientos = asientos
        Auto.cantidadCreados += 1
        
    def cantidadAsientos(self):
        
        numAsientos = 0
        
        for asiento in self.asientos:
            
            if (asiento is not None):
                
                numAsientos += 1
                
        return numAsientos
    
    def verificarIntegridad(self):
        
        if (self.registro == self.Motor.registro):
            
            for i in self.asientos:
                
                if (i is not None):
                    
                    if (i.registro != self.registro):
                        
                        return "Las piezas no son originales"
                    
            return "Auto original"
        
        else:
            
            return "Las piezas no son originales"
                        
                        
                
                
        
        
        
        
        
        
    
    
        
        
        
        
        
    
    