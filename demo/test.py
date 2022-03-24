from read_email import get_messages, get_message
from get_service import get_service
from process_msg import get_msg_info


service = get_service()
user_id = 'me'

info = get_msg_info(service, user_id)

print(info)
