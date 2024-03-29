# Ethical Hacking(Basic) using Socket Programming
<p align="center">
  <img src = "images/ethical_hacker.jpg" />
</p>

Hi there fellows. In this post I am going to take you on an adventure with python sockets. They are the real backbones behind web browsing. In simpler terms there is a server and a client. We will deal with both of them,let's first explore some keyworkds related
to Socket Programming. So lets first begin by seeing what exactly is a Socket.

## Socket
Spcket is one of the endpoint of two-way connection link between two programs running on the network. A socket is bound to a port
number so that TCP layer can identify the application to which the data is destined to be. An endpoint is a combination of IP 
address and port number.

## IP Address
It is an unique set of strings separated by full stops('.') such that two computer systems can communicate with each other using Internet
Protocol over the network. 
They are of two types:
```
                                                IP
                                              `    `
                                             `      `
                                            `        `
                                          Public    Private 
```
## Public IP
It is the IP address provided by the Internet Service Provider(ISP) like Jio, Vodaphone, Idea, Airtel

## Private IP
It is the IP address which is provided by different routers or wifi

### To check your IP address of the system type following command on terminal/command prompt
#### For Windows
``` ipconfig ```

#### For Linux/Mac
``` ifconfig ```

### To see IP address of any website like Google, Facebook etc...
#### Type following on your terminal/command prompt
``` ping facebook.com ```

``` ping google.com ```

### IP Address also classified into
```
                                                IP
                                              `    `
                                             `      `
                                            `        `
                                          Static    Dynamic 
```
### Static IP
These are the IP address of the servers or websites like IP address of Google is 172.217.163.174 and of facebook is 157.240.192.35
These are same throughout the same country but can change from country to country.

### Dynamic IP
Thses are the category of IP address which changes frequently
If you see your IP address using "ipconfig" and if you restart your system and you see that the IP is changed this time.

### Difference between IP and Port number
We can understand this difference better using an analogy
IP address is nothing but the address of the city or street while Port number is the address of out house in which we are living

suppose we are using Skype & Netflix in our system then how TCP layer will know to whom it has to deliver the data i.e. to which application(whether Skype or Netflix) it has to deliver a particular data, so using port number it can distinguish between one or more application where the data is to be delivered.  

### Finding Port number 
First open your command prompt and run as admininstrator and type the followng command on cmd/terminal
``` netstat -a -b -n ```
<p align="center">
  <img src = "images/IMG20190903194406.jpg" />
  <img src = "images/IMG20190903194432.jpg" />
</p>

### Server
Let me explain a little bit about a server. A server has a bind() method which binds it to a specific IP and port so that it can
listen to incoming requests on that IP and port. Next a server has a listen() method which puts the server into listen mode. This allows the server to listen to incoming connections. And lastly a server has an accept() and close() method. The accept method initiates a connection with the client and the close method closes the connection with the client.

### How does Socket works

<p align="center">
  <img src = "images/socket.png" />
</p>

### Commands for creating Sockets and communicate with other systems

` socket.socket(socket.AF_INET, socket.SOCK_STREAM) `

Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address family ipv4. ipv6 requires something different but we won’t be focusing on it. Secondly the SOCK_STREAM means connection oriented TCP protocol. Client will connect to a server using this socket.

Using the above command as a socket is created now we have to bind this socket to an IP address as well as a port number which can be
done using

`socket.bind(host, port)`

After binding the socket we will send the data to the client using the command

`socket.send()`

After this, the client will be sending the data so we will be listening it with the comamnd and will receive the data sent by the client

```socket.listen()```

```socket.recv()```

If conversation is over then we can close the connection using the command

`socket.close()`

All the steps are:
  - socket.socket()
  - socket.bind(host, port)
  - socket.send()
  - socket.listen()
  - socket.recv()
  - socket.close()
  
## How to connect with other System using Socket programming

There are two ways
```                                             
                                          ------|------- 
                                         |              |
                                      Direct        Reverse(used by Hackers)
```

### Direct Connection
Suppose if you are in a city and you want to help your friend who is from non technical backround and livingin another city then you
can easily connect to his/her system remotely using Socket Programming.
  - Create a [Serve.py](https://github.com/kampaitees/Ethical-Hacking-using-Socket-Programming/blob/master/Single%20Client(Reverse%20shell%20V1)/server.py) file
  - Create a [Client.py](https://github.com/kampaitees/Ethical-Hacking-using-Socket-Programming/blob/master/Single%20Client(Reverse%20shell%20V1)/client.py) file

If you open the client.py file then in the host part you have enter the IP address of your friend's system and run both of them.
And you will be able to easily access your friend's system

#### Drawback of this connection
  - It may be difficult to get the IP address of victim's system 
  - Somehow, you got the IP address then again all your efforts may go in vain because as other than servers and websites IP address
    are dynamic they will change if victim will restart his/her system and all your efforts may go in vain.
  - Even if you get regular updates to dynamic IP address of victim's system, the computer has bunch of firewall which makes it             impossible to get to his/her system.
  
### Reverse Connection
Mainly used by the hackers for hacking. Here the name itself suggests that the connection is established by the hacke first via some
messages through mail or some other way. When you will click the messages sent by the hackers then a file will be downloaded in your
system which is nothing but the [Client.py](https://github.com/kampaitees/Ethical-Hacking-using-Socket-Programming/blob/master/Single%20Client(Reverse%20shell%20V1)/client.py) file. 
So one of the problem of direct connection is solved by this file i.e. problem of dynamic IP. As file is always there in your system
whenever you will start your system that file will be sending the IP address of your system and hacker can easily access your system.
But there is one more problem here that as IP addresses are dynamic so when I will send the file my IP address will be there but whenever I will be shutting down my system then that file will be of no use as my IP address will now be changed when I again start my system. so to solve this problem what hackers will do that they will create a server and send the IP address of that server, as we know that servers never shut down the IP address of them are static so now I can easily access your system.

## Running the files
  - Run [Server.py](https://github.com/kampaitees/Ethical-Hacking-using-Socket-Programming/blob/master/Single%20Client(Reverse%20shell%20V1)/server.py) file on terminal/cmd
      `python server.py`
  - Run [Client.py](https://github.com/kampaitees/Ethical-Hacking-using-Socket-Programming/blob/master/Single%20Client(Reverse%20shell%20V1)/client.py) file on another terminal/cmd
      `python client.py`
  
Now whatever you will type on your system will be executed on your friend/victim's system and you have full access to his/her system

I hope this intro to sockets in python was digestible for beginners. In my server and client script I have also included exception handling as it is good style of writing code. Now I hope that you have a solid understanding about the working of sockets in python. However there’s a lot more to it. For further study i recommend the Official python docs. If you liked this post then don’t forget to share it on facebook, tweet it on twitter, share it on linkedin and follow my gtihub.
