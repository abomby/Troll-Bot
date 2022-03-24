from get_service import get_service
from process_msg import get_msg_info
from create_message import create_message
from send_message import send_message



if __name__ == '__main__':
    service = get_service()
    user_id = 'me'
    unread_msgs = get_msg_info(service, user_id)

    for i in range(0,len(unread_msgs)):

        sender = 'kejiabao3@gmail.com'
        message_i = unread_msgs[i]
        thread_Id = message_i['thread_Id']
        to = message_i['from']
        subject = message_i['subject']
        message_text = 'I have effectively set up a reply bot'


        message = create_message(sender, to, subject, message_text, thread_Id)


        send_message(service, user_id, message)
        print('Job Complete')