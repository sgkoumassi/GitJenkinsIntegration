#coding:utf-8
import http.server
import socketserver
import datetime

port =89
adress=("",port)

handler=http.server.SimpleHTTPRequestHandler
httpd=socketserver.TCPServer(adress,handler)

print(f"server start at {datetime.time()} on port {port} ")
httpd.server_forever()
