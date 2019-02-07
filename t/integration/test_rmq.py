import pytest
import amqp


pytestmark = pytest.mark.rabbitmq


class test_rmq:

    def test_connect(self):
        connection = amqp.Connection()
        connection.connect()
        connection.close()
