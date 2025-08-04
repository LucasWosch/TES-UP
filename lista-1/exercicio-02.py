# Conversor de Temperatura

celsius     = float(input("Digite uma temperatura em C°: "))
fahrenheit  = celsius * 1.8 + 32
kelvin      = celsius + 273.15

print(f"Temperatura digitada em C°: {round(celsius, 2)}\n"
      f"Temperatura digitada em F°: {round(fahrenheit, 2)} \n"
      f"Temperatura digitada em K°: {round(kelvin, 2)} \n")