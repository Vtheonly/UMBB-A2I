import cv2

# Reading an image
img = cv2.imread('Images/pepper.bmp')
imgOG = cv2.imread('Images/pepper.bmp')

# Load a colour image with its conversion to greyscale
gray_img = cv2.imread('Images/pepper.bmp', cv2.IMREAD_GRAYSCALE)
# Converting a colour image to a greyscale image
gray_img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Displaying an image
# cv2.imshow('Input Image', img)
# cv2.imshow(' Image loaded in greyscale ', gray_img)
# cv2.imshow(' Image converted to greyscale ', gray_img2)
cv2.waitKey(0)
# Reading the colours of a pixel at position (100, 150)
# pixel = img[100, 150]
# print(f" The RGB values of Pixel at (100, 150) are: {pixel}")
""" Reading image dimensions: dimensions = img.shape
For a colour image, dimensions contains three values:
(height, width, channels). height: number of rows of pixels in the image. width: number of
columns of pixels in the image. channels: number of colour channels (e.g. 3 for RGB, 1 for
greyscale). For a greyscale image, dimensions contains two values: (height, width """
h, w, channels = img.shape
print(f"Height: {h} pixels")
print(f"Width: {w} pixels")
# print(f"Channels: {channels}")
# # Changing the pixel colours of the centre line to red
# for i in range(0, width - 1):
#     img[int(height / 2), i] = [0, 0, 255]  # [B,G,R] modified to red



# cv2.imshow('Converted Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




for i in range(0, w - 1):
    for j in range(int(h / 2)-1,int(h)):
     img[j, i] = [0, 0, 0]  # [B,G,R] modified to red

cv2.imshow('Converted Image', img)
cv2.waitKey(0)


new_width = w
new_height = h//2
resized_image = cv2.resize(imgOG, (new_width, new_height))
cv2.imshow('Converted Image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



center_point = (w // 2, h // 2)
angle = 90


rotation_matrix = cv2.getRotationMatrix2D(center_point, angle, 1.0)
rotated_image = cv2.warpAffine(imgOG, rotation_matrix, (w, h))


cv2.imshow('Converted Image', rotated_image)
cv2.waitKey(0)




blurred_image = cv2.GaussianBlur(imgOG, (15, 15), 0)


cv2.imshow('Converted Image', blurred_image)
cv2.waitKey(0)



y=30
x=200
cropped_image = imgOG[y : y+120 , x : x+200]

cv2.imshow('Converted Image', cropped_image)
cv2.waitKey(0)

cv2.destroyAllWindows()




