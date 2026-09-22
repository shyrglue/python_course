class Pokemon:
    def __init__(self, name, mhp, atk):
        self.name=name
        self.mhp=mhp
        self.atk=atk
        self.hp=mhp
        self.natk=atk
    def get_hp(self):
        return self.hp
    def get_atk(self):
        return self.natk
    def get_name(self):
        return self.name
    def damage(self, who, damage):
        print(self.name, 'received', damage, 'damage from', who.get_name())
        self.hp-=damage
    def move(self, skill, target, ctx):
        pass

class Squirtle(Pokemon):
    def __init__(self, name, mhp, atk):
        Pokemon.__init__(self, name, mhp, atk)
        self.name = 'S('+str(name)+')'
    def move(self, skill, target, ctx):
        if skill==0:
            heal=self.mhp//5
            self.hp=min(self.hp+heal, self.mhp)
            print(self.name,'used Regen')
        else:
            damage=self.natk
            print(self.name,'used Splash to',target.get_name())
            target.damage(self, damage)
    def damage(self, source, damage):
        if self.hp<=self.mhp//5 and damage>=2:
            damage=damage//2
        Pokemon.damage(self, source, damage)

class Charizard(Pokemon):
    def __init__(self, name, mhp, atk):
        Pokemon.__init__(self, name, mhp, atk)
        self.name='C('+str(name)+')'
        self.ignite=1
    def move(self, skill, target, ctx):
        if skill==0:
            self.ignite+=1
            self.natk*=2
            print(self.name,"used Ignite")
            self.damage(self, 10*self.ignite)
        else:
            damage=self.natk
            print(self.name,'used Flame to',target.get_name())
            target.damage(self, damage)

    def damage(self, source, damage):
        odamage=damage
        Pokemon.damage(self, source, damage)
        if source!=self and odamage>=10 and self.hp>0:
            source.damage(self, odamage//5)



type0, hp0, atk0 = map(int, input().split())
type1, hp1, atk1 = map(int, input().split())
rounds = int(input())
            
if type0 == 1:
    pokemon0 = Squirtle(0, hp0, atk0)
else:
    pokemon0 = Charizard(0, hp0, atk0)
if type1 == 1:
    pokemon1 = Squirtle(1, hp1, atk1)
else:
    pokemon1 = Charizard(1, hp1, atk1)
            
for _ in range(rounds):
    if pokemon0.get_hp() <= 0 or pokemon1.get_hp() <= 0:
        break
                
    skill0, target0 = map(int, input().split())
    if skill0 == 0:
        pokemon0.move(skill0, pokemon0, None)
    else:
        target = pokemon0 if target0 == 0 else pokemon1
        pokemon0.move(skill0, target, None)
                
    if pokemon0.get_hp() <= 0 or pokemon1.get_hp() <= 0:
        break
                
    skill1, target1 = map(int, input().split())
    if skill1 == 0:
        pokemon1.move(skill1, pokemon1, None)
    else:
        target = pokemon0 if target1 == 0 else pokemon1
        pokemon1.move(skill1, target, None)
            
print("-----game over-----")
print(pokemon0.get_name(),pokemon0.get_hp(),pokemon0.get_atk())
print(pokemon1.get_name(),pokemon1.get_hp(),pokemon1.get_atk())
