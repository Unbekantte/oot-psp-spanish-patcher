# oot-psp-spanish-patcher
Patcher to use the Spanish translation of The Legend of Zelda: Ocarina of Time with oot-PSP.
Leeme
# Ocarina of Time PSP - Spanish Patcher

Parcheador no oficial para utilizar la traducción castellana de
The Legend of Zelda: Ocarina of Time con el port nativo oot-PSP.

## Qué hace

Este programa adapta los diálogos castellanos de una ROM ya traducida
para que puedan ser utilizados por oot-PSP.

Actualmente:

- Los diálogos aparecen en castellano.
- La fuente castellana está incluida mediante los datos proporcionados
  por la ROM del usuario.
- Algunos menús permanecen en inglés.

## Este repositorio NO incluye

- The Legend of Zelda: Ocarina of Time
- ROMs originales o modificadas
- Assets extraídos del juego
- EBOOT.PBP
- oot_psp_assets.bin
- El parche de traducción de Blade133bo

Cada usuario debe proporcionar sus propios archivos.

## Requisitos

### ROM original

The Legend of Zelda: Ocarina of Time USA NTSC 1.0

MD5:

5bd1fe107bf8106b2ab6650abecd54d6

La ROM debe llamarse:

baserom.z64

### ROM traducida

Se necesita una copia de la misma ROM NTSC-U 1.0 a la que se haya
aplicado la traducción castellana compatible.

Debe llamarse:

oot-ntsc-1.0.z64

Traducción utilizada durante el desarrollo:
Blade133bo - Ocarina of Time Castellano.

### oot-PSP

También se necesitan desde una instalación funcional de oot-PSP:

EBOOT.PBP

y:

data/segments/oot_psp_assets.bin

## Uso

Crea una carpeta y coloca dentro:

oot_psp_es_patch.py
baserom.z64
oot-ntsc-1.0.z64
EBOOT.PBP
oot_psp_assets.bin

Ejecuta:

run_patcher.bat

o desde una terminal:

python oot_psp_es_patch.py

Si todo es correcto se creará:

salida_es/EBOOT.PBP
salida_es/oot_psp_assets.bin

Sustituye estos archivos en tu instalación de oot-PSP:

EBOOT.PBP
-> raíz de la carpeta del port

oot_psp_assets.bin
-> data/segments/oot_psp_assets.bin

Haz siempre una copia de seguridad de los archivos originales.

## Compatibilidad

Probado con la versión de oot-PSP utilizada durante el desarrollo
y con Ocarina of Time NTSC-U 1.0.

Como oot-PSP continúa en desarrollo, futuras versiones podrían cambiar
la disposición interna de los archivos y requerir una actualización
de este parcheador.

## Créditos

- oot-PSP: z2442 y colaboradores
- ZeldaRET / oot: proyecto de decompilación de Ocarina of Time
- Traducción castellana: Blade133bo
- Adaptación de la traducción al port PSP: este proyecto

Este proyecto no está afiliado con Nintendo, ZeldaRET, oot-PSP ni con
el autor de la traducción.
