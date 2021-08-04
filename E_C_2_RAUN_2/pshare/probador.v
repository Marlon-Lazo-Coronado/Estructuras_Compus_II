module probador(
		input [32-1:0]nex_PC,
		input prediction,
		output reg reset,
		output reg clock,
		output reg [32-1:0]PC,
		output reg [32-1:0] etiqueta,
		output reg fix_result
	);
	
	initial begin
		$dumpfile("Mux.vcd");
		$dumpvars;
		$display ("\t\t\tclock,\treset,\tPC,\tnex_PC");
		$monitor($time,"\t%b\t%b\t\t%b\t%b", clock, reset,PC,nex_PC);
		
		// Valores iniciales de las señales.
		reset = 1;
		PC = 'h00000000;
		etiqueta = 'h00000000;        
		fix_result = 0;
		
		repeat (100) begin PC=0;
		repeat (10) begin				
        		@(posedge clock);
        			
        		reset = 0;
			PC = PC+1;
			etiqueta = etiqueta+10; 
			
			fix_result = 'b1;
		end end
		
		repeat (100) begin PC=0;
		repeat (10) begin				
        		@(posedge clock);
        			
        		reset = 0;
			PC = PC+1;
			etiqueta = etiqueta+10;   
			
			fix_result = 'b0;
		end end
		
		$finish;
		
	end
	// Reloj
	initial	clock 	<= 0;			// Valor inicial al reloj, sino siempre será indeterminado
	always	#1 clock 	<= ~clock;		// Hace "toggle" cada 4 segundos
endmodule
