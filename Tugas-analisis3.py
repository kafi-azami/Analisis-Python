# Class Mage adalah anak dari class Hero
class Hero:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"{self.name} | HP: {self.hp} | Power: {self.attack_power}")

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")


# =========================
# CLASS MAGE (CHILD)
# =========================
class Mage(Hero):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal menggunakan Fireball! Mana tidak cukup.")


# =========================
# MAIN PROGRAM
# =========================
print("\n--- GAME DIMULAI ---")

eudora = Mage("Eudora", 80, 30, 100)
balmond = Hero("Balmond", 200, 10)

eudora.info()
balmond.info()

print("\n--- PERTARUNGAN ---")
eudora.serang(balmond)        # Serangan biasa (inherit dari Hero)
eudora.skill_fireball(balmond)
balmond.serang(eudora)

print("\n--- STATUS AKHIR ---")
eudora.info()
balmond.info()