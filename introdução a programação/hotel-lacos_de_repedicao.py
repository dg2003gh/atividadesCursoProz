from time import sleep

andares: int = 20

print("-----------||For Loop||-----------")
for andar in range(andares):
        match andar:
            case 12:
                    pass
            case _:
                print(f"{andar+1}º andar")
                print("||--------------------||")
        sleep(1)

print("-----------||While Loop Reverso||-----------")
while andares > 0:
        andares -= 1
        if andares == 12:
            pass
        else:
                print(f"{andares+1}º andar")
                print("--==||--------------------||==--")
        sleep(1)
       
print("-----------||While Loop||-----------")
while andares < 20:
        andares += 1
        if andares == 13:
            pass
        else:
                print(f"{andares}º andar")
                print("--==||--------------------||==--")
        sleep(1)
                

