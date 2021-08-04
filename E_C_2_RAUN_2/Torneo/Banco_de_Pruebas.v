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
	wire prediction_gh;
	wire prediction_ph;
	wire [n-1:0]ph_PC;
	wire [n-1:0]gh_PC;
	wire [n-1:0]nex_PC;
	wire prediction;
	
	parameter n=32;
	parameter size=16;
	parameter delta_t=4;

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
								 .PC			(PC[n-1:0]),
								 .prediction_gh		(prediction_gh),
								 .prediction_ph		(prediction_ph),
								 .ph_PC			(ph_PC[n-1:0]),
								 .gh_PC			(gh_PC[n-1:0]));
						
	
	
	// Probador: generador de señales y monitor
	probador probador_Inst( /*AUTOINST*/
			       // Outputs
			       .reset		(reset),
			       .clock		(clock),
			       .PC		(PC[32-1:0]),
			       .prediction_gh	(prediction_gh),
			       .prediction_ph	(prediction_ph),
			       .ph_PC		(ph_PC[32-1:0]),
			       .gh_PC		(gh_PC[32-1:0]),
			       .fix_result	(fix_result),
			       // Inputs
			       .nex_PC		(nex_PC[32-1:0]),
			       .prediction	(prediction));
endmodule
