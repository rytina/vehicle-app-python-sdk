from sdv.dapr.client import publish_mqtt_event, wait_for_sidecar
from sdv.dapr.server import register_topic, run_server


class DaprClient:
    """This class is a wrapper for the on_message callback of the MQTT broker."""

    def __init__(self):
        self.register_topic = register_topic
        self.publish_event = publish_mqtt_event
        """Nothing to do"""

    async def run(self):
        await run_server()
        await wait_for_sidecar()
