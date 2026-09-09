import mysql.connector
from mysql.connector import cursor
from MySQL_Connection.student_CRUD import query, values


class BloodDonorManager:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            user="root",
            password="Achulachu@123",
            database="blood_db"
        )
        print("Connected Successfully")

    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query=("insert into donor (name,blood_group,phone,city,last_donation)values (%s,%s,%s,%s,%s)")
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor added successfully")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            #print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select*from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            if record==None:
                print("Donor is found...!")
            print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            if records!=None:
                query="delete from donor where id =%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor deleted Successfully...!")
            else:
                print("Donor not found...!")
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)                     #check whether the record exists
            if record!=None:                                  #if record is found ,record will not be None
                self.cursor=self.connection.cursor()
                placeholder=""                                #creates an empty string
                #This variable will be used to construct the SET part of the SQL Query
                for k in kwargs:
                    placeholder += k + "=%s, "
                    placeholder = placeholder.rstrip(" , ")
                    #Removes the last comma
                    query=f"update donor set{placeholder} where id = %s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("Donor details updated successfully...!")
            else:
                print("Donor not found...!")
        except Exception as e:
            print(e)

                

donor_instance=BloodDonorManager()
# donor_instance.post(name="Adith",blood_group="O+",phone="9876543210",city="Kakkanad",last_donation="2026-08-20")
# donor_instance.get()
#donor_instance.retrieve(id=1)
# donor_instance.delete(id=1)
#print("After deleting a donor...")
# donor_instance.get()