class Message_Template:
	def __init__(
		self, 
		chat_id, 
		text,

		disable_web_page_preview=None,
		reply_to_message_id=None, 
		reply_markup=None,
		parse_mode=None, 
		disable_notification=None, 
		timeout=None
	):

		self.chat_id = chat_id
		self.text = text
		self.disable_web_page_preview = disable_web_page_preview
		self.reply_to_message_id = reply_to_message_id
		self.parse_mode = parse_mode
		self.disable_notification = disable_notification
		self.timeout = timeout
