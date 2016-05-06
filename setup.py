#!/usr/bin/env python2.7
#
# This file is part of Script of Scripts (sos), a workflow system
# for the execution of commands and scripts in different languages.
# Please visit https://github.com/bpeng2000/SOS
#
# Copyright (C) 2016 Bo Peng (bpeng@mdanderson.org)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
from setuptools import setup
from distutils import log
from distutils.command.install import install

try:
    import json
    try:
        from jupyter_client.kernelspec import install_kernel_spec
    except ImportError:
        from IPython.kernel.kernelspec import install_kernel_spec
    from IPython.utils.tempdir import TemporaryDirectory
    ipython = True
except:
    ipython = False

kernel_json = {
    "argv":         ["python","-m", "pysos.kernel", "-f", "{connection_file}"],
    "display_name": "SoS"
}

class InstallWithKernelspec(install):
    def run(self):
        # Regular installation
        install.run(self)

        if not ipython:
            return
        # Now write the kernelspec
        with TemporaryDirectory() as td:
            os.chmod(td, 0o755)  # Starts off as 700, not user readable
            with open(os.path.join(td, 'kernel.json'), 'w') as f:
                json.dump(kernel_json, f, sort_keys=True)
            try:
                install_kernel_spec(td, 'sos', user=self.user, replace=True)
                log.info('IPython kernel named "sos" is installed.')
            except:
                log.error("Could not install SoS Kernel as %s user" % self.user)

exec(open('pysos/_version.py').read())

setup(name = "sos",
    version = __version__,
    description = 'Script of Scripts (SoS): a lightweight workflow system for the creation of readable workflows',
    author = 'Bo Peng',
    url = 'https://github.com/BoPeng/SOS',
    author_email = 'bpeng@mdanderson.org',
    maintainer = 'Bo Peng',
    maintainer_email = 'bpeng@mdanderson.org',
    license = 'GPL3',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        ],
    packages = ['pysos'],
    cmdclass={'install': InstallWithKernelspec},
    install_requires=[
          'psutil',
          'pyyaml',
          'docker-py',
          'pycurl',
          'blessings',
          'pygments',
      ],
    scripts = [
        'sos',
        'sos-runner',
        ]
)
