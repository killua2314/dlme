# meta developer: @yourname
# scope: hikka_only
# scope: hikka_min 1.6.0

from .. import loader, utils

@loader.tds
class DeleteMyMessagesMod(loader.Module):
    """Удаляет все ваши сообщения в текущем чате"""

    strings = {
        "name": "DeleteMyMessages",
        "start": "🧹 Удаляю все ваши сообщения...",
        "done": "✅ Готово! Удалено сообщений: {}"
    }

    async def delmecmd(self, message):
        """Удалить все ваши сообщения в этом чате"""
        chat = message.chat_id
        me = await self.client.get_me()

        status = await utils.answer(message, self.strings["start"])

        count = 0
        async for msg in self.client.iter_messages(chat, from_user=me.id):
            try:
                await msg.delete()
                count += 1
            except Exception:
