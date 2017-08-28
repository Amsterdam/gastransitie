"""
Access the gastransitie project data on the data store.

For now the convention is that only relevant files are in the datastore and
the layout there matches the layout expected by our data loading scripts.

(We may have to complicate this in the future if we get to automatic
delivery of new data for this project.)
"""
import os
import argparse
import logging

from swiftclient.client import Connection

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('swiftclient').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

GASTRANSITIE_OBJECTSTORE_PASSWORD = os.environ['GASTRANSITIE_OBJECTSTORE_PASSWORD']

OS_CONNECT = {
    'auth_version': '2.0',
    'authurl': 'https://identity.stack.cloudvps.com/v2.0',
    'tenant_name': 'BGE000081_gastransitie',
    'user': 'gastransitie',
    'os_options': {
        'tenant_id': '66aef3e8a4bd4c4aa7e0725fe5571e14',  # Project ID
        'region_name': 'NL'
    },
    'key': GASTRANSITIE_OBJECTSTORE_PASSWORD
}

DATASETS = set([
    'alliander',
    'corporatie_bezit',
    'energie_labels',
    'mip',
    'renovaties',
    'warmtekoude'
])


def get_full_container_list(conn, container, **kwargs):
    # Note: taken from the bag_services project
    limit = 10000
    kwargs['limit'] = limit
    page = []

    seed = []

    _, page = conn.get_container(container, **kwargs)
    seed.extend(page)

    while len(page) == limit:
        # keep getting pages..
        kwargs['marker'] = seed[-1]['name']
        _, page = conn.get_container(container, **kwargs)
        seed.extend(page)

    return seed


def download_container(conn, container, datadir):
    target_dir = os.path.join(datadir, container['name'])
    os.makedirs(target_dir)  # will error out if directory exists

    content = get_full_container_list(conn, container['name'])
    for obj in content:
        target_filename = os.path.join(target_dir, obj['name'])
        with open(target_filename, 'wb') as new_file:
            _, obj_content = conn.get_object(container['name'], obj['name'])
            new_file.write(obj_content)


def download_containers(conn, datasets, datadir):
    """
    Download the gas transitie datasets from object store.

    Simplifying assumptions:
    * layout on data store matches intended layout of local data directory
    * datasets do not contain nested directories
    * assumes we are running in a clean container (i.e. empty local data dir)
    * do not overwrite / delete old data
    """
    logger.debug('Checking local data directory exists and is empty')
    if not os.path.exists(datadir):
        raise Exception('Local data directory does not exist.')

    listing = os.listdir(datadir)
    if listing:
        if len(listing) == 1 and listing[0] == 'README':
            # Case where the 'data' dictory is used from a fresh checkout.
            pass
        else:
            raise Exception('Local data directory not empty!')

    logger.debug('Establishing object store connection.')
    resp_headers, containers = conn.get_account()

    logger.debug('Downloading containers ...')
    for c in containers:
        if c['name'] in datasets:
            download_container(conn, c, datadir)


def main(datadir):
    conn = Connection(**OS_CONNECT)
    download_containers(conn, DATASETS, datadir)


if __name__ == '__main__':
    desc = "Download gastransitie data from objectore."
    parser = argparse.ArgumentParser(desc)
    parser.add_argument('datadir', type=str,
                        help='Local data directory.', nargs=1)

    args = parser.parse_args()
    main(args.datadir[0])
    print(os.listdir(args.datadir[0]))