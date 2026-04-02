import websockets
import asyncio
import datetime
import json
url = "ws://localhost:8765"

class TaskManager():
    def __init__(self):
        self.tasks_in_progress = set()
        self.queue_tasks = asyncio.Queue()
        self.running = True
        self.id_response = {}

    async def add_task(self, function, id_task, *args):
        self.task_info = {"function": function, "id_task": id_task, "params": args}
        await self.queue_tasks.put(self.task_info)

    async def start_tasks(self, websocket):
        await asyncio.gather(self.process_task(),
                             self.get_response(websocket))

    async def process_task(self):
        while self.running:
            task_info = await self.queue_tasks.get()
            function = task_info["function"]
            #id_task = task_info["id_task"]
            params = task_info["params"]
            task = asyncio.create_task(function(*params))
            self.tasks_in_progress.add(task)
            task.add_done_callback(lambda x: self.remove_task(x))

    async def get_response(self, websocket):
        async for response in websocket:
            self.id_response[response["id"]] = response["response"]

    async def remove_task(self, task):
        if task in self.tasks_in_progress:
            self.tasks_in_progress.remove(task)



class Client:
    def __init__(self):
        self.temp_id = "" #временный id
        self.user_id = "" # @nickname



    async def connect(self):
        async with websockets.connect(url) as websocket:
            try:
                await websocket.send()
            except Exception as e:
                print(e)

if __name__ == "__main__":
    client = Client()
    asyncio.run(client.connect())