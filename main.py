from openstack_util import OpenstackUtil

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
    create_server(openstackUtil)

def create_server(openstackUtil):
    server_params = {
        "server_name": "lucas-vm",
        "image_name": "ubuntu-14.04-Ago-17",
        "flavor_name": "geral.sd.small",
        "keypair_name": "lucas-key"
    }

    print("- Creating Server -")
    server = openstackUtil.create_server(**server_params)
    print(server.id)
    print("- Created Server -")

    print("- Creating Volume -")
    volume = openstackUtil.create_volume(1)
    print(volume.id)
    print("- Created Volume -")

    print("attaching volume")
    server = openstackUtil.get_server(server.id)
    volume = openstackUtil.get_volume(volume.id)

    openstackUtil.attach_volume(server, volume)

if __name__ == '__main__':
    main()
