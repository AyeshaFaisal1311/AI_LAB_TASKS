class modelbased_reflexagent:
    def __init__(self, des_temp):
        self.des_temp = des_temp
        self.model= {}

        self.cur_room=None
        self.cur_temp=None

    def percept(self,room,temp):
        self.cur_room=room
        self.cur_temp=temp
        self.model[room]=temp
        
    def actuator(self):
        if self.cur_temp>self.des_temp:
            return "Turn OFF Heater"
        else:
            return "Turn ON Heater"

agent=modelbased_reflexagent(26)
       
rooms={
    "bedroom":20,
    "kitchen":21,
    "living_room":19
}

for room,temp in rooms.items():
    agent.percept(room,temp)
    act=agent.actuator()
    print(f"{room}:{temp}===>{act}")

print("\n Current state of int_model:")
for room,temp in agent.model.items():
        print(f"{room}:{temp}")
