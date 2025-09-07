import asyncio


from .zotero_mcp import zotero_mcp


async def main():
    await zotero_mcp.run_stdio_async()


if __name__ == '__main__':
    asyncio.run(main())
