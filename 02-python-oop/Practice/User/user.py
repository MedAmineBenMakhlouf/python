class User:
    # all_users = []
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        # self.all_users.append(self)


    def display_info(self):
        print(f"First Name is {self.first_name}\nLast name {self.last_name}\nemail: {self.email}\nage {self.age}\nis member {self.is_rewards_member}\ngold {self.gold_card_points}\n")
    
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already member")
            return False
        else:
            return True

    
    def spend_points(self, amount):
        if self.gold_card_points>amount:
            self.gold_card_points-=amount
            return self
        else:
            print("Not enough points")
            return self

    # @classmethod
    # def display_all_info(cls):
    #     for user in cls.all_users:
    #         user.display_info()
    



Amine = User ("Amine","Ben Makhlouf","medamin@gmail.com",35)
Amine.display_info()
Amine.enroll()
Yassine = User ("Yassine","Ben Makhlouf","medyassineBm@gmail.com",5)
Sadok = User ("Sadok", "Ben Makhlouf","sadok.bm@gmail.com",2)
Amine.spend_points(50)
Yassine.enroll()
Yassine.spend_points(80)
# User.display_all_info()
Amine.enroll()
Sadok.spend_points(40)
# Amine.display_info()
Amine.spend_points(10)
Amine.display_info()
