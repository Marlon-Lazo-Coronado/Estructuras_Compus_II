`timescale 	1s				/ 100ps
// escala	unidad temporal (valor de "#4") / precisión
// Pueden omitirse y llamarse desde el testbench


`include "tournament.v"
`include "probador.v"
//`include "cmos_cells.v"



module BancoPruebas; // Testbench
	//Los buses se deben declarar en lineas aparte por ser de diferentes tamaños.
	wire reset;
	wire clock;
	wire [n-1:0]PC;
	wire [n-1:0] etiqueta;
	wire [n-1:0]nex_PC;
	wire prediction;
	
	parameter n=32;
	parameter size=16;

	// Descripción conductual de alarma, las instancias se realizan por medio de AUTOINST.
	tournament #(/*AUTOINSTPARAM*/
		     // Parameters
		     .n			(n),
		     .size		(size)) tournament_inst ( /*AUTOINST*/
								 // Outputs
								 .nex_PC		(nex_PC[n-1:0]),
								 .prediction		(prediction),
								 // Inputs
								 .reset			(reset),
								 .clock			(clock),
								 .fix_result		(fix_result),
								 .etiqueta		(etiqueta[n-1:0]),
								 .PC			(PC[n-1:0]));
						
	
	
	// Probador: generador de señales y monitor
	probador probador_Inst( /*AUTOINST*/
			       // Outputs
			       .reset		(reset),
			       .clock		(clock),
			       .PC		(PC[32-1:0]),
			       .etiqueta	(etiqueta[32-1:0]),
			       .fix_result	(fix_result),
			       // Inputs
			       .nex_PC		(nex_PC[32-1:0]),
			       .prediction	(prediction));
endmodule
