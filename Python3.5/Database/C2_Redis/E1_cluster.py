from rediscluster import StrictRedisCluster


if __name__ == '__main__':
    startup_nodes=[
        {'host': '192.168.79.93', 'port': '3000'},
        {'host': '192.168.79.93', 'port': '3001'},
        {'host': '192.168.79.93', 'port': '3002'}
    ]

    rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    rc.set('name', 'lizhen')
    print(rc.get('name'))
