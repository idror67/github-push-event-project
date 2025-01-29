pipeline {
    agent any
    environment {
    GITHUB_TOKEN = credentials('GITHUB_TOKEN') // Use your Jenkins credential ID
}

    stages {
        stage('Clone Git Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/idror67/webhook-push.git'
            }
        }
        
        
        stage('building linode') {
            steps {
                dir('/var/lib/jenkins/workspace/terraform-project/terraform') {
                    sh 'terraform init'
                    sh 'terraform validate'
                    sh 'terraform apply -auto-approve -var "github_token=${GITHUB_TOKEN}"'
                    sh 'terraform output linode_ip_address'
                    sh 'echo "\n$(terraform output -raw linode_ip_address)" >> /var/lib/jenkins/workspace/terraform-project/ansible/inventory.ini'
                }
            }
            
        }
        stage('building app with ansible') {
            steps {
                dir('/var/lib/jenkins/workspace/terraform-project/ansible') {
                    sh 'ansible-playbook site.yml'
                }
            }
            
        }
        
        
        
        
    }
}
