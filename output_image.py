from PIL import Image

def create_color_bar(colors):
    width = len(colors)
    height = 100

    print(colors)

    image = Image.new("RGB", (width, height))

    for x, color in enumerate(colors):
        print(tuple(color[0]))
        for y in range(height):
            bgr_color = tuple(color[0])
            rgb_color = (bgr_color[2], bgr_color[1], bgr_color[0])

            image.putpixel((x, y), rgb_color)

    image.save("output.png")

    return image