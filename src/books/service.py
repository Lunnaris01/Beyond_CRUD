from sqlmodel.ext.asyncio.session import AsyncSession

class BookService:
    async def get_all_books(self, session:AsyncSession):
        pass
    
	async def get_book(self, book_uid:str, session:AsyncSession):
		pass
    async def add_book(self, session:AsyncSession):
        pass
    async def update_book(self, session:AsyncSession):
        pass
    async def get_all_books(self, session:AsyncSession):
        pass
