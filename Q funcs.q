// Problema 1
par:{?[l,$[n mod 2;0b;()],l:((n:count x)div 2)#10b;reverse x;x]}

// Problema 2
noRepetitions: {raze {x[y] cross (y+1)_x}[x;] peach til[count[x]-1]}

// Problema 3
f: {select from x where{1< last deltas((first where x="@")*($[((count x where x="@")<>1) or (first x = "@");0N;1]),(last where x=".") * $[(last x = ".");0N;1]) }each c2}

// Tabla de prueba Problema 3
t:([] c1: til 9; c2: ("usuario1@dominio.com";"@dominio.com";"invalido";"'usuario3@dominio.com";"usu.ario4@dominio";"'usu@dominio.com";"usuari.o6@dominio.com";"usuario@7@dominio.com";"invalido"))
