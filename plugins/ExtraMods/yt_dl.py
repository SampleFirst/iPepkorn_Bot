import os
import requests
import asyncio
import math
import time
import wget
from pyrogram import filters, Client
from pyrogram.types import Message
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from info import LOG_CHANNEL 


@Client.on_message(filters.command(['song', 'mp3']) & filters.private)
async def song(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    rpk = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = await message.reply(f"**Searching for your song...!\n {query}**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        performer = f"[Mᴋɴ Bᴏᴛᴢ™]"
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
    except Exception as e:
        print(str(e))
        return await m.edit("**Could not find or check the link**")
    
    await m.edit("**Downloading your song...!**")
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)

        cap = "**BY›› [Mᴋɴ Bᴏᴛᴢ™](https://t.me/mkn_bots_updates)**"
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        
        # Send audio to LOG_CHANNEL
        await client.send_audio(
            chat_id=LOG_CHANNEL,
            audio=audio_file,
            caption="Video Downloaded for {message.from_user.mention}"
        )

        # Reply to the user with the downloaded audio
        await message.reply_audio(
            audio=audio_file,
            caption=cap,
            quote=False,
            title=title,
            duration=dur,
            performer=performer,
            thumb=thumb_name
        )
        await m.delete()
    except Exception as e:
        await m.edit("**Error occurred while downloading**")
        print(e)
    
    try:
        # Clean up downloaded files
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

@Client.on_message(filters.command(["video", "mp4"]))
async def vsong(client, message: Message):
    urlissed = get_text(message)
    pablo = await client.send_message(message.chat.id, f"**Finding your video** `{urlissed}`")
    
    if not urlissed:
        return await pablo.edit("Invalid command syntax. Please check the help menu for more information!")

    search = SearchVideos(f"{urlissed}", offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    url = mo
    sedlyf = wget.download(kekme)
    
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        return await pablo.edit_text(f"**Failed to download the video**\n**Error:** `{str(e)}`")
    
    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"""**Title:** [{thum}]({mo})\n**Requested by:** {message.from_user.mention}"""
    
    # Send video to LOG_CHANNEL
    await client.send_video(
        chat_id=LOG_CHANNEL,
        video=open(file_stark, "rb"),
        caption="Video Downloaded for {message.from_user.mention}"
    )
    
    # Reply to the user with the downloaded video
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        reply_to_message_id=message.message_id
    )
    
    await pablo.delete()
    
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
            
