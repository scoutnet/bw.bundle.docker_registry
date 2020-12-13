files = {
    '/etc/init.d/docker-registry': {
        'owner': 'root',
        'group': 'root',
        'mode': '0755',
    }
}

svc_systemv = {
    'docker-registry': {
        'needs': ['pkg_apt:docker-ce', 'file:/etc/init.d/docker-registry']
    }
}
