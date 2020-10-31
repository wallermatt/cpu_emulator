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
CALL V,partition
JMP V,end
; 
; partition
;
partition:
; if len = 1 return
LD AM,current_start_pointer
LD BM,current_end_pointer
GTBA
RETNR
; set A to pivot value
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
; partition_gt_loop
partition_gt_loop:
; set B to current value
LDI BDM
; if B is NOT greater than pivot ignore and move along 
GTBA
JMN RV,move_along_gt
; if B > pivot push to stack
PUSHB
; move_along_gt
move_along_gt:
INCD
; check for end of array
LD BM,current_end_pointer
GTDB
; if end reached jump to eq
JMP RV,partition_eq_start
; endloop
JMP V,partition_gt_loop
;
; partition_eq_start
;
partition_eq_start:
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
partition_eq_loop:
LDI BDM
EQBA
JMN RV,move_along_eq
PUSHB
; move_along_eq
move_along_eq:
INCD
LD BM,current_end_pointer
GTDB
JMP RV,partition_lt_start
JMP V,partition_eq_loop
;
; partition_lt_start
;
partition_lt_start:
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
; partition_lt_loop
partition_lt_loop:
LDI BDM
LTBA
JMN RV,move_along_lt
PUSHB
; move_along_lt
move_along_lt:
INCD
LD BM,current_end_pointer
GTDB
JMP RV,write_back
JMP V,partition_lt_loop
;
; write_back
;
write_back:
LD DM,current_start_pointer
LD BM,current_end_pointer
; write_back_loop
write_back_loop_lt:
POPB
EQAB
JMP RV,write_back_equal 
LDIM DB
INCD 
LD BM,current_end_pointer
JMP V,write_back_loop_lt
; write_back_equal
write_back_equal:
; stick first pivot value back on stack
PUSHB
; push start of equal back on stack
PUSHD
; push current end to stack
LD BM,current_end_pointer
PUSHB
; push current pivot value to stack
PUSHA
; set D to end of sub-array
DECD
LD MD,current_end_pointer
CALL V,partition
; set A = pivot
POPA
; reset current end
POPB
LD MB,current_end_pointer
; get new start pos
POPD
; write_back_equal_loop
write_back_equal_loop:
POPB
GTBA
JMP RV,write_back_gt 
LDIM DB
INCD 
LD BM,current_end_pointer
GTDB
RET R
JMP V,write_back_equal_loop
; write_back_gt 
write_back_gt:
LD MD,current_start_pointer
PUSHB
; write_back_gt_loop
write_back_gt_loop:
POPB
LDIM DB
INCD
LD BM,current_end_pointer
GTDB
JMN RV,write_back_gt_loop
; write_back_gt_end
CALL V,partition
RET
; end
end:
0