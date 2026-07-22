import redbot


class MemberList(redbot.Cog):
    """Outputs all member IDs for the server."""

    def __init__(self, bot):
        super().__init__(bot)

    @redbot.commands.command()
    async def memberids(self, ctx):
        """List all member IDs in the server."""
        guild = ctx.guild
        member_ids = [str(m.id) async for m in guild.members]
        total = len(member_ids)

        if total == 0:
            await ctx.send("No members found.")
            return

        chunk_size = 60
        for i in range(0, total, chunk_size):
            chunk = member_ids[i : i + chunk_size]
            text = f"**{guild.name}** — `{i + 1}-{min(i + chunk_size, total)}/{total}`\n"
            text += "\n".join(f"`{idx}`" for idx in chunk)
            await ctx.send(text)

    @redbot.commands.command()
    async def memberinfo(self, ctx):
        """List all members with IDs and usernames."""
        guild = ctx.guild
        members = [(m.id, str(m.display_name), str(m)) async for m in guild.members]
        total = len(members)

        if total == 0:
            await ctx.send("No members found.")
            return

        chunk_size = 40
        for i in range(0, total, chunk_size):
            chunk = members[i : i + chunk_size]
            text = f"**{guild.name}** — `{i + 1}-{min(i + chunk_size, total)}/{total}`\n"
            for uid, display, full in chunk:
                text += f"`{uid}` {display} ({full})\n"
            await ctx.send(text)
