# Análise da qualidade do vinho verde usando características Físico-químicas

Vinhos Verdes são vinhos de origem na região noroeste de Portugal, na província do Minho. Nada tem a ver com sua coloração,
que apresentam nas variedades branco e tinto. 

Neste trabalho vou tentar classificar a qualidade do vinho, analisando apenas as suas características fisico-quimicas, 
disponibilziadas através de um conjunto de dados.

## Análise Exploratória

Analisando os dados de forma a conhecê-lo, descobri valores com entradas inesperadas na coluna 'Alcohol', que possuiam o seguinte formato:

111.111.111.111.111

Dessa forma, foi utilizado uma Regex para substituir o padrão por valores não númericos *(Not A Number - NAN)* e removidas as observações em seguida, que foram
aproximadamente 40 linhas.

## Estratégia de modelagem

O primeiro procedimento adotado foi transformar as variáveis não númericas em valores que pudessem ser analisados. 

A coluna que contém os valores da graduação alcoolica da bebida estava em formato não númerico, devido a inconsistência encontrada. 
Os dados foram convertidos após o tratamento. Em seguida codifiquei as variáveis que indicavam o tipo do vinho como tinto ou branco, 
transformando em variáveis "dummie" para que pudessem ser convertidas em códigos. 

## Modelo selecionado

Para validação do modelo, utilizei duas técnicas para análise de impacto das características na classificação da qualidade do vinho. 
A primeira foi utilizar o selectkfold, com teste de hipótese chi2 para analisar os dados, obtendo o seguinte

|Features     |   Score|
|-------------:|--------:|
|total sulfur dioxide    | 1254.610054|
|    free sulfur dioxide |  916.761779|
|                density |  290.704245|
|         residual sugar |  232.191057|
|               alcohol  |  200.443888|
|              type_Red  |   88.581788|

Decidi, em primeiro momento selecionar as 5 com maiores valores. 

Mas em seguida fiz outra avaliação com o ExtraTreeClassifier, obtendo novas características relevantes. 
As utilizei no restante da abordagem do problema

## Modelos

Para iniciar a classificação, separei as características relevantes da característica desejada: qualidade. 
A partir daí, separei alguns algoritmos simples e conhecidos, como:

- KNN
- Árvores de Decisão
- Random Forest
- SVM (SVC)

Os algoritmos foram usados com o mínimo de alteração do padrão estabelecido pelo framework

Separei os dados de treino e teste, em uma proporção de 75/25, para tentar obter um resultado razoável. 

## Validação

Os resultados ficaram aquém do desejado. Utilizei algumas técnicas para tentar aprimorar o resultado, como a normalização e padronização dos 
valores das observações, mas não encontri alteração satisfatória dos valores. 

Utilização da acurácia como única medida de validação do modelo não é a melhor prática, mas já auxilia na avaliação do desempenho do algoritmo. Em trabalhos futuros, 
pretendo utilizar técnicas como Precisão, Revocação e medidas F. 

## Conclusão

Creio que há melhorias a serem feito nos dados, de forma que o modelo fique mais robusto. A utilização de classificadores diferentes, e o pouco ganho no desempenho final,
me indica que não estou percebendo alguma relação nas características. 

## Trabalhos futuros

Ainda trabalharei nesse conjunto de dados. É um desafio interessante. As próximas abordagens utilizarão duas estratégias:
- Ajustes dos parâmetros dos algoritmos, para obtenção de melhor resultado. Utilizarei do *GridSearch* para auxiliar nessa atividade
- Utilização de redes neurais e estratégias mais recentes de classificação
