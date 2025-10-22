# ----
# Exercise:
# Class "StimmungsOrakel" is given and its methods
# Ask user for current activity and time
# Output mood, tip of the day and energy level with the use of StimmungsOrakel and its methods
class StimmungsOrakel:
    def __init__(self, name):
        self.name = name

    def bestimme_stimmung(self, aktivität, tageszeit):
        if aktivität == "arbeit":
            return "🤯 Gestresst" if tageszeit == "morgen" else "😴 Müde"
        elif aktivität == "freizeit":
            return "😄 Fröhlich" if tageszeit == "nachmittag" else "😎 Entspannt"
        elif aktivität == "kreativ":
            return "🤩 Kreativ"
        else:
            return "😎 Entspannt"

    def gib_tipp(self, stimmung):
        tipps = {
            "😄 Fröhlich": "Teile deine gute Laune mit anderen!",
            "😴 Müde": "Gönn dir eine Pause oder ein Nickerchen.",
            "🤯 Gestresst": "Atme tief durch - du schaffst das!",
            "😎 Entspannt": "Genieße den Moment.",
            "🤩 Kreativ": "Nutze deine Energie für etwas Neues!"
        }
        return tipps.get(stimmung, "Bleib locker - du rockst das!")

    def energielevel(self, stimmung):
        energien = {
            "😄 Fröhlich": "🔋 Hoch",
            "😴 Müde": "🔋 Niedrig",
            "🤯 Gestresst": "🔋 Mittel",
            "😎 Entspannt": "🔋 Mittel",
            "🤩 Kreativ": "🔋 Hoch"
        }
        return energien.get(stimmung, "🔋 Mittel")
# ------

oracle3000 = StimmungsOrakel("Oracle3000")
print(f"Hello! You are using {oracle3000.name} - your personal mood oracle")
activity = input("What are you currently doing? ").strip().lower()
time = input("What time of the day is it? ").strip().lower()
mood = oracle3000.bestimme_stimmung(activity, time)
print("Your actual mood:", mood)
print("Tip of the day:", oracle3000.gib_tipp(mood))
print("Energy level:", oracle3000.energielevel(mood))