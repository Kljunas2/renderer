def write_png(buf, width, height):
	"""koda iz blender repositoryja"""
	import zlib, struct
			
	# reverse the vertical line order and add null bytes at the start
	width_byte_4 = width * 4
	raw_data = b"".join(b'\x00' + buf[span:span + width_byte_4] for span in range((height - 1) * width * 4, -1, - width_byte_4))
			
	def png_pack(png_tag, data):
		chunk_head = png_tag + data
		return struct.pack("!I", len(data)) + chunk_head + struct.pack("!I", 0xFFFFFFFF & zlib.crc32(chunk_head))

	return b"".join([
		b'\x89PNG\r\n\x1a\n',
		png_pack(b'IHDR', struct.pack("!2I5B", width, height, 8, 6, 0, 0, 0)),
		png_pack(b'IDAT', zlib.compress(raw_data, 9)),
		png_pack(b'IEND', b'')])


def save_png(array, filename):
	import struct
	if any([len(row) != len(array[0]) for row in array]):
		raise ValueError("Array should have elements of equal size")

								#First row becomes top row of image.
	flat = []; map(flat.extend, reversed(array))
								 #Big-endian, unsigned 32-byte integer.
	buf = b''.join([struct.pack('>I', ((0xffFFff & i32)<<8)|(i32>>24) ) for i32 in flat])   #Rotate from ARGB to RGBA.

	data = write_png(buf, len(array[0]), len(array))
	f = open(filename, 'wb')
	f.write(data)
	f.close()
