## Representação do Conhecimento

- definido pelos parâmetros livres (pesos sinápticos e bias);

#### Projeto de uma rede neural:
1. Selecionar uma arquitetura, selecionar quantidades de camadas e neurônios, definir função de ativação, definir função de perda, algoritmo de otimização, treinamento supervisionado.
2. Validação, testar a rede com dados nao apresentados anteriormente. O desempenho da rede depende dos acertos nessa etapa. Esta etaá é a Generalização.

#### 'Regras' da representação do conhecimento:
- Entradas similares de classes similares devem produzir representações similares, consequentemente devem ser classificadas como pertencentes à mesma categoria.
- Devem ser atribuídas representações diferentes na rede a itens que devem ser categorizados como classes separadas.
- Se uma característica é importante, então deve haver um grande número de neurônios envolvidos na representação daquele item na rede.
- Informação prévia e invariâncias devem ser incorporadas no projeto de uma rede neural. (resulta em uma estrutura especializada)(redes neurais convolucionais, CNNs)


### Como incorporar informação prévia no Projeto de uma Rede Neural?
- Restringir a arquitetura da rede pelo uso de **campos receptivos**;
- Restringir a escolha de pesos através do uso de **compartilhamento de pesos**.

### Como implementar uma rede neural to tipo classificador invariante a transformaçoes? 
- **Invariância por Estrutura:** imposta diretamente na estrutura da rede, mudando as conexões sinápticas entre os neurônios da rede para que versões transformadas da mesma entrada seja forçada a produzir a mesma saída.
- **Invariância por Treinamento:** Incluir entradas transformadas no conjunto de amostras de treinamento.
- **Espaços de características invariantes:** Extrair o conteúdo essencial das entradas que sejam invariantes a transformaçoes.

