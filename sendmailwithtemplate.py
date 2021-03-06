from flask import make_response, jsonify
from mail.flask_mail import flask_template_email
from auth import token_required


@token_required
def sendemail_with_template(mail_object):
    """
    This function sends email to subscriber/subscribers
    :param people:  person/people to send email to
    :return:        201 on success, 400 on error
    """
    if mail_object is not None:
        sender = mail_object.get('sender')
        subject = mail_object.get('subject')
        recipient = mail_object.get('recipient')
        body = mail_object.get('htmlbody')
        bcc = mail_object.get('bcc')
        cc = mail_object.get('cc')
        
        if recipient == '' or body == '' or subject == '' or recipient == 'string' or body == 'string' or subject == 'string':
            response = {
                'status': 'error',
                'data':{
                    'message': 'Error: subject, recipient, htmlbody fields are required.'
                }
            }
            return make_response(jsonify(response), 400)
        else:
            body = '<strong>' + body + '</strong>'
            json_response = flask_template_email(recipient, subject, body, cc, bcc)
            return json_response
