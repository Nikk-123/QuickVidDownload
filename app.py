from flask import Flask, render_template, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

# Directory to store downloads
DOWNLOAD_FOLDER = 'downloads'
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def download_video(url, download_type, output_path):
    """
    Function to download video or audio using yt-dlp.
    """
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best' if download_type == 'video' else 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    # Set additional options for MP3
    if download_type == 'audio':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'merge_output_format': 'mp3'
        })

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        download_type = request.form['download_type']

        try:
            download_video(video_url, download_type, DOWNLOAD_FOLDER)
            return jsonify({'success': True, 'message': 'File downloaded successfully!'})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
