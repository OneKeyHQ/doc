# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class DebugLinkReseedRandom(p.MessageType):
    MESSAGE_WIRE_TYPE = 9002

    def __init__(
        self,
        value: int = None,
    ) -> None:
        self.value = value

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('value', p.UVarintType, 0),
        }
