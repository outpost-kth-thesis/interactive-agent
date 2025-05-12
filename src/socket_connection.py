import asyncio
import websockets
from main import get_all_form_elements


socket_url = "wss://thesis-gateway.onrender.com"
test_url = "https://test-frontend-ssr.vercel.app/v2/v2/json"
ws = None

async def connect_and_send():
    global ws
    print("connecting to websocket")
    async with websockets.connect(socket_url) as ws:
        await ws.send("connect_client")
        response = await ws.recv()
        print("Received:", response)
        all_elements = get_all_form_elements(test_url)
        await ws.send("\n".join(map(str, all_elements)))
        response = await ws.recv()

async def main():
    await connect_and_send()


if __name__ == "__main__":
    asyncio.run(connect_and_send())
