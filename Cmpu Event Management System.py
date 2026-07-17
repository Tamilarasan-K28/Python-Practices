class Students():
    def __init__(self,s_id,s_name, phone_no, willing_to_volunteer):
        self.s_id = s_id
        self.s_name = s_name
        self.phone_no = phone_no
        self.willing_to_volunteer = willing_to_volunteer
        self.attend_events = "Yes"
        self.student = {}
        self.volunteer = {}
    def add_student(self):
        if self.willing_to_volunteer == 'No':
            self.attend_events = "Yes"
            print("Student Added Successfully.")
        else:
            print("You are a Volunteer.")
    def add_volunteer(self):
        if self.willing_to_volunteer == 'Yes':
            self.volunteer = Students(self.s_id, self.s_name,self.phone_no, self.willing_to_volunteer)
            self.attend_events = "No"
            print("Registered for Volunteer Successfully.")
        else:
            print("You are not registered for Volunteer.")
    def display_student(self):
        print(f"Student Id : {self.s_id} | ")
    def attend_event(self):
        if self.attend_events == 'Yes':
            print(f"Student {self.s_name} is going to attend the event.")
        else:
            print("You are a Volunteer.")

class Events():
    def __init__(self, e_id,e_name, start_time, end_time):
        self.e_id = e_id
        self.e_name = e_name
        self.start_time = start_time
        self.end_time = end_time

class Volunteer():
    def __init__(self,v_role):
        self.v_id = 1
        self.e_id = 1
        self.v_role = v_role
        self.v_status = "Available"
    
    def volunteer_event(self,e_id, end_time):
        if self.v_status == "Available" :
            print("Ready to Volunteer for Event.") 
        else:
            print("You are not Available.")

        


class main():
    student1 = Students(1,"Tamil","856123478","Yes")
    student1.add_volunteer()
    student1 = Volunteer("Technical Support")
    student1.volunteer_event(1,10)
    

       

