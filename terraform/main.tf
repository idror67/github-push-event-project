terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
      version = "2.25.0"
    }
  }
}

provider "linode" {
  token = var.linode_token
}

resource "linode_instance" "HW_Instance" {
  label           = "HW_Instance"
  image           = "linode/ubuntu24.04"
  region          = "us-central"
  type            = "g6-nanode-1"
  authorized_keys = var.ssh_keys
  root_pass       = var.root_pass
  tags            = ["example", "terraform"]
}
resource "local_file" "linode_IP" {
    content  = linode_instance.HW_Instance.ip_address
    filename = "linode_IP.txt"
  
}
output "linode_ip_address" {
    value = linode_instance.HW_Instance.ip_address
}
resource "github_repository_webhook" "my_hook" {
    repository = github_repository.arya.name
    events     = ["push"]
    configuration {
        url          = "http://${linode_instance.name.ip_address}:5000"
        content_type = "json"
    }
