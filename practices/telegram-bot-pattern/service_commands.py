"""
Module description. What's it need for and how we can use it.
"""



def get_server_data():
	"""
	get_server_data(params=None)

	return dictionary {'time': serverTime,'date': serverDate}
	"""
	pass


def get_new_data():
	"""
	get_new_data(params=None)
	
	User 	modulename.py    and make dictionary with data

	return data, that need for bot work. For example, it's music decription or author name
		best way to checkout it - local dictionary 
	"""
	pass


def get_users_list():
	"""
	get_users_list(params=None)

	return all user identificators from    file-/database-name    as list.
	"""
	pass


def get_followers_amount():
	"""
	get_followers_amount(params=None)
    
	return len(get_users_list(params=None))
	"""

def add_user_to_users_list(message_from_user_id):
	"""
	add_user_to_users_list(message_from_user_id)
	
	Add user to 	file-/database-name
	message_from_user_id: id of user, that used ***/sub*** command.
	
	Use    get_users_list(params=None)    function to get a list of users.

	if user is already in    file-/database-name:
		return False

	if user was sucsessfully added to    file-/database-name:
		return True
	"""

def del_user_from_users_list(message_from_user_id):
	"""
	del_user_from_users_list(message_from_user_id)

	Delete user from    users.txt
	message_from_user_id: id of user, that used ***/unfollow*** command.

	Use    get_users_list(params=None)    function to get a list of users.

	if user wasn't found in    ufile-/database-name:
		return False

	if user was sucsessfully delited from    file-/database-name:
		return True
	"""
