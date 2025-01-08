from flask import Flask, render_template, request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            # YouTube Data APIを使用してビデオ情報を取得
            api_key = 'YOUR_API_KEY'  # YouTube Data APIのAPIキーを入力してください
            youtube = build('youtube', 'v3', developerKey=api_key)
            video_id = video_url.split('/')[-1]
            video_response = youtube.videos().get(id=video_id).execute()
            video_title = video_response['snippet']['title']
            video_embed = video_response['snippet']['defaultEmbedd']['url']
            return render_template('video.html', video_title=video_title, video_embed=video_embed)
        except HttpError as e:
            print('Error:', e)
            return '<h2>動画URLが正しくありません。</h2>'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
