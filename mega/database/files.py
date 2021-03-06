import re
from mega.database import MegaDB


class MegaFiles:
    def __init__(self):
        self.files_collection = MegaDB().db['files']

    async def insert_new_files(self, file_name: str, filed_id: str, msg_id: int, chat_id: int, url: str,
                               file_type: str):
        self.files_collection.insert_one(
            {
                "file_name": file_name,
                "file_id": filed_id,
                "msg_id": msg_id,
                "chat_id": chat_id,
                "url": url,
                "file_type": file_type
            }
        )

    async def count_files_by_url(self, url: str):
        return self.files_collection.count({"url": url})

    async def get_file_by_url(self, url: str):
        return self.files_collection.find({"url": url})

    async def get_file_by_file_id(self, file_id: str):
        return self.files_collection.find_one({"file_id": file_id})

    async def get_file_by_name(self, file_name: str):
        return self.files_collection.find({"file_name": re.compile(file_name, re.IGNORECASE)})

