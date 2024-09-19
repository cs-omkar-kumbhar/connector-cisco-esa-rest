"""
Copyright start
Copyright (C) 2008 - 2024 FortinetInc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end
"""

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import _check_health, operations

logger = get_logger('cisco-esa')


class CiscoESA(Connector):

    def execute(self, config, operation, params, **kwargs):
        try:
            operation = operations.get(operation)
            return operation(config, params)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)

    def check_health(self, config):
        try:
            _check_health(config)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(err)

