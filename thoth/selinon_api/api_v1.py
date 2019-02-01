#!/usr/bin/env python3
# ######################################################################
# Copyright (C) 2016-2019  Fridolin Pokorny, fridolin.pokorny@gmail.com
# This file is part of Selinon project.
# ######################################################################

import logging
from .connection import Connection

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def post_run_flow(flow_name, node_args=None, task_names=None):
    """A low-level run flow API.

    :param flow_name: name of flow to be run
    :param node_args: arguments supplied to flow
    :return: resulting dict for the request
    """
    task_names = task_names.split(',') if task_names else None
    logger.info("Scheduling flow '%s' with node_args: '%s' (task names: %s)", flow_name, node_args, task_names)
    dispatcher = Connection.run_selinon_flow(flow_name, node_args, task_names)
    try:
        return (
            {
                "dispatcher_id": dispatcher.id,
                "flow_name": flow_name,
                "node_args": node_args,
            },
            201,
        )
    except Exception as exc:
        return {"error": str(exc)}, 400


def get_flows():
    """List flows available.

    :return: a list of flows available in Selinon configuration.
    """
    from thoth.worker import get_config_files
    from selinon import Config

    Config.set_config_yaml(*get_config_files())
    return {"flows": Config.flows}


def post_sync():
    """Perform sync to the graph database."""
    return post_run_flow("sync_flow", {})


def post_pypi_ingest_project(package_name):
    return post_run_flow("pypi_project", {"package_name": package_name})


def post_pypi_ingest():
    return post_run_flow("pypi")
