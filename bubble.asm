; bubble sort
swap_flag_loc=103
false=0
true=1
start_data_loc=120
end_data_loc=129
; load initial
LD AV,false
LD MA,swap_flag_loc
LD DV,start_data_loc
; loop through data
main_loop:
; load a with contents of memory loc d
LDI ADM
; load b with contents of memory loc d + 1
INCD
LD BV,end_data_loc
GTDB
JMP RV,end_of_data_reached
LDI BDM
; check if a > b
GTAB
JMP RV,swap_values
JMP V,main_loop
swap_values:
; a -> d, b -> d - 1, set flag
LDIM DA
DECD
LDIM DB
INCD
LD AV,true
LD MA,swap_flag_loc
JMP V,main_loop
; when end of data reached, check if any swaps
end_of_data_reached:
LD AM,swap_flag_loc
LD BV,false
EQAB
JMP RV,end
LD MB,swap_flag_loc
LD DV,start_data_loc
JMP V,main_loop
; end of program
end:
0