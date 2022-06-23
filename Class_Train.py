# Write a class Train which has methods to book a ticket, get status(no of seats), and get fare information of trains running under Indian Railways.

class train():
    def __init__(self, name, seats, fare):
        self.name=name
        self.seats=seats
        self.fare=fare

    def getStatus(self):
        print(f"The train name is {self.name}")
        print(f"The seat availability of the train are {self.seats} seats")

    def getFare(self):
        print(f"The train fare is {self.fare}")

    def bookTicket(self):
        if self.seats>0:
            print(f"Your seat is booked and your seat no. is {self.seats}")
            self.seats=self.seats-1 
        else:
            print("Seats are not avalilable ")

    def cancelTicket(self):
        print(f"The train which you have cancelled is {self.name}")
        self.seats=self.seats+1 
        print(f"The seat availability of the train are {self.seats} seats")


Rajdhani = train("Rajdhani Express", 300, 2500)
Rajdhani.getStatus()
Rajdhani.bookTicket()
Rajdhani.bookTicket()
Rajdhani.getStatus()
Rajdhani.cancelTicket()

print('******************************************')

Duranta = train("Duranta Express", 250, 2100)
Duranta.getStatus()
Duranta.bookTicket()
Duranta.bookTicket()
Duranta.getStatus()

