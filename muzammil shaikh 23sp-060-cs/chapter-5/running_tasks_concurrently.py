import asyncio

async def download(file):
    print(f"Downloading {file}")
    await asyncio.sleep(2)
    print(f"{file} downloaded")

async def main():
    tasks = [
        download("File1"),
        download("File2"),
        download("File3")
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())