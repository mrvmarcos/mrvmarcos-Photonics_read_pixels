#Reading pixels from a photo
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



# Load the image
image = Image.open("C:/Users/marco/Documents/4º Ing Fisc+Inds gmu/Segundo Cuatri/Material Science/Homework/Photonics/MercuryLamp (2).jpeg")

#rotate the image
image = image.rotate(-90)

#pixels colors
pixels = np.array(image)


# Display the image
plt.imshow(image)
plt.plot()
plt.show()
# Load the image
image = Image.open("C:/Users/marco/Documents/4º Ing Fisc+Inds gmu/Segundo Cuatri/Material Science/Homework/Photonics/Splitting_Laser.jpeg")

#rotate the image
image = image.rotate(-90)

#pixels colors
pixels = np.array(image)


# Display the image
plt.imshow(image)
plt.plot()
plt.show()