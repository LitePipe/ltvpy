import os, sys
import pprint

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import numpy as np
import numpy.ma as ma
from dataclasses import dataclass
import litevectors

@dataclass
class AClass:
    strdata: str
    fdata: float
    moar_data: int = 0


data = {
    "null": None,
    "a": -5,
    "neg": -128,
    "ok_large": 1234563212342378901,
    "int_max":  9223372036854775807,
    "uint_max": 18446744073709551615,
    "b": True,
    "c": [1, 2, 3],
    "d": { 
        "subthing": "string"
    },
    "e": 1234.4567,
    "tup": (123, "hello"),
    "binary_data": (1024).to_bytes(4, byteorder='little'),
    "AClass": AClass("ThatClass", 99.9, 55),
    "u8[]": np.ones(20, dtype="uint8"),
    "u16[]": np.ones(20, dtype="uint16"),
    "u32[]": np.ones(20, dtype="uint32"),
    "u64[]": np.ones(20, dtype="uint64"),
    "i8[]": np.ones(20, dtype="int8"),
    "i16[]": np.ones(20, dtype="int16"),
    "i32[]": np.ones(20, dtype="int32"),
    "i64[]": np.ones(20, dtype="int64"),
}

with open('python_data.ltv', 'wb') as w:
    litevectors.dump(data, w)

with open('python_data.ltv', 'rb') as f:
    v = litevectors.load(f)
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    pp.pprint(v)