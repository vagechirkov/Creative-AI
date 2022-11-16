import random

from PIL import Image


class StyleDiffusion:
    def __init__(self):
        # download weights if not available
        # load models
        pass

    def generate(
            self,
            prompt: str,
            vector=None,
            guidance_scale=7.5,
            inference_steps=50,
            num_images=1,
            seed=-1):
        # generate images
        images = []

        for _ in range(num_images):

            img = Image.new('RGB', [500, 500], 255)
            data = img.load()

            for x in range(img.size[0]):
                for y in range(img.size[1]):
                    random_color = (random.randint(0, 255),
                                    random.randint(0, 255),
                                    random.randint(0, 255))
                    if random.randint(0, 1):
                        data[x, y] = random_color
                    else:
                        data[x, y] = (
                            x % 255,
                            y % 255,
                            (x ** 2 - y ** 2) % 255,
                        )
            images.append(img)
        return images
