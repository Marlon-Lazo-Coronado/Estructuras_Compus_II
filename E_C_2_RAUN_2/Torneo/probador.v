module probador(
		input [32-1:0]nex_PC,
		input prediction,
		output reg reset,
		output reg clock,
		output reg [32-1:0]PC,
		output reg prediction_gh,
		output reg prediction_ph,
		output reg [32-1:0]ph_PC,
		output reg [32-1:0]gh_PC,
		output reg fix_result
	);
	
	initial begin
		$dumpfile("Mux.vcd");
		$dumpvars;
		$display ("\t\t\tclock,\treset,\tPC, \tprediction_gh,\tprediction_ph,\tph_PC,\tgh_PC,\tnex_PC");
		$monitor($time,"\t%b\t%b\t\t%b\t%b\t%b\t%b\t%b\t%b", clock, reset,PC,prediction_gh,prediction_ph,ph_PC,gh_PC,nex_PC);
		
		// Valores iniciales de las señales.
		reset = 1;
		PC = 'h00000000;
		prediction_gh = 'b0;
		prediction_ph = 'b0;
		ph_PC = 'h00000000;
		gh_PC = 'h00000000;        
		fix_result = 0;
		
		repeat (1000) begin PC=0;
		repeat (10) begin				
        		@(posedge clock);
        			
        		reset = 0;
			PC = PC+1;
			prediction_gh = 'b0;
			prediction_ph = 'b1;
			ph_PC = ph_PC+1;
			gh_PC = gh_PC+10; 
			
			fix_result = fix_result+1;
		end end
		
		repeat (1000) begin PC=0;
		repeat (10) begin				
        		@(posedge clock);
        			
        		reset = 0;
			PC = PC+1;
			prediction_gh = 'b1;
			prediction_ph = 'b0;
			ph_PC = ph_PC+1;
			gh_PC = gh_PC+10;   
			
			fix_result = fix_result+1;
		end end
		
		repeat (1000) begin PC=0;
		repeat (10) begin				
        		@(posedge clock);
        			
        		reset = 0;
			PC = PC+1;
			prediction_gh = 'b1;
			prediction_ph = 'b0;
			ph_PC = ph_PC+1;
			gh_PC = gh_PC+10;   
			
			fix_result = fix_result+3;
		end end
		
		$finish;
		
	end
	// Reloj
	initial	clock 	<= 0;			// Valor inicial al reloj, sino siempre será indeterminado
	always	#1 clock 	<= ~clock;		// Hace "toggle" cada 4 segundos
endmodule
