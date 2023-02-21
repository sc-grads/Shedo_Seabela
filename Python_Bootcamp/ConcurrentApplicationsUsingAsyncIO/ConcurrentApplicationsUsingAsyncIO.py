import asyncio

async def run(cmd):

    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()


    print(f'{cmd} exited with status code: {proc.returncode}]')

    if stdout:
        print(f'STDOUT:\n{stdout.decode()}')

    if stderr:
        print(f'STDERROR:\n{stderr.decode()}')



async def main(commads):
    tasks = []
    for cmd in commads:
        tasks.append(run(cmd))

    await asyncio.gather(*tasks)


commands = ('ifconfig', 'ls', 'who', 'ping -c 1 8.8.8.8')
asyncio.run(main(commands))