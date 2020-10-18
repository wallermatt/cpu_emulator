; load memory locations 100-110 with 9,8,7,6,5,4,3,2,1,0
start_loc=100
i=10
LD AV,start_loc
LD BV,i
loop:
DEC B
JMP CV,12
LDIM AB
INC A
JMP V,loop
0