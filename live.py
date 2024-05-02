#!\bin\python3
import pyautogui
import time
import sys

def separador():
    print ("="*80)

def menu():
    print("""
            1 - Escolher o local do mouse.
            2 - Deixar padrão o local do mouse. 
            0 - Sair.
        """)

def opcao():
    escolha = int(input("Informe um número: "))
   
    return escolha

def resposta1():
    separador()

    print('Posicione o mouse!!')

    for cont in range(1,11):
        print("Faltan {} segundos" .format(cont))
        time.sleep(0.5)

    print("programa inicializado")

    posicao = pyautogui.position()

    return posicao

def resposta2():
    posicao = pyautogui.moveTo(1549,884)

    return posicao

def sair():
    sys.exit()


def mandar_mensagem(posicao_mouse):
    termina = False

    while termina == False:
        # 5 minutos
        separador()
        for cont in range(1,300000):
            print("Mensagem sera enviada em {} milisegundos" .format(cont))
            time.sleep(0.5)
        

        pyautogui.moveTo(posicao_mouse.x, posicao_mouse.y)
        pyautogui.click(posicao_mouse.x, posicao_mouse.y)
        time.sleep(0.5)

        pyautogui.hotkey('win', '.')
        time.sleep(1)
        pyautogui.write('top')
        time.sleep(5)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(posicao_mouse.x, posicao_mouse.y)
        time.sleep(0.5)
        pyautogui.press('enter')

        separador()
        print("Mensagem enviada")


        # Configurar uma tecla para encerrar o boot

def main():
    separador()
    menu()
    escolha = opcao()

    match escolha:
        case 1:
            posicao_mouse = resposta1()

            mandar_mensagem(posicao_mouse)

        case 2:
            print('Em produção!!')

            # posicao_mouse = resposta2()

            # mandar_mensagem(posicao_mouse)
        case 0:
            sair()

    separador()

if __name__ == "__main__":
    main()