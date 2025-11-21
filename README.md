# project - Financial Expense Manager
* An object-oriented desktop application built with Python to help users track, organize, and gain insights into their personal spending for effective financial planning.

# The Problem & Our Solution:-
* The Challenge : Most people struggle to accurately track where their money goes each month. Without clear visibility into spending patterns, budgeting relies on guesswork, which often leads to easy overspending.
* The Solution : We developed a simple desktop application that addresses this by -
  i) Recording every expense.
  ii) Organizing expenses by category (e.g., food, transportation, entertainment).
  iii) Providing a single view that shows exactly how much is being spent in each category.
  
# Technologies & Architecture :- 
* Programming Stack : The application is built using a robust and familiar stack -
*Component    *Technology    *Role

  Language      Python       Primary language, using an Object-Oriented Design
  Database      SQLite       Used for efficient local data storage
  Interface     Tkinter      Used to create the Graphical User Interface (GUI) for the desktop app

* System Architecture : The system is modular, ensuring maintainability and scalability -
  a) Input Module : Handles form-based entry of new expenses
  b) Storage Module :  Manages the SQLite database operations
  c) Report Module : Focuses on data analysis and visualization (charts, summaries)
  d) UI Module : Presents a user-friendly dashboard for interaction and viewing data

  The core process flow is: User enters expense → App validates data → Assigns category → Stores in database → Updates summary display → User views analytics.

# Key Features:-
  * Real-Time Tracking: Know exactly where each dollar goes instantly.
  * Category Organization: Expenses are automatically tagged and grouped for clarity.
  * Custom Categories: Allows users to create personalized categories for unique expenses that don't fit standard types.
  * Detailed Reports: Category-wise spending breakdown with monthly totals and insights.
  * Validation Checks: Added validation to prevent invalid inputs from crashing the app.
    
# Challenges Overcame:-
  * Database Synchronization:
    Issue: Data was not saving properly when the app closed.
    Solution: Implemented proper SQLite connection management and auto-commit functions.
  * Category Logic:
    Issue: Some expenses did not fit standard categories.
    Solution: Added a custom category feature, allowing users to create personalized categories.
  * Error Handling:
    Issue: Invalid inputs could crash the application.
    Solution: Added validation checks and implemented user-friendly error messages.
    
# Future Vision:- The following are planned next steps to enhance the application:
  * Complete Reports Module: Finish building visual charts and analytics dashboards for better expense insights.
  * Mobile Integration: Expand to a mobile platform with a smartphone app so users can log expenses on-the-go.
  * Cloud Sync: Enable backup and synchronization across multiple devices for seamless tracking anywhere.
  * Smart Recommendations: Add AI-powered suggestions to help users optimize spending and reach their budget goals.

# Team Members:-
  * Janamjay Gupta (Reg. No. 25BAI11262)
  * Sayan Manna (Reg. No. 25BAI10467)
  * Ganesh S (Reg. No. 25MEI10020)
  * Vidit Agarwal (Reg. No. 25BCY10049)
  * Rochan R K (Reg. No. 25BCE11177
    
