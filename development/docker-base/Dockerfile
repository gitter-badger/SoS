# This file is part of Script of Scripts (sos), a workflow system
# for the execution of commands and scripts in different languages.
# Please visit https://github.com/vatlab/SOS for more information.
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

# SoS official docker image for latest version of SoS. Use command
# 
#     docker build -t mdabioinfo/sos:latest docker-base 
#
# to build it.
#
FROM continuumio/anaconda3

MAINTAINER Bo Peng <bpeng@mdanderson.org>

RUN     mkdir /home/mdabioinfo
ENV     HOME  /home/mdabioinfo
WORKDIR ${HOME}

RUN     apt-get update
RUN     apt-get install -y  gcc
# these should be installed automatically by sos
RUN     pip install nbformat --upgrade
RUN     pip install sos

