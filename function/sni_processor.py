from urllib.parse import urlparse

import dns.resolver
import requests


class HostHeaderSSLAdapter(requests.adapters.HTTPAdapter):
    """SNI means Server Name Identification
    For more information please follow the link https://www.wikiwand.com/en/Server_Name_Indication
    """
    def __init__(self, forward_fqdn: str):
        super().__init__()
        self.__forward_fqdn = forward_fqdn

    @staticmethod
    def resolve(hostname: str) -> str:
        resolver = dns.resolver.Resolver()
        resolver.timeout = 5
        resolver.lifetime = 5
        answer = resolver.resolve(hostname)
        if answer and len(answer) > 0:
            return str(answer[0])
        else:
            raise Exception(f"Unable to resolve ip address by {hostname} hostname")

    def send(self, request, **kwargs):
        connection_pool_kwargs = self.poolmanager.connection_pool_kw

        result = urlparse(request.url)
        resolved_ip = self.resolve(self.__forward_fqdn)

        if result.scheme == 'https' and resolved_ip:
            request.url = request.url.replace(
                'https://' + result.hostname,
                'https://' + resolved_ip,
            )
            connection_pool_kwargs['server_hostname'] = result.hostname  # SNI
            connection_pool_kwargs['assert_hostname'] = result.hostname

            # overwrite the host header
            request.headers['Host'] = result.hostname
        else:
            # theses headers from a previous request may have been left
            connection_pool_kwargs.pop('server_hostname', None)
            connection_pool_kwargs.pop('assert_hostname', None)

        return super(HostHeaderSSLAdapter, self).send(request, **kwargs)
