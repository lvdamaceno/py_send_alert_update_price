import pymssql
import os
import variables as v
from twilio.rest import Client


def connect():
    conn = pymssql.connect(v.SERVER_NAME, v.USER, v.PSSWD, v.DATABASE)
    return conn


def send_alert_whatsapp(alert):
    account_sid = v.TW_SID
    auth_token = v.TW_TKN
    client = Client(account_sid, auth_token)
    for contact in v.CONTACTS:
        message = client.messages.create(body=alert, from_=f'whatsapp:{v.SENDER}', to=f'whatsapp:{contact}')
        print(message.sid)


def execute_query(query):
    conn = connect()
    conn.cursor(as_dict=True)
    cursor = conn.cursor()
    cursor.execute(query)
    for row in cursor:
        print("Produto atualizado: %s" % row[0])
        send_alert_whatsapp("Produto atualizado: %s" % row[0])
    conn.close()


execute_query(v.QUERY)
