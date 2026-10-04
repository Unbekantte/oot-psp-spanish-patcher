
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

## 1. Instalar primero oot-PSP

Descarga e instala primero el port original de oot-PSP siguiendo las
instrucciones de su desarrollador.

Debes tener una instalación funcional antes de utilizar este parcheador.

La carpeta del port tendrá una estructura similar a:

OOTPSP/
├── EBOOT.PBP
├── data/
└── otros archivos del port

---

## 2. Iniciar oot-PSP al menos una vez

Coloca tu ROM original USA NTSC-U 1.0 en el lugar indicado por oot-PSP y
arranca el port normalmente.

La ROM original debe llamarse:

baserom.z64

La primera vez que se inicia oot-PSP, el port utiliza esa ROM para extraer
y generar los archivos que necesita.

Es importante completar este paso antes de utilizar el parcheador español.

Después del primer inicio debe existir el archivo:

data/segments/oot_psp_assets.bin

Este archivo es necesario para crear la versión española.

Si `oot_psp_assets.bin` todavía no existe, inicia primero el port original
con la ROM limpia.

---

## 3. Preparar una ROM en castellano

Necesitas otra copia de Ocarina of Time basada exactamente en:

Ocarina of Time USA NTSC-U 1.0

A esa segunda ROM debes aplicarle una traducción al castellano compatible.

No importa si tú mismo aplicaste el parche o si ya dispones de una copia
traducida compatible.

Lo importante es que la ROM española esté basada en la misma versión
USA NTSC-U 1.0.

Para utilizar este parcheador, temporalmente renombra la ROM traducida como:

oot-ntsc-1.0.z64

---

## 4. Preparar la carpeta del parcheador

Crea una carpeta nueva en tu PC.

Por ejemplo:

OOT_PSP_ES

Dentro de ella coloca:

OoT_PSP_ES_Patcher.exe
baserom.z64
oot-ntsc-1.0.z64
EBOOT.PBP
oot_psp_assets.bin

La carpeta debe quedar así:

OOT_PSP_ES/
├── OoT_PSP_ES_Patcher.exe
├── baserom.z64
├── oot-ntsc-1.0.z64
├── EBOOT.PBP
└── oot_psp_assets.bin

### Qué es cada archivo

`OoT_PSP_ES_Patcher.exe`

Es el parcheador de este proyecto.

`baserom.z64`

Es la ROM ORIGINAL y limpia de Ocarina of Time USA NTSC-U 1.0.

`oot-ntsc-1.0.z64`

Es la ROM de la MISMA versión, pero ya traducida al castellano.

`EBOOT.PBP`

Debes copiarlo desde tu instalación funcional de oot-PSP.

Se encuentra en la carpeta principal del port:

OOTPSP/EBOOT.PBP

`oot_psp_assets.bin`

Debes copiarlo desde la instalación de oot-PSP después de haber iniciado
el port al menos una vez.

Se encuentra en:

OOTPSP/data/segments/oot_psp_assets.bin

---

## 5. Ejecutar el parcheador

Con los cinco archivos dentro de la misma carpeta, ejecuta:

OoT_PSP_ES_Patcher.exe

El programa comprobará los archivos y realizará automáticamente las
modificaciones necesarias.

El parcheador NO modifica tus archivos originales.

Cuando termine correctamente aparecerá una nueva carpeta:

salida_es

Dentro encontrarás:

salida_es/
├── EBOOT.PBP
└── oot_psp_assets.bin

Estos son los archivos modificados que utilizará oot-PSP para mostrar
los diálogos en castellano.

---

## 6. Sustituir los archivos del port

Haz una copia de seguridad de tu instalación original antes de continuar.

Copia:

salida_es/EBOOT.PBP

y reemplaza:

OOTPSP/EBOOT.PBP

Después copia:

salida_es/oot_psp_assets.bin

y reemplaza:

OOTPSP/data/segments/oot_psp_assets.bin

La estructura final debe incluir:

OOTPSP/
├── EBOOT.PBP
└── data/
    └── segments/
        └── oot_psp_assets.bin

---

## 7. ROM utilizada por el port

Una vez terminado todo el proceso, la ROM que vayas a dejar en la carpeta
del port debe utilizar el nombre esperado por oot-PSP:

baserom.z64

Si estás utilizando la ROM traducida al castellano dentro de tu instalación
final, renómbrala nuevamente como:

baserom.z64

No la dejes con el nombre temporal:

oot-ntsc-1.0.z64

Ese nombre solamente se utiliza para que el parcheador pueda distinguir
entre la ROM original y la ROM traducida mientras genera los archivos.

---

## 8. Iniciar el juego

Copia la carpeta del port nuevamente a tu PSP si trabajaste desde el PC.

Inicia oot-PSP normalmente.

El menú inicial puede continuar apareciendo en inglés.

Esto es normal.

Los diálogos dentro del juego deberían aparecer en castellano.

---

# Resumen rápido

Primero:

1. Instala oot-PSP.
2. Coloca una ROM limpia USA NTSC-U 1.0 como `baserom.z64`.
3. Inicia el port una vez.
4. Espera a que genere `oot_psp_assets.bin`.

Después copia al PC:

- `EBOOT.PBP`
- `data/segments/oot_psp_assets.bin`

Prepara también:

- ROM limpia -> `baserom.z64`
- ROM castellana -> `oot-ntsc-1.0.z64`

Coloca todo junto a:

`OoT_PSP_ES_Patcher.exe`

Ejecuta el parcheador.

Finalmente reemplaza en oot-PSP:

`EBOOT.PBP`

y:

`data/segments/oot_psp_assets.bin`

por las versiones creadas dentro de:

`salida_es`

Si la ROM castellana va a permanecer en la instalación final del port,
renómbrala nuevamente como:

`baserom.z64`

---

# Archivos que NO debes borrar

No borres:

data/segments/oot_psp_assets.bin

después de haber instalado la versión española.

Si el port vuelve a generar este archivo utilizando la ROM original,
los recursos volverán a ser los originales y perderás los diálogos
modificados.

Conserva además una copia de seguridad de:

EBOOT.PBP
oot_psp_assets.bin

originales.

---

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

(por si llega a quedar alguna duda, el baserom, es el rom virgen que usa el port y que incluye al instalarlo, es necesario renombrar la rom parcheada resultante de la traducción y el baserom, ya que así lo detecta el port. Lo renombramos como el rom virgen porque se busca explícitamente ese archivo, asi que rom parcheada (renombrar a "baserom" y conviene guardar el baserom anterior por si acaso).
Rom español + baserom = rom parcheada (se debe renombrar como baserom)

## Credits & Attributions / Créditos

This translation patcher is an external utility and relies heavily on the amazing work of the Zelda emulation and decompilation community. 

* **Spanish Translation Text:** Created by **Blade133bo / Navibyte** (All text and asset localization rights belong to them).
* **PSP Native Port:** Developed by [z2442](https://github.com/z2442) and all the [oot-PSP contributors](https://github.com).
* **Ocarina of Time Decompilation:** Brought to life by the [ZeldaRET project](https://github.com/zeldaret/oot).

*Disclaimer: This tool does not distribute any copyrighted game files or ROMs. Users must supply their own legal assets to perform the compilation/patching process.*

- Adaptación de la traducción al port PSP: este proyecto

Este proyecto no está afiliado con Nintendo, ZeldaRET, oot-PSP ni con
el autor de la traducción.
