from send_message import send_message
from create_message import create_message
from get_service import get_service


if __name__ == '__main__':
    service = get_service()
    sender = 'kejiabao3@gmail.com'
    to = 'yadu.reddy@gmail.com'
    subject = 'Poop on vs code'
    message_text = 'donkey likes waffles'


    user_id = 'me'

    message = create_message(sender, to, subject, message_text)


    send_message(service, user_id, message)
    print('Job Complete')