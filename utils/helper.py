import os


def get_auth_headers():
    access_token = os.environ["access_token"]
    Authorization = "Bearer {}".format(access_token)
    headers = {"Authorization": Authorization}
    return headers
