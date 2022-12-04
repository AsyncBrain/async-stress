import aiohttp
import asyncio


async def main_async(host, port, uri, params=[], headers={}, sni_hostname=None):
    if sni_hostname is not None:
        print('Setting SNI server_name field ')
        #
        # THIS IS WHERE I DON'T KNOW HOW TO TELL ASYNCIO
        # TO SET THE SERVER_NAME FIELD TO sni_hostname
        # IN THE SSL SOCKET BEFORE PERFORMING THE SSL HANDSHAKE
        #
    try:
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(f'https://{host}:{port}/{uri}', params=params, headers=headers) as r:
                body = await r.read()
                print(body)
    except Exception as e:
        print(f'Exception while requesting ({e}) ')


if __name__ == "__main__":
    asyncio.run(main_async(host='s1.example.com', port=443,
                           uri='/api/some/endpoint',
                           params={'apikey': '0123456789'},
                           headers={'Host': 'load-balancer.example.com'},
                           sni_hostname='load-balancer.example.com'))
