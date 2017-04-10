#!/usr/bin/env python

from resource_management.libraries.functions.version import format_hdp_stack_version, compare_versions
from resource_management import *
import commands

# server configurations
config = Script.get_config()

docker_user = "root"
docker_group = "root"
docker_home = '/var/lib/docker'
docker_bin = '/usr/bin/docker'
docker_pid_dir = '/run'
docker_pid_file = format("{docker_pid_dir}/docker.pid")

conf_dir = "/etc/sysconfig"
filename = "docker"
log_dir = '/var/log/'
pid_dir = '/run'
pid_file = '/run/docker.pid'

a,listen_address=commands.getstatusoutput("hostname -i | awk '{print $NF}'")
options = config['configurations']['docker-conf']['OPTIONS']
cert_path = config['configurations']['docker-conf']['DOCKER_CERT_PATH']
