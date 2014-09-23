import sys
from py4j.java_gateway import JavaGateway, GatewayClient

port, module = sys.argv[1:]

gateway = JavaGateway(GatewayClient(port=port))

__builtin__._jgateway = gateway
__builtin__.jvm = gateway.jvm
__builtin__._jvertx = gateway.entry_point.getVertx()

__import__(module)
