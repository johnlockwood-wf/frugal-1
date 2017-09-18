from thrift.protocol import TBinaryProtocol
from thrift.transport import TTransport

from frugal.protocol import FProtocolFactory


def serialize(frugal_object, protocol_factory=TBinaryProtocol.TBinaryProtocolFactory()):
    """Serialize a frugal entity to bytes."""
    transport = TTransport.TMemoryBuffer()
    fprotocolFactory = FProtocolFactory(protocol_factory)
    protocol = fprotocolFactory.get_protocol(transport)
    frugal_object.write(protocol)
    return transport.getvalue()


def deserialize(base,
                buf,
                protocol_factory=TBinaryProtocol.TBinaryProtocolFactory()):
    transport = TTransport.TMemoryBuffer(buf)
    fprotocolFactory = FProtocolFactory(protocol_factory)
    protocol = fprotocolFactory.get_protocol(transport)
    base.read(protocol)
    return base
