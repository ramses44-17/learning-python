class Restaurant:
    """une classe qui modelise un restaurant"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        return f"nom du restaurant: {self.restaurant_name}\n type de cuisine: {self.cuisine_type}"
    def set_number_served(self,num):
        if num >= self.number_served:
            self.number_served = num
        else:
            print("Impossible to down number served")
    def increment_number_served(self, num):
        self.number_served +=num


restaurant_1 = Restaurant(restaurant_name="Planète J",cuisine_type="congolese")
# print(restaurant_1.cuisine_type)
# print(restaurant_1.restaurant_name)
print(restaurant_1.describe_restaurant())

print(restaurant_1.number_served)

restaurant_1.set_number_served(17)
print(restaurant_1.number_served)

restaurant_1.number_served = 0
print(restaurant_1.number_served)

restaurant_1.increment_number_served(12)
print(restaurant_1.number_served)

# restaurant_2 = Restaurant(restaurant_name="Amos restau",cuisine_type="chinese")
# print(restaurant_2.describe_restaurant())
# restaurant_3 = Restaurant(restaurant_name="Dommin resto",cuisine_type="american")
# print(restaurant_3.describe_restaurant())
# restaurant_4 = Restaurant(restaurant_name="Loute resto",cuisine_type="congolese")
# print(restaurant_4.describe_restaurant())