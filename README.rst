selinon-api
-----------

This service is dedicated to be a console for Thoth's developers who would like
to gather and/or experiment with data. It's not part of Thoth deployment.

See `selinon-worker <https://github.com/thoth-station/selinon-worker>`_ for
information about implemented workflows.

Architecture
============

The diagram bellow shows the architecture overview of the Selinon data aggregation and processing pipeline. The main interaction point is an API service exposing core data aggregation, cleansing and preparation. Refer to `selinon-worker repo <https://github.com/thoth-station/selinon-worker>`_ for more information on available workflows.

The worker implements tasks that are grouped into flows. Results of tasks are stored in Thoth's persistent data stores such as Ceph. Redis is used to store temporary data as well as one-time workflow management related data used for a single flow run.

RabbitMQ is used as a message queue for message passing.

.. figure:: https://raw.githubusercontent.com/thoth-station/selinon-api/master/fig/architecture.png
   :alt: Architecture overview.
   :align: center
