import cocotb
import random
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, FallingEdge, ClockCycles

@cocotb.test()
async def test_i2c_master(dut):

    cocotb.start_soon(Clock(dut.clk, 2, units = 'sec').start())
    # cocotb.start_soon(Clock(dut.i2c_clk, 20, units = 'ns').start())

    # Reset and enable module
    await RisingEdge(dut.clk)
    dut.arst.value = 1
    dut.fifo_wr_en.value = 0
    await Timer(2, units="sec")
    dut.arst.value = 0
    dut.fifo_wr_en.value = 1
    await RisingEdge(dut.clk)

    for i in range(4):
        await Timer(50, units="sec")
        dut.data.value = random.randint(0, 256)
        dut.addr.value = random.randint(0, 127)

    await Timer(10, units="sec")