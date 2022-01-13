import imageio
import numpy as np


def main():
    denoised = imageio.imread("denoised.png", as_gray=False).astype(np.uint8)
    # gray values, let's only look at red then
    denoised = denoised[:,:,0]
    chars = [chr(pixel) for pixel in denoised[denoised > 0]]
    print(''.join(chars))

if __name__ == "__main__":
    main()
