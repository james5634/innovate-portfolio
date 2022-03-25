from person import Person

liam = Person("Liam","30","6'7")

print(liam)

jordan = Person("Jordan","27","5'7")

print(f"Our innovate instructor is called {jordan.name}, he is {jordan.age} years old and is only {jordan.height}.")

liam.set_hair("brown and curly")
jordan.set_hair("blonde and straight")

print(f"Liam's hair is {liam.hair}.")
jordan.get_hair()