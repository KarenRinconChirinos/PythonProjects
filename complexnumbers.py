#Complex numbers
z  = 2 + 5j;
type(z)

z = complex(1,-7)
type(z)
z.real # obtiene la parte real con el metodo complex
z.imag # obtiene la parte imaginaria con el metodo complex

#Operations
z1 = 2- 6j
z2 = 5 + 4j

z3 = z1 + z2
z3 = z1 - z2
z3 = z1 * z2
z3 = z1 / z2

#Conjugado de un numero complejo
#Es cambiar de sigo al numero imaginario
z = -2 + 1j
z.conjugate()

#Modulo de un numero complejo
z = -2j
abs(z)

#Argumento de un numero complejo
import cmath
cmath.phase(z)

#Forma binomica  a polar (-0, -2j)
#import cmath 
z
cmath.polar(z) #devolvera una tupla

#Forma polar  a binomica 
cmath.rect(abs(z), cmath.phase(z))



