#!/usr/bin/python
# -*- coding: utf-8*-
from datetime import datetime
from Día import Día


class Hoy(Día):

    apelativo = 'hoy'

    def __str__(self):
        return self.apelativo