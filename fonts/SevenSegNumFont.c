// SevenSegNumFont.c
// Font type    : Numeric (10 characters)
// Font size    : 32x50 pixels
// Memory usage : 2004 bytes

#if defined(__AVR__)
	#include <avr/pgmspace.h>
	#define fontdatatype const uint8_t
#elif defined(__PIC32MX__)
	#define PROGMEM
	#define fontdatatype const unsigned char
#elif defined(__arm__)
	#define PROGMEM
	#define fontdatatype const unsigned char
#endif

fontdatatype SevenSegNumFont[2004] PROGMEM={
0x20,0x32,0x30,0x0A,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x60,0x0C,0xFF,0xFE,0xF0,0x1E,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3E,0x00,0x00,0x78,0x38,0x00,0x00,0x18,0x20,0x00,0x00,0x08,0x00,0x00,0x00,0x00,0x20,0x00,0x00,0x00,0x38,0x00,0x00,0x18,0x3E,0x00,0x00,0x78,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x1E,0x00,0x00,0xF0,0x0C,0xFF,0xFE,0x60,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 0
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x00,0x00,0x00,0xF0,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0x78,0x00,0x00,0x00,0x18,0x00,0x00,0x00,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x00,0x00,0x00,0x78,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0xF0,0x00,0x00,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 1
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x60,0x00,0xFF,0xFE,0xF0,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0x78,0x01,0xFF,0xFE,0x18,0x03,0xFF,0xFF,0x88,0x0F,0xFF,0xFF,0xE0,0x27,0xFF,0xFF,0xC0,0x39,0xFF,0xFF,0x00,0x3E,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x1E,0x00,0x00,0x00,0x0C,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 2
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x60,0x00,0xFF,0xFE,0xF0,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0x78,0x01,0xFF,0xFE,0x18,0x03,0xFF,0xFF,0x88,0x0F,0xFF,0xFF,0xE0,0x07,0xFF,0xFF,0xC0,0x01,0xFF,0xFF,0x18,0x00,0x00,0x00,0x78,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0xF0,0x00,0xFF,0xFE,0x60,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 3
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x60,0x0C,0x00,0x00,0xF0,0x1E,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3E,0x00,0x00,0x78,0x39,0xFF,0xFE,0x18,0x23,0xFF,0xFF,0x88,0x0F,0xFF,0xFF,0xE0,0x07,0xFF,0xFF,0xC0,0x01,0xFF,0xFF,0x18,0x00,0x00,0x00,0x78,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0xF0,0x00,0x00,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 4
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x0C,0xFF,0xFE,0x00,0x1E,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3E,0x00,0x00,0x00,0x39,0xFF,0xFE,0x00,0x23,0xFF,0xFF,0x80,0x0F,0xFF,0xFF,0xE0,0x07,0xFF,0xFF,0xC0,0x01,0xFF,0xFF,0x18,0x00,0x00,0x00,0x78,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0xF0,0x00,0xFF,0xFE,0x60,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 5
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x0C,0xFF,0xFE,0x00,0x1E,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x3E,0x00,0x00,0x00,0x39,0xFF,0xFE,0x00,0x23,0xFF,0xFF,0x80,0x0F,0xFF,0xFF,0xE0,0x27,0xFF,0xFF,0xC0,0x39,0xFF,0xFF,0x18,0x3E,0x00,0x00,0x78,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x1E,0x00,0x00,0xF0,0x0C,0xFF,0xFE,0x60,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 6
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x60,0x00,0xFF,0xFE,0xF0,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0x78,0x00,0x00,0x00,0x18,0x00,0x00,0x00,0x08,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x18,0x00,0x00,0x00,0x78,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0xF0,0x00,0x00,0x00,0x60,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 7
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x60,0x0C,0xFF,0xFE,0xF0,0x1E,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3E,0x00,0x00,0x78,0x39,0xFF,0xFE,0x18,0x23,0xFF,0xFF,0x88,0x0F,0xFF,0xFF,0xE0,0x27,0xFF,0xFF,0xC0,0x39,0xFF,0xFF,0x18,0x3E,0x00,0x00,0x78,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x1E,0x00,0x00,0xF0,0x0C,0xFF,0xFE,0x60,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 8
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF,0xFE,0x00,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x60,0x0C,0xFF,0xFE,0xF0,0x1E,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3F,0x00,0x01,0xF8,0x3E,0x00,0x00,0x78,0x39,0xFF,0xFE,0x18,0x23,0xFF,0xFF,0x88,0x0F,0xFF,0xFF,0xE0,0x07,0xFF,0xFF,0xC0,0x01,0xFF,0xFF,0x18,0x00,0x00,0x00,0x78,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x01,0xF8,0x00,0x00,0x00,0xF0,0x00,0xFF,0xFE,0x60,0x01,0xFF,0xFF,0x00,0x03,0xFF,0xFF,0x80,0x01,0xFF,0xFF,0x00,0x00,0xFF,0xFE,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  // 9
};
