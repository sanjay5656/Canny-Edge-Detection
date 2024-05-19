import cv2
import matplotlib.pyplot as plt

san = 'san.jpg'
san2 = cv2.imread(san, cv2.IMREAD_GRAYSCALE)

if san2 is None:
    print("Error: Could not load image")
    exit()

edges = cv2.Canny(san2, threshold1=100, threshold2=200)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(san2, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Edges')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

parameters = [
    (50, 150),  
    (100, 200),
    (150, 250)
]

san2 = cv2.imread(san, cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(15, 5))

for i, (threshold1, threshold2) in enumerate(parameters):
    edges = cv2.Canny(san2, threshold1, threshold2)
    plt.subplot(1, 3, i + 1)
    plt.title(f'Thresholds: {threshold1}, {threshold2}')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')

plt.tight_layout()
plt.show()    