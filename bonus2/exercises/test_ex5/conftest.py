import pytest
from getpass import getpass
from netmiko import ConnectHandler


# Use function as a fixture to simplify tests
@pytest.fixture(scope="module")
def netmiko_connect(request):
    """Connect to arista1 and return connection object"""
    arista1 = {
        "device_type": "arista_eos",
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": getpass(),
    }

    net_connect = ConnectHandler(**arista1)

    def fin():
        net_connect.disconnect()

    request.addfinalizer(fin)
    return net_connect
