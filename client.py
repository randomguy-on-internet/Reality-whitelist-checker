import json
import subprocess
import os
import time
import requests
from requests.exceptions import ReadTimeout


def terminate(processname):
    os.system('taskkill /IM "' + processname + '" /F')


def send_sni(server_ip, sni , port, proxy=False):
    url = f'http://{server_ip}:33333/'  # Replace with the actual IP address of the server
    proxy_url = f'127.0.0.1:{port}'  # Replace with the actual proxy address and port of your nekoray

    proxies = {
        'http': proxy_url
    }
    
    response = requests.post(url, data=sni, proxies=proxies) if proxy else requests.post(url, data=sni)
    
    if response.status_code == 200:
        print(f"\n***********\nsent {sni} to server successfully\n***********\n")
    else:
        print("something doesnt add up, check your internet or the server!\n you can add a proxy to nekoray and try again")


def make_new_conf(server_ip, sni):
    with open("client.json", 'r') as file:
        data = json.load(file)

    data['outbounds'][0]['settings']['vnext'][0]['address'] = server_ip
    data['outbounds'][0]['streamSettings']['realitySettings']['serverName'] = sni

    with open("client.json", 'w') as file:
        json.dump(data, file, indent=2)


def read_domains(input_file):
    with open(f"{input_file}.txt", "r") as f:
        file = [a.replace("\n", "") for a in f.readlines()]
        file = [f"www.{a}" if a.count(".") == 1 else a for a in file]
    return file


def run_xray(config):
    command = f'.\\xray.exe -c .\\{config}'
    subprocess.Popen(command, shell=True)


# borrowed this from cfscanner :)
# u_size is upload file size in MB, default is 1 MB
def upload_speed_test(timeout, u_size = 1):
    proxies = dict(
        http=f"socks5://127.0.0.1:6565",
        https=f"socks5://127.0.0.1:6565"
    )
    n_bytes = round(u_size * 1000 / 16) * 1000 * 2
    start_time = time.perf_counter()
    r = requests.post(
        url="https://speed.cloudflare.com/__up",
        data="0" * n_bytes,
        timeout=timeout,
        proxies=proxies
    )
    total_time = time.perf_counter() - start_time
    cf_time = float(r.headers.get("Server-Timing").split("=")[1]) / 1000
    latency = total_time - cf_time

    mb = n_bytes * 8 / (10 ** 6)  # (80 * 2 * 8) / 1000 = 1.28 MB upload size
    upload_speed = mb / cf_time
    up_speed = upload_speed / 8 * 1000
    return up_speed, latency


def close_xray():
    terminate("xray.exe")


def is_process_running(process_name):
    try:
        output = subprocess.check_output(["tasklist", "/NH", "/FO", "CSV"]).decode('utf-8')
        lines = output.strip().split('\n')
        for line in lines:
            if process_name in line:
                return True
        return False
    except subprocess.CalledProcessError:
        # Handle errors when executing the tasklist command
        return False


def min_time_out(proxy_port, proxy=False):
    sni = "www.ghbi.ir"
    if is_process_running('xray.exe'):
        print("close v2rayN app")
        close_xray()
    send_sni(server_ip, sni,proxy_port ,bool(proxy_port))
    make_new_conf(server_ip, sni)
    run_xray("client.json")
    for i in range(1, 6):
        try:
            upload_speed_test(i, 2)
            print(f"\n********\nYour Timeout is {i} Seconds\n********\n")
            close_xray()
            return i
        except ReadTimeout:
            pass
        except Exception as e:
            print(e)
            pass
    return 2


if __name__ == "__main__":
    server_ip = input("whats your server ip?\n Your IP: ").strip()
    use_proxy = input("do you want to use proxy to send sni to server? y/n? ").strip()
    if use_proxy == "y" or use_proxy == "n":
        pass
    else:
        print("only y or n")
        exit()
    proxy_port = int(input("proxy port? port:").strip()) if use_proxy == "y" else None
    sni_file = input(
        f"whats your sni file name, only name not extension (for domain.txt type only domain)?\nfile name: "
        f"").strip()
    
    domains = read_domains(sni_file)
    time_out = min_time_out(proxy_port,proxy=bool(proxy_port))
    
    send_sni(server_ip, ",".join(domains),proxy_port,proxy=bool(proxy_port))
    
    with open("output_results.txt", "w") as f:
        f.write("domain, upload_speed, latency,.\n")

    for domain in domains:
        sni = domain
        make_new_conf(server_ip, sni)
        if is_process_running('xray.exe'):
            print("close v2rayN app")
            close_xray()
        run_xray("client.json")
        try:
            upload_speed, latency = upload_speed_test(time_out)
            print(f"\n++++++++\nupload speed is {upload_speed:.2f} KB/s and Latency is {latency:.2f} ms\n++++++++")
            with open("output_results.txt", "a+") as f:
                f.write(f"{sni}, {upload_speed:.2f}, {latency:.2f}\n")
        except ReadTimeout as e:
            with open("output_results.txt", "a+") as f:
                f.write(f"{sni}, -, -\n")
            print(f"\n\n{sni} failed\n\n")
        except Exception as e:
            with open("output_results.txt", "a+") as f:
                f.write(f"{sni}, -, -\n")
            print(
                f"\n\n*** ERROR *** \n{e}\n\n There is an error in running the program, maybe google it or open an "
                f"issue with this Error message or Ignore it :) ")
        time.sleep(0.05)
        close_xray()
