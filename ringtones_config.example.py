from typing import Union, Iterable

import pedalboard
from musicpy import musicpy as mp
from musicpy.musicpy import N, C, S


def fast_seq(chord: mp.chord):
    return chord.set(duration=1 / 32, interval=1 / 32)


def block_chord(chord: mp.chord):
    return chord.set(duration=1 / 8, interval=0)


def short_block(chord: mp.chord):
    return chord.set(duration=1 / 32, interval=0)


SOUNDFONT_PATH = r"D:\User\Documents\MuseScore4\SoundFonts\FluidR3_GM.sf2"
SOUNDFONT_INSTRUMENT = 13

BPM = 156
PEDALBOARD_EFFECT = pedalboard.Pedalboard([pedalboard.Reverb(room_size=0.5, damping=0.5, wet_level=0.3, dry_level=0.6)])

RINGTONES: dict[str, Union[mp.chord, mp.track, mp.piece]] = {
    "aaa": fast_seq(C("C5:maj") @ [1, 2, 3, 1.1, 2.1])
           & fast_seq(C("C4:maj") @ [2.1, 1.1, 3, 2, 1]),
    # 高中群
    "bbb": block_chord(C("F3:maj") @ [1, 3, 1.1, 2.1, 3.1])
           | fast_seq(C("F5:maj") @ [2, 1, 3])
           | short_block(C("F5:maj") @ [1.1, 2.1]),
    "ccc": block_chord(C("F3:maj") @ [1, 3, 1.1, 2.1, 3.1])
           | fast_seq(C("C5:7") @ [3, 2.1, 4])
           | short_block(N("D6") + N("G6")),
    "ddd": block_chord(C("Bb3:maj") @ [1, 2, 3, 1.1, 2.1])
           | fast_seq(S("Bb5 major").get([2, -1, 3, 1, 5], pitch_mode=1)),
    "eee": block_chord(C("C") @ [1, 2, 3, 1.1, 2.1])
           | fast_seq(S("C5 major").get([3, 1, 4, 5], pitch_mode=1)),
    "fff": block_chord(C("D") @ [1, 2, 3, 1.1, 2.1])
           | fast_seq(S("D5 major").get([2.1, 5, 4, 3, 1], pitch_mode=1)),
    "ggg": block_chord(C("E") @ [1, 2, 3, 1.1, 2.1])
           | fast_seq(S("E5 major").get([1, 3, 1.1, 7, 5], pitch_mode=1)),
    "hhh": block_chord(C("F") @ [1, 2, 3, 1.1, 2.1])
           | fast_seq(S("F5 major").get([1, 0, 3, 5, 1.1], pitch_mode=1)),
    "iii": block_chord(C("F#") @ [1, 2, 3, 1.1, 2.1])
           | fast_seq(S("F# major").get([3, 5, 6, 7, 2.1], pitch_mode=1)),
    # 高中同学
    "jjj": fast_seq(C("A3:maj7") @ [3, 2.1, 1.1, 3.1, 2.1, 4.1]),
    "kkk": fast_seq(S("D major").get([3, 1.1, 5, 2.1, 7, 5.1], pitch_mode=1)),
    "lll": fast_seq(C("Bb3:7") / 2 @ [1, 4, 2, 1.1, 4, 3.1]),
    "mmm": fast_seq(S("F#3 major").get([5, 3.1, 1.1, 7.1, 4.1, 6.1], pitch_mode=1)),
    "nnn": fast_seq(C("Bb7") @ [1.1, 2, 3, 3.1, 1.1, 4.1]),
    "ooo": fast_seq((C("Eb5:7") + N("Fb6")) @ [1, 3, 2, 5, 4, 2.1]),
    # 初中同学
    "ppp": fast_seq(C("D5:maj") @ [1, 3, 2, 1.1, 3, 2.1]),
    "qqq": fast_seq((C("G3:maj") + N("E4")) / 2 @ [1, 4, 3, 1.1, 4, 2.1]),
    "rrr": fast_seq(C("G4:maj7") @ [3, 2.1, 1.1, 3.1, 2.1, 4.1]),
}

DUPLICATE_RINGTONES: dict[str, Iterable[str]] = {
    "爸爸 & 妈妈": ("a曹玄", "a汪海"),
}
