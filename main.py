import cv2
import os
import argparse
import random

def convert_video_to_images(video_path: str, output_folder: str, total_images: int, extraction_type: str) -> None:
    """
    Converts a video file into a specified number of images, either evenly spaced or randomly extracted.

    This function takes a video file path, an output folder, the total number of images to be extracted, and the extraction type as input. It saves frames either evenly spaced or randomly extracted as JPEG images in the output folder.

    Args:
        video_path (str): The path to the video file to be converted.
        output_folder (str): The folder where the images will be saved.
        total_images (int): The total number of images to be extracted from the video.
        extraction_type (str): The type of extraction. Can be 'normal' for evenly spaced extraction or 'random' for random extraction.

    Returns:
        None

    Example Usage:
        >>> convert_video_to_images("path/to/video.mp4", "path/to/output/folder", 200, 'normal')

    Expected Input/Output:
        Input: A video file (e.g. MP4, AVI), an output folder, the total number of images to be extracted, and the extraction type.
        Output: JPEG images extracted either evenly spaced or randomly, saved in the output folder.

    Notes:
        The output folder will be created if it does not exist.
        The video file is expected to be in a format that can be read by OpenCV.
    """
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)  # Create the output folder if it doesn't exist
    
    # Initialize the video capture object
    cap = cv2.VideoCapture(video_path)  # Load the video
    
    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error opening video file")  # If the video file cannot be opened, print an error message
        return  # Exit the function
    
    # Retrieve the total number of frames in the video
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # Get the total number of frames
    print(f"Total Frames: {total_frames}")  # Print the total number of frames
    
    # Calculate the extraction rate based on the total number of images to be extracted
    if extraction_type == 'normal':
        extraction_rate = total_frames // total_images  # Calculate the extraction rate for normal extraction
    elif extraction_type == 'random':
        extraction_rate = random.sample(range(1, int(total_frames)), total_images)  # Calculate the extraction rate for random extraction
    else:
        print("Invalid extraction type. Please choose 'normal' or 'random'.")
        return
        
    # Initialize a counter for the number of frames processed
    frame_count = 0
    while cap.isOpened():  # Loop through the video frame by frame
        ret, frame = cap.read()  # Read a frame from the video
        if not ret:
            break  # If the frame cannot be read, break the loop
        
        # Check if the current frame should be saved based on the extraction rate
        if frame_count in extraction_rate:  # Use the calculated extraction rate for comparison
            # Construct the name for the current frame
            frame_name = f"frame_{frame_count:06d}.jpg"  # Format the frame name with a leading zero
            # Save the current frame as a JPEG image
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)
        
        frame_count += 1  # Increment the frame count
    
    # Release the video capture object
    cap.release()  # Release everything if job is finished
    print(f"Converted {total_images} images from the video")  # Print the total number of images converted

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""A tool to convert a video file into a specified number of images. It supports various video formats and saves the images in JPEG format. Example: python main.py -v video.mp4 -o output_folder -n 200 -t normal""")
    parser.add_argument("-v", "--video", type=str, required=True, help="Specify the path to the video file you want to convert. Supported formats include MP4, AVI, and more. Example: video.mp4")
    parser.add_argument("-o", "--output", type=str, required=True, help="Specify the folder where the images extracted from the video will be saved. The folder will be created if it doesn't exist. Example: output_folder")
    parser.add_argument("-n", "--number", type=int, default=200, help="Specify the total number of images to be extracted from the video. Default: 200")  # Updated argument for total number of images
    parser.add_argument("-t", "--type", type=str, default='normal', help="Specify the type of extraction. Can be 'normal' for evenly spaced extraction or 'random' for random extraction. Default: normal")
    args = parser.parse_args()
    
    # Call the function to convert the video to images based on the total number of images and the extraction type
    convert_video_to_images(args.video, args.output, args.number, args.type)
