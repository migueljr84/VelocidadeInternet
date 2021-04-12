

# Monitoramento velocidade internet
> Descrição do projeto

Neste projeto, criei um código em Python em que realiza a captura de velocidade de Download e Upload da internet local no qual você está se conectando.
Nele, atualizamos informaçoes em um arquivo .CSV, onde é alimentado a cada dois minutos, inserindo a velocidade(Download-Upload), data-hora-minuto no qual foi realizado essa captura.
A partir desse insumo de informações, montei um ambiente Elastic Search.
Para quem não conhece é uma tecnologia OpenSource, que realiza tratativa Extract Transformation Load (ETL) pelo Log Stash, armazenamento de informações (Elastic) e nos permite visualizar essas informações através do frame Kibana.
O intuito de utilizar o elastic, pois não gostaria apenas de saber das informações contidas naquela data hora e sim algo automatizado que nos permitisse termos uma visibilidade ao longo do tempo dos picos ocasionadas, ou seja, uma média de velociadade ao longo do período do tempo.
Com o meu processo ligado, neste caso o código Python ficaria alimentando o arquivo CSV, e cada 2 minutos o log stash iria ficar lendo o aquivo no qual está sendo atualizado e iria armazenas as informações no elastic Search.
Com essa arquitetura e processo montado e automatizado, o nosso frame Kibana nos iria viabilizar de tempos em tempos as informações consolidades de acordo com o período de tempo estabelecida.
No Kibana, montei um Dash Board com 4 plots, um Plot nos viabilizaria a média de velociadade de Download ao longo de período de tempo , um segundo plot teria o mesmo formato sendo que seria com velocidade de Upload, e os outros dois plots nos mostaria a média de velocidade de download e upload em todo período de tempo estabelecido.



## Inicialização do ambiente

Abaixo segue os passos para executar o Script Python juntamente com o inicio do ambiente ElasticSearch.
Vale uma pequena observação de quando iniciarmos o logStash, nele devemos obrigatoriamente chamar um arquivo .conf, será o responsável em ter toda a parametrização entre a captura do dado juntamente com o armazenamento.

```shell
python "C:\Temp\Elastic\Python\velocidade.py"
$ELASTICSEARCH_HOME/bin/elasticsearch.bat
$LOGSTASH_HOME/logstash.bat -f $LOGSTASH_HOME\files\stashOrder.conf
$KIBANAH_HOME/binkibana.bat
```


### Configuração Log Stash

Para iniciarmos o logStash, devemos customizar um arquivo de configuração, onde iremos atribuir de onde irá acontecer a captura de informações, realizar os filtros e conversões necessárias e por último o apontamento de onde essas informações serão aramzenadas.



## Licenciamento

Código aberto disponível para utlizações necessárias desenvolvido por Miguel Lima
