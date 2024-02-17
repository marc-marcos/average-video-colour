import splitting
import output_image
import dominant

# Split the Video into frames

FILE_NAME = "Test.mp4"
file_name_without_extension = FILE_NAME.split(".")[0]

splitting.split_video(FILE_NAME)

dominants_colors = []

# Get the dominant pixel of every frame

dominants_colors = dominant.get_all_dominant_colors(file_name_without_extension)

output_image.create_color_bar(dominants_colors)