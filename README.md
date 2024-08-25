# QuickVidDownload

A simple web application built with Flask for downloading videos and audio from various sources including YouTube, Facebook, and Instagram. The application provides an easy-to-use interface to download videos or audio files and notifies users with a popup once the download is complete.

## Features

- **Download Videos**: Download high-quality videos with both audio and video.
- **Download Audio**: Extract and download audio in MP3 format.
- **Popup Notification**: User-friendly notifications when the download is complete.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **yt-dlp**: A powerful command-line program for downloading videos from the web.
- **HTML/CSS**: For the front-end user interface.
- **JavaScript**: To handle form submission and notifications.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the Repository**

   ```bash
   https://github.com/Nikk-123/QuickVidDownload.git
   cd video-downloader
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```

   Open your web browser and go to `http://127.0.0.1:5000` to use the application.

## Usage

1. **Enter the Video URL**: Provide the URL of the video you want to download.
2. **Select Download Type**: Choose between downloading the video (with audio) or just the audio (MP3).
3. **Click Download**: Submit the form and wait for the notification that the download is complete.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

1. **Fork the Repository**
2. **Create a New Branch**
3. **Make Your Changes**
4. **Submit a Pull Request**
