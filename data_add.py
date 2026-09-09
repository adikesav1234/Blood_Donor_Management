import mysql.connector

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

donor_instance=BloodDonorManager()
donor_instance.post(name="Adi",blood_group="O+",phone="9497039336",city="Angamaly",last_donation="2026-04-21")
donor_instance.post(name="Aswin",blood_group="A+",phone="9465478997",city="Kochi",last_donation="2026-06-01")
donor_instance.post(name="Hari",blood_group="B+",phone="9454213445",city="Paravur",last_donation="2026-03-12")

