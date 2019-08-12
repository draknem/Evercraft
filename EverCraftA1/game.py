import actor, strings, constants, dice, time, keyboard

def rollme(actor):
    Hero.set_str(dice.roll())
    Hero.set_dex(dice.roll())
    Hero.set_vit(dice.roll())
    Hero.set_wis(dice.roll())
    Hero.set_int(dice.roll())
    Hero.set_chr(dice.roll())

# checks
def checkname(actor):
    print("Hero's name is", actor.get_name())

def checkalign(actor):
    print(actor.get_name(),"'s alignment is ", actor.get_alignment(), " with carma of ", actor.get_carma(), sep="")

def checknextlvl(actor):
    print(-actor.get_exp()+1000*actor.get_level(),"experience till next level.")

def checkstats(actor):
    print()
    checkname(actor)
    checkalign(actor)
    print("Strength =",actor.get_str(),"Intelligence =",actor.get_int())
    print("Vitality =",actor.get_vit(),"Dexterity =", actor.get_dex())
    print("Charisma =",actor.get_chr(),"Wisdom =",actor.get_wis())
    print("Current level is ", actor.get_level(), ", HP is ", actor.get_hp(),"/",actor.get_maxhp(), sep="")
    print("Current experience is ", actor.get_exp(),", ",end='', sep='')
    checknextlvl(Hero)
    print()


Hero = actor.Actor()
Hero.set_name(strings.defaultname)
Hero.set_alignment(0)
rollme(Hero)
checkstats(Hero)

while True:
  Hero.damage(Hero.attack(dice.rollprint(Hero),Hero),Hero)
  checkstats(Hero)
  if Hero.get_hp()<1:
      break
  keyboard.wait(" ")
  # time.sleep(5)