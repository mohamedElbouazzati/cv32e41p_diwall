
from migen import *

from litex.gen import *

class CPU(LiteXModule):
    category             = None
    family               = None
    name                 = None
    data_width           = None
    endianness           = None
    gcc_triple           = None
    gcc_flags            = None
    clang_triple         = None
    clang_flags          = None
    linker_output_format = None
    interrupts           = {}
    mem_map              = {"csr": 0x82000000}
    io_regions           = {}
    use_rom              = False
    csr_decode           = True
    reset_address_check  = True

    def __init__(self, *args, **kwargs):
        pass

    def set_reset_address(self, reset_address):
        pass # pass must be overloaded (if required)

    def enable_reset_address_check(self):
        self.reset_address_check = True

    def disable_reset_address_check(self):
        self.reset_address_check = False

# CPU None (Used for SoC without a CPU) ------------------------------------------------------------

class CPUNone(CPU):
    variants            = ["standard"]
    endianness          = "little"
    reset_address       = 0x00000000
    reset_address_check = False
    periph_buses        = []
    memory_buses        = []
    mem_map             = {
        "csr"      : 0x0000_0000,
        "ethmac"   : 0x0002_0000, # FIXME: Remove.
        "spiflash" : 0x1000_0000, # FIXME: Remove.
    }

    def __init__(self, data_width=32, addr_width=32):
        self.io_regions = {0: int(2**float(addr_width))} # origin, length
        self.data_width = data_width

# CPUs GCC Triples ---------------------------------------------------------------------------------

CPU_GCC_TRIPLE_RISCV64 = (
    "riscv64-pc-linux-musl",
    "riscv64-unknown-elf",
    "riscv64-unknown-linux-gnu",
    "riscv64-elf",
    "riscv64-linux",
    "riscv64-linux-gnu",
    "riscv-sifive-elf",
    "riscv64-none-elf",
)

CPU_GCC_TRIPLE_RISCV32 = CPU_GCC_TRIPLE_RISCV64 + (
    "riscv32-unknown-elf",
    "riscv32-unknown-linux-gnu",
    "riscv32-elf",
    "riscv-none-embed",
    "riscv-none-elf",
)
