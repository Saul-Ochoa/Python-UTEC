# importar librerias
import random
class Guerrero:
    def __init__(self, nombre, salud, ataque):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque

    def atacar(self, enemigo):
        danio = self.calcular_danio()
        enemigo.recibir_danio(danio)
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {danio} de daño a {enemigo.nombre}")

    def calcular_danio(self):
        return random.randint(self.ataque // 2, self.ataque)

    def recibir_danio(self, danio):
        self.salud -= danio
        print(f"{self.nombre} recibe {danio} de daño y su salud ahora es {self.salud}.")

    def estar_vivo(self):
        return self.salud > 0

              
# clase derivada para un guerrero con habilidades especiales
class GuerreroEspecial(Guerrero):
    def __init__(self, nombre, salud, ataque,habilidad_especial):
        super().__init__(nombre, salud, ataque)
        self.habilidad_especial=habilidad_especial
    def usar_habilidad_especial(self,enemigo):
        danio=self.habilidad_especial() # daño es como una habilidad especial
        enemigo.recibir_danio(danio)
        print(f"{self.nombre} usa su habilidad especial y causa {danio} de daño a {enemigo.nombre}.")
    
# funcion para la habilidad especial
def habilidad_fuego():
    return random.randint(15,30)
def habilidad_hielo():
    return random.randint(10,25)

# funcion principal del fuego 
def jueguo_de_guerreros():
    guerrero1=Guerrero("Guerrero1",100,20)
    guerrero2=GuerreroEspecial("Guerrero2",100,15,habilidad_fuego)
    turno=0
    while guerrero1.estar_vivo() and guerrero2.estar_vivo():
        turno+=1
        print(f"\n--Turno {turno} --")
        if turno %2==1:
            guerrero1.atacar(guerrero2)
        else:
            if random.choice([True,False]):
                guerrero2.usar_habilidad_especial(guerrero1)
            else:
                guerrero2.atacar(guerrero1)
        if not guerrero1.estar_vivo():
            print(f"{guerrero1.nombre} ha sido derrotado. ¡{guerrero2.nombre} gana!")
            return "Guerrero2"
        if not guerrero2.estar_vivo():
            print(f"{guerrero2.nombre} ha sido derrotado. ¡{guerrero1.nombre} gana!")
            return "Guerrero1"
# iniciar juego
# jueguo_de_guerreros()

#######################################################################################
#######################################################################################
#################################Simulacion############################################
#######################################################################################
#######################################################################################
def simulacion(batallas):
    victorias_guerrero1=0
    victorias_guerrero2=0
    for _ in range(batallas):
        ganador=jueguo_de_guerreros()
        if ganador=="Guerrero1":
            victorias_guerrero1+=1
        else:
            victorias_guerrero2+=1
    print(f"\n En {batallas} batallas")
    print(f"Guerrero1 gano {victorias_guerrero1} veces.")
    print(f"Guerrero2 gano {victorias_guerrero2} veces.")

simulacion(1000)