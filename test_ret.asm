; test
LD DV,100
PUSHP
JMP V,function1
PUSHP
JMP V,function1
PUSHP
JMP V,function1
JMP V,end
function1:
LDI MDV,99
INCD
POPA
INCA
INCA
JMPA
end:
0