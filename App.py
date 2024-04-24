import os

def exibirnomedoprograma():
      print('''

      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
      ''')

def exibir_opcoes():
      print('1. Cadatrar restaurante')
      print('2. Listar restaurantes')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def finalizar_app():
      os.system('cls')
      print('Finalizando o app\n')

def opçãoInvalida():
      print('Opção invalida\n')
      input('Digite uma tecla para voltar ao menu principal')


def escolheropcao():
      try:
            opcaoEscolhida = int(input('Escolha uma opção: '))
            # opcaoEscolhida = int(opcaoEscolhida)

            if opcaoEscolhida == 1:
                  print('Cadastrar restaurante')
            elif opcaoEscolhida == 2:
                  print('LIstar restaurantes')
            elif opcaoEscolhida == 3:
                  print('Ativar restaurante')
            elif opcaoEscolhida == 4:
                  finalizar_app()
            else:
                  opçãoInvalida()
      except:   
            opçãoInvalida()        

def main():
      os.system('cls')
      exibirnomedoprograma()
      exibir_opcoes()
      escolheropcao()

if __name__ == '__main__': 
      main() 




