
# Ocarina of Time PSP - Spanish Patcher

Parcheador no oficial para utilizar la traducción castellana de
The Legend of Zelda: Ocarina of Time con el port nativo oot-PSP.
Puedes encontrar el port aqui: https://github.com/z2442/oot-PSP

## Estado actual

- Los diálogos principales funcionan en castellano.
- Los caracteres y la fuente española funcionan correctamente.
- Algunos menús permanecen en inglés.
- El parcheador ha sido probado con Ocarina of Time USA NTSC-U 1.0.
- Es necesario tener previamente una instalación funcional de oot-PSP.

---

## Importante

Este parcheador NO instala oot-PSP por sí solo.

Antes de utilizarlo debes haber instalado y ejecutado correctamente el
port original de oot-PSP al menos una vez.

El parcheador necesita archivos generados por una instalación funcional
del port.

También necesitas dos copias de la misma versión de Ocarina of Time:

1. Una ROM original y limpia de Ocarina of Time USA NTSC-U 1.0. (está vendra al instalar el port de nz2442, así que no te preocupes por conseguirla)
2. Una ROM basada en esa misma versión, pero ya traducida al castellano. (La de Blade133bo funciona bien y la recomiendo)

No utilices ROMs PAL, USA 1.1, USA 1.2, Master Quest, randomizers u otras
versiones modificadas.

La ROM original compatible utilizada para este proyecto tiene el siguiente MD5:

5bd1fe107bf8106b2ab6650abecd54d6

---
# Instalación paso a paso

## 1. Tener oot-PSP instalado y funcionando

Este tutorial asume que ya instalaste correctamente el port original
de Ocarina of Time para PSP de z2442 y que lo ejecutaste al menos una vez.

Esto es necesario porque oot-PSP genera durante su primer inicio archivos
que necesitaremos para crear la versión española.

Antes de modificar nada, recomiendo hacer una copia de seguridad de:

EBOOT.PBP

y:

data/segments/oot_psp_assets.bin

La ROM `baserom.z64` de tu instalación original NO necesita modificarse.

---

## 2. Archivos necesarios

Para utilizar el parcheador necesitas:

- OoT_PSP_ES_Patcher.exe
- baserom.z64
- oot-ntsc-1.0.z64
- EBOOT.PBP
- oot_psp_assets.bin

### baserom.z64

Debe ser una ROM limpia de:

The Legend of Zelda: Ocarina of Time USA NTSC-U 1.0

Esta es la misma ROM utilizada originalmente para instalar y ejecutar oot-PSP.

MD5:

5bd1fe107bf8106b2ab6650abecd54d6

### oot-ntsc-1.0.z64

Debe ser una ROM basada en la MISMA versión USA NTSC-U 1.0,
pero ya traducida al castellano.

Esta ROM solamente se utiliza como fuente para extraer los textos y
otros datos necesarios.

NO sustituye a `baserom.z64` dentro de oot-PSP.

---

## 3. Obtener los archivos desde oot-PSP

Desde tu instalación funcional de oot-PSP copia:

EBOOT.PBP

Este archivo se encuentra en la carpeta principal del port.

También copia:

data/segments/oot_psp_assets.bin

Este archivo se genera después de haber iniciado correctamente oot-PSP
al menos una vez.

Si todavía no existe, inicia primero el port original.

---

## 4. Preparar la carpeta del parcheador

Crea una carpeta nueva en tu PC, por ejemplo:

OOT_PSP_ES

Dentro coloca:

OOT_PSP_ES/
├── OoT_PSP_ES_Patcher.exe
├── baserom.z64
├── oot-ntsc-1.0.z64
├── EBOOT.PBP
└── oot_psp_assets.bin

Donde:

baserom.z64
= ROM limpia USA NTSC-U 1.0

oot-ntsc-1.0.z64
= ROM de la misma versión ya traducida al castellano

EBOOT.PBP
= archivo copiado desde tu instalación funcional de oot-PSP

oot_psp_assets.bin
= archivo generado por oot-PSP durante el primer inicio

---

## 5. Ejecutar el parcheador

Ejecuta:

OoT_PSP_ES_Patcher.exe

El programa utilizará la ROM limpia como referencia y la ROM española
como fuente de los textos necesarios.

Los archivos originales no se modifican.

Si todo es correcto aparecerá:

salida_es/
├── EBOOT.PBP
└── oot_psp_assets.bin

---

## 6. Instalar los archivos españoles

Haz primero una copia de seguridad de los archivos originales.

Copia:

salida_es/EBOOT.PBP

y reemplaza:

OOTPSP/EBOOT.PBP

Después copia:

salida_es/oot_psp_assets.bin

y reemplaza:

OOTPSP/data/segments/oot_psp_assets.bin

---

## 7. NO sustituir baserom.z64

La ROM original:

baserom.z64

debe permanecer exactamente como estaba en tu instalación original de oot-PSP.

NO necesitas copiar la ROM española a la PSP.

NO necesitas renombrar la ROM española como `baserom.z64`.

La ROM española únicamente se utiliza durante el proceso de creación de
los archivos modificados.

Por tanto, al terminar solamente debes reemplazar:

EBOOT.PBP

y:

data/segments/oot_psp_assets.bin

Todo lo demás puede permanecer igual.

---

## 8. Ejecutar oot-PSP

Inicia el port normalmente.

El menú principal puede continuar apareciendo en inglés.

Esto es normal.

Los diálogos dentro del juego deberían aparecer en castellano.

# Compatibilidad

Actualmente este parcheador está diseñado específicamente para la
combinación utilizada durante su desarrollo:

- oot-PSP compatible
- Ocarina of Time USA NTSC-U 1.0
- Traducción castellana basada en esa misma ROM

El port oot-PSP continúa en desarrollo.

Una futura actualización podría modificar la estructura de EBOOT.PBP o
oot_psp_assets.bin y hacer necesario actualizar este parcheador.

Si una versión futura del port deja de funcionar con este parcheador,
prueba primero con la versión de oot-PSP para la que fue publicada esta
versión del parcheador.

## Credits & Attributions / Créditos

This translation patcher is an external utility and relies heavily on the amazing work of the Zelda emulation and decompilation community. 

* **Spanish Translation Text:** Created by **Blade133bo / Navibyte** (All text and asset localization rights belong to them).
* **PSP Native Port:** Developed by [z2442](https://github.com/z2442) and all the [oot-PSP contributors](https://github.com).
* **Ocarina of Time Decompilation:** Brought to life by the [ZeldaRET project](https://github.com/zeldaret/oot).

*Disclaimer: This tool does not distribute any copyrighted game files or ROMs. Users must supply their own legal assets to perform the compilation/patching process.*

- Adaptación de la traducción al port PSP: este proyecto

Este proyecto no está afiliado con Nintendo, ZeldaRET, oot-PSP ni con
el autor de la traducción.
