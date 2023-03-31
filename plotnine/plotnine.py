#Treinando plotnine
from plotnine import *
import pandas as pd
import numpy as np

dados=pd.read_csv("fifa_sample_wsR.csv")
pd.set_option('display.max_columns', None)
dados.head()

#Histograma
(ggplot(dados)+geom_histogram(aes("age"), color="black", fill="#00AFBB")
 +theme_linedraw())
#themes preferidos: theme_matplotlib, theme_linedraw, theme_xkcd 
#cores preferidas: "#d11141","blue","#00b159","#00aedb"

#Boxplot
(ggplot(dados) + aes(0,"age") +
 geom_boxplot(fill="#00AFBB")+
 theme_classic() + coord_flip() +
 labs(x="",  y="Idade")
 )

#Barras
(ggplot(dados)+aes("preferred_foot")+geom_bar(fill="#00aedb")+theme_matplotlib()+
labs(y = "Quantidade", x = "Pé Preferido"))

def combine(counts, percentages):
    fmt = '{} ({:.1f}%)'.format
    return [fmt(c, p) for c, p in zip(counts, percentages)]

#Barras com número em cima da barra
(ggplot(dados)+aes("preferred_foot")+geom_bar(fill="#d11141")+theme_matplotlib()+
labs(y = "Quantidade", x = "Pé Preferido")
+geom_text(
     aes(label=after_stat('combine(count, prop*100)'), group=1),
     stat='count',
     nudge_y=0.125,
     va='bottom'
 ))

#Dispersão
(ggplot(dados) + aes("height_cm",  "weight_kg") + geom_point(color="red")
+theme_linedraw())
dados["weight2"]=dados["weight_kg"]+10
#Linhas separadas e colocando legenda
#Ver depois

#dados2=pd.DataFrame({"teste": np.row_stack((dados[]))})
(ggplot(dados)+geom_point(aes("height_cm", "weight_kg", color='red'))
+ geom_point(aes("height_cm", "weight2", color="blue"))
+scale_color_identity(guide='legend',name='My color legend'))
