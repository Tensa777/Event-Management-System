# 🎉 Event Management System

🧑‍💻 Author:
Name:Adarsh Kumar Singh
Uen:180

A web-based application built using **Streamlit** and **MySQL** that helps users register for events and allows admins to manage event details and participants.

---

## 📋 Features

### 👤 User Functionality
- Register for available events by providing personal details.
- View available event information.
- Automatic validation for email and mobile number.
- Prevents duplicate registration for the same event.
- Automatically checks and restricts registration beyond participant limit.

### 🔐 Admin Functionality
- Secure login for admins.
- View all events and number of participants.
- Add new events with details like fee, type, location, and date.
- Delete events.
- View registered participants for each event.

---

## 🛠️ Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Backend/Database**: [MySQL](https://www.mysql.com/)
- **Python Libraries**: 
  - `mysql-connector-python`
  - `streamlit`

---

## 📦 Setup Instructions

 1. Clone the Repository:

git clone https://github.com/yourusername/event-management-system.git
cd event-management-system

2. Install Dependencies

pip install streamlit mysql-connector-python

3. Setup MySQL Database:

Create a MySQL database named event_mgmt.

Use the following tables (ensure they exist):

events

event_type

location

participants

branch

admin

4. Run the App:

streamlit run your_script_name.py

📁 Project Structure:

event-management-system/
├── event_mgmt.py           # Main Streamlit app file
├── README.md               # This file
└── requirements.txt        # Optional: for pip install

🔐 Admin Credentials:

INSERT INTO admin (username, password) VALUES ('admin', 'admin123');


Demonstration:

**1.Login/Register page:**

![image](https://github.com/user-attachments/assets/510f0a1f-f338-4aff-b71c-8c4ba633eaa9)

📝 Quick Instructions to Register:
Open the app and select "Login/Register" from the sidebar.

Fill in the form:

First Name & Last Name

Mobile Number (10 digits) & Email (must end with .com)

Choose your Event and Branch

Click "Register" to submit.

You'll see a success message if registration is successful. Errors will be shown if inputs are invalid or duplicate.


**2.Admin Login Page**
![image](https://github.com/user-attachments/assets/28330210-6265-409e-8572-4d5907a5f8af)

Admin Login Instructions:
Go to the Admin Login page.

Enter your Username and Password.

Click the eye icon to toggle password visibility (optional).

Hit "Login" to access the admin dashboard.

**3.Event Management:**

![image](https://github.com/user-attachments/assets/eac19c30-ff9c-4495-b5e9-915af6dc9b31)


Event Management Instructions:

View Events:

See the list of current events with their ID, Title, and Participant count.

Add Event:

Fill in the Event Name, Fee, and Max Participants.

Choose Event Type and Location.

Select the Date.

Click "Add Event" to save.

Delete Event:

Enter the Event ID you want to remove.

Click "Delete Event" to delete it from the system.


**4.Event Info:**

![image](https://github.com/user-attachments/assets/2810277b-d894-47d6-be33-9a03744d1b1a)

Event Information Instructions:
This page displays a summary of all scheduled events, including:

Title

Price (Entry Fee)

Maximum Participants Allowed

Event Type (e.g., Technical, Cultural, Seminar)

Location

Date

Current Number of Participants Registered

Use this page to quickly review event details and monitor participant counts.

**5.Participants:**

![image](https://github.com/user-attachments/assets/2605c7f5-4d00-425e-9735-762b5882e0af)


Participants Page Instructions:
Select an event from the dropdown list.

View the list of registered participants for that event.

Each entry displays:

ID

Name

Mobile Number

Email Address

Use this page to track participant details for specific events.


 
