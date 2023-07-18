def crack_pin(pin):
    attempt = 1

    for guess in range(10000):  # максимальное число для 4-значного пина
        guess_pin = str(guess).zfill(4)  # ведущие нули добавляются, чтобы всегда получался 4-значный код

        if attempt % 1000 == 0:
            print(f'Попытка {attempt}: {guess_pin}')

        if guess_pin == pin:
            return f'PIN-код "{pin}" подобран за {attempt} попыток.'
        
        attempt += 1
    
    return 'PIN-код не подобран.'

print(crack_pin('1234'))
