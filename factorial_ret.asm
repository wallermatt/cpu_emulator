; factorial
; load n 
n_pointer = 150
result_pointer = 151
n=2
LD AV,n
LD DV,n_pointer 
LDIM DA
PUSHA
PUSHP
JMP V,fadtorial
POPA
LD MA,result_pointer
JMP V,end
fadtorial:
; check n = 1
LD AM,n_pointer
PUSHA
LD BV,0
EQAB
JMP RV,return
DECA
LD MA,n_pointer
;JMP V,end
JMP V,fadtorial
POPA
LD BM,result_pointer
ADDAB
LD MA,result_pointer
JMP V,return
return:
POPB
INCB
INCB
JMP B
end:
0