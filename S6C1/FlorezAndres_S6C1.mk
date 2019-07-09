    
FlorezAndres_S6C1_plots.py: datos.dat FlorezAndres_S6C1.cpp
	python FlorezAndres_S6C1_plots.py
	rm datos.dat
datos.dat:
	g++ FlorezAndres_S6C1.cpp
	./a.out> datos.dat
    