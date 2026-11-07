# Datos

## Muestra incluida

`muestra_transacciones.csv` contiene 5 000 transacciones aleatorias extraídas del dataset completo con `random_state=42` (ver `muestra.py` en la raíz del proyecto). Se incluye para que el notebook pueda ejecutarse sin descargar el archivo completo.

## Dataset completo

El archivo original pesa 67 MB, por lo que no se incluye en el repositorio.

**Descarga:** [Bank Customer Segmentation en Kaggle](https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation)

1. Entra al enlace y pulsa **Download**.
2. Descomprime el archivo.
3. Copia `bank_transactions.csv` dentro de esta carpeta `data/`.

El archivo completo tiene 1 048 567 transacciones de 884 265 clientes distintos, correspondientes a aproximadamente agosto a octubre de 2016.

## Columnas principales

- `TransactionID`, `CustomerID`: identificadores de transacción y cliente.
- `CustomerDOB`: fecha de nacimiento (`1/1/1800` indica dato faltante).
- `CustGender`, `CustLocation`: género y ciudad del cliente.
- `CustAccountBalance`: saldo de la cuenta tras la transacción.
- `TransactionDate`, `TransactionTime`: fecha y hora de la transacción.
- `TransactionAmount (INR)`: monto en rupias indias.