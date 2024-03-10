import tkinter as tk
from backendtesting import SmartPlug, SmartFridge, SmartDoorbell, SmartHome
from tkinter import messagebox


def setUpHome():
    smartHome1 = SmartHome()
    smartHome1.addDevice(SmartPlug(1))
    smartHome1.addDevice(SmartDoorbell(False))
    smartHome1.addDevice(SmartPlug(3))
    smartHome1.addDevice(SmartPlug(4))
    smartHome1.addDevice(SmartPlug(15))
    return smartHome1




class EditDeviceWindow(tk.Toplevel):
    def __init__(self, device):
        super().__init__()

        self.device = device
        self.UpdateGUI(device)

    def UpdateGUI(self,device):

        self.destroy
        # if no device, create one        
        if device is None:
            device = SmartPlug(0)
            deviceList = tk.Listbox(self)
            deviceList.bind("<<ListboxSelect>>", self.setDevice)
            deviceList.insert(1,"Smart Plug")
            deviceList.insert(2,"Smart Doorbell")
            deviceList.pack()

        self.title("Edit Device")
 
        self.deviceNameLabel = tk.Label(self, text="Device Name:")
        self.deviceNameLabel.pack()

        self.deviceNameEntry = tk.Entry(self, width=20)
        self.deviceNameEntry.insert(0, device.getName())  
        self.deviceNameEntry.pack()
        
        if isinstance(device, SmartPlug):
            lbl = tk.Label(self, text="Consumption Rate:")
            lbl.pack(side="left")

            self.consumptionRateEntry = tk.Entry(self, width=20)
            self.consumptionRateEntry.insert(0, str(device.consumptionRate))
            self.consumptionRateEntry.pack(side="left")

        elif isinstance(device, SmartDoorbell):
            lbl = tk.Label(self, text="Sleep Mode")
            lbl.pack(side="left")

            self.sleepModeEntry = tk.Entry(self, width=20)
            self.sleepModeEntry.insert(0, str(device.getSelectedSleepMode()))  
            self.sleepModeEntry.pack(side="left")

        lbl = tk.Label(self, text="Switched On:")
        lbl.pack(side="left")

        self.tkValue = tk.IntVar()
        self.tkValue.set(device.getSwitchedOn())
        val = tk.Entry(self, width=20, textvariable=self.tkValue)
        val.pack(side="left")

        self.saveButton = tk.Button(self, text="Save", command=self.saveChanges)
        self.saveButton.pack()

    def saveChanges(self):
        
        if self.device is None:
            self.device = SmartPlug(666)
            smartHome1.addDevice(self.device)

        self.device.setName( self.deviceNameEntry.get() )

        if isinstance(self.device,SmartPlug):
            self.device.consumptionRate = float(self.consumptionRateEntry.get()) 

        elif isinstance(self.device,SmartDoorbell):
            sleepMode = self.sleepModeEntry.get()
            if sleepMode.lower() == "True":
                self.device.setOption(True)
            elif sleepMode.lower() == "False":
                 self.device.setOption(False)
            else:
                print("Invalid sleep mode")

       
            self.device.setOption(self.tkValue.get())
            self.device.setOption(self.sleepModeEntry.get())
        self.destroy()

    def setDevice(self, event):

        if isinstance(self.device,SmartPlug):
            
            self.device.consumptionRate = float(self.consumptionRateEntry.get()) 

        elif isinstance(self.device,SmartDoorbell):
            sleepMode = self.sleepModeEntry.get()
            
       
            self.device.setOption(self.tkValue.get())
            self.device.setOption(self.sleepModeEntry.get())
        self.UpdateGUI(self.device)
        


        
        
        





class SmartHomeSystem(tk.Tk):
    def __init__(self, smartHome):
        super().__init__()
        self.smartHome = smartHome

        self.title("Smart Home System")

        self.topFrame = tk.Frame(self)
        self.updateGUI()  

    def updateGUI(self):
        
        
       
        for widget in self.topFrame.winfo_children():
            widget.destroy()

        devices = self.smartHome.getDevices()
        y = 0

        turnOnAllButton = tk.Button(self.topFrame, text="Turn on all")
        turnOnAllButton.grid(row=y, column=0, padx=5, pady=5)
        turnOnAllButton.bind("<Button-1>", self.turnOnAllDevices)
        turnOnAllButton.grid(row=y, column=1, padx=5, pady=5)

        turnOffAllButton = tk.Button(self.topFrame, text="Turn off all")
        turnOffAllButton.grid(row=y, column=1, padx=5, pady=5)
        turnOffAllButton.bind("<Button-1>", self.turnOffAllDevices)
        turnOffAllButton.grid(row=y, column=2, padx=5, pady=5)

        addButton = tk.Button(self.topFrame, text="Add")
        addButton.grid(row=y, column=1, padx=5, pady=5)
        addButton.bind("<Button-1>", self.addDevice)
        addButton.grid(row=y, column=3, padx=5, pady=5)

        y += 1

        for i, device in enumerate(devices):
            status = tk.Label(self.topFrame, text=device.status())
            status.grid(row=y, column=0, padx=5, pady=5)

            buttonText = "Switch on" if device.getSwitchedOn() else "Switch off"
            toggleButton = tk.Button(self.topFrame, text=buttonText)
            toggleButton.grid(row=y, column=1, padx=5, pady=5)
            toggleButton.bind("<Button-1>", lambda event, idx=i: self.toggleDevice(event, idx))

            editButton = tk.Button(self.topFrame, text="Edit", command=lambda idx=i: self.editDevice(idx))  
            editButton.grid(row=y, column=2, padx=5, pady=5)

            deleteButton = tk.Button(self.topFrame, text="Delete", command=lambda idx=i: self.removeDevice(idx))
            deleteButton.grid(row=y, column=3, padx=5, pady=5)

            y += 1

        self.topFrame.pack()


    def turnOnAllDevices(self, event):
        for device in self.smartHome.getDevices():
            device.turnOn()
        self.updateGUI()
    
    def turnOffAllDevices(self, event):
        for device in self.smartHome.getDevices():
            device.turnOff()
        self.updateGUI()

    def addDevice(self, event):
        editWindow = EditDeviceWindow(None)
        self.updateGUI()

    def toggleDevice(self, event, index):
        
        device = self.smartHome.getDevices()[index]
        if device.getSwitchedOn():
            device.turnOff()
        else:
            device.turnOn()

        # Update the GUI
        self.updateGUI()

    def editDevice(self, index):
        device = self.smartHome.getDevices()[index]
        editWindow = EditDeviceWindow(device)

    def removeDevice(self, index):
        self.smartHome.removeDeviceAt(index)
        self.updateGUI()


if __name__ == "__main__":

    smartHome1 = setUpHome()

    mainWindow = SmartHomeSystem(smartHome1)

    mainWindow.mainloop()
