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










module tournament #(parameter n=32, size=16, delta_t=4)( //El alto de la tabla es (2**size)-1
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
//Para comparar despues
reg [delta_t-1:0] fifo_ph;
reg [delta_t-1:0] fifo_gh;
reg [delta_t-1:0] fifo_prediction;
reg [delta_t-1:0] fifo_swich_0;
reg [delta_t-1:0] fifo_swich_1;
reg [delta_t-1:0] fifo_PC [n-1:0]; //Ojo
reg prediction_ph_dt;
reg prediction_gh_dt;
reg prediction_dt;
reg [1:0]swich_dt;

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
		
		//=============================================================
		prediction_ph_dt = fifo_ph[delta_t-1];
		prediction_gh_dt = fifo_gh[delta_t-1];
		prediction_dt = fifo_prediction[delta_t-1];
		swich_dt[0] = fifo_swich_0[delta_t-1];
		swich_dt[1] = fifo_swich_1[delta_t-1];
		//==============================================================

		//Actualizar el BHT, planteamos varios casos, esto se hace instantaneo, el despase de tiempo lodebe de traer fix_result
		if (fix_result == 0 && prediction_ph_dt == 1 && prediction_gh_dt == 0) begin//Pegamos!
			if (swich_dt == 2'b11)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]+1;
		end
		else if (fix_result == 0 && prediction_ph_dt == 0 && prediction_gh_dt == 1) begin//Nos acercamos a pshare
			if (swich_dt == 2'b00)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]-1;
		end
		else if (fix_result == 1 && prediction_ph_dt == 1 && prediction_gh_dt == 0) begin//Nos hacercamos a pshare
			if (swich_dt == 2'b00)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]-1;
		end
		else if (fix_result == 1 && prediction_ph_dt == 0 && prediction_gh_dt == 1) begin//Nos acercamos a gshare
			if (swich_dt == 2'b11)
				table_states[PC] = table_states[PC];
			else
				table_states[PC] = table_states[PC]+1;
		end
		//else 
			//table_states[PC] = table_states[PC];
		
		if (fix_result == prediction_dt)
			hit = hit+1;
		else
			miss = miss+1;
	end 
end

always @(posedge clock) begin

	if (reset) begin
		prediction_ph_dt<= 0;
		prediction_gh_dt<= 0;
		prediction_dt<= 0;
		swich_dt <= 0;
    		fifo_ph <= 0;
    		fifo_gh <= 0;
    		fifo_prediction <=0;
    		fifo_swich_0  <=0;
    		fifo_swich_1  <=0;
	end
	else begin
		fifo_ph[0] <= prediction_ph;
		fifo_ph <= fifo_ph >>1;
    
		fifo_gh[0] <= prediction_gh;
		fifo_gh <= fifo_gh >>1;

		fifo_prediction[0] <= prediction;
		fifo_prediction <= fifo_prediction >>1;
		
		fifo_swich_0[0] <= swich[0];
		fifo_swich_0 <= fifo_swich_0 >>1;
		fifo_swich_1[0] <= swich[1];
		fifo_swich_0 <= fifo_swich_1 >>1;
	end
end

endmodule
