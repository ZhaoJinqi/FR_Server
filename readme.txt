This is an API server for face detection
The main code files are FR_API.py and facedetect.py.
And test.py is the code file that tests the API server.

Note:
1.The IP address in the test.py file needs to be changed. If the server is running on the local computer, the IP address needs to be changed to the IP of your own computer. If the server IP has been deployed on another computer or remote host, the IP address needs to be changed to the address of the remote host.
2.list, for example, like [221, 33, 54, 54], means [top, left, width, height]. It shows the relative position of a face in the picture.