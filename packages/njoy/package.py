##############################################################################
# Copyright (c) 2017, Los Alamos National Security, LLC
# Produced at the Los Alamos National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *


class Njoy(CMakePackage):
    """NJOY, the nuclear data processing code developed at Los Alamos National Laboratory."""

    homepage = "https://njoy.github.io"
    url      = "https://github.com/njoy/NJOY2016"

    version('master', git='https://github.com/njoy/NJOY2016.git', branch='master')
    
    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release'))#, 'RelWithDebInfo', 'MinSizeRel'))

    #def cmake_args(self):
    #    spec = self.spec

    #    cmake_args=[]

    #    return cmake_args
