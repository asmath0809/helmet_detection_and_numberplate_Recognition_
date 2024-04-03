from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_video', methods=['POST'])
def process_video():
    if 'video' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    video_file = request.files['video']

    # Save the uploaded video file
    video_path = 'uploaded_video.mp4'
    video_file.save(video_path)

    try:
        # Execute the existing Python script for video processing
        subprocess.run(['python', 'detect.py', '-i', video_path], check=True)
        return jsonify({'message': 'Video processed successfully'}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({'message': f'Error occurred during video processing: {e.stderr}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

