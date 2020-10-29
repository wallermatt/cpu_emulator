; factorial
; load n 
n_pointer = 150
result_pointer = 151
n=20
LD AV,n
LD DV,n_pointer 
LDIM DA
CALL V,fadtorial
JMP V,end
fadtorial:
; check n = 1
LD AM,n_pointer
LD BV,0
EQAB
RETR
PUSHA
DECA
LD MA,n_pointer
CALL V,fadtorial
LD AM,result_pointer
POPB
ADD AB
LD MA,result_pointer
RET
end:
0