import instaloader

def download_video(post_url):
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Extract the shortcode from the URL and download the post
    post = instaloader.Post.from_shortcode(L.context, post_url.split("/")[-2])  # Get the shortcode from URL
    
    # Check if it's a video
    if post.is_video:
        video_url = post.url
        print(f"Downloading video from: {video_url}")
        L.download_post(post, target="downloads")
    else:
        print("This is not a video.")

# Get the Instagram post URL from user input
post_url = input("Enter the Instagram post URL: ")

# Call the function to download the video
download_video(post_url)