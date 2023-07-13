#Conversion of temperature of degree centigrade to farenheit.  
def centigrade_to_fahrenheit(celsius):
  F=(celsius*1.8)+32
  return F
celsius = int(input("Enter temperature in centigrade:"))
temperature= centigrade_to_fahrenheit(celsius)
print("Temperature in degree fahrenheit:",temperature)