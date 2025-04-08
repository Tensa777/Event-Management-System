import mysql.connector
import datetime
from mysql.connector import Error
import streamlit as st
from random import randint

# Database connection function (same as before)
def runQuery(query):
    try:
        db = mysql.connector.connect(
            host='localhost',
            database='event_mgmt',
            user='root',
            password=''
        )
        if db.is_connected():
            print("Connected to MySQL, running query: ", query)
            cursor = db.cursor(buffered=True)
            cursor.execute(query)
            db.commit()
            try:
                res = cursor.fetchall()
                return res
            except Exception as e:
                print("Query returned nothing, ", e)
                return []
    except Exception as e:
        print(e)
        return []
    finally:
        if 'db' in locals():
            db.close()
    print("Couldn't connect to MySQL")
    return None

# Main app
def main():
    st.title("Event Management System")
    
    # Sidebar menu
    menu = ["Login/Register", "Admin Login", "Event Management", "Event Info", "Participants"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login/Register":
        st.subheader("Register for an Event")
        
        # Fetch events and branches
        events = runQuery("SELECT * FROM events")
        branches = runQuery("SELECT * FROM branch")
        
        with st.form("registration_form"):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name")
                mobile = st.text_input("Mobile Number")
                event = st.selectbox("Event", [e[1] for e in events] if events else ["No events"])
            with col2:
                last_name = st.text_input("Last Name")
                email = st.text_input("Email")
                branch = st.selectbox("Branch", [b[1] for b in branches] if branches else ["No branches"])
            
            submitted = st.form_submit_button("Register")
            
            if submitted:
                name = f"{first_name} {last_name}"
                event_id = [e[0] for e in events if e[1] == event][0] if events else None
                branch_id = [b[0] for b in branches if b[1] == branch][0] if branches else None
                
                # Check if required data is available
                if not event_id or not branch_id:
                    st.error("Event or Branch information not available!")
                    return
                
                # Validation with error handling
                if len(mobile) != 10:
                    st.error("Invalid Mobile Number!")
                elif email[-4:] != '.com':
                    st.error("Invalid Email!")
                else:
                    # Check if participant already registered
                    existing_participants = runQuery(f"SELECT * FROM participants WHERE event_id={event_id} AND mobile='{mobile}'")
                    if existing_participants and len(existing_participants) > 0:
                        st.error("Student already Registered for the Event!")
                    else:
                        # Check participant limit
                        current_count_query = runQuery(f"SELECT COUNT(*) FROM participants WHERE event_id={event_id}")
                        max_participants_query = runQuery(f"SELECT participants FROM events WHERE event_id={event_id}")
                        
                        # Verify we got results from both queries
                        if not current_count_query or not max_participants_query:
                            st.error("Error retrieving event information!")
                            return
                            
                        current_count = current_count_query[0][0] if current_count_query else 0
                        max_participants = max_participants_query[0][0] if max_participants_query else 0
                        
                        if current_count >= max_participants:
                            st.error("Participants count fulfilled Already!")
                        else:
                            # All validations passed, proceed with registration
                            runQuery(f"INSERT INTO participants(event_id,fullname,email,mobile,college,branch_id) VALUES({event_id},'{name}','{email}','{mobile}','COEP',{branch_id})")
                            st.success("Successfully Registered!")

    elif choice == "Admin Login":
        st.subheader("Admin Login")
        with st.form("admin_login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Login")
            
            if submitted:
                cred = runQuery("SELECT * FROM admin")
                if cred and any(username == user[0] and password == user[1] for user in cred):
                    st.session_state['admin_logged_in'] = True
                    st.success("Logged in successfully!")
                else:
                    st.error("Wrong Username/Password")

    elif choice == "Event Management":
        if 'admin_logged_in' not in st.session_state or not st.session_state['admin_logged_in']:
            st.warning("Please login as admin first!")
            return
            
        st.subheader("Event Management")
        
        # Display existing events
        events = runQuery("SELECT event_id, event_title, (SELECT COUNT(*) FROM participants AS P WHERE P.event_id = E.event_id) AS count FROM events AS E")
        if events:
            st.write("Current Events:")
            for event in events:
                st.write(f"ID: {event[0]}, Title: {event[1]}, Participants: {event[2]}")
        
        # Add new event
        with st.form("new_event"):
            name = st.text_input("Event Name")
            fee = st.number_input("Fee", min_value=0)
            max_p = st.number_input("Max Participants", min_value=1)
            types = runQuery("SELECT * FROM event_type")
            type_id = st.selectbox("Event Type", [t[1] for t in types] if types else ["No types"])
            locations = runQuery("SELECT * FROM location")
            location_id = st.selectbox("Location", [l[1] for l in locations] if locations else ["No locations"])
            date = st.date_input("Date")
            submitted = st.form_submit_button("Add Event")
            
            if submitted:
                type_id = [t[0] for t in types if t[1] == type_id][0] if types else None
                location_id = [l[0] for l in locations if l[1] == location_id][0] if locations else None
                if type_id and location_id:
                    runQuery(f"INSERT INTO events(event_title,event_price,participants,type_id,location_id,date) VALUES('{name}',{fee},{max_p},{type_id},{location_id},'{date}')")
                    st.success("Event added successfully!")
                else:
                    st.error("Invalid event type or location!")

        # Delete event
        with st.form("delete_event"):
            event_id = st.number_input("Event ID to Delete", min_value=1)
            submitted = st.form_submit_button("Delete Event")
            if submitted:
                runQuery(f"DELETE FROM events WHERE event_id={event_id}")
                st.success("Event deleted successfully!")

    elif choice == "Event Info":
        st.subheader("Event Information")
        events = runQuery("SELECT *,(SELECT COUNT(*) FROM participants AS P WHERE P.event_id = E.event_id) AS count FROM events AS E LEFT JOIN event_type USING(type_id) LEFT JOIN location USING(location_id)")
        if events:
            for event in events:
                st.write(f"Title: {event[1]}, Price: {event[2]}, Max Participants: {event[3]}, Type: {event[7]}, Location: {event[9]}, Date: {event[5]}, Current Participants: {event[10]}")

    elif choice == "Participants":
        st.subheader("Participants")
        events = runQuery("SELECT * FROM events")
        event = st.selectbox("Select Event", [e[1] for e in events] if events else ["No events"])
        
        if event:
            event_id = [e[0] for e in events if e[1] == event][0] if events else None
            if event_id:
                participants = runQuery(f"SELECT p_id,fullname,mobile,email FROM participants WHERE event_id={event_id}")
                if participants:
                    for p in participants:
                        st.write(f"ID: {p[0]}, Name: {p[1]}, Mobile: {p[2]}, Email: {p[3]}")
                else:
                    st.write("No participants yet")
            else:
                st.error("Invalid event selected!")

if __name__ == "__main__":
    main()