#!/usr/bin/bash

set -x

SELINON_NAMESPACE=${THOTH_NAMESPACE:=fpokorny-thoth-dev}

oc delete template selinon-api-imagestream worker-imagestream selinon-api-imagestream selinon-api-buildconfig  worker-buildconfig selinon-api-deploymentconfig selinon-configmap selinon-secret  worker-buildconfig  worker-deploymentconfig rabbitmq-deploymentconfig
oc delete is selinon-api worker rabbitmq redis
oc delete secret/selinon configmap/selinon
oc delete bc/selinon-api bc/worker
oc delete dc/selinon-api dc/worker dc/worker-dispatcher
ansible-playbook ansible/deprovision.yaml --extra-vars=SELINON_NAMESPACE=$SELINON_NAMESPACE
oc delete svc selinon-api rabbitmq redis
oc delete dc/selinon-api dc/worker dc/worker-dispatcher dc/rabbitmq
oc delete routes selinon-api rabbitmq
oc delete template redis-deploymentconfig
oc delete dc redis
