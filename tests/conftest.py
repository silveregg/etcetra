import os
import pytest
import pytest_asyncio

from etcetra import EtcdClient, EtcdCredential, HostPortPair


@pytest.fixture
def etcd_addr():
    env_addr = os.environ.get('BACKEND_ETCD_ADDR')
    if env_addr:
        return HostPortPair.parse(env_addr)
    return HostPortPair.parse('localhost:2379')


@pytest_asyncio.fixture
async def etcd(etcd_addr):
    creds = EtcdCredential(
        username=os.environ.get('BACKEND_ETCD_USERNAME', 'root'),
        password=os.environ.get('BACKEND_ETCD_PASSWORD', 'root')
    )
    etcd = EtcdClient(etcd_addr, creds)
    try:
        yield etcd
    finally:
        async with etcd.connect() as communicator:
            await communicator.delete_prefix('/test')
        del etcd
