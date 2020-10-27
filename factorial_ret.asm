; factorial
; load n 
n_pointer = 150
result_pointer = 151
n=10
LD AV,n
LD DV,n_pointer 
LDIM DA
PUSHP
JMP V,fadtorial
JMP V,end
fadtorial:
; check n = 1
LD AM,n_pointer
LD BV,0
EQAB
JMP RV,return
PUSHA
DECA
LD MA,n_pointer
PUSHP
JMP V,fadtorial
LD AM,result_pointer
POPB
ADD AB
LD MA,result_pointer
JMP V,return
return:
POPB
INCB
INCB
JMP B
end:
0