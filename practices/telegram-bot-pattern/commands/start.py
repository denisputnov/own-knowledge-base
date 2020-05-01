from commands.message_template import Message_Template

DISABLE_WEB_PAGE_PREVIEW = None # True or False
REPLY_TO_MESSAGE_ID = None
DISABLE_NOTIFICATION = None 
PARSE_MODE = 'html'

COMMAND_TEXT = 'Привет, это стартовая команда!'


REPLY_MARKUP = None


def construct_message(message_chat_id):
	message = Message_Template(
			chat_id = message_chat_id,
			text = COMMAND_TEXT, 

			disable_web_page_preview=DISABLE_WEB_PAGE_PREVIEW,
			reply_to_message_id=REPLY_TO_MESSAGE_ID, 
			reply_markup=REPLY_MARKUP,
			parse_mode=PARSE_MODE, 
			disable_notification=DISABLE_NOTIFICATION, 
			timeout=None
		)
	return message
