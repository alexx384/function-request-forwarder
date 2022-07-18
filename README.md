# function-request-forwarder
Function request forwarder with DNS resolution customization (based on Google Cloud Function)

It represents a simple proxy that will redirect the request to the URL in FORWARD_URL replacing the hostname in the URL 
with the IP address resolved for FORWARD_FQDN.

Note: Most of the request headers will be dropped as Google adds lost of unnecessary headers to the request. 
The request with such headers usually dropped by Web Application Firewall

# How to test it
Run server with the following command
```bash
bash run.sh
```
Run script to send request to the server
```bash
bash script/trigger.sh
```
