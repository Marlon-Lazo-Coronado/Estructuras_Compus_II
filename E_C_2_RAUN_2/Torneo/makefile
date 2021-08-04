objetivo1: dependencia1 dependencia2
	gtkwave Mux.vcd
	
dependencia1:
	
	emacs --batch Banco_de_Pruebas.v -f verilog-batch-auto
dependencia2:
	iverilog -o resultado Banco_de_Pruebas.v
	vvp resultado
