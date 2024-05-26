from dog_class import Dog

class German_Shepherd(Dog):
    def __init__(self, name):
        super().__init__(name)
        self.hair_count = 50

    def shed_hair(self):
        self.hair_count -= 5

spike = German_Shepherd('Spike')
print(f"Is spike a dog: {isinstance(spike, Dog)}")
print(f"Is spike a German Shepherd: {isinstance(spike, German_Shepherd)}")
print(f"Is spike a dog and a German Shepherd: {isinstance(spike, Dog) and isinstance(spike, German_Shepherd)}")
print(f"Is a German Shepherd a dog: {issubclass(German_Shepherd, Dog)}")
print(f"Is a dog a German Shepherd: {issubclass(Dog, German_Shepherd)}")

print(f"Name: {spike.name}")
print(f"Kind: {spike.kind}")
print(f"Number of hairs: {spike.hair_count}")
print(f"Shedding hair...")
spike.shed_hair()
print(f"Number of hairs: {spike.hair_count}")
