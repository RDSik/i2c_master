########################################
#  This file was generated by hdlmake  #
#  http://ohwr.org/projects/hdl-make/  #
########################################

TOP_MODULE := i2c_master
PROJECT := i2c_master
PROJECT_FILE := $(PROJECT).xpr
TOOL_PATH := C:\Xilinx\Vivado\2019.1\bin
TCL_INTERPRETER := vivado -mode tcl -source
ifneq ($(strip $(TOOL_PATH)),)
TCL_INTERPRETER := $(TOOL_PATH)/$(TCL_INTERPRETER)
endif

SYN_FAMILY := 
SYN_DEVICE := xc7z020clg484
SYN_PACKAGE := 
SYN_GRADE := -1

TCL_CREATE := create_project $(PROJECT) ./
TCL_OPEN := open_project $(PROJECT_FILE)
TCL_CLOSE := exit
ifneq ($(wildcard $(PROJECT_FILE)),)
TCL_CREATE := $(TCL_OPEN)
endif

#target for performing local synthesis
all: bitstream

SOURCES_VerilogFile := \
../../src/i2c_fsm.v \
../../src/i2c_master.v \
../../src/sync_fifo.v

SOURCES_XDCFile := \
i2c_master.xdc

files.tcl:
		@$(foreach sourcefile, $(SOURCES_VerilogFile), echo add_files -norecurse $(sourcefile); set_property IS_GLOBAL_INCLUDE 1 [get_files $(sourcefile)] >> $@ &)
		@$(foreach sourcefile, $(SOURCES_XDCFile), echo add_files -norecurse $(sourcefile); set_property IS_GLOBAL_INCLUDE 1 [get_files $(sourcefile)] >> $@ &)

SYN_PRE_PROJECT_CMD := 
SYN_POST_PROJECT_CMD := vivado -mode tcl -source add_ip.tcl

SYN_PRE_SYNTHESIZE_CMD := 
SYN_POST_SYNTHESIZE_CMD := 

SYN_PRE_PAR_CMD := 
SYN_POST_PAR_CMD := 

SYN_PRE_BITSTREAM_CMD := 
SYN_POST_BITSTREAM_CMD := 

project.tcl:
		echo $(TCL_CREATE) >> $@
		echo # project properties >> $@
		echo set_property "part" "$(SYN_DEVICE)$(SYN_PACKAGE)$(SYN_GRADE)" [current_project] >> $@
		echo set_property "target_language" "vhdl" [current_project] >> $@
		echo set_property "top" "$(TOP_MODULE)" [get_property srcset [current_run]] >> $@
		echo source files.tcl >> $@
		echo update_compile_order -fileset sources_1 >> $@
		echo update_compile_order -fileset sim_1 >> $@
		echo $(TCL_CLOSE) >> $@

project: files.tcl project.tcl
		$(SYN_PRE_PROJECT_CMD)
		$(TCL_INTERPRETER) $@.tcl
		$(SYN_POST_PROJECT_CMD)
		type nul >> $@

synthesize.tcl:
		echo $(TCL_OPEN) >> $@
		echo # synthesize properties >> $@
		echo reset_run synth_1 >> $@
		echo launch_runs synth_1 >> $@
		echo wait_on_run synth_1 >> $@
		echo set result [get_property STATUS [get_runs synth_1]] >> $@
		echo set keyword [lindex [split $$result " "] end] >> $@
		echo if { $$keyword != "Complete!" } { >> $@
		echo     exit 1 >> $@
		echo } >> $@
		echo $(TCL_CLOSE) >> $@

synthesize: project synthesize.tcl
		$(SYN_PRE_SYNTHESIZE_CMD)
		$(TCL_INTERPRETER) $@.tcl
		$(SYN_POST_SYNTHESIZE_CMD)
		type nul >> $@

par.tcl:
		echo $(TCL_OPEN) >> $@
		echo # par properties >> $@
		echo reset_run impl_1 >> $@
		echo launch_runs impl_1 >> $@
		echo wait_on_run impl_1 >> $@
		echo set result [get_property STATUS [get_runs impl_1]] >> $@
		echo set keyword [lindex [split $$result " "] end] >> $@
		echo if { $$keyword != "Complete!" } { >> $@
		echo     exit 1 >> $@
		echo } >> $@
		echo $(TCL_CLOSE) >> $@

par: synthesize par.tcl
		$(SYN_PRE_PAR_CMD)
		$(TCL_INTERPRETER) $@.tcl
		$(SYN_POST_PAR_CMD)
		type nul >> $@

bitstream.tcl:
		echo $(TCL_OPEN) >> $@
		echo launch_runs impl_1 -to_step write_bitstream >> $@
		echo wait_on_run impl_1 >> $@
		echo $(TCL_CLOSE) >> $@

bitstream: par bitstream.tcl
		$(SYN_PRE_BITSTREAM_CMD)
		$(TCL_INTERPRETER) $@.tcl
		$(SYN_POST_BITSTREAM_CMD)
		type nul >> $@

CLEAN_TARGETS := $(LIBS) .Xil *.jou *.log *.pb *.dmp $(PROJECT).cache $(PROJECT).data work $(PROJECT).runs $(PROJECT).hw $(PROJECT).ip_user_files $(PROJECT_FILE)

clean:
		del /s /q /f $(CLEAN_TARGETS)
		@-rmdir /s /q $(CLEAN_TARGETS) >nul 2>&1
		del /s /q /f project synthesize translate map par bitstream
		del /s /q /f project.tcl synthesize.tcl translate.tcl map.tcl par.tcl bitstream.tcl files.tcl

mrproper: clean
		del /s /q /f *.bit *.bin

.PHONY: mrproper clean all
