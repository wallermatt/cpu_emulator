; factorial
; load n 
n_pointer = 150
result_pointer = 151
n=7
LD AV,n
LD DV,n_pointer 
LDIM DA
PUSHA
PUSHP
JMP V,fadtorial
JMP V,end
fadtorial:
LD AM,n_pointer
LD BM,result_pointer
ADD AB
LD MA,result_pointer
; check n = 1
LD AM,n_pointer
LD BV,1
EQAB
JMP RV,end
DECA
LD MA,n_pointer
;JMP V,end
JMP V,fadtorial
end:
0