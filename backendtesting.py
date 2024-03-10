class SmartPlug:
    def __init__(self, initialConsumptionRate):
        self.switchedOn = False
        self.consumptionRate = initialConsumptionRate
        self.initialConsumptionRate = initialConsumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def turnOn(self):
        self.switchedOn = True

    def turnOff(self):
        self.switchedOn = False

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def getInitialConsumptionRate(self):
        return self.initialConsumptionRate

    def setConsumptionRate(self, rate):
        self.consumptionRate = rate

    def status(self):
        return f"SmartPlug: switchedOn = {self.switchedOn}, consumptionRate = {self.consumptionRate}, initialConsumptionRate = {self.initialConsumptionRate}"

    def __str__(self):
        return self.status()


class SmartFridge:
    def __init__(self):
        self.switchedOn = False
        self.defaultTemperature = 3
        self.temperature = None
        self.temperatureOptions = {1: "1 Degree Celsius", 3: "3 Degrees Celsius", 5: "5 Degrees Celsius"}

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def turnOn(self):
        self.switchedOn = True

    def turnOff(self):
        self.switchedOn = False

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
        return self.temperatureOptions[self.temperature]

    def status(self):
        return f"SmartFridge: switchedOn = {self.switchedOn}, Temperature Option = {self.temperature}, initialTemperature = {self.temperatureOptions.get(self.defaultTemperature, 'No Initial Temperature')}"

    def __str__(self):
        return self.status()


class SmartDoorbell:
    def __init__(self, sleepMode):
        self.switchedOn = False
        self.defaultState = False
        self.sleepSettings = {True: "On", False: "Off"}
        self.setOption(sleepMode)

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def turnOn(self):
        self.switchedOn = True

    def turnOff(self):
        self.switchedOn = False

    def getSwitchedOn(self):
        return self.switchedOn

    def getOptions(self):
        return self.sleepSettings

    def setOption(self, sleepMode):
        if sleepMode in self.sleepSettings.keys():
            self.sleepMode = sleepMode
        else:
            print("Invalid sleep mode")

    def getSelectedSleepMode(self):
        return self.sleepSettings[self.sleepMode]

    def status(self):
        return "Smart Doorbell -  On = {}, Sleep Mode = {}, Default State = {}".format(self.switchedOn, self.sleepMode, self.sleepSettings.get(self.defaultState, "No Initial State"))


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
        if isinstance(device, SmartPlug) or isinstance(device, SmartFridge) or isinstance(device, SmartDoorbell):
            self.devices.append(device)
        else:
            raise ValueError("Invalid device type")

    def toggleSwitch(self, index):
        if index < len(self.devices):
            self.devices[index].toggleSwitch()

    def turnOffAll(self):
        for device in self.devices:
            device.turnOff()

    def __str__(self):
        deviceInfo = "\n".join([str(device) for device in self.devices])
        return f"SmartHome Devices:\n{deviceInfo}"


def testSmartHome():

    smartHome = SmartHome()

    plug1 = SmartPlug(45)
    plug2 = SmartPlug(45)
    fridge = SmartFridge()
    doorbell = SmartDoorbell()

    plug1.toggleSwitch()
    plug1.setConsumptionRate(150)
    plug2.setConsumptionRate(25)
    fridge.setOption(5)
    doorbell.setSleepMode(True)

    smartHome.addDevice(fridge)
    smartHome.addDevice(plug1)
    smartHome.addDevice(plug2)
    smartHome.addDevice(doorbell)

    plug2.toggleSwitch()

    print(smartHome)

    fridge.toggleSwitch()
    print(smartHome)

    smartHome.removeDeviceAt(0)

    print(smartHome)

# testSmartHome()
