from character import Character

batman = Character("Bruce Wayne", "Batman")
superman = Character("Clark Kent", "Superman")

print(batman.real_name)

superman.set_superhero_power("all")
batman.set_superhero_power("rich")
batman.get_superhero_power()

batman.set_mothers_name("Martha")
superman.set_mothers_name("Martha")

if batman.mothers_name == superman.mothers_name:
    print("How do you know that name!? *hugs it out*")
else:
    print("Do you bleed?")