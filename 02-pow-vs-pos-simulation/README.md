# Simulación de Proof of Work y Proof of Stake

## Objetivo

Desarrollar una simulación básica de una red blockchain y comparar dos mecanismos de consenso: Proof of Work y Proof of Stake.

## Funcionamiento

La simulación crea bloques enlazados mediante hashes SHA-256. Cada bloque contiene:

- Índice
- Timestamp
- Transacciones
- Hash del bloque anterior
- Nonce
- Hash actual

## Proof of Work

En PoW, el sistema busca un nonce que permita generar un hash con un número determinado de ceros iniciales. Esto simula el trabajo computacional de la minería.

## Proof of Stake

En PoS, se selecciona un validador en función de su stake. Cuanto mayor es el stake, mayor es la probabilidad de ser seleccionado.

## Resultados observados

- PoW requiere más tiempo y esfuerzo computacional.
- PoS valida bloques de forma mucho más rápida.
- PoW basa su seguridad en coste computacional.
- PoS basa su seguridad en incentivos económicos.

## Ejecución

```bash
python reto2_blockchain.py
```

## Conclusión

PoW maximiza seguridad a través del coste computacional, mientras que PoS mejora la eficiencia y reduce el consumo de recursos, aunque introduce riesgos relacionados con la concentración de stake.
