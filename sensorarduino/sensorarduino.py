import serial
import time

# Abrir a porta COM (troque COM3 caso seu Arduino use outra)
arduino = serial.Serial("COM3", 9600)
time.sleep(2)  # tempo para iniciar conexão

print("Lendo dados do Arduino...\n")

while True:
    if arduino.in_waiting > 0:
        linha = arduino.readline().decode().strip()
        
        # Mostrar o que veio da serial
        print(linha)

        # Se a linha contiver a distância, vamos pegar o número
        if "Distancia:" in linha:
            try:
                valor = float(linha.split(":")[1].split("cm")[0])
                print(f"Distância lida = {valor} cm\n")

            except:
                pass
