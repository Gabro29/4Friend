from datetime import date
import calendar
import pandas as pd
start_date = date(2021, 11, 19)
end_date = date(2022, 11, 19)

choice = input("Digita per esempio Feriale o Festivo ")

dizi = {0: "Lunedì", 1: "Martedì", 2: "Mercoledì", 3: "Giovedì", 4: "Venerdì", 5: "Sabato", 6: "Domenica"}
data = [date.fromordinal(day) for day in range(start_date.toordinal(), end_date.toordinal())]
dayp = [dizi[date.fromordinal(day).weekday()] for day in range(start_date.toordinal(), end_date.toordinal())]
typep = ["Feriale" if dizi[date.fromordinal(day).weekday()] not in ("Sabato", "Domenica") else "Festivo" for day in range(start_date.toordinal(), end_date.toordinal())]

dataf = pd.DataFrame(data)
dataf["1"] = pd.Series(dayp)
dataf["2"] = pd.Series(typep)
dataf.columns = ["Data", "DayP", "TypeP"]
# print(dataf)
# print(calendar.day_name[my_date.weekday()])
if choice == "":
    pass
else:
    dataf = dataf[dataf["TypeP"] == choice]
print(f"Numero di giorni tra l'uno e l'altro {dataf.Data.size}")
print(f"Numero di ore tra l'uno e l'altro {dataf.Data.size*24}")
print(f"Numero di minuti tra l'uno e l'altro {dataf.Data.size*24*60}")
print(f"Numero di secondi tra l'uno e l'altro {dataf.Data.size*24*60*60}")



