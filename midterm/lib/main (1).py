from lib.room_sensor import TemperatureSensor, LightSensor, RoomSensor

temp = TemperatureSensor("Temp1")
light = LightSensor("Light1")

print(f"Temp: {temp.read()}")
print(f"Light: {light.read()}")

room = RoomSensor("Living Room", 26, 55, 420)
room.show_info()