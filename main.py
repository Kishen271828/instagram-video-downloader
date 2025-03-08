import instaloader

def download_video(post_url):
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Download the post using the URL
    post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])  # Get the shortcode from URL
    
    # Check if it's a video
    if post.is_video:
        video_url = post.url
        print(f"Downloading video from: {video_url}")
        L.download_post(post, target="downloads")
    else:
        print("This is not a video.")

# Example usage
post_url = "https://www.instagram.com/reel/DGEa0WhIMVY/?igsh=Y2Y4cHVtNG94M2Yy"
download_video(post_url)
