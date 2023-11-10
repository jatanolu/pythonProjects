import re

message = 'Call me at 190-129-1919 or don\'t I dont\'t care 123-456-7890'
phoneNumReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumReg.search(message)
print(phoneNumReg.findall(message))
print(mo.group())

def isPhoneNumber(txt):
    if len(txt) != 12:
        return False # not phone number-sized
    for i in range(0,3):
        if not txt[i].isdecimal():
            return False # no area code
    if txt[3] != '-':
        return False
    for i in range (4, 7):
        if not txt[i].isdecimal():
            return False 
    if txt[7] != '-':
        return False
    for i in range (8, 12):
        if not txt[i].isdecimal():
            return False 
    return True
print(isPhoneNumber('415-555-1234'))
print(isPhoneNumber("hey"))


