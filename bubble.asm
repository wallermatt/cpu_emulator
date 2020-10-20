; bubble sort
a_temp_loc=100
b_temp_loc=101
d_temp_loc=102
swap_flag_loc=103
swap_flag_value=0
start_data_loc=120
end_data_loc=129
; load initial
LD AV,swap_flag_value
LD MA,swap_flag_loc
LD DV,start_data_loc
; loop through data
main_loop:
; load a with contents of memory loc d
LDI ADM
; load b with contents of memory loc d + 1
INCD
LDI BDM
; check if a > b
GTAB
JMP RV,swap_values
JMP RV,end
LD IM
JMP V,main_loop
swap_values:
; a -> d, b -> d - 1, set flag
end:
0