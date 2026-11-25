# Requirements

## Windows

The listed requirements are for APEX DX.

Supported 64 bit Windows versions: Windows 10 (see [Software Release Policies — System Requirements](../Release%20Policies/system-requirements.md) for current 64-bit Windows 10/11, Windows Server, `AVX2`, RAM, and 18-month version support policies)

## Linux

DX releases are built on a centos7/redhat7 linux system and tested on more recent distributions for compatibility. Below is a list of these required operating system components and their minimum versions:

| Name | "Library" | "Minimum version" |
| --- | --- | --- |
| XRender | libXrender | 0.9.0 |
| xcb-render | libxcb-render | 1.8.1 |
| xcb-render-util | libxcb-render-util | 0.3.8 |
| xcb-shape | libxcb-shape | 1.8.1 |
| xcb-randr | libxcb-randr | 1.8.1 |
| xcb-xfixes | libxcb-xfixes | 1.8.1 |
| xcb-sync | libxcb-sync | 1.8.1 |
| xcb-shm | libxcb-shm | 1.8.1 |
| xcb-icccm | libxcb-icccm | 0.3.9 |
| xcb-keysyms | libxcb-keysyms | 0.3.9 |
| xcb-image | libxcb-image | 0.3.9 |
| Fontconfig | libfontconfig | 2.1 |
| FreeType | libfreetype | 2.1.3 |
| Xi | libXi | 1.3.0 |
| Xext | libXext | 6.4.3 |
| X11 | libX11 | 6.2.1 |
| xcb | libxcb | 1.8.1 |
| X11-xcb | libX11-xcb | 1.3.2 |
| SM | libSM | 6.0.4 |
| ICE | libICE | 6.3.5 |
| glib | libglib-2.0 | 2.8.3 |
| pthread | libpthread | 2.3.5 |

## Hardware

DX is supported on 64-bit `x86-64` processors with mandatory **AVX2** instruction set support running either Windows (primary) or Linux. Only 64-bit versions are available; ARM and other architectures are not supported. For current baseline RAM recommendations, workstation CPU guidelines, and the **18-month version support policy**, see **[Software Release Policies — System Requirements](../Release%20Policies/system-requirements.md)**.

> Legacy minimum baseline (older releases):
>
> - 64-bit dual core 2Ghz CPU.
> - 2048MB memory.
> - 120GB 7200RPM hard drive.
> - Graphics controller and monitor capable of 1280x1024.
>
> Recommended baseline 64 bit hardware:
>
> - 64-bit quad core CPU.
> - 4096MB memory
> - 500GB 7200RPM hard drive.
> - Graphics controller and monitor capable of 1920x1080.
