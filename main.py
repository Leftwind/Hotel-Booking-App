import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id": str})#Change ID to str so you can change it. Was Int. 
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")#It has to be a dictionary so we can compare it to the other dic in line 47
df_card_security = pd.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        pass

    #Change availability in csv file. 
    def book(self):
        """Books a hotel by changin its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index = False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()   
        if  availability == "yes":
            return True
        else:
            return False


class RevervationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thanks you for your reservation!
        Here are your booking data: 
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
"""
        return content
    
class Creditcard:
    def __init__(self, number):
        self.number = number
    
    def validate(self, expiration, holder, cvc):
        card_data={"number":self.number, "expiration":expiration, "holder":holder, "cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


#Child Class, takes all the information from the CreditCard class:
class SecureCreaditCard(Creditcard):
    def autenticate(self, given_password):
        #We get the self.number from the Parten Class, and ask for the password:
        password = df_card_security.loc[df_card_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False



#No user interface in the program, CLI all

#Main Loop
print(df)
hotel_ID = input("Enter id of the hotel: ")
hotel = Hotel(hotel_ID)
#Available = True process continues
if hotel.available():
    #We use the child class, so don't need to rewrite the class method. 
    credit_card = SecureCreaditCard(number="1234")
    #Check if data is in Database or API. 
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        #given_password = input("Input the password please: ")
        if credit_card.autenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name:" )
            reservation_ticket = RevervationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authetication failed.")    
    else:
        print("There was a problem with your payment")    
else:
    print("Hotel is not free")
