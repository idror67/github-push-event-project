variable "region" {
default = "us-central"
}

variable "root_pass"{
default = "this-is-not-a-safe-password"
}

variable "ssh_keys" {
    default = ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIDSLFiVX+b25tXnsYMUnDU42e9qA5cdruoRjkNWImxR3 default"]
    }

variable "label" {
    default = "HW_Instance"
    }

variable "linode_token" {
    default = "43bf5d1300c95905a7deddc2c12f7fd2e99dcac3c2ef8189b18d3b89de55a3e7"
    } 
variable "github_token" {
    default = "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"
    }
