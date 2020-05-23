import syntax #Needed to access the HEXTOFUNCTIONDICT dictionary

class Interpreter:
    def __init__(self, currentRAM, master, runFreq):
        self.master = master
        self.runFreq = runFreq
        self.args = { #Dictionary that holds all arguments needed
            "PC": 0, #Program counter
            "RAM": currentRAM, #State of RAM
            "ACC": 0, #Accumulator
            "IX": 0, #Index register
            "ZMP": False, #Comparison flag
            "halt": False, #Halt flag
            "errorMsg": "Execution successful" #Error message to be given out in the case of a flag
            }

    def execute(self, stepFlag):
        if self.args["RAM"][self.args["PC"]] in syntax.HEXTOFUNCTIONDICT: #Checking if the opcode exists in the dictionary before calling the method
            syntax.HEXTOFUNCTIONDICT[self.args["RAM"][self.args["PC"]]](self.args) #Calls the respective method for the opcode that the PC is pointing at, passing the dictionary in as a parameter
            if not self.args["halt"] and not stepFlag: #Checking if we can schedule the next call to execute
                self.master.after(self.runFreq, lambda: self.execute(stepFlag))
        else: #Undefined opcode case
            self.args["RAM"][self.args["halt"]] = True #Setting the halt flag as we have got to an invalid opcode
            self.args["RAM"][self.args["errorMsg"]] = f"Opcode {self.args['RAM'][self.args['PC']]} is undefined."
        return self.args #We need to return the dictionary in any case


    def updateArgs(self): #Stub function which will be overwritten by Adi's updateArgs method
        print(self.args)

    def stop(self): #Method to be called in the event that the stop button is pressed
        self.args["halt"] = True


"""PLAN:

class Interpreter:
    constructor(RAM, symbolTable):
        self.RAM = RAM
        self.symbolTable = symbolTable
        self.PC = 0
        self.registers = {
            "EE": 0, #ACC
            "FF": 0  #IX
        }
        self.haltFlag = False

    executeMethod():
        self.RAM, self.PC, self.registers, self.haltFlag = HEXTOFUNCTIONDICT[self.RAM[self.PC]](self.PC, self.RAM, self.registers) #We call the syntax.py methods, which return RAM, PC and registers
        return self.RAM, self.PC, self.registers, self.haltFlag #This gets returned to whatever called it so it can be displayed




#Not sure where this method would go so here's a rough plan of what I'm thinking

Put this in main

interpreter = Interpreter(RAM, symbolTable) #Creating interpreter object here
haltFlag = False


interpretMethod(stepFlag):
    RAM, PC, registers, haltFlag = interpreter.executeMethod()
    if not(stepFlag): #We can by default have some step flag which indicates if we are stepping or not
        #SCHEDULE CALL HERE

"""
