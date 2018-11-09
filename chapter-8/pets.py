# def describe_pet(animal_type, pet_name):
#     print("\n I have a " + animal_type + ".")
#     print("My " +animal_type + "'s name is " + pet_name.title() + ".")
#
# # describe_pet('hamster', 'harry')
# # describe_pet('dog', 'willie')
#
# describe_pet('harry', 'hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet(pet_name='willie')
describe_pet('willie')

