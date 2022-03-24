from read_email import get_messages, get_message


def get_msg_info(service, user_id):

    msg_info = []

    messages = get_messages(service, user_id)['messages']

    for i in range (0,len(messages)):
        msg_i_info = {}

        message_data = messages[i]
        msg_id = message_data['id']
        thread_id = message_data['threadId']

        read_message = get_message(service, user_id, msg_id)

        payload = read_message['payload']
        headers = payload['headers']
        from_info = headers[5]
        subject_info = headers[6]
        from_value = from_info['value']
        subject_value = subject_info['value']

        if 'UNREAD' in read_message['labelIds']:

            msg_i_info['id'] = msg_id
            msg_i_info['thread_Id'] = thread_id
            msg_i_info['subject'] = subject_value
            msg_i_info['from'] = from_value
            msg_i_info['body'] = read_message['snippet']
            msg_i_info['date'] = read_message['payload']['headers'][1]['value']

            msg_info.append(msg_i_info)


        

    return msg_info








    