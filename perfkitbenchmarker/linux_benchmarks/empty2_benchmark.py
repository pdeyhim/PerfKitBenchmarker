# Copyright 2014 PerfKitBenchmarker Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



import json
import logging
import posixpath
import time

from perfkitbenchmarker import sample
from perfkitbenchmarker import configs



BENCHMARK_NAME = 'empty2'
BENCHMARK_CONFIG = """
empty2:
  description: Runs fio in sequential, random, read and write modes.
  vm_groups:
    default:
      vm_spec: *default_single_core
      disk_spec: *default_500_gb
"""


def GetConfig(user_config):
    return configs.LoadConfig(BENCHMARK_CONFIG, user_config, BENCHMARK_NAME)


def Prepare(benchmark_spec):

    vm = benchmark_spec.vms[0]
    logging.info('empty running on %s', vm)


def Run(benchmark_spec):

    vm = benchmark_spec.vms[0]

    logging.info('empty running on %s', vm)

    samples = []
    samples.append(sample.Sample('test',1, 'none', {}, time.time()))
    return samples


def Cleanup(benchmark_spec):
    """Uninstall packages required for fio and remove benchmark files.

    Args:
      benchmark_spec: The benchmark specification. Contains all data that is
          required to run the benchmark.
    """
    vm = benchmark_spec.vms[0]
    logging.info('empty Cleanup up on %s', vm)
