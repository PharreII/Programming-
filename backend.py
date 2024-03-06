class SmartPlug:
    
    def __init__(self, initialConsumptionRate):
        self.switchedOn = False
        self.consumptionRate = initialConsumptionRate
        self.initialConsumptionRate = initialConsumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def getInitialConsumptionRate(self):
        return self.initialConsumptionRate

    def setConsumptionRate(self, rate):
        self.consumptionRate = rate

    def __str__(self):
        return "SmartPlug: switchedOn = {}, consumptionRate = {}, initialConsumptionRate = {}".format(self.switchedOn, self.consumptionRate, self.initialConsumptionRate)

    

def testSmartPlug():

    testPlug = SmartPlug(45)

    testPlug.toggleSwitch()

    print("Plug switchedOn: ", testPlug.getSwitchedOn())

    print("Consumption rate: ", testPlug.getConsumptionRate())

    testPlug.setConsumptionRate(30)

    print("New consumption rate: ", testPlug.getConsumptionRate())
        
    print("SmartPlug object: ", testPlug)

#testSmartPlug()




class SmartFridge:
    
    def __init__(self):
        self.switchedOn = False
        self.defaultTemperature = 3
        self.temperature = None
        self.temperatureOptions = {1: "1 Degree Celsius", 3: "3 Degrees Celsius", 5: "5 Degrees Celsius"}

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn
    
    def getOptions(self):
        return self.temperatureOptions

    def setOption(self, temperature):
        if temperature in self.temperatureOptions.keys():
            self.temperature = temperature
        else:
            print("Invalid temperature option")

    
    def getSelectedTemperature(self):
        return self.temperatureOptions [self.temperature]


    def __str__(self):
        return "SmartFridge: switchedOn = {}, Temperature Option = {}, initialTemperature = {}".format(self.switchedOn, self.temperature, self.temperatureOptions.get(self.defaultTemperature, "No Initial Temperature"))




def testSmartFridge():

    testFridge = SmartFridge()

    testFridge.toggleSwitch()

    testFridge.setOption(1)


    print("SmartFridge switched on: ", testFridge.getSwitchedOn())

    temperatureOptions = testFridge.getOptions()


    print("Temperature options: ", temperatureOptions)

    print("Default Temperature: ", testFridge.defaultTemperature())

    print("Selected Fridge temperature: ", testFridge.getSelectedTemperature())

    

#testSmartFridge()
    




class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices[:]

    def getDeviceAt(self, index):
        if index < len(self.devices):
            return self.devices[index]
        else:
            return None
    def removeDeviceAt(self, index):
        if index < len(self.devices):
            del self.devices[index]

    def addDevice(self, device):
        if (isinstance(device, SmartPlug) or
        isinstance(device, SmartFridge)):
            self.devices.append(device)
        else:
            raise ValueError("Invalid device type")

    def xtoggleSwitch(self, index):
        if index < len(self.devices):
            self.devices[index].toggleSwitch()
        else: None

    def turnOffAll(self):
        for device in self.devices:
            device.setSwitchedOn(False)

    def __str__(self):
        device_info = "\n".join([str(device) for device in self.devices])
        return f"SmartHome Devices:\n{device_info}"




def testSmarthome():

    smartHome = SmartHome()

    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    fridge = SmartFridge()


    plug1.toggleSwitch()
    plug1.setConsumptionRate(150)
    plug2.setConsumptionRate(25)
    fridge.setOption(5)

    smartHome.addDevice(fridge)
    smartHome.addDevice(plug1)
    smartHome.addDevice(plug2)

    plug2.toggleSwitch()

    print(smartHome)

    fridge.toggleSwitch()
    print(smartHome)

    smartHome.removeDeviceAt(0)

    print(smartHome)

#testSmarthome()


  



 


        


























    






    



