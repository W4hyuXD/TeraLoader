#!usr/bin/env python3

# <--- Import Module --->
import requests
import os, time, datetime, sys, random, base64
from datetime import datetime
from time import sleep
from time import strftime
from urllib.parse import unquote
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.panel import Panel
from rich.tree import Tree
from rich import print as cihuy

console = Console()
sys.stdout.write('\x1b]2; Teraloaders | WahyuXD Downloader Terabox \x07')

# <--- Waktu --->
bulan = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10': 'October', '11': 'November', '12': 'December'}
tgl = datetime.now().day
bln = bulan[(str(datetime.now().month))]
thn = datetime.now().year
tanggal = (str(tgl)+' '+str(bln)+' '+str(thn))
waktu = strftime('%H:%M:%S')
hari = datetime.now().strftime("%A")

# <---  Warna  --->
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
N = '\x1b[0m'	# WARNA MATI
PT = '\x1b[1;97m' # PUTIH TEBAL
MT = '\x1b[1;91m' # MERAH TEBAL
HT = '\x1b[1;92m' # HIJAU TEBAL
KT = '\x1b[1;93m' # KUNING TEBAL
BT = '\x1b[1;94m' # BIRU TEBAL
UT = '\x1b[1;95m' # UNGU TEBAL
OT = '\x1b[1;96m' # BIRU MUDA TEBAL

# <!--  Warna 2  -->
Z2 = "[#FF0505]" # HITAM
mera  = "[#F00000]"
M2 = "[#AAAAAA]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00E2F5]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
M2, H2, K2, P2, B2, U2, O2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#00C8FF]", "[#AF00FF]", "[#00FFFF]"]
acak = [M2, H2, K2, B2, U2, O2, P2]
warna = random.choice(acak)
til =f"{mera}● {K2}● {H2}●"
ken = f'{mera}›{K2}›{H2}› '
tod = f' {H2}‹{K2}‹{mera}‹'

exec(base64.b64decode(b'QVBJX0tFWSA9ICIyM2E0NTM0ZmQ2bXNoNWMwYWQzNDQ5ZjBkMWM1cDEzMWM1ZWpzbjQ3NWMzODk2OWI0ZiI=='))
#API_KEY = "23a4534fd6msh5c0ad3449f0d1c5p131c5ejsn475c38969b4f"
# <--- Text Animasi --->
def ketik(s):
  for c in s + '\n':
    sys.stdout.write(c);sys.stdout.flush();time.sleep(0.1)

# <--- Banner --->
def banner():
    logo = f"""{til}
          {warna}____  ____  ____   __   __     __    __   ____  ____ 
         (_  _)(  __)(  _ \ / _\ (  )   /  \  / _\ (    \/ ___)
           )(   ) _)  )   //    \/ (_/\(  O )/    \ ) D (\___ \_
          (__) (____)(__\_)\_/\_/\____/ \__/ \_/\_/(____/(____/
                    
                [italic white][on red]Free Tools Terabox Downloader By WahyuXD.[/][/]
"""
    cihuy(Panel(logo, title=f"{ken}{P2}{hari}, {tanggal}{tod}",width=80 , style="#aaaaaa"))
    cihuy(Panel(f"[italic]{P2}Gunakan tools ini dengan bijak, Author tidak bertanggung jawab apabila tools ini disalah gunakan dan merugikan orang lain! stay positive brother.",width=80, style="#aaaaaa"))

# <--- Tampilkan Response --->
def kie_response(data, file_name):
    tree = Tree(f"[bold green]⬇ Downloading - {file_name}[/bold green]")
    if isinstance(data, dict):
        for key, value in data.items():
            tree.add(f"{P2}{key}{P2}:{H2} {value}")
    panel = Panel(tree, title=f"{ken}{A2}API Response - {file_name} to {simpan_folder}{tod}", border_style="#aaaaaa")
    cihuy(panel)

# <--- Banner --->
def get_direct_links(terabox_url):
    api_url = "https://terabox-downloader-direct-download-link-generator2.p.rapidapi.com/url"
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "terabox-downloader-direct-download-link-generator2.p.rapidapi.com"
    }
    params = {"url": terabox_url}
    ketik(f"\n   {BT}Menghubungkan ke API...")
    response = requests.get(api_url, headers=headers, params=params)
    try:
        data = response.json()
        if not data:
            cihuy("")
            cihuy(Panel.fit(f"{P2}Response kosong!",style="#aaaaaa"))
            return []
        files = []
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict):
                    direct_link = item.get("direct_link")
                    file_name = item.get("file_name")
                    if direct_link and file_name:
                        files.append((direct_link, file_name, item))
        elif isinstance(data, dict):
            direct_link = data.get("direct_link")
            file_name = data.get("file_name")
            if direct_link and file_name:
                files.append((direct_link, file_name, data))
        return files
    except Exception as e:
        cihuy(Panel.fit(f"{P2}Gagal membaca JSON: {M2}{e}",style="#FFAAAA"))
        return []

# <--- Donlot dek --->
def donlot_pile(download_url, save_path, file_info):
    kie_response(file_info, os.path.basename(save_path))
    response = requests.get(download_url, stream=True)
    total_size = int(response.headers.get("content-length", 0))
    if response.status_code == 200:
        with open(save_path, "wb") as file, Progress(
            TextColumn("[bold #00FAAE]{task.fields[filename]}[/bold #00FAAE]"),
            BarColumn(),
            TextColumn("[bold cyan]{task.percentage:.2f}%[/bold cyan]"),
            console=console
        ) as progress:
            task = progress.add_task("Download", total=total_size, filename=os.path.basename(save_path))
            for chunk in response.iter_content(1024):
                file.write(chunk)
                progress.update(task, advance=len(chunk))
        cihuy(Panel.fit(f"{P2}Download selesai: {H2}{save_path}",style="#aaaaaa"))
    else:
        cihuy(Panel.fit(f"{P2}Gagal mengunduh file!",style="#FFAAAA"))

# <--- Mlayu --->
if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    banner()
    cihuy(Panel.fit(f'{P2}Masukkan URL Teraboxnya Bang{A2}',subtitle=f'{A2}╭─{ken}{P2}(Vid/Pict){tod}',subtitle_align='left',style="#aaaaaa"))
    terabox_url = input(f"{A}   ╰─> {H}")
    cihuy(Panel.fit(f'{P2}Input folder penyimpanan file{A2}',subtitle=f'{A2}╭─{ken}{P2}(Enter = default){tod}',subtitle_align='left',style="#aaaaaa"))
    simpan_folder = input(f"{A}   ╰─> {H}")
    if not simpan_folder:
        simpan_folder = os.getcwd()
    if not os.path.exists(simpan_folder):
        os.makedirs(simpan_folder)
    files = get_direct_links(terabox_url)
    if files:
        for direct_link, file_name, file_info in files:
            file_name = unquote(file_name)
            save_path = os.path.join(simpan_folder, file_name)
            #cihuy(f"[bold magenta]Downloading: {file_name} to {simpan_folder}[/bold magenta]")
            donlot_pile(direct_link, save_path, file_info)
    else:
        cihuy(Panel.fit(f"{P2}Gagal mendapatkan direct link.",style="#FFAAAA"))