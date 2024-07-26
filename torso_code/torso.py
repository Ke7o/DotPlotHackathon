from PIL import Image, ImageDraw, ImageFont

def draw_grid(draw, image_size, grid_size, line_color, label_color):
    img_width, img_height = image_size
    # Adjust these values to change the size of the grid
    padding_left = img_width * 0.29  # Padding for the left side
    padding_right = img_width * 0.32  # Padding for the right side
    padding_y_top = img_height * 0.58  # Increase padding to move the grid down
    padding_y_bottom = img_height * 0.245  # Increase padding to move the grid up
    cell_width = (img_width - padding_left - padding_right) / grid_size[0]
    cell_height = (img_height - padding_y_top - padding_y_bottom) / grid_size[1]

    font = ImageFont.truetype("arial.ttf", 20)  # Increase font size

    # Draw vertical lines and column labels
    for i, x in enumerate(range(int(padding_left), int(img_width - padding_right), int(cell_width))):
        draw.line([(x, padding_y_top), (x, img_height - padding_y_bottom)], fill=line_color)
        if i < grid_size[0]:
            label = chr(65 + i)  # Convert 0 -> A, 1 -> B, etc.
            draw.text((x + cell_width // 2, padding_y_top - cell_height // 2), label, fill=label_color, font=font, anchor="mm")

    # Draw horizontal lines and row labels
    for j, y in enumerate(range(int(padding_y_top), int(img_height - padding_y_bottom), int(cell_height))):
        draw.line([(padding_left, y), (img_width - padding_right, y)], fill=line_color)
        if j < grid_size[1]:
            label = str(j + 1)
            draw.text((padding_left - cell_width // 2, y + cell_height // 2), label, fill=label_color, font=font, anchor="mm")

    return cell_width, cell_height, padding_left, padding_y_top

def plot_lesions(draw, lesions, cell_size, grid_size, lesion_color):
    columns = "ABCDEFGH"
    rows = "1234"
    cell_width, cell_height, padding_left, padding_y_top = cell_size

    font = ImageFont.truetype("arial.ttf", 30)  # Increase font size for 'X'

    for lesion in lesions:
        column, row = lesion[0], lesion[1]
        x = padding_left + columns.index(column) * cell_width
        y = padding_y_top + (int(row) - 1) * cell_height
        draw.text((x + cell_width // 2, y + cell_height // 2), "X", fill=lesion_color, font=font, anchor="mm")

def main():
    # Load torso image
    torso_image = Image.open("torso.png")  # Replace with your torso image file path
    draw = ImageDraw.Draw(torso_image)

    # Grid settings
    grid_size = (8, 4)
    line_color = "blue"
    label_color = "black"
    lesion_color = "red"
    lesions = [("B", "2"), ("D", "3"), ("H", "1")]  # Example lesions, replace with actual data

    # Draw grid with labels
    cell_size = draw_grid(draw, torso_image.size, grid_size, line_color, label_color)

    # Plot lesions
    plot_lesions(draw, lesions, cell_size, grid_size, lesion_color)

    # Save the result
    torso_image.save("torso_with_lesions.png")
    torso_image.show()

if __name__ == "__main__":
    main()
