# Customizable-Load-Balancer
Analysis:

Launching requests to the servers instructions:
A python code which sends 10000 requests to the api endpoint is used and the message recieved is broken down and the server number extracted to know the count of the requests handled by each server.

### A-1:

Launched 10000 async requests on **N = 3** server containers and reported the request count handled by each server instance in a bar chart

<img src=images/S3.jpg width="250" >

The above image suggests that server 3 is the one handling more than 50% of the total requests. The hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

### A-2:

Launched 10000 async requests on **N = 2** server containers and reported the request count handled by each server instance in a line chart

<img src=images/S2.jpg width="250" >

The above image suggests that server 1 is the one handling more than 80% of the total requests. The hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 3** server containers and reported the request count handled by each server instance in a line chart

<img src=images/S3-line.jpg width="250" >+


The above image suggests that server 3 is the one handling more than 50% of the total requests. The hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 4** server containers and reported the request count handled by each server instance in a line chart

<img src=images/S4.jpg width="250" >

The above image suggests that server 1 and server are the ones handling more than 80% of the total requests. The hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 5** server containers and reported the request count handled by each server instance in a line chart

<img src=images/S5.jpg width="250" >

The above image suggests that servers 1,2,3,4 handle almost similar no of requests but server 5 handles less than 10% of the total requests. The hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 6** server containers and reported the request count handled by each server instance in a line chart

<img src=images/S6.jpg width="250" >

The above image suggests that all servers handle almost similar percentage of the total number of requests. The hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

The above results show that as the number of servers increase the percentage gets divided more and more evenly and all servers have near similar no of requests to handle. The hash function controls these numbers and is designed to equalize as the number of servers increase.

### A4:

Launched 10000 async requests on **N = 3** server containers and reported the request count handled by each server instance in a bar chart

<img src=images/N3-bar.jpg width="250" >

The above image suggests that server 2 is the one handling more than 50% of the total requests. The modified hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 2** server containers and reported the request count handled by each server instance in a line chart

<img src=images/N2.jpg width="250" >

The above image suggests that server 1 is the one handling more than 80% of the total requests. The modified hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 3** server containers and reported the request count handled by each server instance in a line chart

<img src=images/N3-line.jpg width="250" >

The above image suggests that server 3 is the one handling more than 50% of the total requests. The modified hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 4** server containers and reported the request count handled by each server instance in a line chart

<img src=images/N4.jpg width="250" >

The above image suggests that server 1 and server are the ones handling more than 80% of the total requests. The modified hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 5** server containers and reported the request count handled by each server instance in a line chart

<img src=images/N5.jpg width="250" >

The above image suggests that servers 1,2,3,4 handle almost similar no of requests but server 5 handles less than 10% of the total requests. The modified hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

Launched 10000 async requests on **N = 6** server containers and reported the request count handled by each server instance in a line chart

<img src=images/N6.jpg width="250" >

The above image suggests that all servers handle almost similar percentage of the total number of requests. The modified hash function in the load balancer handles the no of requests going to all servers which divides the requests unequally like shown.

The above results show that though the servers handle similar load when there are less number of servers, the numbers become a little skewed when the number of servers increase. This shows that the modified hash function is not perfect for handling load when there are more servers.