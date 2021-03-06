#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016.

# Author(s):

#
#   David Hoese <david.hoese@ssec.wisc.edu>
#

# This file is part of satpy.

# satpy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# satpy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with
# satpy.  If not, see <http://www.gnu.org/licenses/>.

"""Helpers for reading netcdf-based files.

"""
import os.path
from datetime import datetime, timedelta
import numpy as np
import logging
import h5py
import six

NO_DATE = datetime(1958, 1, 1)
EPSILON_TIME = timedelta(days=2)
LOG = logging.getLogger(__name__)


class HDF5MetaData(object):
    """Small class for inspecting a HDF5 file and retrieve its metadata/header data.
    """
    def __init__(self, filename, **kwargs):
        self.metadata = {}
        self.filename = filename
        if not os.path.exists(filename):
            raise IOError("File {} does not exist!".format(filename))
        file_handle = h5py.File(self.filename, 'r')
        file_handle.visititems(self.collect_metadata)
        self._collect_attrs('', file_handle.attrs)
        file_handle.close()

    def _collect_attrs(self, name, attrs):
        for key, value in six.iteritems(attrs):
            value = np.squeeze(value)
            if issubclass(value.dtype.type, str):
                self.metadata["{}/attr/{}".format(name, key)] = str(value)
            else:
                self.metadata["{}/attr/{}".format(name, key)] = value

    def collect_metadata(self, name, obj):
        if isinstance(obj, h5py.Dataset):
            self.metadata[name] = obj
            self.metadata[name + "/shape"] = obj.shape
        self._collect_attrs(name, obj.attrs)

    def __getitem__(self, key):
        val = self.metadata[key]
        if isinstance(val, h5py.Dataset):
            # these datasets are closed and inaccessible when the file is closed, need to reopen
            return h5py.File(self.filename, 'r')[key].value
        return val

