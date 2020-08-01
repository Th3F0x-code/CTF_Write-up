import os
import subprocess

filetypes = ['xz', 'zip', 'bzip', 'gzip']
os.system("mkdir trash")
while True:
    x = subprocess.check_output('ls', shell=True).decode().split('\n')[0]
    print(x)

    y = subprocess.check_output(f'file {x}', shell=True).decode()
    print(y)

    if 'gzip' in y:
        if not x.endswith('.gz'):
            os.system(f'mv {x} {x}.gz')
            x = f'{x}.gz'
        os.system(f'gunzip {x}')
        print('Uncompressed gzip')

    if 'XZ' in y:
        if not x.endswith('.xz'):
            os.system(f'mv {x} {x}.xz')
            x = f'{x}.xz'
        os.system(f'unxz {x}')
        print('Uncompressed xz')

    if 'bzip2' in y:
        if not x.endswith('.bz2'):
            os.system(f'mv {x} {x}.bz2')
            x = f'{x}.bz2'
        os.system(f'bzip2 -d {x}')
        print('Uncompressed bz2')

    if 'Zip' in y:
        if not x.endswith('.zip'):
            os.system(f'mv {x} {x}.zip')
            x = f'{x}.zip'
        os.system(f'unzip {x}')
        print('Uncompressed zip')
        os.system(f'mv {x} trash/{x}')

    if 'ASCII' in y:
        os.system(f'cat {x}')
        break

# FLAG --> flag{the_answer_is_1548_licks}
