# Copyright (c) 2022 Robert Bosch GmbH and Microsoft Corporation
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0

from sdv.base import PubSubClient
from sdv.dapr.client import publish_mqtt_event, wait_for_sidecar
from sdv.dapr.server import register_topic, run_server


class DaprClient(PubSubClient):
    """This class is a wrapper for the on_message callback of the MQTT broker."""

    def __init__(self):
        """Nothing to do"""

    async def init(self):
        """Disabled, run_server is not only pubsub specfic for dapr."""
        await run_server()

    async def run(self):
        await wait_for_sidecar()

    async def subscribe_topic(self, topic: str, coro):
        register_topic(topic, coro)

    async def publish_event(self, topic: str, data: str):
        return publish_mqtt_event(topic, data)
