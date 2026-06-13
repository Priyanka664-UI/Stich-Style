from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import socketio
from app.config.database import create_tables, get_database
from app.config.firebase import initialize_firebase
from app.middleware.error_handler import global_exception_handler
from app.middleware.logger import RequestLoggingMiddleware

from app.api.routes import auth, users, orders, designs, payments, tailor, admin, chat, ar, content

app = FastAPI(title="Stitch & Style Backend")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception Handler
app.add_exception_handler(Exception, global_exception_handler)

# Request Logging
app.add_middleware(RequestLoggingMiddleware)

# Socket.IO
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_app = socketio.ASGIApp(sio)
app.mount("/ws", socket_app)

@app.on_event("startup")
async def startup_event():
    await create_tables()
    initialize_firebase()

@app.on_event("shutdown")
async def shutdown_event():
    # SQLAlchemy async engines handle their own cleanup typically,
    # but you could call engine.dispose() here if imported.
    pass

# Health check
@app.get("/api/health")
async def health_check(db=Depends(get_database)):
    db_status = "connected" if db is not None else "disconnected"
    return {
        "status": "online",
        "database": db_status
    }

# Register Routers
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/users", tags=["users"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(designs.router, prefix="/api/designs", tags=["designs"])
app.include_router(payments.router, prefix="/api/payments", tags=["payments"])
app.include_router(tailor.router, prefix="/api/tailor", tags=["tailor"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(ar.router, prefix="/api/ar", tags=["ar"])
app.include_router(content.router, prefix="/api/content", tags=["content"])
