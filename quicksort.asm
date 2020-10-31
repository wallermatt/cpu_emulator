; quicksort
; sorts an array in place between array_start_address and array_end_address
;
; define variables
array_start_address=200
array_end_address=209
current_start_pointer=197
current_end_pointer=198
;
; set initial current start and end variables
LD AV,array_start_address
LD MA,current_start_pointer
LD AV,array_end_address
LD MA,current_end_pointer
CALL V,quicksort_array
JMP V,end
; 
; quicksort_array
; splits array into 3 partitions based on pivot chosen as last element
; 3 partitions are less than pivot, equals pivot, greater than pivot.
; These sections are pushed to the stack in order: gt,eq,lt
; Then they're taken from the stack (in reverse order), and written back to the array
; After they're written back the less than and greater than sections are then quicksorted 
; themselves before being joined together with equals in between.
;
quicksort_array:
; if length of array <= 1 return
LD AM,current_start_pointer
LD BM,current_end_pointer
GTBA
RETNR
; set A to pivot value (chosen to be last element)
LD DM,current_end_pointer
LDI ADM
LD DM,current_start_pointer
;
; partition_gt_loop
; loop through array pushing all elements greater than pivot to stack
;
partition_gt_loop:
; set B to current value of array indexed by D
LDI BDM
; if B is NOT greater than pivot ignore and move along 
GTBA
JMN RV,move_along_gt
; if B > pivot push to stack
PUSHB
; move_along_gt
; moves along array checking if end is reached
move_along_gt:
INCD
; check for end of array
LD BM,current_end_pointer
GTDB
; if end reached jump to code than handles values equal to pivot
JMP RV,partition_eq_start
; endloop
JMP V,partition_gt_loop
;
; partition_eq_start
; loop through array pushing all elements equal to pivot to stack
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
; moves along array checking if end is reached
move_along_eq:
INCD
LD BM,current_end_pointer
GTDB
JMP RV,partition_lt_start
JMP V,partition_eq_loop
;
; partition_lt_start
; loop through array pushing all elements less than pivot to stack
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
; moves along array checking if end is reached
move_along_lt:
INCD
LD BM,current_end_pointer
GTDB
JMP RV,write_back
JMP V,partition_lt_loop
;
; write_back
; the partitioned array is now on the stack in order lt,eq,gt
; This code takes each partition in turn and writes it back to the 
; array in order.
; Then the less than pivot and greater than pivot partitions are passed 
; recursively to quicksort_array.
;
write_back:
LD DM,current_start_pointer
LD BM,current_end_pointer
; write_back_loop_lt
; pops values from stack that are less than pivot and writes to start of array
write_back_loop_lt:
POPB
EQAB
JMP RV,write_back_equal 
LDIM DB
INCD 
LD BM,current_end_pointer
JMP V,write_back_loop_lt
;
; write_back_equal
; First push current start, end and pivot to stack
; Then call quicksort_array on partition that is less than pivot
; Then pop current start, end and pivot and write all equal values
; to array
;
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
; set D to end of lt sub-array
DECD
; for recursion set current_end_pointer to end of lt sub-array
LD MD,current_end_pointer
; recursive quicksort_array call on lt sub-array
CALL V,quicksort_array
; now lt has been sorted, get previous pushed current start, end and pivot
POPA
; reset current end
POPB
LD MB,current_end_pointer
; get new start pos
POPD
;
; write_back_equal_loop
; pop equal values and write back to array
;
write_back_equal_loop:
POPB
GTBA
JMP RV,write_back_gt 
LDIM DB
INCD 
; if end of array reached now it means that no values are greater than pivot 
; so just return
LD BM,current_end_pointer
GTDB
RET R
JMP V,write_back_equal_loop
;
; write_back_gt 
; pops all gt values from stack and writes back to end of array
; then calls quicksort recursively on this partition
;
write_back_gt:
; sets current start to start of gt sub-array
LD MD,current_start_pointer
; B is already set to the first element greater than pivot
; pushed back to stack to make loop logic easier for me
PUSHB
; write_back_gt_loop
; pops from stack and writes back to array until end is reached
write_back_gt_loop:
POPB
LDIM DB
INCD
LD BM,current_end_pointer
GTDB
JMN RV,write_back_gt_loop
;
; write_back_gt_end
; recursively calls quicksort_array - current start and end are set to start and
; end of the gt array partition
;
CALL V,quicksort_array
; this array has now been sorted!
; return to calling code
RET
; end
end:
0