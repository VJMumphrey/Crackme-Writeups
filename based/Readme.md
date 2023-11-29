
Based
=====

Info
=====

This was a 1.3 difficulty binary from mt77 for Unix/Linux. This was the first crackme that I have done in a while so this was a good refresher.
Unzipping the download gave me a binary called ***luna***. I will refer to the binary as ***luna*** to keep things simple. I will also denote a function with *@ name* because r2 and rizin use this for temperoray seek. This would make it easier to follow along. 

Some ouput from rz-bin about the binary
```bash
[Info]
arch     x86
cpu      N/A
bintype  elf
bits     64
class    ELF64
compiler GCC: (GNU) 13.0.1 20230401 (Red Hat 13.0.1-0) GCC: (GNU) 13.2.1 20230728 (Red Hat 13.2.1-1)
endian   LE
intrp    /lib64/ld-linux-x86-64.so.2
lang     c++
machine  AMD x86-64 architecture
os       linux
cc       N/A
stripped false
```

Exploration
===========

running afl on ***luna*** shows this,
```asm
0x00401070    1 37           entry0
0x004010b0    4 33   -> 31   sym.deregister_tm_clones
0x004010e0    4 49           sym.register_tm_clones
0x00401120    3 33   -> 32   sym.__do_global_dtors_aux
0x00401150    1 6            entry.init0
0x00401262    7 166          main
0x00401308    1 13           sym._fini
0x004010a0    1 5            loc..annobin_static_reloc.c
0x00401000    3 27           sym._init
0x00401156    9 268          sym.luna_uint64_t
0x00401040    1 6            method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const
0x00401050    1 6            method.std::ostream.operator___std::ostream______std::ostream
0x00401060    1 6            method.std::istream.operator___uint64_t
0x00401030    1 6            method.std::basic_ostream_char__std::char_traits_char_____std.endl_char__std::char_traits_char____std::basic_ostream_char__std::char_traits_char


```

There are two important fuctions: *@ main* and *@ luna*.

main
```asm
┌ int main(int argc, char **argv, char **envp);
│           ; var int64_t var_18h @ stack - 0x18
│           ; var int64_t var_9h @ stack - 0x9
│           0x00401262      push  rbp
│           0x00401263      mov   rbp, rsp
│           0x00401266      sub   rsp, 0x10
│           0x0040126a      mov   qword [var_18h], 0
│           0x00401272      mov   esi, str.Enter_password__plz:        ; 0x402010 ; "Enter password, plz: "
│           0x00401277      mov   edi, obj.std::cout                   ; 0x404040
│           0x0040127c      call  method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const ;  method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const(void)
│           0x00401281      lea   rax, [var_18h]
│           0x00401285      mov   rsi, rax
│           0x00401288      mov   edi, obj.std::cin                    ; 0x404160
│           0x0040128d      call  method.std::istream.operator___uint64_t ;  method.std::istream.operator___uint64_t(void)
│           0x00401292      mov   rax, qword [var_18h]
│           0x00401296      mov   rdi, rax                             ; int64_t arg1
│           0x00401299      call  sym.luna_uint64_t
│           0x0040129e      mov   byte [var_9h], al
│           0x004012a1      mov   rax, qword [var_18h]
│           0x004012a5      cmp   rax, 0x1869f
│       ┌─< 0x004012ab      jbe   0x4012b9
│       │   0x004012ad      mov   rax, qword [var_18h]
│       │   0x004012b1      cmp   rax, 0x989680
│      ┌──< 0x004012b7      jbe   0x4012bd
│      │└─> 0x004012b9      mov   byte [var_9h], 0
│      └──> 0x004012bd      movzx eax, byte [var_9h]
│           0x004012c1      cmp   eax, 1                               ; 1
│       ┌─< 0x004012c4      je    0x4012e4
│       │   0x004012c6      mov   esi, str.Invalid_value               ; 0x402026 ; "Invalid value"
│       │   0x004012cb      mov   edi, obj.std::cout                   ; 0x404040
│       │   0x004012d0      call  method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const ;  method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const(void)
│       │   0x004012d5      mov   esi, method.std::basic_ostream_char__std::char_traits_char_____std.endl_char__std::char_traits_char____std::basic_ostream_char__std::char_traits_char ; 0x401030
│       │   0x004012da      mov   rdi, rax
│       │   0x004012dd      call  method.std::ostream.operator___std::ostream______std::ostream ;  method.std::ostream.operator___std::ostream______std::ostream(void)
│      ┌──< 0x004012e2      jmp   0x401301
│      │└─> 0x004012e4      mov   esi, str.Welcome                     ; 0x402034 ; "Welcome!"
│      │    0x004012e9      mov   edi, obj.std::cout                   ; 0x404040
│      │    0x004012ee      call  method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const ;  method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const(void)
│      │    0x004012f3      mov   esi, method.std::basic_ostream_char__std::char_traits_char_____std.endl_char__std::char_traits_char____std::basic_ostream_char__std::char_traits_char ; 0x401030
│      │    0x004012f8      mov   rdi, rax
│      │    0x004012fb      call  method.std::ostream.operator___std::ostream______std::ostream ;  method.std::ostream.operator___std::ostream______std::ostream(void)
│      │    0x00401300      nop
│      │    ; CODE XREF from main @ 0x4012e2
│      └──> 0x00401301      mov   eax, 0
│           0x00401306      leave
└           0x00401307      ret

```

luna
```asm
┌ luna(int64_t arg1);
│           ; arg int64_t arg1 @ rdi
│           ; var int64_t var_30h @ stack - 0x30
│           ; var int64_t var_1ch @ stack - 0x1c
│           ; var int64_t var_18h @ stack - 0x18
│           ; var int64_t var_14h @ stack - 0x14
│           ; var uint64_t var_10h @ stack - 0x10
│           0x00401156      push  rbp                                  ; luna(uint64_t)
│           0x00401157      mov   rbp, rsp
│           0x0040115a      mov   qword [var_30h], rdi                 ; arg1
│           0x0040115e      mov   rax, qword [var_30h]
│           0x00401162      mov   qword [var_10h], rax
│           0x00401166      mov   dword [var_14h], 0
│       ┌─< 0x0040116d      jmp   0x40121b
│      ┌──> 0x00401172      mov   rcx, qword [var_10h]
│      ╎│   0x00401176      movabs rdx, 0xcccccccccccccccd
│      ╎│   0x00401180      mov   rax, rcx
│      ╎│   0x00401183      mul   rdx
│      ╎│   0x00401186      shr   rdx, 3
│      ╎│   0x0040118a      mov   rax, rdx
│      ╎│   0x0040118d      shl   rax, 2
│      ╎│   0x00401191      add   rax, rdx
│      ╎│   0x00401194      add   rax, rax
│      ╎│   0x00401197      sub   rcx, rax
│      ╎│   0x0040119a      mov   rdx, rcx
│      ╎│   0x0040119d      mov   dword [var_1ch], edx
│      ╎│   0x004011a0      mov   rax, qword [var_10h]
│      ╎│   0x004011a4      movabs rdx, 0xcccccccccccccccd
│      ╎│   0x004011ae      mul   rdx
│      ╎│   0x004011b1      mov   rcx, rdx
│      ╎│   0x004011b4      shr   rcx, 3
│      ╎│   0x004011b8      movabs rdx, 0xcccccccccccccccd
│      ╎│   0x004011c2      mov   rax, rcx
│      ╎│   0x004011c5      mul   rdx
│      ╎│   0x004011c8      shr   rdx, 3
│      ╎│   0x004011cc      mov   rax, rdx
│      ╎│   0x004011cf      shl   rax, 2
│      ╎│   0x004011d3      add   rax, rdx
│      ╎│   0x004011d6      add   rax, rax
│      ╎│   0x004011d9      sub   rcx, rax
│      ╎│   0x004011dc      mov   rdx, rcx
│      ╎│   0x004011df      mov   eax, edx
│      ╎│   0x004011e1      add   eax, eax
│      ╎│   0x004011e3      mov   dword [var_18h], eax
│      ╎│   0x004011e6      cmp   dword [var_18h], 9
│     ┌───< 0x004011ea      jle   0x4011f0
│     │╎│   0x004011ec      sub   dword [var_18h], 9
│     └───> 0x004011f0      mov   edx, dword [var_18h]
│      ╎│   0x004011f3      mov   eax, dword [var_1ch]
│      ╎│   0x004011f6      add   eax, edx
│      ╎│   0x004011f8      add   dword [var_14h], eax
│      ╎│   0x004011fb      mov   rax, qword [var_10h]
│      ╎│   0x004011ff      shr   rax, 2
│      ╎│   0x00401203      movabs rdx, 0x28f5c28f5c28f5c3
│      ╎│   0x0040120d      mul   rdx
│      ╎│   0x00401210      mov   rax, rdx
│      ╎│   0x00401213      shr   rax, 2
│      ╎│   0x00401217      mov   qword [var_10h], rax
│      ╎│   ; CODE XREF from luna @ 0x40116d
│      ╎└─> 0x0040121b      cmp   qword [var_10h], 0
│      └──< 0x00401220      jne   0x401172
│           0x00401226      mov   ecx, dword [var_14h]
│           0x00401229      movsxd rax, ecx
│           0x0040122c      imul  rax, rax, 0x66666667
│           0x00401233      shr   rax, 0x20
│           0x00401237      mov   edx, eax
│           0x00401239      sar   edx, 2
│           0x0040123c      mov   eax, ecx
│           0x0040123e      sar   eax, 0x1f
│           0x00401241      sub   edx, eax
│           0x00401243      mov   eax, edx
│           0x00401245      shl   eax, 2
│           0x00401248      add   eax, edx
│           0x0040124a      add   eax, eax
│           0x0040124c      sub   ecx, eax
│           0x0040124e      mov   edx, ecx
│           0x00401250      test  edx, edx
│       ┌─< 0x00401252      jne   0x40125b
│       │   0x00401254      mov   eax, 1
│      ┌──< 0x00401259      jmp   0x401260
│      │└─> 0x0040125b      mov   eax, 0
│      │    ; CODE XREF from luna @ 0x401259
│      └──> 0x00401260      pop   rbp
└           0x00401261      ret
```

Judgeing on the assembly in luna there is a algorithim of some kind operating on the input from main.

Reversing
==========

Here is a decompilation of main using rz-ghidra for ease of viewing
```cpp
    var_9h._0_1_ = luna(var_18h);
    if (((uint64_t)var_18h < 100000) || (10000000 < (uint64_t)var_18h)) {
        var_9h._0_1_ = '\0';
    }
    if ((char)var_9h == '\x01') {
        uVar1 = method.std::basic_ostream_char__std::char_traits_char_____std.operator____std::char_traits_char____std::basic_ostream_char__std::char_traits_char______char_const
        (reloc.std::cout, "Welcome!");
    }

```
After doing some more looking around, the result of the function *@ luna* is either a true(1) or false(0). This means that the resulting number needs to be a one in order to get the *Welcome* statement in *@ main*. The value < *100000* or > *10000000*. To reverse the algorithim I exported *@ luna* to try and find the number needed and figure out how the algorithim worked. The resulting file in included as ***key.cpp***.

Solution
========

So the number that has to be inputed needs to be greater than *100000* because if it's lower than that it will automatically fail.

Below is the following logic that comes from *@ luna* about how to find the final number ie *100000* + n-9 (which n is [0,10] or 9 + 1).
-9 is because the algorithm subtracts 9.

This is logic of *n* in *@ luna* with the python interpreter

``` python
>>> for i in range(0,11):
...     print(i % 10)
...
0
1
2
3
4
5
6
7
8
9
0
>>> 100001 % 10
1
>>> 100000 % 10
0
>>>
```

running key.cpp generates 1000009 as the answer but really answer that follows the formula should work. Overall a pretty easy crackme and a good refresher.