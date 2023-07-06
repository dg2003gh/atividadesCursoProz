from time import sleep

segundos: int = 11

bomb: str = '''
                                  ..-^~~~^-..
                                .~           ~.
                               (;:           :;)
                                (:           :)
                                  ':._   _.:'
                                      | |
                                    (=====)
                                      | |
-O-                                   | |
  \                                   | |
  /\                               ((/   \))

'''

class nice_colors:
    YELLOW = '\033[93m'
    GREEN= '\033[92m'
    RED = '\033[91m'

print('Iniciando contagem regressiva!')
print('--------------//--------------')

while segundos > 0:
        segundos -= 1
      
        if segundos == 0:
            print(nice_colors.RED + 'BUM!')
            print(bomb)
            break
        elif segundos <= 5:
            print(nice_colors.YELLOW + f"Explodindo em 0:0{segundos}...")
            sleep(1)
        elif segundos == 10:
            print(nice_colors.GREEN + f"Explodindo em 0:{segundos}...")
            sleep(1)
        else:
            print(nice_colors.GREEN + f"Explodindo em 0:0{segundos}...")
            sleep(1)
