def check_speed():
    allowed_speed = 70
    above_speed = 5
    demerit = 0
    while demerit < 12:
        speed = int(input("Your speed: "))
        if speed <= allowed_speed:
            print("OK")
            yield demerit
        elif speed > allowed_speed:
            demerit += int((speed - allowed_speed) / above_speed)
            yield demerit
        elif demerit >= 12:
            print("License suspended")
            yield False, demerit


check = check_speed()
for value in check:
    print(f"Points: {value}")

