# github.com/haze0001
# haze#1337
import os
import time
# Variablen
id = 0 # Nicht ändern
plan = "b0562473-f874-4649-a974-5e8b66e7eae1" # Anpassen an die eigene Plan-ID
clear = "cls" # Nicht ändern
# Code
os.system(clear)
running = True
while running == True:
    id = id + 1
    time.sleep(25)
    os.system("powercfg.exe /setactive " + plan)
    print(id, "| Erfolgreich, warte 25 Sekunden bevor neustart.")

