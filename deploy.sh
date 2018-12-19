export SELINON_NAMESPACE=${SELINON_NAMESPACE:=fpokorny-thoth-dev}
export OCP_URL=$(oc whoami --show-server)
export OCP_TOKEN=$(oc whoami --show-token)
ansible-playbook ansible/provision.yaml
