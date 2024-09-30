from django.shortcuts import render
from django.http import HttpResponse
from .forms import VideoForm
import yt_dlp
import re

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', filename)

def download_video(request):
    message = ''
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']

            ydl_opts = {'quiet': True, 'skip_download': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_title = info.get('title', None)
                sanitized_title = sanitize_filename(video_title)
                file_name = f"{sanitized_title}.mp4"
                file_path = f'downloads/{file_name}'

            ydl_opts = {
                'format': 'best',
                'outtmpl': file_path,
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            # After download, set the success message
            message = f'Video "{video_title}" downloaded successfully.'

    else:
        form = VideoForm()

    # Pass the form and message to the template
    return render(request, 'downloader/download.html', {'form': form, 'message': message})