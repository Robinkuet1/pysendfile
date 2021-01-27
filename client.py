import socket, tqdm, os, sys

seperator = "<#SEPERATOR#>"
buffer_size = 1024
port = 65432
while True:
	print("Your IP Adress = ",socket.gethostbyname(socket.gethostname()))
	host = input("Target ip Address: ")
	filename = input("Filepath: ")
	filesize = os.path.getsize(filename)
	
	s = socket.socket()
	
	os.system("cls")
	print(f"[+] Connecting to {host}:{port}")
	s.connect((host, port))
	print("[+ Connected.")
	
	s.send(f"{filename}{seperator}{filesize}".encode())
	
	progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	
	with open(filename, "rb") as f:
		for _ in progress:
			bytes_read = f.read(buffer_size)
			if not bytes_read:
				print("complete")
				break
			s.sendall(bytes_read)
			progress.update(len(bytes_read))
	s.close()
	print("[q] für Quit | Enter für Noch eine Datei")
	if input()=="q":
		sys.exit()