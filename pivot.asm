; pivot array
array_start_address=120
array_end_address=129
pivot_value_address=119
; pivot=last element in array
LD AM,array_end_address
LD DV,array_start_address
partition_gt_loop:
LDI BDM
GTBA
JMN RV,move_along_gt
PUSHB
move_along_gt:
INCD
LD BV,array_end_address
GTDB
JMP RV,partition_eq_start
JMP V,partition_gt_loop
; start equal
partition_eq_start:
LD AM,array_end_address
LD DV,array_start_address
partition_eq_loop:
LDI BDM
EQBA
JMN RV,move_along_eq
PUSHB
move_along_eq:
INCD
LD BV,array_end_address
GTDB
JMP RV,partition_lt_start
JMP V,partition_eq_loop
; start lt
partition_lt_start:
LD AM,array_end_address
LD DV,array_start_address
partition_lt_loop:
LDI BDM
LTBA
JMN RV,move_along_lt
PUSHB
move_along_lt:
INCD
LD BV,array_end_address
GTDB
JMP RV,write_back
JMP V,partition_lt_loop
write_back:
LD DV,pivot_value_address
LDIM DA
LD DV,array_start_address
LD BV,array_end_address
write_back_loop:
POPA
LDIM DA 
INCD 
GTDB
JMP RV,end_write_back
JMP V,write_back_loop
end_write_back:
0