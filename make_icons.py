#!/usr/bin/env python3
import struct, zlib, base64

def png(w, h, pixels):
    def chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)
    raw = b''
    for row in pixels:
        raw += b'\x00'
        for r,g,b,a in row:
            raw += bytes([r,g,b,a])
    compressed = zlib.compress(raw, 9)
    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
    # use RGBA
    ihdr = chunk(b'IHDR', struct.pack('>II', w, h) + bytes([8,6,0,0,0]))
    idat = chunk(b'IDAT', compressed)
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

def make_icon(size):
    pixels = []
    cx, cy = size/2, size/2
    r = size/2
    for y in range(size):
        row = []
        for x in range(size):
            dx, dy = x - cx, y - cy
            dist = (dx*dx + dy*dy) ** 0.5
            if dist > r:
                row.append((0,0,0,0))
            else:
                # Blue background
                br, bg, bb = 0x18, 0x5F, 0xA5
                # Water drop shape in white
                # Simple water drop: circle top half + teardrop bottom
                ndx, ndy = dx/r, dy/r
                # draw white drop shape
                in_drop = False
                # circle part (upper portion)
                drop_cx, drop_cy = 0, -0.15
                drop_r = 0.38
                if (ndx - drop_cx)**2 + (ndy - drop_cy)**2 < drop_r**2:
                    in_drop = True
                # triangle/teardrop bottom
                if not in_drop and ndy > -0.15 and abs(ndx) < (0.55 - ndy*0.55) and ndy < 0.55:
                    in_drop = True
                if in_drop:
                    row.append((255,255,255,255))
                else:
                    row.append((br,bg,bb,255))
        pixels.append(row)
    return png(size, size, pixels)

with open('icons/icon-192.png','wb') as f:
    f.write(make_icon(192))
with open('icons/icon-512.png','wb') as f:
    f.write(make_icon(512))
print("Icons created")
