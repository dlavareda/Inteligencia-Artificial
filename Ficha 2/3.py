"""Construa uma tabela como a seguinte, onde guarda para 10 diferentes problemas, a distância obtida usando a pesquisa informada e a não informada.
Por exemplo, comece por pedir o caminho de Faro a Bragança na primeira
experiência; na segunda de Beja a Lisboa; etc.. No final ache a média das
distâncias obtidas para cada tipo de pesquisa e tire conclusões.

+-----------------------+-------------------------------+-------------+---------------------------------+
|         Viagem        |    Não informada Largura   	|  Informada  |   Não informada Profundidade	|
+-----------------------+-------------------------------+-------------+---------------------------------+
|    Beja -> Faro       |        	    170           	|     170     |	             395       			|
|  Lisboa -> Porto      |      	        350           	|     350     |	             350 	    		|	
|   Braga -> Faro       |            	710	        	|     710     |	            1905		    	|
|   Viseu -> Portalegre |            	260           	|     260     |	            1580			    |
|   Evora -> Porto      |            	630	        	|     490     |	             540		    	|
|    Beja -> Braga      |              	750           	|     585     |	             665			    |
| Coimbra -> Guarda     |           	160           	|     160     |	             720			    |
|  Guarda -> Faro       |           	670          	|     530     |	            1315			    |
|    Faro -> Braganca   |           	870           	|     730     |	            1030		    	|
|  Lisboa -> Braganca   |           	560           	|     530     |	             720    			|
+-----------------------+-------------------------------+-------------+---------------------------------+
|         Média         |               486             |    451.5    |              922				|
+-----------------------+-------------------------------+-------------+---------------------------------+

"""