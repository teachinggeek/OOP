class Dog():

  #Class Object Attribute
  #Same for any instance of a class

  species='mammal'

  def __init__(self,breed,name,spots):
    #attributes
    #we take in the argument
    #Assign it using self.attribute_name
    self.breed=breed
    self.name = name

    #boolean attribute
    self.spots = spots

  #Methods are actions or operations
  def bark(self):
    print('Woof! My name is {}'.format(self.name))




