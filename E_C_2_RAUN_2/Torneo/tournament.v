module tournament #(parameter n=32, size=16)( //El alto de la tabla es (2**size)-1
			input reset,
			input clock,
			input fix_result,
			input [n-1:0]PC,
			input prediction_gh,
			input prediction_ph,
			input [n-1:0]ph_PC,
			input [n-1:0]gh_PC,
			output reg [n-1:0]nex_PC,
			output reg prediction);

reg [1:0]table_states[0:1000];
integer i;
reg [1:0]swich;
reg [n-1:0]miss;
reg [n-1:0]hit;

//Logica combinacional
always @(*) begin

	if (reset) begin
		swich[1:0] = 2'b00;
		miss[n-1:0] = 32'h00000000;
		hit[n-1:0] = 32'h00000000;
		
		for (i=0; i<=(2^size)-1; i++)
			table_states [i] = 2'b00;
	end
	else begin
		swich = table_states[PC];
		
		if ( swich == 2'b00 || swich == 2'b01)begin 
			nex_PC = ph_PC;
			prediction = prediction_ph;
		end
		else begin
			nex_PC = gh_PC;
			prediction = prediction_gh;
		end	

		//Actualizar el BHT, planteamos varios casos, esto se hace instantaneo, el despase de tiempo lodebe de traer fix_result
		if (fix_result == 0 && prediction_ph == 1 && prediction_gh == 0) begin//Pegamos!
			if (swich == 2'b11)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]+1;
		end
		else if (fix_result == 0 && prediction_ph == 0 && prediction_gh == 1) begin//Nos acercamos a pshare
			if (swich == 2'b00)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]-1;
		end
		else if (fix_result == 1 && prediction_ph == 1 && prediction_gh == 0) begin//Nos hacercamos a pshare
			if (swich == 2'b00)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]-1;
		end
		else if (fix_result == 1 && prediction_ph == 0 && prediction_gh == 1) begin//Nos acercamos a gshare
			if (swich == 2'b11)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]+1;
		end
		else
			table_states[PC] = table_states[PC];
		
		if (fix_result == prediction)
			hit = hit+1;
		else
			miss = miss+1;
	end 
end

endmodule
