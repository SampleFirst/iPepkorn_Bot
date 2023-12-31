from pyrogram import Client, filters
from pyrogram.types import *
from aiohttp import ClientSession
from telegraph import upload_file
from io import BytesIO
from info import LOG_CHANNEL, UPDATE_CHANNEL

# Define a set to keep track of banned users
banned_users = set()

ai_client = ClientSession()

async def make_carbon(code, tele=False):
    url = "https://carbonara.solopov.dev/api/cook"
    async with ai_client.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    if tele:
        uf = upload_file(image)
        image.close()
        return f"https://graph.org{uf[0]}"
    return image


@Client.on_message(filters.command("carbon"))
async def carbon_function(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Please reply to a message with text.")
    if not message.reply_to_message.text:
        return await message.reply_text("The replied message must be text.")
    user_id = message.from_user.id
    m = await message.reply_text("Generating carbon image...")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("Uploading carbon image...")
    await client.send_photo(
        chat_id=LOG_CHANNEL,
        photo=carbon,
        caption=f"Carbon image generated by\n\nUser Name: {message.from_user.first_name} \nUser ID: {user_id}",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Ban Carbon: {message.from_user.first_name}", callback_data=f"ban_{user_id}")
                    ]
                ]
            ),
        )
    await message.reply_photo(
        photo=carbon,
        caption=f"Hey, {message.from_user.first_name}! Carbon image generated",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Support us", url=UPDATE_CHANNEL)
                ]
            ]
        ),
    )
    await m.delete()
    carbon.close()

@Client.on_callback_query(filters.regex(r'^ban_'))
async def ban_carbon_user(client, query):
    # Extract the user ID from the callback data
    user_id = int(query.data.split("_")[1])

    if user_id not in banned_users:
        banned_users.add(user_id)
        await query.answer("User has been banned from generating Carbon images.")
    else:
        await query.answer("User is already banned from generating Carbon images.")
