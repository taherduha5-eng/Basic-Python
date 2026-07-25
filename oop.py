# class member:
#     not_allowed_names = ["Hell","Shit","Baloot"]
#     def __init__(self,firstName,middleName,lastName,gender):
#         self.fName=firstName
#         self.mName=middleName
#         self.lName=lastName
#         self.gender=gender
        
        
#     def full_name(self):
#         if self.fName in member.not_allowed_names:
#             raise ValueError("name not allowed")
#         else:
#             return f"{self.fName}"
#         return f"{self.fName} {self.mName} {self.lName}"
#     def name_with_title(self):
#         if self.gender=="female":
        
#           return f" hello miss {self.fName}"
#         elif self.gender=="male":
#             return f" hello mr{self.fName}"
#         else:
#             return f"{self.fName}"
#     def get_all_info(self):
#         return f"{self.name_with_title()}, your Full Name Is: {self.full_name}"
# member_one=member("duha","taher","ebrhim","female")
# member_two=member("ahmed","taher","ebrhim","male")

# print(member_one.full_name())
# print(member_one.name_with_title())
# print(member_one.get_all_info())
#print(dir(member))
# print(member_one.get_all_info())


# class skill:
#     def __init__(self):
#         self.skill= ["html","css","js"]
# profile = skill()
# print(profile)
        # inheritance
        
# class food:  #base class
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} is created from base class")
#     def eat(self):
#         print("eat method from base class")
# class apple(food):  #derived class
#     def __init__(self,name,price):
#         # food.__init__(self, name)
#         super().__init__(name,price)
#         print(f"{self.name} is created from derived class and price is {self.price}")

# # food_one = food("pizza")
# food_two = apple("pizza",150)
# food_two.eat()


#multiple inheritance
# class Baseone:
#     def __init__(self):
#         print("Baseone")

# class Basetwo:
#     def __init__(self):
#         print("Basetwo")

# class Derived(Baseone,Basetwo):
#     pass

# my_var = Derived()


# class Base:
#     pass

# class Derivedone(Base):
#     pass
# class Derivedtwo(Derivedone):
#     pass

#  encapsulation
# class member:
#     def __init__(self,name):
#         self.name = name #public 
        
# one =member("dudu")
# print(one.name)

# one.name = "muhamed"
# print(one.name)
# class member:
#     def __init__(self,name):
#         self._namename = name #protected
        
# one =member("dudu")
# # print(one._name)

# one._name = "muhamed"
# print(one._name)

# class member:
#     def __init__(self,name):
#         self.__name = name #private
#     def say_hello(self):
#         return f"hello {self.__name}"  
# one =member("dudu")
# print(one.__name)

# one._name = "muhamed"
# print(one.__name)
# print(one.say_hello())
# getter and setter
# class member:
#     def __init__(self,name):
#         self.__name = name #private
#     def say_hello(self):
#         return f"hello {self.__name}"  
#     def get_name(self):
#         return self.__name
#     def set_name(self,new_name):
#         self.__name = new_name
        
# one =member("dudu")
# # print(one._member__name)
# print(one.get_name())
# one.set_name("Abbas")
# print(one.get_name())



# ABCs
class programming:
    def has_oop(self):
        return "yes"
    
class python(programming):
    def has_oop(self):
        return "yes"
    
    
class pascal(programming):
    def has_oop(self):
        return "No"

one = programming()
print(one.has_oop)