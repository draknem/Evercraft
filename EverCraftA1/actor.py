import strings, constants


class Actor:
    def __init__(self):
        self.__name = "UnsetName"
        self.__myalignment = "UnsetAlignment"
        self.__mycarma = -255
        self.__level = 1
        self.__exp = 0
        self.__basearmor = 10
        self.__basehp = 5
        self.__str = 10
        self.__dex = 10
        self.__vit = 10
        self.__wis = 10
        self.__int = 10
        self.__chr = 10
        self.__hp = self.__basehp+constants.modifiersw.get(self.__vit)
        self.__maxhp = self.__hp
        self.__myclass = constants.classesw.get(1)
        self.__myrace = constants.racesw.get(1)
        self.__myspecies = "None"

# sets
    def set_name(self, new_name):
        self.__name = new_name

    def set_alignment(self, new_alignment):
        self.__myalignment = strings.alignments[new_alignment]
        switcher = {
            0: constants.goodbound + 2,
            1: 0,
            2: constants.evilbound - 2,
        }
        self.__mycarma = switcher.get(new_alignment)

    def set_str(self, new_str):
        if 20 >= new_str >= 1:
            self.__str=new_str
        else:
            print("WTF 2strong4me")

    def set_dex(self, new_dex):
        if 20 >= new_dex >= 1:
            self.__dex=new_dex
        else:
            print("WTF check dex")

    def set_vit(self, new_vit):
        if 20 >= new_vit >= 1:
            self.__vit=new_vit
        else:
            print("WTF check vit")
        self.__hp = self.__basehp+constants.modifiersw.get(self.__vit)
        if self.__hp<1:
            self.__hp=1
        self.__maxhp = self.__hp

    def set_wis(self, new_wis):
        if 20 >= new_wis >= 1:
            self.__wis = new_wis
        else:
            print("WTF 2wise4me")

    def set_int(self, new_int):
        if 20 >= new_int >= 1:
            self.__int = new_int
        else:
            print("200 iq plays")

    def set_chr(self, new_chr):
        if 20 >= new_chr >= 1:
            self.__int = new_chr
        else:
            print("2sexy")

# gets
    def get_name(self):
        return self.__name

    def get_alignment(self):
        return self.__myalignment

    def get_carma(self):
        return self.__mycarma

    def get_level(self):
        return self.__level

    def get_exp(self):
        return self.__exp

    def get_str(self):
        return self.__str

    def get_dex(self):
        return self.__dex

    def get_vit(self):
        return self.__vit

    def get_wis(self):
        return self.__wis

    def get_int(self):
        return self.__int

    def get_chr(self):
        return self.__chr

    def get_hp(self):
        return self.__hp

    def get_maxhp(self):
        return self.__maxhp

    def get_armor(self):
        return self.__basearmor+constants.modifiersw.get(self.__dex)

    def get_class(self):
        return self.__myclass

# gives
    def give_carma(self, carma):
        self.__mycarma = self.__mycarma + carma

        if self.__mycarma >= constants.goodbound:
            self.__myalignment = strings.alignments[0]
        elif self.__mycarma <= constants.evilbound:
            self.__myalignment = strings.alignments[2]
        else:
            self.__myalignment = strings.alignments[1]

    def give_exp(self, exp):
        self.__exp = self.__exp + exp
        new_level = self.__exp // 1000 + 1
        if new_level>self.__level:
            self.__maxhp=self.__maxhp+(-self.get_level()+new_level)*(constants.leveluphpbonusw.get(self.get_class())+constants.modifiersw.get(self.get_vit()))
            self.__hp=self.__maxhp
            self.__level = new_level
            print(self.get_name()," has leveled up to level ", self.get_level(), ", maximum HP is now ", self.get_hp(), ", health is replenished.", sep="")



# actions
    def attack(self, roll, enemy):
        armor=enemy.get_armor()
        rollbonuslvlsw = {
            "Normal": (self.get_level()+1)%2,
            "Fighter": self.get_level(),
            "Rogue": (self.get_level()+1)%2,
            "Monk": (self.get_level()+2)%3,
            "Paladin": self.get_level()
        }
        roll = roll+constants.modifiersw.get(self.get_str())+rollbonuslvlsw.get(self.get_class())

        if roll >= armor:
            if roll >= 20:
                return 2
            else:
                return 1
        else:
            return 0

    def damage(self,attack,enemy):
        strmod = constants.modifiersw.get(enemy.get_str())
        if attack == 0:
            print(enemy.get_name(),"'s attack was stopped by ",self.get_name(),"'s armor", sep="")
        else:
            enemy.give_exp(10)
            print(enemy.get_name(),"'s hit lands!", sep="")
        dmg=attack*(1+strmod)
        if dmg<1 and attack>0:
            dmg=1
        self.__hp=self.__hp-dmg
        if self.get_hp() <= 0:
            print (self.get_name()," was slain by ", enemy.get_name(),"'s hand (", dmg," damage dealt)." , sep="")
            return dmg
        else:
            print(enemy.get_name(), "hit", self.get_name(), "for", dmg, "damage.")
            return dmg
