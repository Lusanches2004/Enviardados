import serial
import time

# ALTERE para a sua porta (COM3, COM4, etc.)
PORTA = "COM3" 
BAUD_RATE = 9600

try:
    # Abre a porta serial
    arduino = serial.Serial(PORTA, BAUD_RATE, timeout=1)
    time.sleep(2)  # necessário para o Arduino reiniciar

    print("Conectado ao Arduino em", PORTA)
    print("Digite uma letra (a–k) ou 'sair' para fechar.")
    print("-------------------------------------------")

    while True:
        # Lê do teclado
        dado = input("Enviar: ")

        if dado == "sair":
            break

        if len(dado) > 0:
            # envia só o primeiro caractere
            arduino.write(dado[0].encode())

        # recebe resposta do Arduino (se tiver)
        if arduino.in_waiting > 0:
            resposta = arduino.readline().decode().strip()
            if resposta:
                print("Arduino:", resposta)

    arduino.close()
    print("Conexão encerrada.")

except serial.SerialException:
    print("Erro ao abrir a porta. Verifique se o Arduino está conectado e qual COM é.")
