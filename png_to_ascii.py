import urllib.request
import numpy as np
from numpy import asarray
from PIL import Image

# symbolList = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"; 
symbolList = " .:-=+*#%@"

def intensityToChar(input):
    result = ' '
    # input /= 3.642857
    input /= 22.5
    input = int(input)

    # if (input < 70):
    if (input < 10):
        result = symbolList[input]
    # elif (input <= 71):
    elif (input <= 11):
        # result = symbolList[69]
        result = symbolList[9]
    else:
        print("You did a fuck up\nUnknown intensity value: " + str(input))
    
    return result

def convertImg(img_address):

    urllib.request.urlretrieve(img_address, "tempFile.png")
    img = Image.open("tempFile.png").convert('LA')
    
    #resized_im = img.resize((44, 44))
    resized_im = img.resize((64, 18))

    resized_im.save("tempFile.png")

    width, height = resized_im.size
    numpydata = asarray(resized_im)

    result = [[0 for u in range(width)] for p in range(height)]
    print(numpydata)

    for i in range(height):
        for j in range(width):
            num = numpydata[i, j][0]
            character = intensityToChar(num)
            result[i][j] = character          

    print(result)
    print('\n')
    print("Successfully executed: png_to_ascii.py\n")

    return result, width, height



