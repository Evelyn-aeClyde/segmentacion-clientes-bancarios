# Segmentación de clientes bancarios

Proyecto de análisis de datos para identificar segmentos de clientes a partir de transacciones bancarias, usando Python, pandas y K-Means.

## Problema

¿Qué grupos de clientes existen según su saldo, monto de transacciones, edad y perfil, y qué acción de negocio conviene para cada uno?

## Datos

- **Fuente:** dataset público "Bank Customer Segmentation" de Kaggle (banca de la India, montos en INR).
- **Tamaño del archivo completo:** 1 048 567 transacciones de 884 265 clientes distintos, con un periodo de aproximadamente 3 meses (agosto a octubre de 2016).
- **Muestra incluida:** `data/muestra_transacciones.csv` (5 000 transacciones aleatorias, `random_state=42`), usada para desarrollar y revisar la limpieza. El archivo completo (67 MB) no se incluye; ver `data/README.md` para descargarlo.

## Metodología

1. **Limpieza:** conversión de fechas de nacimiento y de transacción. El valor de relleno `1/1/1800` se trató como dato faltante. En la muestra de 5 000 filas, esto afectó a 280 registros.
2. **Filtro:** se excluyeron clientes menores de 18 años.
3. **Agregación por cliente:** número de transacciones, monto total, monto promedio, saldo promedio y edad.
4. **Transformación:** logaritmo para montos y saldos (muy asimétricos) y estandarización.
5. **Modelo:** K-Means con k=4, elegido con el método del codo y el coeficiente de silueta (0.298 para k=4 y 0.310 para k=5; se prefirió 4 por ser más fácil de interpretar).

## Resultados

La siguiente tabla proviene del modelo final entrenado sobre los **838 055 clientes** del archivo completo, no de la muestra incluida en el repositorio.

| Segmento | Clientes | % | Nº de transacciones (mediana) | Monto total (mediana, INR) | Saldo (mediana, INR) | Edad (mediana) |
|---|---|---|---|---|---|---|
| 0. Consumo medio | 334 036 | 39.9 % | 1 | 900 | 23 137 | 29 |
| 1. Bajo uso | 285 536 | 34.1 % | 1 | 108 | 7 211 | 26 |
| 2. Recurrentes | 120 638 | 14.4 % | 2 | 1 350 | 27 281 | 28 |
| 3. Alto saldo | 97 845 | 11.7 % | 1 | 1 176 | 64 300 | 46 |

**Lectura de cada segmento:**

- **Consumo medio:** el grupo más grande. Clientes jóvenes con uso ocasional y saldo moderado.
- **Bajo uso:** saldo y montos bajos. Candidatos para campañas de activación.
- **Recurrentes:** los únicos con más de una transacción en el periodo. Son los clientes más activos.
- **Alto saldo:** clientes mayores con saldo alto. Candidatos para productos de inversión o de mayor monto.

## Limitaciones

- La mayoría de clientes tiene una sola transacción en el periodo, así que la segmentación se basa sobre todo en saldo, edad y monto.
- Los datos son de una banca de la India. La técnica es transferible, pero los montos no representan a clientes peruanos.
- La separación entre grupos es moderada (silueta cercana a 0.3), lo que es común en datos bancarios.

## Cómo ejecutarlo

1. Clona el repositorio.
2. Crea un entorno virtual e instala dependencias: `pip install -r requirements.txt`
3. Descarga el dataset completo si quieres reproducir el análisis completo (ver `data/README.md`).
4. Abre `notebooks/01_limpieza.ipynb` y ejecuta las celdas en orden.

## Estructura

- `data/`: muestra de datos y documentación del dataset.
- `notebooks/01_limpieza.ipynb`: limpieza, agregación por cliente y segmentación.
- `muestra.py`: script que generó la muestra.
- `requirements.txt`: dependencias con versiones fijas.