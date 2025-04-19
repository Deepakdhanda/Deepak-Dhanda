    📄 Overview
This project is a simple console-based application for managing a gaming zone where users can:

Add players

Add games

Book a game for a player

View all bookings

The system uses object-oriented programming concepts and adheres to key software design principles such as abstraction, encapsulation, and modularity.

🛠 File Structure
bash
Copy
Edit
├── player.py             # Defines the Player class
├── game.py               # Defines the Game class
├── booking.py            # Defines the Booking class
├── booking_manager.py    # Manages bookings
└── main.py               # User interface (menu-based CLI)
✅ Software Design Principles Applied
1. Encapsulation
Each class encapsulates its own data and methods:

Player holds player details.

Game stores game details.

Booking includes both player, game, and booking timestamp.

BookingManager handles a list of bookings and operations on them.

2. Abstraction
The BookingManager class hides the logic of how bookings are added and stored.

Users of this class only interact with public methods like add_booking() and get_all_bookings().

3. Modularity
The code is divided into multiple files by responsibility (player.py, game.py, etc.), making it easier to maintain and scale.

Changes in one module won’t affect others as long as the interfaces remain consistent.

4. Reusability
Classes like Player and Game can be reused in other systems that need player or game data management.

🐞 Known Issues
All __init__ and __str__ methods are incorrectly written as _init_ and _str_.
➤ They should be corrected to __init__ and __str__ with double underscores on both sides.

The main function check in main.py is written as _name_ == '_main_'
➤ This should be __name__ == '__main__'.

🚀 How to Run
Make sure you have Python installed.

Correct the issues mentioned in the "Known Issues" section.

Run the main.py file:

bash
Copy
Edit
python main.py
💡 Future Enhancements
Add persistence (e.g., store data in files or a database)

Add exception handling for invalid inputs

Support game cancellation and editing

Implement a GUI using frameworks like Tkinter or PyQt

🙌 Author's Note
This project was built as a learning tool to understand the principles of object-oriented design and modular programming in Python. Each module was intentionally separated to highlight clear responsibilities, making the system clean and easy to extend.
