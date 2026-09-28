total_secondes = int(input("insère un nombre de secondes : "))
heures = total_secondes // 3600
reste_secondes = total_secondes % 3600
minutes = reste_secondes // 60
secondes = reste_secondes % 60
print(f" {heures} heure, {minutes} minute et {secondes} seconde.")