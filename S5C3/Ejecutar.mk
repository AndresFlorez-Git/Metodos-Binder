plotDatos.py: datos.dat FlorezAndres_S5C3_ODEs.cpp
	python plotDatos.py
	rm datos.dat 
datos.dat:
	g++ FlorezAndres_S5C3_ODEs.cpp
	./a.out> datos.dat
    