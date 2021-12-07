# YAML

Here you will find a `SmartHome.yml` file where you can :

1. `GET` the resource associated to a Smart Home to get the list of rooms
2. `GET` the resource associated to a room (the id is a URL parameter) to get the list of connected devices it contains. Focus on two types of devices: color light bulbs, and smart TVs.
3. `GET` the resource associated to a connected device (the id of the room and the id of the connected device are URL parameters) to obtain the current status of the device.
4. `PUT` the resource associated to a connected device (same path as before) to change the status of the device.




