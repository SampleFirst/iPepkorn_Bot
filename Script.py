class script(object):  
    START_TXT = """<b>✨ Hello {user}.

My Name Is {bot}.

I Can Provide Movies For You. Just Add Me In Your Group Or Join Our Group</b>"""

    HELP_TXT = "Hey {}\nHere's My Help"

    ABOUT_TXT = """<b>✯ My Name: {}
✯ Coded On: Python/Pyrogram
✯ My Database: MongoDB
✯ My Server: Anywhere
✯ My Version: iPepkornBot v1.0.0</b>"""
   
    SOURCE_TXT = """<b>NOTE:</b>
- Source Code ◉› : Private
"""

    FILE_TXT = """<b>➤ Help For File Store</b>

<i>By Using This Module, You Can Store Files in My Database, and I Will Give You a Permanent Link to Access the Saved Files. If You Want to Add Files From a Public Channel, Send the File Link Only, or If You Want to Add Files From a Private Channel, You Must Make Me Admin on the Channel to Access Files.</i>

<b>⪼ Command & Usage</b>
➪ /link › Reply to Any Media to Get the Link
➪ /batch › To Create Links for Multiple Media

<b>⪼ Example:</b>
</code>/batch https://t.me/examples/1 https://t.me/examples/10</code>"""

    FILTER_TXT = """Select Which One You Want...✨"""

    GLOBALFILTER_TXT = """<b>Help For Global Filters</b>

<i>Filter is the feature where users can set automated replies for a particular keyword, and the bot will respond whenever that keyword is found in a message.</i>

<b>Note:</b>
This module only works for my admins.

<b>Commands and Usage:</b>
• /gfilter - To Add Global Filters
• /gfilters - To View List of All Global Filters
• /delg - To Delete a Specific Global Filter
• /delallg - To Delete All Global Filters

• /g_filter off - Use this command + on/off in your group to control Global Filters in your group
"""

    MANUELFILTER_TXT = """<b>Help For Filters</b>

<i>Filter is the feature where users can set automated replies for a particular keyword, and the bot will respond whenever that keyword is found in a message.</i>

<b>Note:</b>
1. This Bot Should Have Admin Privilege.
2. Only Admins Can Add Filters in a Chat.
3. Alert Buttons Have a Limit of 64 Characters.

<b>Commands and Usage:</b>
• /filter - Add a Filter in Chat
• /filters - List All the Filters of a Chat
• /del - Delete a Specific Filter in Chat
• /delall - Delete the Whole Filters in a Chat (Chat Owner Only)

• /g_filter off - Use this command + on/off in your group to control Global Filter in your group
"""

    BUTTON_TXT = """<b>Help For Buttons</b>

<i>This Bot Supports Both URL and Alert Inline Buttons.</i>

<b>Note:</b>
1. Telegram Will Not Allow You to Send Buttons Without Any Content, So Content Is Mandatory.
2. This Bot Supports Buttons With Any Telegram Media Type.
3. Buttons Should Be Properly Parsed in Markdown Format

<b>URL Buttons:</b>
[Button Text](buttonurl:xxxxxxxxxxxx)

<b>Alert Buttons:</b>
[Button Text](buttonalert:This Is An Alert Message)
"""

    AUTOFILTER_TXT = """<b>Help For AutoFilter</b>

<i>AutoFilter is the feature to filter and save files automatically from a channel to a group. You can use the following command to enable/disable the AutoFilter in your group.</i>

• /autofilter on - Enable AutoFilter in your chat
• /autofilter off - Disable AutoFilter in your chat

<b>Other Commands:</b>
• /set_template - Set IMDb Template for your group
• /get_template - Get current IMDb Template for your group
"""

    CONNECTION_TXT = """<b>Help For Connections</b>

<i>Used to connect bot to PM for managing filters. It helps to avoid spamming in groups.</i>

<b>Note:</b>
• Only admins can add a connection.
• Send /connect for connecting me to your PM.

<b>Commands and Usage:</b>
• /connect - Connect a particular chat to your PM
• /disconnect - Disconnect from a chat
• /connections - List all your connections
"""

    ADMIN_TXT = """<b>Help For Admins</b>

<i>This module only works for my admins</i>

<b>Command & Usage</b>
• /logs - Get the recent errors
• /delete - Delete a specific file from DB
• /deleteall - Delete all files from DB
• /users - Get list of my users and IDs
• /chats - Get list of my chats and IDs
• /channel - Get list of total connected channels
• /broadcast - Broadcast a message to all users
• /group_broadcast - Broadcast a message to all connected groups
• /leave - With chat ID to leave from a chat
• /disable - With chat ID to disable a chat
• /invite - With chat ID to get the invite link of any chat where the bot is admin
• /ban_user - With ID to ban a user
• /unban_user - With ID to unban a user
• /restart - Restart the bot
• /clear_junk - Clear all deleted accounts and blocked accounts in database
• /clear_junk_group - Clear added, removed, or deactivated groups on DB
"""

    STATUS_TXT = """<b>◉ Total Files: <code>{}</code>
◉ Total Users: <code>{}</code>
◉ Total Chats: <code>{}</code>
◉ Used DB Size: <code>{}</code>
◉ Free DB Size: <code>{}</code></b>"""

    LOG_TEXT_G = """<b>#New_Group

◉ Group: {a}
◉ G-ID: <code>{b}</code>
◉ Link: @{c}
◉ Members: <code>{d}</code>
◉ Added by: {e}

◉ By: @{f}</b>"""

    LOG_TEXT_P = """#New_User

◉ User-ID: <code>{}</code>
◉ Account Name: {}
◉ Username: @{}

◉ By: @{}</b>"""
  
    GROUPMANAGER_TXT = """<b>Help for Group Manager</b>

<i>This is help for managing your group. This will work only for group admins.</i>

<b>Commands & Usage:</b>
• /inkick - Command with required arguments, and I will kick members from the group.
• /instatus - To check the current status of chat members from the group.
• /dkick - To kick deleted accounts.
• /ban - To ban a user from the group.
• /unban - Unban the banned user.
• /tban - Temporary ban a user.
• /mute - To mute a user.
• /unmute - To unmute the muted user.
• /tmute - With value to mute a user for a particular time, e.g., <code>/tmute 2h</code> to mute for 2 hours (values: m/h/d).
• /pin - To pin a message on your chat.
• /unpin - To unpin the message on your chat.
• /purge - Delete all messages from the replied message, or the current message."""

    EXTRAMOD_TXT = """<b>Help for Extra Module</b>

<i>Just send any image to edit image ✨</i>

<b>Commands & Usage:</b>
• /id - Get the ID of a specified user.
• /info - Get information about a user.
• /imdb - Get the film information from IMDb source.
• /paste [text] - Paste the given text on Pastey.
• /tts [text] - Convert text to speech.
• /telegraph - Send me this command reply with a picture or video under (5MB).
• /json - Reply with any message to get message info (useful for groups).
• /written - Reply with text to get a file (useful for coders).
• /carbon - Reply with text to get a carbonated image.
• /font [text] - To change your text fonts to fancy fonts.
• /share - Reply with text to get a text shareable link.
• /song [name] - To search the song on YouTube.
• /video [link] - To download the YouTube video."""

    CREATOR_REQUIRED = "❗<b>You have to be the group creator to do that</b>"

    INPUT_REQUIRED = "❗ **Argument Required**"

    KICKED = "✔️ Successfully kicked {} members according to the provided arguments"

    START_KICK = "Removing inactive members. This may take a while."

    ADMIN_REQUIRED = "❗<b>I am not an admin in this chat, so please add me again with all permissions</b>"

    DKICK = "✔️ Kicked {} deleted accounts successfully"

    FETCHING_INFO = "<b>Wait, I will fetch all info</b>"

    SERVER_STATS = """Server Stats:

Uptime: {}
CPU Usage: {}%
RAM Usage: {}%
Total Disk: {}
Used Disk: {} ({}%)
Free Disk: {}"""

    BUTTON_LOCK_TEXT = "Hey {query}\nThis is not for you. Search yourself."

    FORCE_SUB_TEXT = "Sorry, you have not joined my channel, so please click the join button to join my channel and try again."

    WELCOM_TEXT = """Hey {user} 💞

Welcome to {chat}.

Share & Support, request the movies you wanted"""

    FILE_MSG = """
<b>Hello 👋 {} </b>😍

<b>📫 Your File is Ready</b>

<b>📂 File Name</b> : <code>{}</code>              

<b>⚙️ File Size</b> : <b>{}</b>
"""

    CHANNEL_CAP = """
<b>Hello 👋 {}</b> 😍

<code>{}</code>

<b>Due to copyright, the file will be deleted from here in 10 minutes after moving from here to somewhere else!</b>

<b>© Powered by {}</b>
"""

    IMDB_TEMPLATE = """<b>Query: {query}</b>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a>/10
"""
