class Hall:
    def __init__(self, rows, cols, hall_no):
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no 
        
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.seats[(row, col)] = 0
    
    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)    
        self.show_list.append(show_info)
        available_seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[str(show_id)] = available_seats
              
    def book_seats(self, show_id, seats):
        found = False
        for show in self.show_list:
            if int(show[0]) == show_id:
                found = True
                for seat in seats:
                    if len(seat) == 2:
                        row, col = map(int, seat)
                        if 1 <= row <= self.rows and 1 <= col <= self.cols:
                            if self.seats[str(show_id)][row - 1][col - 1] == 1:
                                print(f"This seat ({row}, {col}) is already booked.")
                            elif self.seats[str(show_id)][row - 1][col - 1] == 0:
                                self.seats[str(show_id)][row - 1][col - 1] = 1
                                print(f"Seat ({row}, {col}) booked successfully for the Show ID {show_id}.")
                        else:
                            print(f"Invalid Seat ({row}, {col})")
                    else:
                        print(f"Invalid seat format: {seat}.")
                return
        if not found:
            print(f"We can't find a show with ID {show_id}!")      
     
    def view_show_list(self, hall_no):        
        if self.hall_no == hall_no:
            print(f"Running Shows of Hall {hall_no}")
            for show in self.show_list:
                show_id, movie_name, time = show
                print(f"Show ID: {show_id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        found = False
        for show in self.show_list:
            if int(show[0]) == show_id:
                found = True
                print(f"Available seats for Show ID {show_id}:")
                for row in range(1, self.rows + 1):
                    for col in range(1, self.cols + 1):
                        if self.seats[str(show_id)][row - 1][col - 1] == 0:
                            print(f"({row}, {col})")
                for row in range(1, self.rows + 1):
                    for col in range(1, self.cols + 1):
                        if self.seats[str(show_id)][row - 1][col - 1] == 0:
                            print("0", end=" ")
                        else:
                            print("1", end=" ")
                    print()
                return
        if not found and int(show[0]) != show_id:
            print(f"We can't find a show with ID {show_id}!")                        

class Star_Cinema:
    hall_list = []
    
    @classmethod
    def entry_hall(cls, hall_obj):
        cls.hall_list.append(hall_obj)
        
# Adding initial data
hall1 = Hall(rows=10, cols=10, hall_no=1)
hall1.entry_show("101", "Movie 1", "12:00 PM, 4 Oct 2024")
hall1.entry_show("102", "Movie 2", "3:00 PM, 4 Oct 2024")
hall1.entry_show("103", "Movie 3", "6:00 PM, 4 Oct 2024")

hall2 = Hall(rows=10, cols=10, hall_no=2)
hall2.entry_show("201", "Movie 4", "6:00 PM, 4 Oct 2024")
hall2.entry_show("202", "Movie 5", "9:00 PM, 4 Oct 2024")

Star_Cinema.entry_hall(hall1)
Star_Cinema.entry_hall(hall2)
           
        
options = ["1. VIEW ALL SHOWS", "2. VIEW AVAILABLE SEATS", "3. BOOK A TICKET",  "4. EXIT"]   
for option in options:
    print(option)
op = int(input("Enter Option: "))

if op == 1:
    hall_no = int(input("Enter Hall No: "))
    for hall in Star_Cinema.hall_list:
        hall.view_show_list(hall_no)

elif op == 2:
    show_id = int(input("Enter the Show ID: "))
    for hall in Star_Cinema.hall_list:
        hall.view_available_seats(show_id)

elif op == 3:
    show_id = int(input("Enter the Show ID: "))
    tickets = int(input("Number of Tickets: "))
    seats = []
    for _ in range(tickets):
        seat = tuple(map(int, input("Enter Seat (row, col): ").split()))
        seats.append(seat)
    
    for hall in Star_Cinema.hall_list:
        hall.book_seats(show_id, seats)

elif op == 4:
    print("Exiting the program.")

else:
    print("Invalid Input")