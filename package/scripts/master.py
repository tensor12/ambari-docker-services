#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  The ASF licenses this file
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
import signal
import sys
import os
from os.path import isfile
from docker import docker

class Docker_Master(Script):
    def install(self, env):
        import params
        env.set_params(params)
        print 'Install'
        self.install_packages(env)
    def configure(self, env):
        import params
        env.set_params(params)
        print 'Install plugins';
	docker()
    def stop(self, env):
        import params
        env.set_params(params)
        stop_cmd = format("systemctl stop docker.service")
        Execute(stop_cmd)
        print 'Stop the docker'
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        start_cmd = format("systemctl start docker.service")
        Execute(start_cmd)
        print 'Start the docker'
    def status(self, env):
        import params
        env.set_params(params)
        status_cmd = format("systemctl status docker.service")
        Execute(status_cmd)
        print 'Status of the Docker'
    
if __name__ == "__main__":
    Docker_Master().execute()
