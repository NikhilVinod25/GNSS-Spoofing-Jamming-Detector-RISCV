OUTPUT_ARCH(riscv)
ENTRY(_start)

MEMORY
{
    /* 256KB BRAM starting at 0x0 for the PicoRV32 */
    BRAM (rwx) : ORIGIN = 0x00000000, LENGTH = 256K
}

SECTIONS
{
    /* Code section */
    .text :
    {
        . = ALIGN(4);
        *(.text.start)      /* Put startup code at the very beginning */
        *(.text*)           /* All other code */
        *(.rodata*)         /* Read-only data (strings, constants) */
        *(.srodata*)
        . = ALIGN(4);
        _etext = .;         /* End of text symbol */
    } > BRAM

    /* Initialized Data */
    .data :
    {
        . = ALIGN(4);
        _sdata = .;
        *(.data*)
        *(.sdata*)
        . = ALIGN(4);
        _edata = .;
    } > BRAM

    /* Uninitialized Data (BSS) - Zeroed out at start */
    .bss :
    {
        . = ALIGN(4);
        _sbss = .;
        *(.bss*)
        *(.sbss*)
        *(COMMON)
        . = ALIGN(4);
        _ebss = .;
    } > BRAM

    /* Stack Setup */
    /* We place the stack pointer at the very end of the 256KB BRAM */
    /* 256KB = 0x40000 bytes */
    _stack_top = 0x00040000;
}