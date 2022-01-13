import imageio
import numpy as np


def main():
    image_1 = imageio.imread("pepe.png", as_gray=False).astype(np.uint8)
    image_2 = imageio.imread("pepe_bruh.png", as_gray=False).astype(np.uint8)
    difference = image_1 ^ image_2
    # put alpha channel on 255 so we can see something
    difference[:, :, 3] = 255
    imageio.imsave("xor.png", difference.astype(np.uint8))

if __name__ == "__main__":
    main()
