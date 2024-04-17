import speedtest

speedtester = speedtest.Speedtest()

print("Iniciando prueba de velocidad...")
download_speed = speedtester.download()
upload_speed = speedtester.upload()

print(f"Velocidad de descarga: {download_speed / 1024 / 1024:.2f} Mbps")
print(f"Velocidad de subida: {upload_speed / 1024 / 1024:.2f} Mbps")
