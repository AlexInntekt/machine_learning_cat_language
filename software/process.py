import base64
 
with open("t.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print str

def train():
    pass