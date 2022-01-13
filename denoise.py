import imageio
import numpy as np


def main():
    xor_image = imageio.imread("xor.png", as_gray=False).astype(np.uint8)
    noise = xor_image <= 20
    xor_image[noise] = 0
    imageio.imsave("denoised.png", xor_image.astype(np.uint8))

if __name__ == "__main__":
    main()
