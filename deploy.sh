set -x

export CEPH_BUCKET=${CEPH_BUCKET:=DH-DEV-DATA}
export CEPH_BUCKET_PREFIX={CEPH_BUCKET_PREFIX:=data/thoth/selinon/}
[ -z "$S3_ENDPOINT_URL" -o -z "$S3_KEY_ID" -o -z "$S3_SECRET_KEY" ] && { echo "Please S3 configuration"; exit 1; }
export S3_ENDPOINT_URL=${S3_ENDPOINT_URL}
export S3_KEY_ID=${S3_KEY_ID}
export S3_SECRET_KEY=${S3_SECRET_KEY}
export SELINON_NAMESPACE=${SELINON_NAMESPACE:=fpokorny-thoth-dev}
export OCP_URL=$(oc whoami --show-server)
export OCP_TOKEN=$(oc whoami --show-token)
ansible-playbook ansible/provision.yaml
