import sqlite3
import time
import random
import re
from core import HuachiNet

conn = sqlite3.connect('boveda.sqlite3')

cursor = conn.cursor()


def huachilate(redditor_id):
    """Vengase y agarre su !huachilote"""

    #Acceder a cuenta del redditor
    Huachis_redditor = HuachiNet(redditor_id)
        
    #Verificar que tenga cuenta
    if Huachis_redditor.Verificar_Usuario(redditor_id) == False:
        
        return random.choice(resp_tip_cuenta)

    else: 
        #Verificar que tenga saldo
        if Huachis_redditor.saldo_total < 50:
            
            return random.choice(resp_tip_sinbineros)

        else:
            #Cobrar la entrada
            Huachis_redditor.Enviar_Bineros("Huachicuenta",50,nota="Huachilate")

            huachiclave = Huachis_redditor.Huachiclave()

            valores = (time.time(),redditor_id,huachiclave[1])
            
            conn.execute("""INSERT INTO boletitos (timestamp,usuario,huachiclave) VALUES (?,?,?)""",valores)

            conn.commit()

            huachicuenta = HuachiNet("Huachicuenta")

            if int(huachicuenta.saldo_total) >= huachiclave[2]:
                premio_huachilate()

            return f"Huachilote vendido a {redditor_id}"


def premio_huachilate():
    """Repartir premios del huachilate"""

    huachicuenta = HuachiNet("Huachicuenta")

    huachiclave = huachicuenta.Huachiclave()

    participantes = [usuario[0] for usuario in cursor.execute("""SELECT usuario FROM boletitos WHERE huachiclave = ?""",(huachiclave[1],)).fetchall()]

    ganadores = set(random.sample(participantes,k = 10))

    ganadores = list(ganadores)

    premios = [round((int(huachicuenta.saldo_total) * 50 ) / 100),round((int(huachicuenta.saldo_total) * 30 ) / 100),round((int(huachicuenta.saldo_total) * 20 ) / 100)]

    #Entregar premios
    #Primer lugar 50%
    huachicuenta.Enviar_Bineros(ganadores[0],premios[0],nota="Premio Huachilate")
    #Segundo lugar 30%
    huachicuenta.Enviar_Bineros(ganadores[1],premios[1],nota="Premio Huachilate")
    #Tercer lugar 20%
    huachicuenta.Enviar_Bineros(ganadores[2],premios[2],nota="Premio Huachilate")

    cursor.execute("""UPDATE huachilate SET entregado = 1 WHERE huachiclave = ?""",(huachiclave[1],))

    conn.commit()


if __name__ == "__main__":
    
    huachilate("")

    
