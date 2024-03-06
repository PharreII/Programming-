import tkinter as tk
from backend import SmartPlug, SmartFridge, SmartHome
from tkinter import messagebox



def setUpHome():
    smartHome1 = SmartHome()

    for _ in range(5):
        deviceType = input("Enter the device type (SmartPlug or SmartFridge): ").lower()
        
        if deviceType == "smartplug":
            consumptionRate = float(input("Enter the consumption rate for the SmartPlug (e.g. 10W): "))
            device = SmartPlug(consumptionRate)
        elif deviceType == "smartfridge":
            setOption = int(input("Set the temperature for the SmartFridge (1, 3, or 5): "))
            device = SmartFridge(setOption)
            device.setOption(setOption)
        else:
            False

        smartHome1.addDevice(device)

    return smartHome1




class EditWindow(tk.Toplevel):
    def __init__(self, device):
        super().__init__()

        self.device = device

        self.title("Edit Device")
        self.geometry("400x200")

        self.device_name_label = tk.Label(self, text="Device Name:")
        self.device_name_label.pack()

        self.device_name_entry = tk.Entry(self)
        self.device_name_entry.insert(0, device.name)
        self.device_name_entry.pack()

        save_button = tk.Button(self, text="Save")
        save_button.pack()
        save_button.bind("<Button-1>", self.update_device)

    def update_device(self, event):
        self.device.name = self.device_name_entry.get()
        self.destroy()  



class SmartHomeSystem(tk.Tk):
    def __init__(self, smartHome):
        super().__init__()
        self.smartHome = smartHome
        self.devices = smartHome.get_devices()
        
        
        self.smartHome = smartHome
        self.title("Smart Home System")
        self.geometry("800x600")

        topFrame = tk.Frame(self)
        topFrame.pack()

        turnOnAllButton = tk.Button(topFrame, text="Turn on all")
        turnOnAllButton.pack(pady=10)
        turnOnAllButton.bind("<Button-1>", self.turnOnAllDevices)

        turnOffAllButton = tk.Button(topFrame, text="Turn off all")
        turnOffAllButton.pack(pady=10)
        turnOffAllButton.bind("<Button-1>", self.turnOffAllDevices)

        self.deviceNamesLabel = tk.Label(self, text="", padx=10, pady=10)
        self.deviceNamesLabel.pack()

        self.updateDeviceList

        
        
    def getDeviceTypeFromUser(self):
        deviceTypes = ["smartPlug", "smartFridge"]
        selectedDeviceType = messagebox.askquestion(
            "Select Device Type",
            "Please select the type of device you want to add:",
            options=deviceTypes
        )
        return selectedDeviceType
    
    def turnOnAllDevices(self, event):
        for device in self.smartHome.getDevices():
            device.turnOn()
        self.updateDeviceList()

    def turnOffAllDevices(self, event):
        for device in self.smartHome.getDevices():
            device.turnOff()
        self.updateDeviceList()

    def toggleDevice(self, device):
        if device.switchedOn:
            device.turnOff()
        else:
            device.turnOn()
        self.updateDeviceList()

    def editDevice(self, index):
        device = self.smartHome.getDevices[index]
        editWindow = EditWindow(device)
    
    def getConsumptionRateFromUser(self):
        consumption_rate = float(input("Enter the consumption rate for the SmartPlug (e.g. 10W): "))
        return consumption_rate

    def updateDeviceList(self):
        deviceNames = [device.getName() for device in self.devices]
        deviceNamesStr = "\n".join(deviceNames)
        self.deviceNamesLabel.config(text=deviceNamesStr)
        

if __name__ == "__main__":
 
    smartHome1 = setUpHome()

  
    mainWindow = SmartHomeSystem(smartHome1)

    mainWindow.mainloop()


        






