# Smart Contract Escrow

## Objetivo

Desarrollar y probar un smart contract de depósito en garantía usando Solidity y Remix IDE.

## Qué es un escrow

Un escrow es un sistema donde los fondos quedan bloqueados hasta que se cumple una condición acordada entre las partes.

## Funcionamiento

1. El payer despliega el contrato y deposita ETH.
2. El contrato almacena los fondos.
3. El payer ejecuta `release()`.
4. El contrato transfiere los fondos al payee.

## Variables principales

- `payer`: dirección del pagador.
- `payee`: dirección del beneficiario.
- `amount`: cantidad depositada.
- `isReleased`: estado de liberación del pago.

## Funciones

### constructor()
Inicializa el contrato y recibe el depósito inicial.

### release()
Libera los fondos al beneficiario.

### getBalance()
Devuelve el balance actual del contrato.

## Pruebas realizadas

En Remix IDE se verificó:

- Despliegue del contrato con 1 ETH.
- Estado inicial: `isReleased = false`.
- Balance inicial: 1 ETH.
- Ejecución de `release()`.
- Estado final: `isReleased = true`.
- Balance final: 0 ETH.

## Limitación detectada

El contrato básico depende de que el `payer` libere el pago. Para mejorar el sistema podrían añadirse:

- Árbitro externo
- Contrato multifirma
- Liberación automática por tiempo
- Oráculos para confirmar entrega

## Conclusión

El contrato demuestra cómo blockchain puede sustituir mecanismos tradicionales de confianza mediante reglas programables, aunque en aplicaciones reales requiere mecanismos adicionales de resolución de disputas.
