# IT5016
Contains all of the course work for IT5016: Software Development Fundamentals. 

It includes Lab Work, Exam Submissions, Revision Exercises and Research Code.

Below is a summary of the Research Code: The AT Hop Card Personal Checker Program 

The AT Hop Card Personal Checker Program is a simple solution for managing a AT Hop Card used for public transport in Auckland. 

As someone who regularly travels by bus, I was inspired by my daily commutes to create a tool that helps users like myself, manage their hop card balance and track their transport usage. It allows users to track their balance, deposit funds, and manage commutes in a user-friendly manner. 

While the current implementation is simple, it lays the groundwork for future improvements and additional features that can enhance user interaction. For example, introducing variable fares based on different routes.

Features:
- User identification: Prompts users for their name to personalise interactions.
- Balance management: Users can check their current balance, deposit funds, and withdraw money for commutes.
- Commute functionality: Provides methods to simulate commuting to and from the university, including fare deduction.
- Error handling: Manages insufficient funds and invalid inputs, enhancing user experience.
- Object-oriented design: Uses classes to encapsulate functionality and promote code reuse and maintainability.

Usage: 
1. Run the program. 
2. Input your name when prompted for personalised interaction. 
3. Input an initial balance if needed. 
4. Use the menu options to manage your hop card and perform transactions.

SDLC principles that guided the design and development of the code:

Keep it Simple, Stupid: The program focused on core functionalities—checking balance, depositing funds, and managing commutes—without unnecessary complexities. Each function is straightforward, making it easy for users to understand and navigate the interface. It serves the purpose for which it was designed for.

Don’t Repeat Yourself: Redundancies were avoided by encapsulating common functionalities like balance management and transaction replies within the methods in the HopCard class. This ensured that all Hop Card-related operations are handled in a single place.

Open/Closed Principle: With a view to enhance the code in future, code is designed to allow modifications without affecting the existing code. New Fares and Locations can be added by extending the HopCard or UniversityCommute classes, adhering to the open/closed principle.

Composition > Inheritance: While inheritance is used in the code (e.g., UniversityCommute inheriting from HopCard), the program can also be extended using composition. For example, if new types of transportation cards are introduced, they can be created as new classes that use the existing HopCard class without needing deep inheritance chains.

Single Responsibility: Each class and method has a specific purpose. The HopCard class handles card-related functionalities, while UniversityCommute focuses on commuting logic. This separation makes the code easier to maintain and understand.

Separation of Concerns: The user interface is separated from the logic part of the Program. The personal_checker function handles user interactions, while the classes manage the data and operations. This distinction allows for easier updates to either the UI or the backend without affecting the other.

YAGNI (You Aren’t Gonna Need It): While it may be useless code for someone not commuting from West Auckland, it’s designed to be a functional prototype for now. There are no unnecessary methods or classes that could complicate the codebase. . The current implementations focuses on essential features only. Future features can be added as needed, rather than preemptively building for every possible requirement

Avoid Premature Optimisation: The straight-forward design of the code focuses mainly on functionality and to provide a foundation for future enhancements. It was tempting to optimise straight away but it was important to focus on functionality first.

Refactor, Refactor, Refactor:  As I developed this code, I focused on refactoring to enhance readability and maintainability. For example, methods were named clearly to indicate their functions, and comments were added to describe each part of the code.

Clean Code > Clever Code: The program avoids overly complex logic.  Instead, it prioritises clean, understandable code. Each method and class is documented, making it easier for anyone reviewing or maintaining the code in the future.

Author: Akaash Deo
