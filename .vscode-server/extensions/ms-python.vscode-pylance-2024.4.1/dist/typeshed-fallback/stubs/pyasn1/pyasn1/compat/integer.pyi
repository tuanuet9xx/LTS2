from typing import Literal

implementation: str
null: Literal[b""]

def from_bytes(octets, signed: bool = False): ...
def to_bytes(value, signed: bool = False, length: int = 0): ...
def bitLength(number): ...
