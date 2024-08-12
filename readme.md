# README

## Overview

This project is a Python-based application that captures live video from a webcam and uses OpenAI's GPT model to detect if a person has their hand near their mouth in the video feed. If the model detects this behavior, an alert sound is played using Pygame.
## Images

If the application of these products didn't work for you, try our auto nail chowing detector:
<img src="docs/nail_chowing.jpg" alt="drawing" width="200"/>
<img src="docs/nail_chowing_protection.jpg" alt="drawing" width="200"/>

If the application struggles to accurately detect the hand near mouth condition with your own images or live feed, these test images can help you troubleshoot and refine the solution.
## Features

- **Real-time Video Processing:** Captures video frames in real-time using OpenCV.
- **Image Compression:** Compresses captured frames to reduce the size before sending them for analysis.
- **Hand Near Mouth Detection:** Uses an OpenAI GPT model to analyze the image and determine if a hand is near the mouth.
- **Audio Alert:** Plays a sound alert if the hand near mouth condition is detected.

## Requirements

- Python 3.7 or higher
- OpenAI API key

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/nail-chewing-detector.git
   cd nail-chewing-detector
   ```

2. **Install the required Python packages:**

   ```bash
   pip install requirement.txt
   ```

3. **Set your OpenAI API key:**

   Replace `"api_key"` in the script with your actual OpenAI API key or set it as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

4. **Prepare the alert sound:**

   Place an MP3 file named `alert_sound.mp3` in the root directory of the project. This sound will be played when the hand near mouth condition is detected.

## Usage

To run the application, simply execute the Python script:

```bash
python detector.py
```

The program will start capturing video from your default webcam. If the application detects a hand near the mouth, it will play the alert sound continuously until the hand is no longer near the mouth.

## How It Works

1. The application captures a frame from the webcam.
2. The frame is compressed and converted to a base64 encoded string.
3. This encoded image is sent to OpenAI's GPT model, which analyzes the image to determine if a hand is near the mouth.
4. If the model detects a hand near the mouth, an alert sound is played. The sound stops once the condition is no longer met.

## Limitations

- The accuracy of the detection relies on the capabilities of the GPT model and the quality of the captured images.
- The current setup uses a hardcoded prompt for the GPT model, which may need adjustment based on specific use cases or image quality.

## Future Enhancements

- Improve the detection algorithm by fine-tuning prompts or using a different model.
- Add support for different alert sounds or more complex alert conditions.
- Optimize image processing for faster detection.

