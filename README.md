# Video to Images Converter

This is a simple tool to convert a video file into a specified number of images. It supports various video formats and saves the images in JPEG format. The tool is designed to be user-friendly and easy to use, making it accessible to anyone who needs to extract images from a video.

## Create Virtual Environment

To ensure a clean and isolated environment for the tool, it is recommended to create a virtual environment using conda. To do this, run the following commands in your terminal or command prompt:

```
conda create -n video_to_images python=3.10 -y
```

```
conda activate video_to_images
```

This will create a new virtual environment named `video_to_images` with Python 3.10 and activate it. You can verify that the virtual environment is activated by checking the command prompt, which should now include the name of the virtual environment.

## Installation

Once the virtual environment is activated, you can install the required dependencies using pip. The dependencies are listed in the `requirements.txt` file and can be installed by running the following command:

```
python -m pip install -r requirements.txt
```

This command will install the required dependencies, including OpenCV and NumPy, which are necessary for the tool to function properly.

## Usage

To use the tool, you need to run the `main.py` script with the required arguments. The basic usage is as follows:

```
python main.py --video /path/to/video.mp4 --output /path/to/output_folder --number 200 --type normal
```

Here's a breakdown of the arguments:

- `--video` or `-v`: Specify the path to the video file you want to convert. Supported formats include MP4, AVI, and more. For example:
  - `python main.py -v /path/to/video.mp4`
  - `python main.py --video /path/to/video.avi`
- `--output` or `-o`: Specify the folder where the images extracted from the video will be saved. The folder will be created if it doesn't exist. For example:
  - `python main.py -o /path/to/output_folder`
  - `python main.py --output /path/to/output_folder`
- `--number` or `-n`: Specify the total number of images to be extracted from the video. The default is 200. For example:
  - `python main.py -n 100`
  - `python main.py --number 500`
- `--type` or `-t`: Specify the type of extraction. Can be `normal` for evenly spaced extraction or `random` for random extraction. The default is `normal`. For example:
  - `python main.py -t normal`
  - `python main.py --type random`

## Example

To convert a video file `video.mp4` into 200 images and save them in the folder `output_folder` using evenly spaced extraction, run the following command:

```
python main.py -v video.mp4 -o output_folder -n 200 -t normal
```

This will extract 200 images from the video file `video.mp4` and save them in the folder `output_folder` with evenly spaced extraction.

## Notes

- The output folder will be created if it doesn't exist.
- The video file is expected to be in a format that can be read by OpenCV.
- The tool supports both evenly spaced and random extraction of images from the video.
- The images are saved in JPEG format.

## License

This tool is released under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/), which allows for free use, modification, and distribution of the software, but requires attribution of the original authors.

## Example Use Cases

* Extracting images from a video for data annotation and machine learning model training
* Creating a photo gallery from a video
* Extracting keyframes from a video for video summarization
* Converting a video to a series of images for further processing or analysis

These are just a few examples of the many use cases for this tool. The possibilities are endless, and we hope that this tool will be useful for your specific needs.