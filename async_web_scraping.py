import aiohttp
import asyncio
import timeit

# async web scraping list of urls and looking for specific keyword

url_lst = []
message = "specific string text"

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def read_html(url):
    async with aiohttp.ClientSession() as session:
        try:
            html_txt = await fetch(session, url)
            if message in str(html_txt):
                print("found message on:", url)
        except Exception as e:
            print("cannot fetch data:", str(e))


async def gather_tasks(url_lst):
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(read_html(url)) for url in url_lst]
    await asyncio.gather(*tasks)


def main():
    if len(url_lst) > 0:
        print("number of web pages:", len(url_lst))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(gather_tasks(url_lst))



if __name__ == '__main__':
    # main()
    print(timeit.timeit(main, number=1))
