#!/usr/bin/env python3
from pathlib import Path
import struct
import hashlib
import sys

# ---- Archivos esperados en la misma carpeta que este script ----
CLEAN_ROM = Path('baserom.z64')               # OoT USA NTSC 1.0 limpia
SPANISH_ROM = Path('oot-ntsc-1.0.z64')        # ROM ya parcheada al castellano
EBOOT = Path('EBOOT.PBP')
ASSETS = Path('oot_psp_assets.bin')
OUT_DIR = Path('salida_es')

# ---- Constantes del port/build que subiste ----
DMADATA_OFF = 0x7430
DMADATA_COUNT = 1510
MESSAGE_TABLE_OFF_IN_CODE = 0xF98AC

# VROM originales NTSC 1.0
VROM_NES_FONT = 0x00928000
VROM_NES_MESSAGES = 0x0092D000
VROM_JPN_MESSAGES = 0x008EB000

# Slots dentro de oot_psp_assets.bin, según tu EBOOT/port
PSP_JPN_MSG_FILE_OFF = 0x008D72B0
PSP_JPN_MSG_VROM = 0x208D72B0
PSP_JPN_MSG_CAPACITY = 0x003A350

PSP_NES_FONT_FILE_OFF = 0x00912800
PSP_NES_FONT_SIZE = 0x00004580

PSP_OLD_NES_MSG_VROM = 0x20916D80
PSP_OLD_NES_MSG_FILE_OFF = 0x00916D80
PSP_OLD_NES_MSG_SIZE = 0x00038130

EXPECTED_CLEAN_MD5 = '5bd1fe107bf8106b2ab6650abecd54d6'
EXPECTED_ASSETS_SIZE = 0x03267B10
EXPECTED_MSG_COUNT = 2115  # sin el 0xFFFF final; incluye 0xFFFD


def md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def be32(b: bytes, off: int) -> int:
    return struct.unpack_from('>I', b, off)[0]


def parse_dmadata(rom: bytes):
    out = []
    for i in range(DMADATA_COUNT):
        off = DMADATA_OFF + i * 16
        if off + 16 > len(rom):
            break
        vs, ve, rs, re = struct.unpack_from('>IIII', rom, off)
        out.append((vs, ve, rs, re))
    return out


def yaz0_decompress(src: bytes, expected_size: int) -> bytes:
    if src[:4] != b'Yaz0':
        raise ValueError('El bloque no es Yaz0')
    if be32(src, 4) != expected_size:
        raise ValueError('Tamaño Yaz0 inesperado')

    pos = 16
    out = bytearray()
    code = 0
    bits_left = 0

    while len(out) < expected_size:
        if bits_left == 0:
            if pos >= len(src):
                raise ValueError('Yaz0 truncado')
            code = src[pos]
            pos += 1
            bits_left = 8

        if code & 0x80:
            if pos >= len(src):
                raise ValueError('Yaz0 truncado')
            out.append(src[pos])
            pos += 1
        else:
            if pos + 1 >= len(src):
                raise ValueError('Yaz0 truncado')
            b1, b2 = src[pos], src[pos + 1]
            pos += 2
            distance = ((b1 & 0x0F) << 8) | b2
            length = b1 >> 4
            if length == 0:
                if pos >= len(src):
                    raise ValueError('Yaz0 truncado')
                length = src[pos] + 0x12
                pos += 1
            else:
                length += 2

            copy_pos = len(out) - distance - 1
            if copy_pos < 0:
                raise ValueError('Referencia Yaz0 inválida')
            for _ in range(length):
                out.append(out[copy_pos])
                copy_pos += 1
                if len(out) == expected_size:
                    break

        code = (code << 1) & 0xFF
        bits_left -= 1

    return bytes(out)


def load_dma_asset(rom: bytes, entry) -> bytes:
    vs, ve, rs, re = entry
    size = ve - vs
    if size <= 0:
        raise ValueError('Entrada DMA vacía')
    if re == 0:
        if rs + size > len(rom):
            raise ValueError('Activo DMA fuera de la ROM')
        return rom[rs:rs + size]

    if re > len(rom) or rs >= re:
        raise ValueError('Entrada DMA comprimida inválida')
    stored = rom[rs:re]
    if stored[:4] == b'Yaz0':
        return yaz0_decompress(stored, size)
    raise ValueError('Compresión desconocida en un activo DMA')


def find_dma_by_vrom(entries, vrom_start: int):
    for e in entries:
        if e[0] == vrom_start:
            return e
    raise ValueError(f'No encontré VROM 0x{vrom_start:08X} en dmadata')


def find_code_blob(rom: bytes, entries) -> bytes:
    # El code de esta versión mide ~1 MiB. En vez de confiar en el índice,
    # comprobamos la firma real de la tabla japonesa en 0xF98AC.
    signature = bytes.fromhex('00 01 23 00 08 00 00 00 00 02 23 00 08 00 00 6C')
    for e in entries:
        size = e[1] - e[0]
        if not (0x100000 <= size <= 0x110000):
            continue
        try:
            data = load_dma_asset(rom, e)
        except Exception:
            continue
        if len(data) >= MESSAGE_TABLE_OFF_IN_CODE + len(signature):
            if data[MESSAGE_TABLE_OFF_IN_CODE:MESSAGE_TABLE_OFF_IN_CODE + len(signature)] == signature:
                return data
    raise ValueError('No pude localizar el archivo code / tabla de mensajes')


def parse_spanish_english_table(code: bytes):
    pos = MESSAGE_TABLE_OFF_IN_CODE

    # En NTSC vienen primero los mensajes japoneses hasta 0xFFFF.
    while True:
        if pos + 8 > len(code):
            raise ValueError('Tabla japonesa truncada')
        text_id, type_pos, pad, ptr = struct.unpack_from('>HBBI', code, pos)
        pos += 8
        if text_id == 0xFFFF:
            break

    english = []
    while True:
        if pos + 8 > len(code):
            raise ValueError('Tabla inglesa/española truncada')
        text_id, type_pos, pad, ptr = struct.unpack_from('>HBBI', code, pos)
        pos += 8
        if text_id == 0xFFFF:
            break
        if (ptr >> 24) != 0x07:
            raise ValueError(f'Puntero de mensaje raro en ID 0x{text_id:04X}: 0x{ptr:08X}')
        english.append((text_id, type_pos, ptr & 0x00FFFFFF))

    if len(english) != EXPECTED_MSG_COUNT:
        raise ValueError(f'Esperaba {EXPECTED_MSG_COUNT} mensajes, encontré {len(english)}')
    if english[0][0] != 0x0001 or english[-1][0] != 0xFFFD:
        raise ValueError('La tabla de mensajes no tiene la forma esperada')
    return english


def reverse_8byte_blocks(data: bytes) -> bytes:
    if len(data) % 8 != 0:
        raise ValueError('El font no está alineado a 8 bytes')
    out = bytearray(len(data))
    for i in range(0, len(data), 8):
        out[i:i+8] = data[i:i+8][::-1]
    return bytes(out)


def build_psp_message_table(entries, bank_size: int) -> bytes:
    out = bytearray()
    for i, (text_id, type_pos, start_off) in enumerate(entries):
        if i + 1 < len(entries):
            end_off = entries[i + 1][2]
        else:
            end_off = bank_size

        if not (0 <= start_off <= end_off <= bank_size):
            raise ValueError(
                f'Offsets inválidos en mensaje 0x{text_id:04X}: '
                f'0x{start_off:X}..0x{end_off:X} / 0x{bank_size:X}'
            )

        out += struct.pack(
            '<HBBII',
            text_id,
            type_pos,
            0,
            PSP_JPN_MSG_VROM + start_off,
            PSP_JPN_MSG_VROM + end_off,
        )
    return bytes(out)


def find_psp_nes_table(eboot: bytes) -> int:
    # Firma de la tabla inglesa original del EBOOT que subiste.
    signature = (
        struct.pack('<I', EXPECTED_MSG_COUNT) +
        struct.pack('<HBBII', 0x0001, 0x23, 0, 0x20916D80, 0x20916E04) +
        struct.pack('<HBBII', 0x0002, 0x23, 0, 0x20916E04, 0x20916E70)
    )
    hits = []
    start = 0
    while True:
        p = eboot.find(signature, start)
        if p < 0:
            break
        hits.append(p)
        start = p + 1
    if len(hits) != 1:
        raise ValueError(f'No pude identificar de forma única la tabla PSP (coincidencias: {len(hits)})')
    return hits[0] + 4  # saltar el contador u32


def verify_external_asset_layout(eboot: bytes):
    # Comprobamos que este EBOOT usa exactamente los slots que vamos a tocar.
    jpn_desc = struct.pack(
        '<IIIIII',
        0x208D72B0, 0x20911600,
        0x008EB000, 0x00925350,
        0x00000000, 0x008D72B0,
    )
    font_desc = struct.pack(
        '<IIIIII',
        0x20912800, 0x20916D80,
        0x00928000, 0x0092C580,
        0x00000003, 0x00912800,
    )
    if eboot.find(jpn_desc) < 0:
        raise ValueError('El EBOOT no tiene el descriptor esperado de jpn_message_data_static')
    if eboot.find(font_desc) < 0:
        raise ValueError('El EBOOT no tiene el descriptor esperado de nes_font_static')


def main():
    for p in (CLEAN_ROM, SPANISH_ROM, EBOOT, ASSETS):
        if not p.is_file():
            print(f'ERROR: falta {p}')
            print('Pon los 4 archivos en la misma carpeta que este script.')
            return 1

    clean = CLEAN_ROM.read_bytes()
    spanish = SPANISH_ROM.read_bytes()
    eboot = bytearray(EBOOT.read_bytes())
    assets = bytearray(ASSETS.read_bytes())

    print('== Verificando archivos ==')
    print(f'ROM limpia MD5:   {md5(clean)}')
    print(f'ROM española MD5: {md5(spanish)}')
    print(f'EBOOT MD5:        {md5(eboot)}')
    print(f'Assets MD5:       {md5(assets)}')

    if md5(clean) != EXPECTED_CLEAN_MD5:
        raise ValueError('baserom.z64 no es la USA NTSC 1.0 limpia esperada')
    if len(assets) != EXPECTED_ASSETS_SIZE:
        raise ValueError(
            f'oot_psp_assets.bin tiene tamaño 0x{len(assets):X}; '
            f'esperaba 0x{EXPECTED_ASSETS_SIZE:X}'
        )

    verify_external_asset_layout(eboot)

    clean_dma = parse_dmadata(clean)
    spa_dma = parse_dmadata(spanish)

    # --- Extraer banco español de diálogos ---
    spa_msg_entry = find_dma_by_vrom(spa_dma, VROM_NES_MESSAGES)
    spa_messages = load_dma_asset(spanish, spa_msg_entry)
    print(f'Banco español:    0x{len(spa_messages):X} bytes')
    if len(spa_messages) > PSP_JPN_MSG_CAPACITY:
        raise ValueError('El banco español no cabe en el slot japonés del asset pack')

    # Verificar que el pack original realmente contiene el banco inglés limpio
    clean_msg_entry = find_dma_by_vrom(clean_dma, VROM_NES_MESSAGES)
    clean_messages = load_dma_asset(clean, clean_msg_entry)
    packed_old = bytes(assets[PSP_OLD_NES_MSG_FILE_OFF:PSP_OLD_NES_MSG_FILE_OFF + len(clean_messages)])
    if packed_old != clean_messages:
        raise ValueError('El bloque inglés del asset pack no coincide con la ROM limpia; abortando por seguridad')

    # --- Extraer y convertir font español ---
    clean_font = load_dma_asset(clean, find_dma_by_vrom(clean_dma, VROM_NES_FONT))
    spa_font = load_dma_asset(spanish, find_dma_by_vrom(spa_dma, VROM_NES_FONT))
    if len(clean_font) != PSP_NES_FONT_SIZE or len(spa_font) != PSP_NES_FONT_SIZE:
        raise ValueError('Tamaño inesperado de nes_font_static')

    # En este port, nes_font_static se convierte invirtiendo cada palabra de 8 bytes.
    # Lo verificamos contra el asset pack antes de aplicar la misma conversión al font español.
    expected_clean_psp_font = reverse_8byte_blocks(clean_font)
    actual_clean_psp_font = bytes(assets[PSP_NES_FONT_FILE_OFF:PSP_NES_FONT_FILE_OFF + PSP_NES_FONT_SIZE])
    if expected_clean_psp_font != actual_clean_psp_font:
        raise ValueError('La conversión del font no coincide con este build del port; no voy a parchearlo a ciegas')
    spa_font_psp = reverse_8byte_blocks(spa_font)

    # --- Leer la tabla española desde code ---
    spa_code = find_code_blob(spanish, spa_dma)
    spa_entries = parse_spanish_english_table(spa_code)
    new_psp_table = build_psp_message_table(spa_entries, len(spa_messages))

    # --- Localizar y verificar tabla PSP original ---
    table_off = find_psp_nes_table(eboot)
    print(f'Tabla PSP NES:    0x{table_off:X} dentro de EBOOT.PBP')
    old_table_size = EXPECTED_MSG_COUNT * 12
    old_table = bytes(eboot[table_off:table_off + old_table_size])

    # Comprobar que IDs/order coinciden antes de sobrescribir.
    for i, (text_id, _, _) in enumerate(spa_entries):
        old_id = struct.unpack_from('<H', old_table, i * 12)[0]
        if old_id != text_id:
            raise ValueError(
                f'Orden de mensajes incompatible en entrada {i}: '
                f'EBOOT=0x{old_id:04X}, ROM ES=0x{text_id:04X}'
            )

    # --- Aplicar parches ---
    # 1) Guardamos el banco ES dentro del slot japonés, que es más grande.
    assets[PSP_JPN_MSG_FILE_OFF:PSP_JPN_MSG_FILE_OFF + len(spa_messages)] = spa_messages

    # 2) Font castellano ya convertido al formato PSP.
    assets[PSP_NES_FONT_FILE_OFF:PSP_NES_FONT_FILE_OFF + PSP_NES_FONT_SIZE] = spa_font_psp

    # 3) La tabla NES del EBOOT ahora apunta al banco ES alojado en el slot japonés.
    eboot[table_off:table_off + len(new_psp_table)] = new_psp_table

    # --- Verificaciones finales ---
    if len(assets) != EXPECTED_ASSETS_SIZE:
        raise AssertionError('El tamaño del asset pack cambió; eso no debería pasar')
    if len(new_psp_table) != old_table_size:
        raise AssertionError('La tabla PSP cambió de tamaño')

    # Confirmar que el primer/último puntero quedan dentro del slot japonés.
    first = struct.unpack_from('<HBBII', new_psp_table, 0)
    last = struct.unpack_from('<HBBII', new_psp_table, len(new_psp_table) - 12)
    if first[3] != PSP_JPN_MSG_VROM:
        raise AssertionError('Primer mensaje no apunta al banco español')
    if last[4] != PSP_JPN_MSG_VROM + len(spa_messages):
        raise AssertionError('Último mensaje no termina al final del banco español')

    OUT_DIR.mkdir(exist_ok=True)
    out_eboot = OUT_DIR / 'EBOOT.PBP'
    out_assets = OUT_DIR / 'oot_psp_assets.bin'
    out_eboot.write_bytes(eboot)
    out_assets.write_bytes(assets)

    print('\n== LISTO ==')
    print(f'Creado: {out_eboot}')
    print(f'Creado: {out_assets}')
    print(f'Nuevo EBOOT MD5:  {md5(eboot)}')
    print(f'Nuevo Assets MD5: {md5(assets)}')
    print('\nCopia SOLO esos dos archivos a tu port:')
    print('  EBOOT.PBP -> raíz de OOTPSP_M')
    print('  oot_psp_assets.bin -> OOTPSP_M/data/segments/')
    print('\nNO borres oot_psp_assets.bin después: si lo borras, el port lo reconstruirá en inglés.')
    print('Conserva una copia de tus archivos originales para poder volver atrás.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as exc:
        print(f'\nERROR: {exc}')
        print('No se modificaron los archivos originales; el script sólo escribe dentro de salida_es al final.')
        sys.exit(1)
