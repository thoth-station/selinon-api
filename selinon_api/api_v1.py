#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ######################################################################
# Copyright (C) 2016-2017  Fridolin Pokorny, fridolin.pokorny@gmail.com
# This file is part of Selinon project.
# ######################################################################

import logging
from .connection import Connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def post_run_flow(flow_name, node_args=None):
    """A low-level run flow API.

    :param flow_name: name of flow to be run
    :param node_args: arguments supplied to flow
    :return: resulting dict for the request
    """
    logger.info("Scheduling flow '%s' with node_args: '%s'", flow_name, node_args)
    dispatcher = Connection.run_selinon_flow(flow_name, node_args)
    return {"dispatcher_id": dispatcher.id, "flow_name": flow_name, "node_args": node_args}, 201


def get_flows():
    """List flows available.

    :return: a list of flows available in Selinon configuration.
    """
    from demo_worker import get_config_files
    from selinon import Config

    Config.set_config_yaml(*get_config_files())
    return {"flows": Config.flows}


def post_travis_org_logs(organization):
    """Scan for registered repos under organization and gather build logs repos from them."""
    return post_run_flow('travis_org_logs', {'organization': organization})


def post_travis_repo_logs(organization, repo):
    """Gather logs for a project given by organization/repo."""
    return post_run_flow('travis_repo_logs', {'organization': organization, 'repo': repo})
