; pivot array
array_start_address=200
array_end_address=209
pivot_value_address=199
current_start_pointer=197
current_end_pointer=198
; pivot=last element in array
LD AV,array_start_address
LD MA,current_start_pointer
LD AV,array_end_address
LD MA,current_end_pointer
PUSHP
JMP V,quicksort
JMP V,end
; quicksort
quicksort:
LD AM,current_start_pointer
LD BM,current_end_pointer
SUBBA
LD AV,0
EQAB
JMP RV,quicksort_return
LD AV,1
EQAB
JMP RV,quicksort_return
PUSHB
LD BM,current_start_pointer
;PUSHB
;PUSHB
PUSHP
JMP V,partition
LD AM,pivot_value_address
LD DM,current_start_pointer
LDI BDM
; quicksort_return
quicksort_return:
POPA
INCA
INCA
JMPA
; partition
partition:
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
partition_gt_loop:
LDI BDM
GTBA
JMN RV,move_along_gt
PUSHB
move_along_gt:
INCD
LD BM,current_end_pointer
GTDB
JMP RV,partition_eq_start
JMP V,partition_gt_loop
; start equal
partition_eq_start:
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
partition_eq_loop:
LDI BDM
EQBA
JMN RV,move_along_eq
PUSHB
move_along_eq:
INCD
LD BM,current_end_pointer
GTDB
JMP RV,partition_lt_start
JMP V,partition_eq_loop
; start lt
partition_lt_start:
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
partition_lt_loop:
LDI BDM
LTBA
JMN RV,move_along_lt
PUSHB
move_along_lt:
INCD
LD BM,current_end_pointer
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
POPA
INCA
INCA
JMPA
end:
0