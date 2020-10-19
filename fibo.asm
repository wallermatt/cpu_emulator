; Fibonacci sequence
; define variables
previous=1
current=0
results_start=100
iterations=6
iterations_loc=51
temp_store=50
; load initial
LD AV,iterations
LD MA,iterations_loc
LD AV,current
LD BV,previous
LD DV,results_start
; main loop
start_loop:
LDIM DA
INCD
LD MA,temp_store
ADD AB
; check if max iterations
LD BM,iterations_loc
DECB
JMP CV,end
LD MB,iterations_loc
; load B with current and loop
LD BM,temp_store
JMP V,start_loop
end:
0