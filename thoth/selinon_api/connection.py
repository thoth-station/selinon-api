#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ######################################################################
# Copyright (C) 2016-2017  Fridolin Pokorny, fridolin.pokorny@gmail.com
# This file is part of Selinon project.
# ######################################################################

import typing

from selinon import run_flow
from selinon import run_flow_selective


class Connection(object):
    """ Connect to broker handling """
    _connected = False

    def __init__(self):
        raise NotImplementedError()

    @classmethod
    def run_selinon_flow(cls, flow_name: str, node_args: dict, task_names: typing.List[str] = None):
        """ Run Selinon flow, connect to broker if necessary

        :param flow_name: name of flow to run
        :param node_args: flow arguments
        :param: task_names: a list of tasks that should be run on selective flow
        :return: celery.AsyncResult describing dispatcher task
        """
        if not cls._connected:
            from thoth.worker import init
            # It is not necessary to connect to result backend, we just publish messages
            init(with_result_backend=False)
            cls._connected = True

        if task_names:
            # We hardcode follow_subflows and run_subsequent, we can later adjust it if needed.
            return run_flow_selective(flow_name, task_names, node_args=node_args, follow_subflows=True, run_subsequent=False)
        else:
            return run_flow(flow_name, node_args)
