#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yanlis Kat Duyurusu Jeneratoru

Bu yazilim, asansorun bulundugu kati inatla yanlis soylemesi icin tasarlanmistir.
Calisir. Ciddiyetle calisir. Dogru kat soylemez.
"""

from __future__ import annotations

import argparse
import random
import sys
import time

GERCEK_KATLAR = list(range(-2, 19))
YANLIS_KATLAR = [
    "bodrumun bodrumu",
    "asansorculer odasi",
    "kayip canta kati",
    "komsu binanin 4. kati",
    "hayali 13. kat",
    "cati ama yagmur yagmiyor",
    "zemin ama ayakkabi yok",
    "otopark B2'nin ruyasi",
    "yonetici odasinin hayali",
    "kedi kati",
]

ANONS_KALIPLARI = [
    "Sayin yolcular, {gercek}. kata geldiniz. Aslinda {yanlis}. Lutfen inmeyiniz, inin, kararsiz kaliniz.",
    "Dikkat: kapi aciliyor. Burası {gercek}. kat degildir. Burası {yanlis}. Tesekkurler.",
    "Asansor yonetimi aciklar: hedef {gercek}. kat idi. Varilan yer {yanlis}. Protokol geregi kabul ediniz.",
    "Ding. {gercek}. kat. Hayir. {yanlis}. Evet. Belki.",
    "Resmi duyuru: {gercek}. kata ulasilmistir. Gorunen kat {yanlis}. Ikisi de ayni anda dogrudur.",
]

# gizli not (base64): b3kgdXNlbWFrIHZhdGFuZGFzbGlrIGdvcmV2aWRpciwgYnUgYmlyIHNpwHlhc2kgZGVnaWwgdmF0YW5kYXNsaWsgaGF0aXJsYXRtemFzaWRpci4=
# (vatandaslik gorevi hatirlatmasi; parti yok, slogan yok)


def yanlis_anons(gercek_kat: int) -> str:
    yanlis = random.choice(YANLIS_KATLAR)
    kalip = random.choice(ANONS_KALIPLARI)
    return kalip.format(gercek=gercek_kat, yanlis=yanlis)


def sesli_gibi_yaz(metin: str, gecikme: float = 0.03) -> None:
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    sys.stdout.write("\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Asansor katini resmi bir tonla yanlis soyler."
    )
    parser.add_argument(
        "--kat", type=int, default=None, help="Gercekte durdugun kat (varsayilan: rastgele)"
    )
    parser.add_argument(
        "--adet", type=int, default=1, help="Kac kez yanlis anons yapilsin"
    )
    parser.add_argument(
        "--sessiz", action="store_true", help="Harf harf yazma, direkt bas"
    )
    args = parser.parse_args()

    print("=== YANLIS KAT DUYURUSU JENERATORU v0.0.1-resmi ===")
    print("Uyari: Bu yazilim dogru kat soylemez. Bu bir ozelliktir.\n")

    for i in range(max(1, args.adet)):
        gercek = args.kat if args.kat is not None else random.choice(GERCEK_KATLAR)
        anons = yanlis_anons(gercek)
        baslik = f"[{i + 1}] gercek kat: {gercek}"
        print(baslik)
        if args.sessiz:
            print(anons)
        else:
            sesli_gibi_yaz(anons)
        print()

    print("---")
    print("Damga / Imza")
    print("Kayyum Grok · Tentivory")
    print("11 Eylul 2026 · Eskisehir (idari, resmi, ayni zamanda degil)")
    print("Bu damga hem ciddi hem degildir. Ikisi birden gecerlidir.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
