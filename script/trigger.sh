curl -X POST \
  -H 'content-type: application/json' \
  -H 'Authorization: Bearer dG9rZW4K' \
  -H 'FORWARD_URL: https://ws.bestwestern.it/JSONWebserviceDEV/DialogFlow/' \
  -H 'FORWARD_FQDN: app-external-bw-1199579930.eu-west-1.elb.amazonaws.com' \
  -H 'FORWARD-Authorization: Basic dXNlcjpwYXNzd29yZAo=' \
  -d '{ "hello": "World" }' \
  http://127.0.0.1:8080
