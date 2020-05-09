# Episode 3
def converter(conversion):
    euros = 4168.79
    aryAry = 0.00024

    if conversion[:2] == "AE":
        print(float(conversion[3:])*aryAry)
    elif conversion[:2] == "EA":
        print(float(conversion[3:])*euros)

converter("AE 4000")
