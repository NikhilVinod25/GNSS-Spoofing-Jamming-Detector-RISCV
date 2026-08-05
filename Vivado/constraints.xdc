## RGB LED (LD4) on PYNQ-Z2
## IO Standard is LVCMOS33 for all three

# LD4 Blue (Bit 0) - Pin L15
set_property -dict { PACKAGE_PIN L15   IOSTANDARD LVCMOS33 } [get_ports { led_rgb_tri_o[0] }]; 

# LD4 Green (Bit 1) - Pin G17
set_property -dict { PACKAGE_PIN G17   IOSTANDARD LVCMOS33 } [get_ports { led_rgb_tri_o[1] }]; 

# LD4 Red (Bit 2) - Pin N15
set_property -dict { PACKAGE_PIN N15   IOSTANDARD LVCMOS33 } [get_ports { led_rgb_tri_o[2] }];

# =========================================================================
# PYNQ-Z2 ARDUINO HEADER PINS FOR 7-SEGMENT DISPLAY
# =========================================================================

# AR0 mapped to 7-Segment Pin A
set_property -dict { PACKAGE_PIN T14   IOSTANDARD LVCMOS33 } [get_ports { seg_0[0] }]; 

# AR1 mapped to 7-Segment Pin B
set_property -dict { PACKAGE_PIN U12   IOSTANDARD LVCMOS33 } [get_ports { seg_0[1] }]; 

# AR2 mapped to 7-Segment Pin C
set_property -dict { PACKAGE_PIN U13   IOSTANDARD LVCMOS33 } [get_ports { seg_0[2] }]; 

# AR3 mapped to 7-Segment Pin D
set_property -dict { PACKAGE_PIN V13   IOSTANDARD LVCMOS33 } [get_ports { seg_0[3] }]; 

# AR4 mapped to 7-Segment Pin E
set_property -dict { PACKAGE_PIN V15   IOSTANDARD LVCMOS33 } [get_ports { seg_0[4] }]; 

# AR5 mapped to 7-Segment Pin F
set_property -dict { PACKAGE_PIN T15   IOSTANDARD LVCMOS33 } [get_ports { seg_0[5] }]; 

# AR6 mapped to 7-Segment Pin G
set_property -dict { PACKAGE_PIN R16   IOSTANDARD LVCMOS33 } [get_ports { seg_0[6] }]; 
