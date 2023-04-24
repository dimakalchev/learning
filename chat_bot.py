# import logging
# import os
# import telegram
# from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
# import requests
#
# # Set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.DEBUG)
#
# # Set up ChatGPT API endpoint
# CHATGPT_API_URL = 'https://chat.openai.com'
#
# # Telegram bot token
# TOKEN = '5857712441:AAEiAT3bljNvUlCXGZkXy_bXUbyPVIrhInA'
# API_KEY = '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'
#
# # Check if API key is available
# if not API_KEY:
#     logging.error('API key not found. Please set the CHATGPT_API_KEY environment variable.')
#     exit(1)
#
# # Handler for /start command
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text='Welcome to ChatGPT Bot! Send me a message and I will respond with the help of ChatGPT.')
#
#
# # Handler for incoming messages
# def message(update, context):
#     # Get user input
#     user_input = update.message.text
#
#     # Call ChatGPT API to generate response
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {API_KEY}'
#     }
#     data = {
#         'prompt': user_input,
#         'max_tokens': 50
#     }
#     try:
#         response = requests.post(CHATGPT_API_URL, headers=headers, json=data)
#         if response.status_code == 200:
#             # Extract generated text from response
#             generated_text = response.json()['choices'][0]['text']
#             # Send the generated text as a reply
#             context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text)
#         else:
#             context.bot.send_message(chat_id=update.effective_chat.id, text='Failed to generate response.')
#     except Exception as e:
#         logging.error(f'Error generating response: {e}')
#         context.bot.send_message(chat_id=update.effective_chat.id, text='Failed to generate response.')
#
# # Create the Telegram bot
# updater = Updater(token=TOKEN, use_context=True)
#
# # Add handlers
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(MessageHandler(Filters.text, message))
#
# # Start the bot
# updater.start_polling()
# updater.idle()



import logging
import os
import telegram
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import requests

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

# Set up ChatGPT API endpoint
CHATGPT_API_URL = 'https://chat.openai.com'

# Telegram bot token
TOKEN = '5857712441:AAEiAT3bljNvUlCXGZkXy_bXUbyPVIrhInA'
API_KEY = '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'

# Check if API key is available
if not API_KEY:
    logging.error('API key not found. Please set the CHATGPT_API_KEY environment variable.')
    exit(1)

# Handler for /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Welcome to ChatGPT Bot! Send me a message and I will respond with the help of ChatGPT.')


# Handler for incoming messages
def message(update, context):
    # Get user input
    user_input = update.message.text

    # Call ChatGPT API to generate response
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    data = {
        'prompt': user_input,
        'max_tokens': 50
    }
    try:
        response = requests.post(CHATGPT_API_URL, headers=headers, json=data)
        logging.debug(f'Response status code: {response.status_code}')
        logging.debug(f'Response content: {response.content}')
        if response.status_code == 200:
            response_json = response.json()
            if 'choices' in response_json and len(response_json['choices']) > 0:
                # Extract generated text from response
                generated_text = response_json['choices'][0]['text']
                # Send the generated text as a reply
                context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text)
            else:
                logging.error('Failed to generate response. Response does not contain the expected JSON structure.')
                context.bot.send_message(chat_id=update.effective_chat.id, text='Failed to generate response.')
        else:
            logging.error('Failed to generate response. Response status code is not 200.')
            context.bot.send_message(chat_id=update.effective_chat.id, text='Failed to generate response.')
    except Exception as e:
        logging.error(f'Error generating response: {e}')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Failed to generate response.')

# Create the Telegram bot
updater = Updater(token=TOKEN, use_context=True)

# Add handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message))

# Start the bot
updater.start_polling()
updater.idle()
