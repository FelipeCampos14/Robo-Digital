O projeto foi organizado em duas partes principais, os códigos, objetos e cena do godot em uma pasta e todos os códigos de backend, frontend e banco de dados em outra.

Para entender é necessário explicar a segunda parte antes:

O backend e frontend foram estruturados de maneira simples para que executassem apenas o necessário, que é o recebimento das coordenadas por meio de um formulário e envio delas para o godot.

Há duas rotas principais que executam as funções ditas acima. A primeira é a "coord" e a segunda é a "godot". A função de coordenadas recebe os valores, os adiciona a uma sessão, mediante as chaves da classe Coordenada, que organiza os dados para enviá-los ao db. Já a segunda rota, faz uma requisição para o banco de dados e dispõe a coordenada na tela para que futuramente o godot possa ler os números. Além disso, no frontend há uma integração onde é disposta a última coordenada enviada.

O Banco de dados foi estruturado usando SQL Alchemy e segue a mesma princípio simples das outras estruturas: de apenas executar sua função, ou seja, armazenar as coordenadas em uma única tabela chamada coordenada que possui as chaves "x","y" e "z", uma para cada vetor do robô.

Já na parte do godot, foi feito um código que busca o endpoint "\godot" de acordo com a segunda rota, já citada no backend. Além disso, há uma função lê a informações que foram dipostas no body do endpoint. Tais informações são as coordenadas, que são adicionadas a uma variável e essa variável e transformada na posição do objeto no godot, por meio do comando "translate(Vector(*variável*))"