# meta developer: @killua2314
# scope: hikka_only
# scope: hikka_min 1.6.0

from .. import loader, utils

@loader.tds
class DeleteMyMessagesMod(loader.Module):
    """Удаляет ваши сообщения: весь чат или текущий топик"""

    strings = {
        "name": "DeleteMyMessages",
        "start_all": "🧹 Удаляю все ваши сообщения в чате...",
        "start_topic": "🧹 Удаляю ваши сообщения в этом топике...",
        "done": "✅ Готово! Удалено сообщений: {}",
        "no_topic": "⚠️ В этом чате нет топика."
    }

    async def delmecmd(self, message):
        """Удалить все ваши сообщения во всём чате"""
        chat = message.chat_id
        me = await self.client.get_me()

        status = await utils.answer(message, self.strings["start_all"])

        count = 0
        async for msg in self.client.iter_messages(chat, from_user=me.id):
            try:
                await msg.delete()
                count += 1
            except Exception:
                continue

        await status.edit(self.strings["done"].format(count))

    async def delmetopiccmd(self, message):
        """Удалить все ваши сообщения только в текущем топике"""
        chat = message.chat_id
        # Берём ID текущего топика
        topic_id = getattr(message, "message_thread_id", None)

        if not topic_id:
            await utils.answer(message, self.strings["no_topic"])
            return

        me = await self.client.get_me()
        status = await utils.answer(message, self.strings["start_topic"])

        count = 0
        async for msg in self.client.iter_messages(chat, from_user=me.id):
            try:
                if getattr(msg, "message_thread_id", None) == topic_id:
                    await msg.delete()
                    count += 1
            except Exception:
                continue

        await status.edit(self.strings["done"].format(count))
