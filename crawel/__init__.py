from urllib import request


def get_request(config):
    return request.Request(config.host_url, headers=config.header)


