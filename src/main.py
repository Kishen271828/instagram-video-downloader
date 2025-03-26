import instaloader
import yt_dlp
import re

def download_instagram_video(post_url):
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Extract the shortcode from the URL and download the post
    post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])  # Get the shortcode from URL
    
    # Check if it's a video
    if post.is_video:
        video_url = post.url
        print(f"Downloading Instagram video from: {video_url}")
        L.download_post(post, target="downloads")
    else:
        print("This is not a video on Instagram.")

def download_youtube_video(post_url):
    try:
        print(f"Downloading YouTube video from: {post_url}")
        
        # Create a downloader instance
        ydl_opts = {'outtmpl': 'downloads/%(title)s.%(ext)s'}
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([post_url])

    except Exception as e:
        print(f"Error downloading YouTube video: {e}")


def download_video(post_url):
    if "instagram.com" in post_url:
        download_instagram_video(post_url)
    elif "youtube.com" in post_url or "youtu.be" in post_url:
        download_youtube_video(post_url)
    else:
        print("Unsupported URL. Please provide an Instagram or YouTube video URL.")

# Get the URL from user input
post_url = input("Enter the Instagram or YouTube post URL: ")

# Call the function to download the video
download_video(post_url)
