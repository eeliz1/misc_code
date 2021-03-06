# !/usr/bin/env python
# encoding: utf-8

"""
BOW 2016 family practice
Created by Andre Moncrieff on 13 April 2016.
Copyright 2016 Andre E. Moncrieff. All rights reserved.
"""

import random

family_number_dict = {"Struthionidae": 2,
                      "Casuariidae": 3,
                      "Dromaiidae": 1,
                      "Apterygidae": 5,
                      "Rheidae": 2,
                      "Tinamidae": 47,
                      "Spheniscidae": 16,
                      "Diomedeidae": 13,
                      "Procellariidae": 80,
                      "Pelecanoididae": 4,
                      "Hydrobatidae": 21,
                      "Gaviidae": 5,
                      "Podicipedidae": 21,
                      "Phoenicopteridae": 6,
                      "Phaethontidae": 3,
                      "Sulidae": 10,
                      "Phalacrocoracidae": 31,
                      "Anhingidae": 4,
                      "Fregatidae": 5,
                      "Pelecanidae": 8,
                      "Balaenicipitidae": 1,
                      "Scopidae": 1,
                      "Ciconiidae": 19,
                      "Ardeidae": 63,
                      "Threskiornithidae": 34,
                      "Anhimidae": 3,
                      "Anseranatidae": 1,
                      "Anatidae": 160,
                      "Cathartidae": 7,
                      "Sagittariidae": 1,
                      "Pandionidae": 1,
                      "Accipitridae": 240,
                      "Falconidae": 65,
                      "Megapodiidae": 22,
                      "Cracidae": 54,
                      "Odontophoridae": 33,
                      "Tetraonidae": 19,
                      "Meleagrididae": 2,
                      "Phasianidae": 159,
                      "Numididae": 6,
                      "Opisthocomidae": 1,
                      "Gruidae": 15,
                      "Aramidae": 1,
                      "Psophiidae": 3,
                      "Rallidae": 149,
                      "Sarothruridae": 9,
                      "Heliornithidae": 3,
                      "Otididae": 26,
                      "Rhynochetidae": 1,
                      "Eurypygidae": 1,
                      "Cariamidae": 2,
                      "Mesitornithidae": 3,
                      "Jacanidae": 8,
                      "Rostratulidae": 3,
                      "Haematopodidae": 11,
                      "Ibidorhynchidae": 1,
                      "Recurvirostridae": 10,
                      "Charadriidae": 64,
                      "Pluvianidae": 1,
                      "Burhinidae": 9,
                      "Glareolidae": 16,
                      "Scolopacidae": 88,
                      "Thinocoridae": 4,
                      "Pedionomidae": 1,
                      "Pluvianellidae": 1,
                      "Chionidae": 2,
                      "Dromadidae": 1,
                      "Stercorariidae": 7,
                      "Laridae": 100,
                      "Rynchopidae": 3,
                      "Alcidae": 23,
                      "Turnicidae": 17,
                      "Pteroclidae": 16,
                      "Columbidae": 313,
                      "Strigopidae": 4,
                      "Cacatuidae": 21,
                      "Psittaculidae": 184,
                      "Psittacidae": 167,
                      "Musophagidae": 23,
                      "Cuculidae": 140,
                      "Tytonidae": 19,
                      "Strigidae": 194,
                      "Caprimulgidae": 92,
                      "Steatornithidae": 1,
                      "Podargidae": 13,
                      "Nyctibiidae": 7,
                      "Aegothelidae": 11,
                      "Apodidae": 95,
                      "Hemiprocnidae": 4,
                      "Trochilidae": 340,
                      "Coliidae": 6,
                      "Trogonidae": 44,
                      "Alcedinidae": 95,
                      "Todidae": 5,
                      "Momotidae": 14,
                      "Meropidae": 27,
                      "Coraciidae": 12,
                      "Brachypteraciidae": 5,
                      "Leptosomidae": 1,
                      "Upupidae": 2,
                      "Phoeniculidae": 8,
                      "Bucerotidae": 53,
                      "Galbulidae": 18,
                      "Bucconidae": 35,
                      "Indicatoridae": 16,
                      "Lybiidae": 42,
                      "Megalaimidae": 25,
                      "Capitonidae": 20,
                      "Semnornithidae": 2,
                      "Ramphastidae": 40,
                      "Picidae": 217,
                      "Xenicidae": 4,
                      "Eurylaimidae": 8,
                      "Philepittidae": 4,
                      "Calyptomenidae": 6,
                      "Sapayoidae": 1,
                      "Scleruridae": 17,
                      "Dendrocolaptidae": 51,
                      "Furnariidae": 212,
                      "Thamnophilidae": 232,
                      "Formicariidae": 12,
                      "Grallariidae": 50,
                      "Conopophagidae": 10,
                      "Rhinocryptidae": 57,
                      "Melanopareidae": 4,
                      "Cotingidae": 65,
                      "Oxyruncidae": 1,
                      "Pipridae": 48,
                      "Tyrannidae": 420,
                      "Tityridae": 35,
                      "Pipritidae": 3,
                      "Pittidae": 29,
                      "Menuridae": 2,
                      "Atrichornithidae": 2,
                      "Alaudidae": 93,
                      "Hirundinidae": 84,
                      "Campephagidae": 85,
                      "Pycnonotidae": 130,
                      "Nicatoridae": 3,
                      "Maluridae": 30,
                      "Acanthizidae": 59,
                      "Psophodidae": 5,
                      "Mohouidae": 2,
                      "Neosittidae": 2,
                      "Cinclosomatidae": 10,
                      "Pomatostomidae": 5,
                      "Pachycephalidae": 50,
                      "Falcunculidae": 3,
                      "Oreoicidae": 3,
                      "Eulacestomatidae": 1,
                      "Paramythiidae": 2,
                      "Melanocharitidae": 10,
                      "Cnemophilidae": 3,
                      "Pardalotidae": 4,
                      "Meliphagidae": 180,
                      "Petroicidae": 49,
                      "Aegithinidae": 4,
                      "Hyliotidae": 4,
                      "Panuridae": 1,
                      "Laniidae": 34,
                      "Malacanotidae": 46,
                      "Vangidae": 36,
                      "Machaerirhynchidae": 2,
                      "Elachuridae": 1,
                      "Dulidae": 1,
                      "Bombycillidae": 3,
                      "Hypocoliidae": 1,
                      "Ptilogonatidae": 4,
                      "Mohoidae": 5,
                      "Cinclidae": 5,
                      "Troglodytidae": 82,
                      "Polioptilidae": 15,
                      "Buphagidae": 2,
                      "Mimidae": 34,
                      "Sturnidae": 115,
                      "Rhabdornithidae": 3,
                      "Turdidae": 160,
                      "Timaliidae": 46,
                      "Pellorneidae": 54,
                      "Leiothrichidae": 125,
                      "Picathartidae": 2,
                      "Eupetidae": 1,
                      "Chaetopidae": 2,
                      "Sylviidae": 62,
                      "Donacobiidae": 1,
                      "Macrosphenidae": 18,
                      "Locustellidae": 57,
                      "Cisticolidae": 113,
                      "Bernieridae": 11,
                      "Acrocephalidae": 59,
                      "Phylloscopidae": 77,
                      "Scotocercidae": 37,
                      "Pnoepygidae": 4,
                      "Regulidae": 6,
                      "Stenostiridae": 9,
                      "Muscicapidae": 303,
                      "Platysteiridae": 29,
                      "Monarchidae": 96,
                      "Rhipiduridae": 46,
                      "Melampittidae": 2,
                      "Ifritidae": 1,
                      "Aegithalidae": 10,
                      "Remizidae": 10,
                      "Paridae": 59,
                      "Sittidae": 28,
                      "Certhiidae": 9,
                      "Urocynchramidae": 1,
                      "Promeropidae": 5,
                      "Modulatricidae": 3,
                      "Nectariniidae": 136,
                      "Dicaeidae": 45,
                      "Zosteropidae": 122,
                      "Irenidae": 2,
                      "Chloropseidae": 11,
                      "Oriolidae": 35,
                      "Rhagologidae": 1,
                      "Dicruridae": 22,
                      "Callaeidae": 4,
                      "Notiomystidae": 1,
                      "Peltopsidae": 2,
                      "Artamidae": 11,
                      "Cracticidae": 10,
                      "Corcoracidae": 2,
                      "Pityriaseidae": 1,
                      "Climacteridae": 7,
                      "Ptilonorhynchidae": 20,
                      "Paradisaeidae": 42,
                      "Platylophidae": 1,
                      "Corvidae": 125,
                      "Vireonidae": 62,
                      "Prunellidae": 13,
                      "Motacillidae": 67,
                      "Calcariidae": 6,
                      "Zeledonidae": 1,
                      "Emberizidae": 168,
                      "Cardinalidae": 63,
                      "Thraupidae": 371,
                      "Parulidae": 108,
                      "Peucedramidae": 1,
                      "Icteridae": 105,
                      "Fringillidae": 221,
                      "Estrildidae": 131,
                      "Viduidae": 20,
                      "Passeridae": 38,
                      "Ploceidae": 115
                      }


def number_quiz():
    family = random.choice(list(family_number_dict.keys()))
    answer = input("How many species in {}? ".format(family))
    while int(answer) != family_number_dict[family]:
        print("Oops! Try again.")
        answer = input("How many species in {}? ".format(family))
    if int(answer) == family_number_dict[family]:
        print("Awesome!! Correct.")
        number_quiz()


def main():
    number_quiz()


if __name__ == '__main__':
    main()
