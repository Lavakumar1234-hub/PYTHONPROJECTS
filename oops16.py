class Vehicle:
    service_charge_rate=4
    def __init__(self,model,kilometers_run,year):
        self.model=model
        self.kilometers_run=kilometers_run
        self.service_history=[]
        self.year=year
    def calculating_service_charge(self):
        return self.kilometers_run*Vehicle.service_charge_rate
    def add_service_record(self,service):
        self.service_history.append(service)
    @classmethod
    def update_service_rate(cls,new_rate):
        cls.service_charge_rate=new_rate
    @staticmethod
    def check_service_eligibility(year):
        current_year=2026
        return (current_year-year)<=15
    def display(self):
        print("MODEL:",self.model)
        print("KILOMETERS RUN:",self.kilometers_run)
        print("SERVICE CHARGE:",self.calculating_service_charge())
        print("SERVICE HISTORY:",self.service_history)
        print("ELIGIBLE FOR SERVICE:",Vehicle.check_service_eligibility(self.year))
        print()
s1=Vehicle("MAHINDRA THAR",50000,2018)
s2=Vehicle("MERCEDES BENZ A-CLASS",70000,2020)
s3=Vehicle("BMW X5",40000,2015)
vehicles=[s1,s2,s3]
s1.add_service_record("ENGINE CHANGE")
s2.add_service_record("BREAK CHANGE")
s3.add_service_record("OIL CHANGE")
print("BEFORE UPDATING SERVICE RATE:")
print()
for vehicle in vehicles:
    vehicle.display()
Vehicle.update_service_rate(8)
print("AFTER UPDATING SERVICE CHARGE TO 8RS FOR KM:")
print()
for vehicle in vehicles:
    vehicle.display()


