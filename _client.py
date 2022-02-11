# import socketio
# import os
# import subprocess
# import time


# sio = socketio.Client()
# sio.connect('http://localhost:8080')
# print('my sid is', sio.sid)

# @sio.event
# def connect():
#     sio.connect('http://localhost:8080')
#     print('my sid is', sio.sid)
#     print("I'm connected!")
#     #message()
    
# #sio.emit('message','timelapse')

# @sio.event
# def on_message(data):
#     print('I received a message1!')
# #sio.emit('message', 'toserver')
# @sio.event
# def message(data):
#     #sio.emit('message','mtto.png', room='chat_users', skip_sid=sio.sid)
#     print(os.getcwd())
#     #os.system('cd C:/Users/murrutiam/Desktop/apk/scada/ && run.cmd')
#     #os.system('echo ifconfig')
#     #os.system('npm run dev')
#     #cmd = 'cd C:/Users/murrutiam/Desktop/apk/scada/ && npm run dev'
#     #os.popen('cd C:/Users/murrutiam/Desktop/apk/scada/ && npm run dev')
    
#     #time.sleep(30)
#     print(data,'*-*')
#     return
    
    
# @sio.on('screenshot')
# def catch_all(data):
#     print(data,"**")
#     directorio = os.getcwd()
#     with open('../../scada/src/public/scada1.png', 'rb') as f:
#         image_data = f.read()
#     sio.emit('remote', {'image_data': image_data})
#     pass



# @sio.event
# def connect_error(data):
#     print("The connection failed!3")

# @sio.event
# def disconnect():
#     print("I'm disconnected4!")

# #connect()
# #message('hola mundo')
# #sio.disconnect()
