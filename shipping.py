import serialCreator

class ShippingContainer:
    serialnumber = 0
    def __init__(self,owner_code,contents):
        self.owner_code = owner_code
        self.contents = contents
        #self.container_Serial_Number = ShippingContainer.generate_serial()
        self.container_Serial_Number = ShippingContainer.generate_serial_class()
        #self.globalSerialNumber =  ShippingContainer.genSerialNumber(self.owner_code,self.container_Serial_Number)#serialCreator.createGolbalSerial(self.owner_code,self.container_Serial_Number,"U" )
        self.globalSerialNumber =  self.genSerialNumber(self.owner_code,self.container_Serial_Number)
    def display(self):
        print(self.contents)
    @staticmethod
    def generate_serial():
        ShippingContainer.serialnumber+=1
        return ShippingContainer.serialnumber
    @classmethod
    def generate_serial_class(cls):
        cls.serialnumber+=1
        return cls.serialnumber
    @classmethod
    def create_obj(cls, owner_code):
        return cls(owner_code,contents="")
    @property
    def serial_number(self):
        return (self.container_Serial_Number)
    @staticmethod
    def genSerialNumber(owner_code,container_Serial_Number):
        return serialCreator.createGolbalSerial(owner_code,container_Serial_Number,"U" )
    
class RefrigeratedShippingContainer(ShippingContainer):
    @staticmethod
    def genSerialNumber(owner_code,container_Serial_Number):
        return serialCreator.createGolbalSerial(owner_code, container_Serial_Number,"R" )

c1 = ShippingContainer("nithish", "books")
c2 = ShippingContainer("Dhivya", "Phone")

#print(c1.serial_number)
#print(c2.container_Serial_Number)
#print(f"last serial: {ShippingContainer.serialnumber}")
c3 = ShippingContainer.create_obj("rahul")
c4 = RefrigeratedShippingContainer("Ram","fish")
print(f"Global Serial Number Shippping: {c3.globalSerialNumber}")
print(f"Global Serial Number Refrigerated Shipping: {c4.globalSerialNumber}")

