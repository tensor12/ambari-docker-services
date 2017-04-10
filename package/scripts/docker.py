#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from resource_management import *
from properties_config import properties_config
import sys
from copy import deepcopy

def docker():
    import params

    Directory([params.log_dir, params.pid_dir, params.conf_dir],
              owner=params.docker_user,
              group=params.docker_group,
              recursive=True
          )
    configurations = params.config['configurations']['docker-conf']
    File(format("/etc/sysconfig/docker"),
       content=Template("docker.j2",
			configurations = configurations),
       owner=params.docker_user,
       group=params.docker_group
		)
