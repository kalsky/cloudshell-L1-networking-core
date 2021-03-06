#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.layer_one.core.response.resource_info.entities.attributes import StringAttribute
from cloudshell.layer_one.core.response.resource_info.entities.base import ResourceInfo


class Blade(ResourceInfo):
    """Blade resource entity"""
    NAME_TEMPLATE = 'Blade{}'
    FAMILY_NAME = 'L1 Switch Blade'

    def __init__(self, resource_id, model_name, serial_number):
        name = self.NAME_TEMPLATE.format(resource_id)
        family_name = self.FAMILY_NAME
        super(Blade, self).__init__(resource_id, name, family_name, model_name, serial_number)

    def set_model_name(self, value):
        if value:
            self.attributes.append(StringAttribute('Model Name', value))

    def set_serial_number(self, value):
        if value:
            self.attributes.append(StringAttribute('Serial Number', value))
