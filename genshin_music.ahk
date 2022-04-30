#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

$a::
    Send, {g}{w}
    return
$s::
    Send, {v}{q}
    return
$q::
    Send, {a}{q}
    return
$,::
    Send, {m}{e}
    return
$w::
    Send, {g}{e}
    return
$7::
    Send, {b}{s}{g}{j}
    return
$.::
    Send, {b}{e}
    return
$2::
    Send, {b}{d}
    return
$1::
    Send, {m}{g}
    return
$3::
    Send, {c}{d}
    return
$5::
    Send, {d}{q}
    return
$;::
    Send, {g}{q}
    return
$4::
    Send, {a}{w}
    return
$8::
    Send, {b}{q}
    return
r::q
t::w
y::e
u::r
i::t
o::y
p::u
d::a
f::s
g::d
h::f
j::g
k::h
l::j
`::g