from openstack_util import OpenstackUtil

import time

def main(): 
    auth_args = {
        "auth_url": "https://cloud.lsd.ufcg.edu.br:5000/v3",
        "project_name": "SD3",
        "user_domain_name": "geral",
        "project_domain_name": "geral",
        "username": "user-sd-3",
        "password": "lucas123"
    }

    openstackUtil = OpenstackUtil(**auth_args)
    script(openstackUtil)

def script(openstackUtil):
    server_params = {
        "server_name": "vm-app",
        "image_name": "ubuntu-14.04-Ago-17",
        "flavor_name": "geral.sd.small",
        "keypair_name": "lucas-key",
        "file_name": "cloud_init.sh"
    }

    print("- Creating Server -")
    server = openstackUtil.create_server(**server_params)
    print("- Created Server -")

    while True:
        time.sleep(360)
        
        snap_name = "snap-test"

        print("- Creating Snapshot -")
        openstackUtil.create_snapshot(snap_name, server.id)
        print("- Created Snapshot -")

        time.sleep(530)

        print("- Deleting Server -")
        openstackUtil.delete_server(server.id)
        print ("- Deleted Server -")
        
        time.sleep(530)
        
        print("- Creating Server from snapshot -")
        server_params = {
            "server_name": "vm-app",
            "image_name": snap_name,
            "flavor_name": "geral.sd.small",
            "keypair_name": "lucas-key",
            "file_name": "start_app.sh"
        }

        server = openstackUtil.create_server(**server_params)
        print("- Created Server from snapshot -")

        print("- Deleting Snapshot -")
        openstackUtil.delete_snapshot(snap_name)
        print("- Deleted Snapshot -")

# def create_server(openstackUtil):
#     server_params = {
#         "server_name": "lucas-vm-node",
#         "image_name": "ubuntu-14.04-Ago-17",
#         "flavor_name": "geral.sd.small",
#         "keypair_name": "lucas-key",
#         "file_name": "cloud_init.sh"
#     }

#     print("- Creating Server -")
#     server = openstackUtil.create_server(**server_params)
#     print(server.id)
#     print("- Created Server -")

#     print(" - Creating Snapshot -")
#     openstackUtil.create_snapshot("snap-test", server.id)
#     print(" - Created Snapshot -")

#     print(" - Deleting Server - ")
#     openstackUtil.delete_server(server.id)
#     print (" - Deleted Server ")
    
#     print(" - Creating Server from snapshot -")
#     server_params = {
#         "server_name": "lucas-from-snap",
#         "image_name": "snap-test",
#         "flavor_name": "geral.sd.small",
#         "keypair_name": "lucas-key"
#     }

#     server = openstackUtil.create_server(**server_params)
#     print("- Created Server from snapshot -")

#     print("- Creating Volume -")
#     volume = openstackUtil.create_volume(10)
#     print(volume.id)
#     print("- Created Volume -")

#     print(" - Attaching Volume -")
#     server = openstackUtil.get_server(server.id)
#     volume = openstackUtil.get_volume(volume.id)

#     openstackUtil.attach_volume(server, volume)
#     print(" - Attached Volume -")

#     print(" - Deleting Server - ")
#     openstackUtil.delete_server(server.id)
#     print (" - Deleted Server ")

#     print(" - Creating Server -")
#     server_params = {
#         "server_name": "lucas-vm2",
#         "image_name": "ubuntu-14.04-Ago-17",
#         "flavor_name": "geral.sd.small",
#         "keypair_name": "lucas-key"
#     }

#     server = openstackUtil.create_server(**server_params)
#     print("- Created Server -")

#     print(" - Attaching Volume -")
#     server = openstackUtil.get_server(server.id)
#     volume = openstackUtil.get_volume(volume.id)

#     openstackUtil.attach_volume(server, volume)
#     print(" - Attached Volume -")

if __name__ == '__main__':
    main()
