import json
import subprocess
import os
import time
import requests


def terminate(processname):
    os.system('taskkill /IM "' + processname + '" /F')


def send_sni(server_ip, sni):
    url = f'http://{server_ip}:33333/'  # Replace with the actual IP address of the server
    response = requests.post(url, data=sni)
    if response.status_code == 200:
        print(f"sent {sni} to server successfully")
    else:
        print("something doesnt add up, check your stuff")


def make_new_conf(server_ip, sni):
    with open("client.json", 'r') as file:
        data = json.load(file)

    # Replace the "serverName" field with "TEXT"
    data['outbounds'][0]['settings']['vnext'][0]['address'] = server_ip
    data['outbounds'][0]['streamSettings']['realitySettings']['serverName'] = sni

    with open("client.json", 'w') as file:
        json.dump(data, file, indent=2)


def read_domains(input_file):
    with open(f"{input_file}.txt", "r") as f:
        file = [a.replace("\n", "") for a in f.readlines()]
    return file


def run_xray(config):
    command = f'.\\xray.exe -c .\\{config}'
    subprocess.Popen(command, shell=True)


def upload_speed_test(timeout):
    proxies = dict(
        http=f"socks5://127.0.0.1:6565",
        https=f"socks5://127.0.0.1:6565"
    )
    n_bytes = 500 * 1000 * 2
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

    mb = n_bytes * 8 / (10 ** 6)
    upload_speed = mb / cf_time
    up_speed = upload_speed / 8 * 1000
    return up_speed, latency


def close_xray():
    terminate("xray.exe")


if __name__ == "__main__":
    server_ip = input("whats your server ip? ").strip()
    sni_file = input("whats your sni file name, only name not extension (for domain.txt type only domain)? ").strip()
    domains = read_domains(sni_file)
    with open("output_results.txt", "w") as f:
        f.write("domain,speed,latency\n")
    for domain in domains:
        # sni = f"www.{domain}" if domain.count("w") < 3 else domain
        sni = domain
        send_sni(server_ip, sni)
        make_new_conf(server_ip, sni)
        run_xray("client.json")
        try:
            upload_speed, latency = upload_speed_test(4)  # timeout is 4 Seconds, change based on ur internet.
            print(f"upload speed is {upload_speed:.2f} KB/s and Latency is {latency:.2f} ms")
            with open("output_results.txt", "a+") as f:
                f.write(f"{sni},{upload_speed:.2f},{latency:.2f}\n")
        except:
            with open("output_results.txt", "a+") as f:
                f.write(f"{sni},-,-\n")
            print(f"{sni} failed")
        time.sleep(0.5)
        close_xray()
