def istrue(tuplle):
    for i in tuplle:
        if not i:
            return False
    return True
tuplle = (True, True, True)
print(istrue(tuplle))