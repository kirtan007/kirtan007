def centimeter_to_meter(centimeter):
    meter = centimeter*10
    return meter
def display_BMI(weight , height):
    BMI = weight / (height/100)**2
    return BMI

weight = int(input("Enter weight:-"))
height = int(input("Enter height:-"))
print(display_BMI(weight , height))