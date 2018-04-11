# Morabaraba-2 recreated in python

				  ___  ___                _                     _           
				  |  \/  |               | |                   | |          
				  | .  . | ___  _ __ __ _| |__   __ _ _ __ __ _| |__   __ _ 
				  | |\/| |/ _ \| '__/ _` | '_ \ / _` | '__/ _` | '_ \ / _` |
				  | |  | | (_) | | | (_| | |_) | (_| | | | (_| | |_) | (_| |
				  \_|  |_/\___/|_|  \__,_|_.__/ \__,_|_|  \__,_|_.__/ \__,_|

Basic game rules can be found here: https://en.wikipedia.org/wiki/Morabaraba

This game can either be played locally (with both players on the same computer) or on a server:
  -	To play locally, simply run client.py where you'll be asked if you want to play locally. Enter Y for yes.
  -	To play on a server, the server computer needs to run the server.py program (which will display the server's IP). Then on the 
	client computers run client.py where you'll be asked if you want to play locally- simply enter N for no. You'll then be prompted
	to enter the server's IP address (it's already displayed on the server's screen so simply enter that in).

If playing on a server that is not on your local network. You need to follow these instructions:
- For the server:
	1)	Enable port forwarding on your router of the server computer (use the port the server says it's open on)
	2)	Use the TCP/IP protocol for the port forwarding
- For the client:
	1)	Use the IP address of the server's router and not the server's local IP
