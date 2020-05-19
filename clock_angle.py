def calcAngle(h, m):
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print("Invalid input")
    if (h == 12):
        h = 0
    if (m == 60):
        m = 0

    # Hour and minute hand angle with reference to 12:00
    hour_angle = 0.5 * (h * 60 + m)
    minute_angle = 6 * m

    # Find the difference between two angles
    angle = abs(hour_angle - minute_angle)

    # Get the angle of two possible
    angle = min(360 - angle, angle)

    return angle
# Passing the input
h = int(input("Enter the hours" ))
m = int(input("Enter the minutes"))
print('Angle ', calcAngle(h,m))