#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2016 Dean Jackson <deanishe@deanishe.net>
#
# MIT Licence. See http://opensource.org/licenses/MIT
#
# Created on 2016-03-13
#

"""Searchio! engines."""

from __future__ import print_function, absolute_import

from searchio.engines._engines import (
    engine,
    engines,
    load,
    search,
    searches,
)

__all__ = [
    'engine',
    'engines',
    'load',
    'search',
    'searches',
]
