"""Cut Health Target up into pieces."""
import collections
import logging

LOG = logging.getLogger(__name__)


def splay_health(health_target):
    """Set Health Check path, port, and protocol.

    Args:
        health_target (str): The health target. ie ``HTTP:80``
    Returns:
        HealthCheck: A **collections.namedtuple** class with *path*, *port*,
        *proto*, and *target* attributes.
    """
    HealthCheck = collections.namedtuple('HealthCheck', ['path', 'port',
                                                         'proto', 'target'])

    proto, health_port_path = health_target.split(':')
    port, *health_path = health_port_path.split('/')

    if proto == 'TCP':
        path = ''
    elif not health_path:
        path = '/healthcheck'
    else:
        path = '/{0}'.format('/'.join(health_path))

    target = '{0}:{1}{2}'.format(proto, port, path)

    health = HealthCheck(path, port, proto, target)
    LOG.info(health)

    return health
