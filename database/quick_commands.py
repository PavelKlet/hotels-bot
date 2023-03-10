from database.user import User


async def add_user_info(user_id: int, hotels: str, command: str, datet: str):

    user = User(user_id=user_id, hotels=hotels, command=command, date=datet)
    await user.create()


async def select_user(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.all()
    return user

