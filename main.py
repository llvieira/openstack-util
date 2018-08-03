from openstack_util import OpenstackUtil

import time
import datetime
import random

def print_time():
    now = datetime.datetime.now()
    return str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

def main(): 
    auth_args = {
        "auth_url": "https://cloud.lsd.ufcg.edu.br:5000/v3",
        "project_name": "SD3",
        "user_domain_name": "geral",
        "project_domain_name": "geral",
        "username": "user-sd-3",
        "password": "passwd"
    }

    openstackUtil = OpenstackUtil(**auth_args)
    script(openstackUtil)

def script(openstackUtil):
    server_params = {
        "server_name": "vm-app",
        "image_name": "ubuntu-14.04-Ago-17",
        "flavor_name": "geral.sd.small",
        "keypair_name": "lucas-lsd-key",
        "file_name": "cloud_init.sh"
    }

    print("- Creating Server - " + print_time())
    server = openstackUtil.create_server(**server_params)
    print("- Created Server - " + print_time())

    snapshots = []
    snapshot_quantity = 0

    while True:
        time.sleep(120)
        
        snap_name = "snap-app-" + str(snapshot_quantity)
        snapshots.append(snap_name)
        snapshot_quantity += 1

        print("- Creating Snapshot - " + print_time())
        openstackUtil.create_snapshot(snap_name, server.id)
        print("- Created Snapshot - " + print_time())

        time.sleep(120)

        print("- Deleting Server - " + print_time())
        openstackUtil.delete_server(server.id)
        print ("- Deleted Server - " + print_time())
        
        time.sleep(120)
        
        print("- Creating Server from snapshot - " + print_time())
        server_params = {
            "server_name": "vm-app",
            "image_name": snap_name,
            "flavor_name": "geral.sd.small",
            "keypair_name": "lucas-lsd-key",
            "file_name": "start_app.sh"
        }

        server = openstackUtil.create_server(**server_params)
        print("- Created Server from snapshot - " + print_time())

        # do not delete in use snapshot
        if (snapshot_quantity > 1):
            print("- Deleting Snapshot - " + print_time())
            openstackUtil.delete_snapshot(snapshots[snapshot_quantity - 2])
            print("- Deleted Snapshot - " + print_time())

if __name__ == '__main__':
    main()
