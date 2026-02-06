class hero :
    def __init__(self, name, hp, attack_power, ):
     self.name = name # Nama Hero
     self.hp = hp # Nyawa (Health Point)
     self.attack_power = attack_power # Kekuatan Serangan
    def serang(self, lawan):
     print(f"{self.name} menyerang {lawan.name}!")
     lawan.diserang(self.attack_power)
 # Method diserang: Menerima damage
    def diserang(self, damage):
     self.hp -= damage
     print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

# Membuat Object (Instansiasi)
hero1= hero("Layla", 100, 15,)
hero2 = hero("Zilong", 120, 20,)
 # Tambah kode Output di akhir program
print("\n--- Pertarungan Dimulai ---")
hero1.serang(hero2) # Layla menyerang Zilong
hero2.serang(hero1) # Zilong membalas