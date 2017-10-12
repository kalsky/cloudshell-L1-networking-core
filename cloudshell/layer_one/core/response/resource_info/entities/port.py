#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

from cloudshell.layer_one.core.response.resource_info.entities.attributes import StringAttribute, NumericAttribute, \
    BooleanAttribute
from cloudshell.layer_one.core.response.resource_info.entities.base import ResourceInfo


class Port(ResourceInfo):
    """
    Port resource entity
    """
    NAME_TEMPLATE = 'Port{}'
    FAMILY_NAME = 'L1 Switch Port'

    def __init__(self, resource_id, model_name, serial_number, mapping=None):
        name = self.NAME_TEMPLATE.format(resource_id)
        family_name = self.FAMILY_NAME
        super(Port, self).__init__(resource_id, name, family_name, model_name, serial_number, mapping)

    def set_model_name(self, value):
        if value:
            self.attributes.append(StringAttribute('Model Name', value))

    def set_protocol_value(self, value):
        if value:
            self.attributes.append(StringAttribute('Protocol Value', value))

    def set_protocol_type_value(self, value):
        if value:
            self.attributes.append(StringAttribute('Protocol Type Value', value))

    def set_duplex(self, value):
        if value:
            if re.match(r'full', value, flags=re.IGNORECASE):
                num_value = '3'
            else:
                num_value = '2'
            self.attributes.append(NumericAttribute('Duplex', num_value))

    def set_auto_negotiation(self, value):
        if not isinstance(value, bool):
            return

        if value:
            bool_value = BooleanAttribute.TRUE
        else:
            bool_value = BooleanAttribute.FALSE

        self.attributes.append(BooleanAttribute('Auto Negotiation', bool_value))

    def set_rx_power(self, value):
        if value:
            self.attributes.append(StringAttribute('Rx Power (dBm)', value))

    def set_tx_power(self, value):
        if value:
            self.attributes.append(StringAttribute('Tx Power (dBm)', value))

    def set_port_speed(self, value):
        if value:
            self.attributes.append(StringAttribute('Port Speed', value))

    def set_wavelength(self, value):
        if value:
            self.attributes.append(StringAttribute('Wavelength', value))
