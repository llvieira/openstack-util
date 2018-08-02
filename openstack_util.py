import base64

from openstack import connection

class OpenstackUtil:

    def __init__(self, auth_url, project_name, user_domain_name, project_domain_name, username, password):
        self.conn = connection.Connection(auth_url=auth_url, project_name=project_name,
                                          user_domain_name=user_domain_name,
                                          project_domain_name=project_domain_name,
                                          username=username, password=password)

    def create_server(self, server_name, image_name, flavor_name, keypair_name, file_name=""):
        image_id_found = self._get_image_id(image_name)
        flavor_id_found = self._get_flavor_id(flavor_name)
        keypair_name_found = self._get_keypair_name(keypair_name)
        user_data_script = self._convert_to_base64(file_name)

        server = self.conn.compute.create_server(name=server_name, image_id=image_id_found, flavor_id=flavor_id_found,
                                                 key_name=keypair_name_found, user_data=user_data_script, wait=True)

        self.conn.compute.wait_for_server(server)
        return server

    def delete_server(self, server_name):
        self.conn.compute.delete_server(server_name)

    def create_volume(self, volume_size):
        return self.conn.create_volume(volume_size, wait=True)

    def attach_volume(self, server, volume):
        self.conn.attach_volume(server, volume, wait=True)

    def detach_volume(self, server, volume):
        self.conn.detach_volume(server, volume, wait=True)

    def create_snapshot(self, name, server):
        self.conn.create_image_snapshot(name, server, wait=True)

    def delete_snapshot(self, name, server):
        self.conn.delete_volume_snapshot(name, server, wait=True)

    # utilitary functions
    def get_server(self, server_name):
        return self.conn.get_server(server_name)

    def get_volume(self, volume_name):
        return self.conn.get_volume(volume_name)

    def get_image(self, image_name):
        return self.conn.compute.find_image(image_name)

    def _get_image_id(self, image_name):
        return self.get_image(image_name).id

    def _get_flavor_id(self, flavor_name):
        return self.conn.compute.find_flavor(flavor_name).id

    def _get_keypair_name(self, keypair_name):
        if keypair_name is not None:
            return self.conn.compute.find_keypair(keypair_name).name

    def _convert_to_base64(self, file_name):
        if file_name == "":
            return ""

        cloud_init = open(file_name, "r")
        content = cloud_init.read()

        return str(base64.b64encode(content.encode()).decode("utf-8"))
