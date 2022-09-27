import asyncio

from get_english_word_list import get_english_word_list_contents_from_url

vals = []


async def get_some_values_from_io():
    return get_english_word_list_contents_from_url().split('\n')


async def fetcher():
    io_vals = await get_some_values_from_io()
    print('got io vals', io_vals[0])

    for val in io_vals:
        vals.append(val)
        await asyncio.sleep(0.000001)


async def monitor():
    last_word = None
    while True:
        if vals:
            if last_word == vals[-1]:
                break
            last_word = vals[-1]

        print(len(vals))
        await asyncio.sleep(0.2)


async def main():
    await asyncio.gather(fetcher(), monitor())


asyncio.run(main())
