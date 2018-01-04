"""
Access the gastransitie project data on the data store.

For now the convention is that only relevant files are in the datastore and
the layout there matches the layout expected by our data loading scripts.

(We may have to complicate this in the future if we get to automatic
delivery of new data for this project.)
"""
import os
import logging
import subprocess

import objectstore

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.getLogger('swiftclient').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)

GASTRANSITIE_OBJECTSTORE_PASSWORD = os.environ['GASTRANSITIE_OBJECTSTORE_PASSWORD']

OBJECTSTORE = {
    'VERSION': '2.0',
    'AUTHURL': 'https://identity.stack.cloudvps.com/v2.0',
    'TENANT_NAME': 'BGE000081_gastransitie',
    'USER': 'gastransitie',
    'TENANT_ID': '66aef3e8a4bd4c4aa7e0725fe5571e14',  # Project ID
    'REGION_NAME': 'NL',
    'PASSWORD': GASTRANSITIE_OBJECTSTORE_PASSWORD
}

DATASETS = set([
    'alliander',
    'corporatie_bezit',
    'energie_labels',
    'mip',
    'renovaties',
    'warmtekoude',
    'cbs',
    'eigendomskaart',
    'functiekaart'
])


def download_container(conn, container, datadir):
    logger.debug('Downloading dataset: %s', container['name'])
    target_dir = os.path.join(datadir, container['name'])
    os.makedirs(target_dir, exist_ok=True)

    content = objectstore.get_full_container_list(conn, container['name'])
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

    p = subprocess.Popen(['ls', '-l', datadir])
    p.wait()

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
    conn = objectstore.get_connection(OBJECTSTORE)
    download_containers(conn, DATASETS, datadir)
