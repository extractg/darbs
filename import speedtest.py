import sys
sys.path.append("C:/Users/777/AppData/Local/Programs/Python/Python39/Lib/site-packages")
import redis

# Izveidojiet Redis klientu
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def run_speedtest():
    # Pārbauda, vai datus var iegūt no kešatmiņas
    cached_download_speed = redis_client.get('download_speed')
    cached_upload_speed = redis_client.get('upload_speed')

    if cached_download_speed and cached_upload_speed:
        print("Dati iegūti no kešatmiņas:")
        print(f"Pašreizējais lejupielādes ātrums: {cached_download_speed.decode('utf-8')} Mbps")
        print(f"Pašreizējais augšupielādes ātrums: {cached_upload_speed.decode('utf-8')} Mbps")
    else:
        # Ja nav kešatmiņas datu, izveido Speedtest objektu un veic jaunu testu
        st = speedtest.Speedtest()
        print("Veic interneta ātruma testu...")
        download_speed = st.download() / 1024 / 1024  # pārvēršam baitos megabaitos
        upload_speed = st.upload() / 1024 / 1024

        # Saglabā datus kešatmiņā uz 60 sekundēm
        redis_client.setex('download_speed', 60, download_speed)
        redis_client.setex('upload_speed', 60, upload_speed)

        print(f"Pašreizējais lejupielādes ātrums: {download_speed:.2f} Mbps")
        print(f"Pašreizējais augšupielādes ātrums: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    run_speedtest()
    