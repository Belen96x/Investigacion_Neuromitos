#importación de librerías

import spacy

#Segmentación método 2

from spacy.language import Language
import spacy

text = """¿Quiénes somos?. Familias, docentes, estudiantes e integrantes de la comunidad en general en alerta por el retorno a la presencialidad en las escuelas sin condiciones de seguridad. ¿Cómo nos organizamos?. La convocatoria a participar del colectivo es abierta al público. Nos comunicamos por redes y grupos de WhatsApp organizados en comisiones para desarrollar acciones que visibilicen y denuncien la problemática que estamos atravesando. Elaboramos informes con trabajo de profesionales de distintas disciplinas que integran el colectivo, pronunciamientos, gacetillas, contenido para redes sociales y medios de comunicación. El sentido de lo colectivo. Entendemos que la lucha colectiva es clave para exigir que se respeten nuestros derechos. En tiempos de lógicas "individuales", proponemos actuar desde los lazos entre diferentes actores de la comunidad educativa, poniendo en práctica la solidaridad, la empatía, el debate y la construcción colectiva de estrategias y acciones para cuidarnos entre todxs. ¿Qué puedo hacer si no quiero presencialidad en pandemia?. Es tu derecho, podes elegir. Desde el colectivo brindamos herramientas para hacer el pedido de excepción formalmente. Lxs invitamos a leer la entrada en el blog 'Excepción de Asistencia'. ¿Qué exigimos?. A partir de las primeras reuniones virtuales multitudinarias se definieron una serie de demandas para el retorno seguro a la escuela.​ Teletrabajo para madres y padres de menores de 14 años. Licencias en el trabajo (por razones de salud y cuidado de menores). Ayudas por parte del Estado para familias desempleadas o con empleos informales para garantizar el cuidado de las niñas y los niños. Índice o "semáforo epidemiológico" (CDC SAP) – Desde nuestro colectivo exigimos que el gobierno de CABA explique cuál es el criterio que utiliza para definir la apertura de la presencialidad en las escuelas. El semáforo epidemiológico establecido por el Consejo Federal de Educación o el de la SAP que toma como referencia el semáforo de los CDC indican que la Ciudad de Buenos Aires está en rojo. Entrega de dispositivos y conectividad gratuita. Entrega de libros de texto de todas las áreas, kits escolares, textos literarios y cuadernillos para utilizar hasta que estén las condiciones dadas para el retorno a la presencialidad y para que, en caso de tener que volver a suspender después, los recursos necesarios para la virtualidad ya estén garantizados. Transporte escolar – Por lo expresado anteriormente, proponemos que se haga uso del trasporte escolar ya existente para el plan de natación y salidas didácticas para ponerlo a disposición de las familias que vivan a más de 15 cuadras de sus escuelas de manera gratuita. Condiciones de bioseguridad dentro de las escuelas (insumos y personal de limpieza) bajo control de comisiones conformadas por las direcciones de las escuelas, docentes y cooperadoras que tengan la potestad de suspender las clases presenciales toda vez que los protocolos no puedan llevarse adelante o no estén dadas las condiciones. Distanciamiento mínimo de 2 metros en las aulas y todos los espacios de permanencia de estudiantes que es la distancia mínima para evitar contagios. Ventilación de las aulas y de todos los espacios de permanencia. Reducción de la cantidad de alumnos por grupo.  Para que esto sea posible es necesario el desdoblamiento de los grupos que implica más aulas y más docentes. Exigimos el acondicionamiento para el uso escolar de inmuebles ociosos para fines escolares. Señalamos, como lo venimos haciendo desde siempre, la necesidad de un plan integral de construcción de escuelas. La falta de vacantes va año a año en aumento y la pandemia ha dejado al descubierto con crudeza la falta de aulas y el derrumbe edilicio en que se encuentran las escuelas públicas. Para la reducción de cantidad de alumnos por grupo es necesario el nombramiento de cargos docentes y profesionales de emergencia bajo los lineamientos del Estatuto Docente. Tarjeta alimentaria para todos los niveles y modalidades del sistema educativo por igual (o bolsones saludables, nutritivos y en cantidad y calidad acorde a las necesidades de los estudiantes y sus familias).​"""


nlp = spacy.load("es_core_news_sm")
doc = nlp(text)
"Before:", [sent.text for sent in doc.sents]

@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == ".":
            doc[token.i + 1].is_sent_start = True
    return doc

nlp.add_pipe("set_custom_boundaries", before="parser")
doc = nlp(text)
segmentado = [sent.text for sent in doc.sents]

print(segmentado)

