import pyrogram
from pyrogram import Client, filters
import requests


# Function to get the Instagram post image
def get_instagram_post_image(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            html = response.text
            start_index = html.find("display_url") + 15
            end_index = html.find('"', start_index)
            image_url = html[start_index:end_index]
            return image_url
    except Exception as e:
        print(e)
    return None

# Function to get the Instagram reel video
def get_instagram_reel_video(link):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            html = response.text
            start_index = html.find("video_url") + 12
            end_index = html.find('"', start_index)
            video_url = html[start_index:end_index]
            return video_url
    except Exception as e:
        print(e)
    return None

# Command handler for /insta
@Client.on_message(filters.command("insta"))
def get_instagram_media(client, message):
    # Get the Instagram link from the command arguments
    link = message.text.split(" ", 1)[1]

    if "instagram.com/p/" in link:
        # It's an Instagram post link
        image_url = get_instagram_post_image(link)
        if image_url:
            client.send_photo(
                chat_id=message.chat.id,
                photo=image_url,
                caption="Here's the image from the Instagram post."
            )
        else:
            client.send_message(
                chat_id=message.chat.id,
                text="Sorry, I couldn't retrieve the image from the Instagram post link."
            )
    elif "instagram.com/reel/" in link:
        # It's an Instagram reel link
        video_url = get_instagram_reel_video(link)
        if video_url:
            client.send_video(
                chat_id=message.chat.id,
                video=video_url,
                caption="Here's the video from the Instagram reel."
            )
        else:
            client.send_message(
                chat_id=message.chat.id,
                text="Sorry, I couldn't retrieve the video from the Instagram reel link."
            )
    else:
        client.send_message(
            chat_id=message.chat.id,
            text="Please provide a valid Instagram post or reel link."
        )
