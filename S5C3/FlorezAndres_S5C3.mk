FlorezAndres_S5C3_plots.py: datos.dat FlorezAndres_S5C3_ODEs.cpp
	python FlorezAndres_S5C3_plots.py
	rm datos.dat 
datos.dat:
	g++ FlorezAndres_S5C3_ODEs.cpp
	./a.out> datos.dat
	./a.out
    