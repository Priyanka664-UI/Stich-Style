# Socket.IO handlers should be registered here.
# Since we mount Socket.IO in main.py, we can define events here.

def register_socket_events(sio):
    @sio.event
    async def connect(sid, environ):
        print(f"Client connected: {sid}")

    @sio.event
    async def disconnect(sid):
        print(f"Client disconnected: {sid}")
