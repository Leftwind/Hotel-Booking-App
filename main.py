import pandas as pd


df = pd.read_csv("hotels.csv", dtype={"id": str})#Change ID to str so you can change it. Was Int. 


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
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
    def __init__(self, customer_name, hotel_name):
        pass

    def generate(self):
        content = f"Name of the customer hotel"
        return content
    

#No user interface in the program, CLI all

#Main Loop
print(df)
hotel_ID = input("Enter id of the hotel: ")
hotel = Hotel(hotel_ID)
#Available = True process continues
if hotel.available():
    hotel.book()
    name = input("Enter your name:" )
    reservation_ticket = RevervationTicket(customer_name, hotel_name)
    print(reservation_ticket.generate())
