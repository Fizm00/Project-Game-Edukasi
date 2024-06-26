﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Define methods
init python:
    import random
    def jawaban_benar():
        randombenar = random.randint(1, 2)
        if randombenar == 1:
            renpy.say("{color=#7ABA78}Kakek Gamelan", "Bagus sekali")
        elif randombenar == 2:
            renpy.say("{color=#7ABA78}Kakek Gamelan", "Yap, betul sekali")

    def jawaban_salah():
        randomsalah = random.randint(1, 3)
        if randomsalah == 1:
            renpy.say("{color=#7ABA78}Kakek Gamelan", "Tebakan yang bagus nak, tetapi")
        elif randomsalah == 2:
            renpy.say("{color=#7ABA78}Kakek Gamelan", "Haha, bukan gamelan yang itu nak,")
        elif randomsalah == 3:
            renpy.say("{color=#7ABA78}Kakek Gamelan", "Tidak apa apa, kesalahan adalah bagian dari perjalanan,")

init:
    transform customzoom:
        zoom 0.3

#Define picture button
image bonang:
    "bonang.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image saron:
    "saron.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image kendang:
    "kendang.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image slenthem:
    "slenthem.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image gong:
    "gong.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image kempul:
    "kempul.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image rebab:
    "rebab.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image siter:
    "siter.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image gambang:
    "gambang.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image kenong:
    "kenong.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image gender:
    "gender.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image kempul:
    "kempul.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image demung:
    "demung.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75
image siter:
    "siter.png"
    zoom 0.7
    xpos 0.5
    ypos 0.75

screen opsi_gambar_saron():
    imagebutton:
        idle "gelap_bonang.png"
        hover "bonang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_saron")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_gambang.png"
        hover "gambang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_saron")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_saron")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_saron")

screen opsi_gambar_kendhang():
    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kendang")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_kendang")

    imagebutton:
        idle "gelap_bonang.png"
        hover "bonang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_kendang")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kendang")

    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

screen opsi_gambar_slenthem():
    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_slenthem")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_slenthem")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_slenthem")

    imagebutton:
        idle "gelap_bonang.png"
        hover "bonang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_slenthem")

screen opsi_gambar_gong():
    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_gong")

    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_gong")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_gong")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_bonang.png"
        hover "bonang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_gong")

screen opsi_gambar_bonang():
    imagebutton:
        idle "gelap_bonang.png"
        hover "bonang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_bonang")

    imagebutton:
        idle "gelap_gambang.png"
        hover "gambang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_bonang")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_bonang")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_bonang")

screen opsi_gambar_kempul():
    imagebutton:
        idle "gelap_rebab.png"
        hover "rebab.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_siter.png"
        hover "siter.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_kempul.png"
        hover "kempul.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

screen opsi_gambar_rebab():
    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_rebab")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_rebab")

    imagebutton:
        idle "gelap_rebab.png"
        hover "rebab.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_kenong.png"
        hover "kenong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_rebab")

    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_rebab")

screen opsi_gambar_kempul():
    imagebutton:
        idle "gelap_rebab.png"
        hover "rebab.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_siter.png"
        hover "siter.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kempul")

    imagebutton:
        idle "gelap_kempul.png"
        hover "kempul.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

screen opsi_gambar_siter():
    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_siter")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_siter")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_siter")

    imagebutton:
        idle "gelap_siter.png"
        hover "siter.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_kenong.png"
        hover "kenong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_siter")

screen opsi_gambar_gambang():
    imagebutton:
        idle "gelap_bonang.png"
        hover "bonang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_gambang")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_salah_gambang")

    imagebutton:
        idle "gelap_gong.png"
        hover "gong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_gambang")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_gambang")

    imagebutton:
        idle "gelap_gambang.png"
        hover "gambang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

screen opsi_gambar_kenong():
    imagebutton:
        idle "gelap_rebab.png"
        hover "rebab.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kenong")

    imagebutton:
        idle "gelap_kenong.png"
        hover "kenong.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.3
        ypos 0.3
        at customzoom
        action Call("jawab_benar")

    imagebutton:
        idle "gelap_kendang.png"
        hover "kendang.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.5
        at customzoom
        action Call("jawab_salah_kenong")

    imagebutton:
        idle "gelap_slenthem.png"
        hover "slenthem.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.7
        at customzoom
        action Call("jawab_salah_kenong")

    imagebutton:
        idle "gelap_saron.png"
        hover "saron.png"
        xanchor 0.5
        yanchor 0.5
        xpos 0.7
        ypos 0.3
        at customzoom
        action Call("jawab_salah_kenong")

#sound & music effect
define audio.bell = "sfx_bell.mp3"

#respon jawaban pertanyaan
label jawab_benar:
    $ jawab_benar += 1
    python:
        jawaban_benar()
return

label jawab_salah_saron:
    python:
        jawaban_salah()
    show saron with dissolve
    kg "Saron itu biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator"
    hide saron with dissolve
return

label jawab_salah_kendang:
    python:
        jawaban_salah()
    show kendang with dissolve
    kg "Kendhang dapat mengatur irama musik gamelan."
    kg "Cara memainkan gamelan ini adalah dengan memukul dengan telapak tangan bagian pinggir gamelan yang terbuat dari kulit hewan."
    hide kendang with dissolve
return

label jawab_salah_slenthem:
    python:
        jawaban_salah()
    show slenthem with dissolve
    kg "Gamelan slenthem adalah salah satu instrumen gamelan yang masuk dalam keluarga balungan seperti saron dan demung."
    kg "Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain."
    hide slenthem with dissolve
return

label jawab_salah_gong:
    python:
        jawaban_salah()
    show gong with dissolve
    kg "Gong memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."
    kg "Gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas." 
    kg "Gong dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus."
    hide gong with dissolve
return

label jawab_salah_bonang:
    python:
        jawaban_salah()
    show bonang with dissolve
    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak)."
    kg "Bonang termasuk pencon yaitu dari logam."
    hide bonang with dissolve
return

label jawab_salah_kempul:
    python:
        jawaban_salah()
    show kempul with dissolve
    kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."
    kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus."
    kg "Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."
    hide kempul with dissolve
return

label jawab_salah_rebab:
    python:
        jawaban_salah()
    show rebab with dissolve
    kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."
    kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas."
    kg "Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."
    hide rebab with dissolve
return

label jawab_salah_siter:
    python:
        jawaban_salah()
    show siter with dissolve
    kg "Siter adalah salah satu instrumen gamelan yang memainkannya dengan cara dipetik seperti alat musik guzheng asal cina atau sitar asal India."
    kg "Alat musik ini sudah jarang ditemukan atau digunakan dalam set-set gamelan saat ini."
    kg "Alat musik ini biasa juga disebut gitar Jawa yang memiliki suara yang khas."
    hide siter with dissolve
return

label jawab_salah_gambang:
    python:
        jawaban_salah()
    show gambang with dissolve
    kg "Gambang terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik."
    kg "Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu."
    kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang"
    hide gambang with dissolve
return

label jawab_salah_kenong:
    python:
        jawaban_salah()
    show kenong with dissolve
    kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan."
    kg "Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."
    kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh."
    kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."
    hide kenong with dissolve
return

# The game starts here.

label start:
    $ click = 0
    $ jawab_benar = 0
    scene bg stasiun
    with fade

    play audio bell volume 0.5
    stop audio fadeout 1.0

    show mc senyum 2 #gambar mc sedang senyum
    with dissolve

    mc "Wow, Jogja! Akhirnya aku sampai juga"

    mc "Jadi ini kota asal kakek, kakek pernah bercerita tentang pengalamannya di kota ini. 
        Sekarang giliran ku untuk merasakannya sendiri. 
        Baiklah, pertama-tama aku harus mencari tempat untuk tinggal dan kemudian mulai menjelajahi kota ini."

    show mc flat #gambar mc ekspresi flat
    with dissolve
    mc "Waduh, ramai sekali stasiun ini, ditambah kata kakek jumlah kendaraan di Jogja yang lumayan padat. 
        Mungkin ada informasi turis di sekitar sini."
    
    aangs "Aduh!!!"

    mc "Suara apa itu? Kedengarannya seperti orang yang jatuh, dalam keadaan seramai ini aku harus berhati-hati, 
        bisa saja ada barang bawaanku yang jatuh, atau lebih buruk…"

    show mc kaget #gambar mc kaget
    with dissolve
    mc "DICULIK!!"
    
    show mc netral #gambar mc netral
    with dissolve
    mc "Astaghfirullah Totok, nauzubillah min zalik semoga aku selalu dijaga Allah"

    #nanti kasih gambar pop-up disini

    show mc kaget
    with dissolve
    mc "Ya ampun, baru saja aku pikirkan, langsung kejadian, kira kira ini ponsel siapa ya? 
        APA? PONSEL INI SAMSUNG GALAXY Z FLIP? 
        Harganya pasti sangat mahal, sayang sekali apabila ada kehilangan."
    
    aangs "Aduh… HP ku dimanaaa, sial sekali aku hari ini"

    show mc netral
    with dissolve
    mc "Ah, sepertinya ponsel ini milik orang itu, sebaiknya ku hampiri"

    hide mc#totok jalan off-screen

    show aang kaget #gambar aang kaget
    with dissolve
    aangs "Permisi mas, apakah anda melihat hp jatuh? Permisi mbak…."

    aangs "permisi mas, apakah mas melihat HP jatuh?"

    hide aang
    
    menu:
        "mengembalikkan ponsel":
            jump bagian2
        "menyimpan ponsel untuk dirimu":
            mc "Apa yang aku lakukan? Aku tidak boleh berbohong! Semua perbuatan pasti akan dibalas baik maupun buruk"
            mc "Aku sebaiknya mengembalikan ponselnya ke orang malang ini"
            jump bagian2    

label bagian2:
    show mc bingung at left
    with dissolve
    mc "Apakah ini ponselmu?"

    show aang senyum at right
    with dissolve
    aangs "Iya! Ini ponselku, terima kasih banyak mas, sebaiknya kita menghindari keramaian dulu"

label stasiun_tugu:
    scene bg stasiun silhouette hilang
    with fade

    show aang senyum
    with dissolve
    aangs "Terima kasih, atas bantuannya mas, Perkenalkan nama aku Aang."

    show aang senyum #udah ganti karakter aang tanpa shadow atau misterius
    with dissolve
    aang "Aku baru saja kembali ke Jogja dari liburanku, entah apa yang akan ku lakukan tanpa HP ku, kau lah penyelamatku. Nama mas siapa ya?"

    hide aang

    show mc senyum 2
    with dissolve
    mc "Perkenalkan namaku Totok, salam kenal Aang. Jadi apakah kamu penduduk Jogja Aang?"

    hide mc

    show aang senyum
    with dissolve
    aang "Jadi namamu Totok? Baiklah Salam kenal Totok."

    aang "Iya aku asli Jogja nih! Bagaimana denganmu Tok? Kau tidak terlihat seperti orang sini"

    hide aang

    show mc netral
    with dissolve
    mc "Oh, iya mas, saya baru saja sampai di Jogja, saya dari desa kecil bernama X. Saya datang ke Jogja untuk melihat pemandangan dan mempelajari kulinernya."

    hide mc

    show aang senyum
    with dissolve
    aang "Haha, santai aja kali, panggil saja aku Aang"

    show aang netral
    with dissolve
    aang    "Jadi kamu turis ya? Baiklah baiklah, sebagai ucapan terima kasihku, aku akan menjadi tour guide mu selama perjalananmu di Jogja! 
            Aku akan membawamu ke beberapa tempat monumental yang tak boleh dilewatkan"
    
    hide aang
    
    show mc senyum 1
    with dissolve
    mc "Be-benarkah mas? Apakah kau rela menjadi pemandu wisata untukku?"

    hide mc

    show aang netral
    with dissolve
    aang    "Sudah ku bilang panggil saja aku Aang, tentu saja! Aku sendiri juga udah lama gak keliling Jogja, 
            ini akan menjadi perjalanan seru untuk kita berdua, bepergian lebih asik apabila bersama teman bukan?"

    hide aang

    show mc senyum 1
    with dissolve
    mc "Terima kasih banyak mas, maksudku Aang. Semoga beberapa hari kedepan perjalanan di Jogja ini akan menjadi pengalaman tak terlupakan"

    hide mc

    show aang netral
    with dissolve
    aang "Akhhh kece Tok, jadi mau kemana kamu sekarang?"

    hide aang

    show mc bingung
    with dissolve
    mc "aku sendiri belum tau tempat yang ingin ku kunjungi, apakah kamu ada saran tempat Aang?"

    hide mc

    show aang senyum
    with dissolve
    aang "Akkhhhh aku menyarankan Tugu Jogja, Keraton, Alun-Alun, Malioboro, Candi Borobudur, Monjali…."

    aang "Oh ya, tadi kau bilang ingin mempelajari kuliner Jogja?"

    aang "aku juga tau tempat Gudeg yang enak banget, harganya juga terjangkau, kalau mau berguru, aku saranin dari dia"

    hide aang

    show mc netral
    with dissolve
    mc "Banyak juga tempat kunjungan di Jogja, tetapi sepertinya aku akan mengunjungi beberapa saja, tempat yang benar benar berbau Jogja serta kulinernya"

    hide mc

    show aang senyum
    with dissolve
    aang "Haha siap boss, mau langsung gas ke Tugu?"

    hide aang

    show mc senyum 1
    with dissolve
    mc " Haha, aku suka semangatmu Aang, tapi sebaiknya aku mencari tempat penginapan dulu untuk menaruh barang bawaanku."

    hide mc

    show aang netral
    with dissolve
    aang "Baiklah, mari ikut denganku, akan ku boncengi kamu."
    hide aang netral

label luar_stasiun_tugu:
    scene bg stasiun tugu luar
    #kasih sound effect kendaraan bermotor

    show aang netral
    with dissolve
    aang "Ini motorku, naiklah Tok."

    hide aang

    show mc kaget
    with dissolve
    mc "Wah, aku tidak pernah melihat motor dan mobil sebanyak ini dalam satu tempat. Beragam sekali kendaraan bermotor yang digunakan orang orang"

    show mc netral
    with dissolve
    mc "Plat mobil itu berawalan B, mobil yang itu berawalan D,dan Motor yang itu berawalan BD, aku hanya pernah melihat motor berplat AB."

    hide mc

    #gambar pop up Berbagai plat di kendaraan berbeda beserta eksposisi Aang yang menjelaskan
    show aang netral
    with dissolve
    aang "Plat nomor kendaraan itu kombinasi angka dan huruf yang terpasang di kendaraan bermotor seperti mobil, motor, ataupun truk."

    aang    "Plat nomor kendaraan mu bergantung pada tempat pendaftaran awal kendaraan tersebut. 
            Huruf di depan itu Kode wilayah yang merepresentasikan daerah asal kendaraan, memungkinkan identifikasi tempat pendaftaran kendaraan, 
            seperti Provinsi atau daerah administratif tertentu."

    #Gambar pop up: Kode wilayah beserta penjelasan
    aang    "Misalnya, kode \"B\" menandakan Provinsi Jawa Barat, \"D\" menunjukkan Provinsi Bali, BD mengartikan Provinsi Lampung, 
            sedangkan AB melambangkan Daerah Istimewah Yogyakarta, yoiii"

    aang    "Plat nomor ini penting untuk keperluan administrasi, penegakan hukum, dan identifikasi kendaraan, 
            memudahkan manajemen data registrasi kendaraan dan memungkinkan pelacakan asal kendaraan yang dicari untuk macam-macam keperluan, 
            termasuk lalu lintas dan penegakan hukum."

    hide aang

    #Gambar pop up: Gambar end
    show mc netral
    with dissolve
    mc "Ohhhh begitu Aang, kamu tau banyak juga ya, tidak sia-sia aku bertemu kamu"

    hide mc

    show aang senyum
    with dissolve
    aang "Haha, bersyukurlah kamu menemukan hpku"

    aang "Ayo berangkat menuju hotel"
    hide aang

label depan_hotel:
    scene bg depan hotel
    with fade

    show mc bingung
    with dissolve
    mc "Berdasarkan hasil google search, rekomendasi orang orang adalah Malioboro, Kraton, dan Tugu."

    hide mc

    show aang senyum
    with dissolve
    aang    "Hehe, biarkan aku memasak sebagai tour guide mu, saranku adalah kita hari ini ke tugu untuk melihat monumen khas Jogja, 
            lalu ke Keraton untuk melihat sejarah dan adat Jogjakarta"
    
    aang    "setelah itu kita akan ke Alun-Alun Selatan untuk melihat monumen seperti Masjid Gedhe Kauman dan Benteng Vredeburg"

    aang    "besoknya kita akan mengunjungi rumah makan spesialis Gudeg agar kamu dapat mempelajari kuliner kami"

    aang    "Lalu beberapa hari setelah itu kita akan ke Pusat Jogja yaitu Malioboro untuk membeli souvenir."

    hide aang

    show mc senyum 1
    with dissolve
    mc "Waaaah! Kau sudah familiar sekali dengan Jogja. Aku tidak sabar keliling Jogja bersamamu Aang"

    hide mc

    show aang senyum
    with dissolve
    aang "hehe, kan aku emang orang asli sini"

    aang "Ayo kita mulai perjalanan kita!"

    hide aang

label tugu_jogja:
    scene bg tugu yogya
    with fade

    show mc senyum 2
    with dissolve
    mc "Wow, Tugu Jogja benar-benar mengesankan ya!"

    hide mc

    #disini munculin image pop up tugu jogja

    show aang netral
    with dissolve
    aang "Woiyadong, sejarah Tugu Jogja ini…"

    aang "Sejarahnya ini…."

    hide aang

    show mc netral
    with dissolve
    mc "apa Aang sejarahnya?"

    hide mc

    show aang senyum
    with dissolve
    aang "Jujur aku sendiri sedikit lupa hehe, biar aku google sebentar"

    hide aang

    show mc senyum 1
    with dissolve
    mc "Hahaha, bisa saja kamu Aang."

    hide mc

    show aang netral
    with dissolve
    aang "oh ini dia sudah ketemu"

    aang    "Tugu Jogja, dibangun pada 1755 oleh Sri Sultan Hamengku Buwono I, memiliki nilai simbolis sebagai titik magis yang menghubungkan Laut Selatan, 
            Keraton Yogyakarta, dan Gunung Merapi, mencerminkan semangat persatuan rakyat dan penguasa dalam melawan penjajah."

    aang    "Dikenal sebagai Tugu Golong-Gilig, tugu awalnya berbentuk silinder dengan puncak bulat, mencapai tinggi 25 meter. 
            Namun, setelah gempa besar pada 10 Juni 1867, tugu mengalami perubahan signifikan dan dikenal sebagai De White Paal, 
            dengan bentuk persegi dan tingginya yang berkurang sebanyak 10 meter menjadi 15 meter."

    aang    "Renovasi oleh pemerintah Belanda bertujuan mengikis persatuan, namun perjuangan rakyat dan raja membuktikan sebaliknya. 
            Tugu memiliki empat bentuk fisik, dengan bagian atas berbentuk kerucut ulir."

    hide aang

    show mc kaget
    with dissolve
    mc "Wah, mengagumkan sekali, bangunan ini masih tegak setelah bertahun-tahun. Dan bentuknya yang unik, 
        seperti menara yang menjulang tinggi, benar-benar mencuri perhatian."

    hide mc

    show aang netral
    with dissolve
    aang    "Di malam hari, Tugu Jogja juga menjadi salah satu tempat favorit warga Jogja untuk 
            berkumpul dan menikmati keindahan lampu-lampu yang menghiasi sekitarnya."

    hide aang
    
    show mc netral
    with dissolve
    mc "Terima kasih telah membawaku ke sini, Aang. Sangat mengesankan!"

    hide mc

    show aang netral
    with dissolve
    aang "Next stop, Keraton Jogja skuy"

    hide aang

label keraton_yogya:
    scene bg keraton yogya
    with fade

    show aang netral
    with dissolve
    mc "Sudah sampai Tok, inilah Keraton Yogyakarta"

    hide aang

    show mc kaget
    with dissolve
    mc "Waaaaah!! Jadi ini yang mereka sebut kerajaan Keraton."

    hide mc

    #munculin pop up gambar keraton yogya

    show aang netral
    with dissolve
    aang "Betul Tok, sekarang Keraton ini dibuka untuk umum, terdapat museum untuk melihat berbagai macam koleksi barang dan peninggalan"

    hide aang

    show penjual netral
    with dissolve
    penjual "Betul itu mas! Ada banyak sekali hal menarik dalam Keraton"

    hide penjual

    show aang kaget
    with dissolve
    aang "Astaghfirullah kaget!"

    hide aang

    show mc netral
    with dissolve
    mc "Wah benar begitu kah pak?"

    hide mc

    show penjual senyum
    with dissolve
    penjual "Woooooh ya bener lah, kalo mau tau toh mas, saya ceritakan sedikit nih"

    hide penjual

    show mc netral
    with dissolve
    mc "Oh, boleh pak, saya sendiri juga penasaran"

    hide mc

    show penjual senyum
    with dissolve
    penjual "Siap mas, bapak saya dulu jadi tour guide disini jadi saya juga tau banyak."

    #disini munculin image pop up (kek presentasi): Sejarah Keraton Yogyakarta

    show penjual netral
    with dissolve
    penjual "Kesultanan Yogyakarta, bersama dengan Kesultanan Surakarta, adalah dua wilayah yang merupakan pecahan dari Kesultanan Mataram pada abad ke-18. 
            Pemecahan ini terjadi setelah terjadinya Perang Suksesi Jawa antara para pewaris tahta Kesultanan Mataram."

    penjual "Perjanjian Giyanti yang ditandatangani pada tanggal 13 Februari 1755 ini menyatakan bahwa Kerajaan Mataram dibagi menjadi dua yaitu 
            Kasunanan Surakarta Hadiningrat dan Kasultanan Ngayogyakarta Hadiningrat."

    penjual "Surakarta dipimpin oleh Susuhunan Paku Buwono III, sementara Ngayogyakarta atau sekarang Yogyakarta dipimpin oleh Pangeran Mangkubumi 
            yang kemudian bergelar Sultan Hamengku Buwono I."

    penjual "Perjanjian Giyanti ini kemudian diikuti pula dengan pertemuan antara Sultan Yogyakarta dengan Sunan Surakarta di Lebak, 
            Jatisari pada tanggal 15 Februari 1755 yang membahas Perjanjian Jatisari"

    penjual "Perjanjian Jatisari ini membahas tentang perbedaan identitas kedua wilayah yang sudah menjadi dua kerajaan yang berbeda."

    penjual "Ketika pecahannya terjadi, Sri Sultan Hamengku Buwono I mendirikan Kesultanan Yogyakarta dengan Keraton Yogyakarta sebagai pusat pemerintahannya,
            yang masih berada di wilayah Pulau Jawa, yang saat itu merupakan bagian dari Hindia Belanda."

    penjual "Pada 13 Maret 1755, proklamasi Hadeging Nagari Ngayogyakarta Hadiningrat dikumandangkan, diikuti dengan pembangunan Keraton Yogyakarta dimulai 
            pada 9 Oktober 1755."

    penjual "Sultan Hamengku Buwono I beserta keluarga memasuki Keraton pada 7 Oktober 1756. Peristiwa ini ditandai dengan sengkalan memet: 
            Dwi Naga Rasa Tunggal dan Dwi Naga Rasa Wani."

    penjual "Setelah Republik Indonesia berdiri pada 17 Agustus 1945, Sri Sultan Hamengku Buwono IX menyatakan dukungan penuh terhadap republik baru tersebut."

    penjual "Lalu, pada 5 September 1945, Sri Sultan Hamengku Buwono IX dan Sri Paduka Paku Alam VIII mengeluarkan amanat pada tanggal 5 September 1945 
            yang menyatakan bahwa wilayahnya yang bersifat kerajaan adalah bagian dari Negara Republik Indonesia. Undang-Undang nomor 13 tahun 2012 
            memperkuat status keistimewaan DIY, memastikan warisan budaya Kesultanan Yogyakarta dan Kadipaten Pakualaman tetap terjaga dan lestari."

    hide penjual

    show aang netral
    with dissolve
    aang "Wah bapak ini emang agak lain… Seluruh sejarahnya dijelaskan, bagaimana menurutmu Aang?"

    hide aang

    show mc senyum 2
    with dissolve
    mc "Wah, bapak wawasannya banyak sekali, aku semakin tertarik memasuki Keraton"

    hide mc

    show penjual senyum
    with dissolve
    penjual "Hahaha, senang sekali aku melihat orang sepertimu mas, boleh tuh ke Keraton, beli tiketnya disana mas."

    hide penjual

    show aang netral
    with dissolve
    aang "Bapak ini tau banyak sekali, sebagian besar informasi sudah kami dapatkan"

    hide aang

    show penjual netral
    with dissolve
    penjual "Tetap saja mas, kalau mau pengalaman spesial dan informasi lebih lengkap boleh banget masuk ke Keratonnya"

    penjual "Seperti yang mas sebutkan tadi, Keraton ini memang ada museumnya"

    penjual "Beberapa hal yang bisa dilihat adalah sejumlah koleksi peninggalan Sri Sultan HB IX, seperti foto-foto, piagam, medali, tanda jasa, 
            surat keputusan presiden, baju-baju bersejarah beliau, koleksi mobil-mobilan beliau sewaktu kecil , peralatan memasak, kamera 
            yang sering dipergunakan beliau, dan berbagai benda lainnya."

    penjual "Lalu juga ada museum Batik yang menyimpan berbagai macam koleksi kain batik, patung, lukisan, topeng batik,peralatan membatik,serta sepeda tua 
            sebagai pengangkut batik serta museum Kristal menyimpan berbagai koleksi kristal milik Keraton mas"

    penjual "Wajib banget dicek itu, udah jauh-jauh ke Keraton masak iya gak mau masuk"

    hide penjual

    show mc senyum 2 at left
    with dissolve
    mc "Ayo Aang kita masuk, aku tidak sabar melihat semua koleksi Keraton"

    show aang netral at right
    with dissolve
    aang "Baik Tok ayo, terima kasih ya pak"

    hide mc
    
    hide aang

    #disini Char Totok dan Aang otw jalan off screen

    show penjual kaget
    with dissolve
    penjual "Sebentar mas!!! hampir lupa…"

    hide penjual

    #disini Char Totok dan Aang berhenti jalan terus nengok ke arah penjual

    show aang flat
    with dissolve
    aang "Ada apa pak?"

    hide aang

    show penjual senyum
    with dissolve
    penjual "Sebelum masuk Keraton, beli minum dulu biar gak haus, ayo larisin dagangan saya"

    hide penjual

    show aang flat
    with dissolve
    aang "Yaelah pak…."

    hide aang

    show mc senyum 1
    with dissolve
    mc "Haha baiklah pak, aku juga kehausan dari tadi"

    hide mc

    show aang netral
    with dissolve
    aang "Baiklah Totok, akan ku traktir kamu, mau minum apa kamu?"

    hide aang
    
    show mc bingung
    menu:
        mc "Aku mau minum apa?"
        
        "Air Dingin":
            show penjual senyum
            penjual "Terima kasih banyak mas, selamat bersenang-senang di Keraton nggih."
            hide penjual
            jump joglo_keraton
        "Soft Drink":
            show penjual senyum
            penjual "Terima kasih banyak mas, selamat bersenang-senang di Keraton nggih."
            hide penjual
            jump joglo_keraton        
        "Jamu{b}(?){/b}":
            show mc bingung
            mc "Jamu? Ini apa ya pak? Kok warnanya ada yang kuning dan coklat begini?"

            hide mc

            show penjual senyum
            penjual "Woooo, mas ini punya bakat menemukan benda baguss mas. Biar saya jelaskan apa ini."

            penjual "Jamu atau djamoe merupakan singkatan dari djampi yang berarti doa atau obat dan husada yang berarti kesehatan. 
            Dengan kata lain djamoe ini artinya doa atau obat untuk meningkatkan kesehatan."

            penjual "Sejak zaman penjajahan Belanda pada awal abad ke-17, para dokter berkebangsaan Belanda, Inggris ataupun Jerman tertarik mempelajari jamu mass sampe mereka itu menulis buku tentang jamu"

            penjual "Sampai pada 27 Mei 2008 Presiden Indonesia Susilo Bambang Yudhoyono secara resmi menetapkan tanggal 27 Mei sebagai hari kebangkitan Jamu Indonesia sekaligus meresmikan jamu sebagai kearifan lokal milik Indonesia."

            penjual "Bayangin mas, sebegitu pentingnya Jamu, sampai ada penambahan ayat baru tentang pengobatan dan perawatan herbal, itu merupakan salah satu upaya pemerintah dalam pelestarian jamu."

            penjual "Jamu ini ada banyak jenis jamu yang ada di Indonesia yaitu  beras kencur, kunyit asam, sinom, cabe puyang, pahitan, uyup-uyup, kunci sirih, kudu laos. Jamu yang sedang mas lihat ini adalah jamu kunyit asam."

            penjual "Kunyit asam adalah minuman tradisional atau jamu yang diracik dari dua jenis rempah yang berbeda, yaitu kunyit dan asam Jawa. 
            Di Indonesia, kedua rempah ini tidak hanya bisa digunakan sebagai bumbu masakan, tetapi juga diolah menjadi minuman yang dikenal berkhasiat bagi kesehatan."

            penjual "Jadi gimana mas? Tertarik beli toh?"

            hide penjual
            
            show mc senyum 2
            mc "Wahhhh, boleh deh pak saya coba satu, Aang, kalo boleh Jamu 1 ya"

            hide mc

            show aang flat
            aang "Korban marketing dan iklan kamu ini Tok... Bapak ini emang jiwa pedagangnya mahir."

            hide aang

            show aang senyum
            aang "Baiklah kalau begitu, Jamu nya 2 ya pak, saya sendiri juga mau nyoba."

            hide aang

            show penjual senyum
            penjual "Siap mas e. Saya bungkus plastik nih khusus buat mas e."

            penjual "Terima kasih banyak mas, selamat bersenang-senang di Keraton nggih."

            hide penjual
            
            jump joglo_keraton
return
        
label joglo_keraton:
    scene bg joglo keraton
    with fade

    show mc senyum 2
    with dissolve
    mc "Luar biasa sekali. Bangunan-bangunan dan koleksi barang di sini memiliki sejarah yang begitu kaya"

    hide mc

    show aang netral
    with dissolve
    aang "iya tuh, Kraton Yogyakarta merupakan pusat kebudayaan dan kekuasaan di masa lalu. Banyak cerita menarik yang tersembunyi di balik temboknya."

    hide aang

    show mc netral
    with dissolve
    mc "Benar-benar menarik. Senang bisa melihat dan mempelajari sejarah dan budaya."

    hide mc

    show aang netral
    with dissolve
    aang "Aku tinggal ke toilet dulu ya Tok, jangan pergi jauh-jauh."

    hide aang

    show mc netral
    with dissolve
    mc "Baiklah, aku akan menunggu mu."

    hide mc

    #disini Char Aang lari off screen

    show mc netral
    with dissolve
    mc "Perjalananku di Jogja sejauh ini menyenangkan sekali, aku jadi penasaran apakah kakek dulu sering pergi mengunjungi tempat wisata seperti ini 
        di masa mudanya."
    
    mc "…"

    mc "(Kakek akan senang melihat ini, andaikan kakek bisa pergi bersamaku)"

    mc "(Jangan khawatir kek, aku akan menceritakan seluruh kisahku dan menjadi koki kuliner terhebat yang pernah ada, nantikan aku di rumah)"

    #disini tambahin suara bonang dipukul

    show mc bingung
    with dissolve
    mc "Hmmm? Suara apa itu?"

    #disini munculin iamge pop up Gamelan kek Bonang, Saron, Gong

    show mc kaget
    with dissolve
    mc "Wah! Menarik sekali, apakah ini alat musik khas Yogyakarta? Banyak sekali jenisnya, yang ini terlihat seperti mangkuk. 
        Yang ini seperti piano, hmmmm banyak sekali jumlahnya."

    hide mc

    show kg netral
    with dissolve
    kg "Hai anak muda, apakah kamu tertarik dengan gamelan?"

    hide kg

    show mc bingung
    with dissolve
    mc "Gamelan? Apa itu pak? Apakah semacam tarian?"

    hide mc

    show kg senyum
    with dissolve
    kg "Hahaha, instrumen yang di depanmu ini disebut Gamelan, jenisnya memang bervariasi sekali"

    hide kg

    show mc senyum 2
    with dissolve
    mc "Wah, jadi ini alat musik dari Yogyakarta…"

    hide mc

    show kg netral
    with dissolve
    kg "Benar sekali, sebenarnya gamelan ini berasal dari Jawa dan Bali, Gamelan ini sering digunakan untuk musik karawitan. 
        Oh kau mungkin tidak tau arti karawitan."
    
    kg "Karawitan adalah seni gamelan dan seni suara yang bertangga nada slendro dan pelog. Karawitan berasal dari bahasa Jawa yaitu kata \"rawit\" yang berarti
        halus dan lembut Jadi karawitan ini berarti kelembutan perasaan yang terkandung dalam seni gamelan."

    hide kg

    #disini Char Aang jalan on screen

    show aang netral
    with dissolve
    aang "Hai Totok, aku kembali, sedang apa kamu?"

    aang "Oh, apakah gamelan gamelan ini menarik perhatianmu?"

    hide aang

    show mc netral
    with dissolve
    mc "Iya Aang, bapak ini baru saja menjelaskan kepadaku apa itu Gamelan."

    hide mc

    show aang senyum
    with dissolve
    aang "Hahaha, sugeng enjing pak, temanku dari luar Jogja nih. Tolong jelasin semua tentang gamelan"

    hide aang

    show kg senyum
    with dissolve
    kg "Ahahaha, dengan senang hati anak muda."

    kg "Apakah kau ingin dijelaskan secara jelas?"

    menu:
        "{color=#ff0000}Pilihanmu dapat berpengaruh dalam pengalamanmu*"

        "Penjelasan Singkat, aku hanya ingin tahu sedikit":
                $ pilihan = 1
                $ jumlah_soal = 10
                show kg senyum
                kg "Baik, akan ku mulai penjelasannya, perhatikan ya."
                hide kg
                call gamelan1
                jump after_gamelan
        "Penjelasan sedang, ilmu ini pasti akan berguna bagiku":
                $ pilihan = 2
                $ jumlah_soal = 15
                show kg senyum
                kg "Baik, akan ku mulai penjelasannya, perhatikan ya."
                hide kg
                call gamelan1
                call gamelan2
                jump after_gamelan
        "Penjelasan Lengkap, beri tahu aku semua gamelan": 
                $ pilihan = 3
                $ jumlah_soal = 20
                show kg senyum
                kg "Baik, akan ku mulai penjelasannya, perhatikan ya."
                hide kg
                call gamelan1
                call gamelan2
                call gamelan3
                jump after_gamelan

return

label gamelan1:
        show bonang with dissolve

        kg "Bonang adalah instrumen gamelan berbentuk ceret atau pot yang diletakan di atas string (tali) dalam bingkai kayu (rancak)."

        kg "Bonang termasuk dalam pencon yang merupakan alat musik dari logam dan berbentuk cekungan di bawahnya dengan poros cembung untuk dipukul"

        aang "Bentuknya mirip mangkuk kek"

        kg "Masing-masing pot kemudian memiliki poros cembung (pencon) di bagian atas sebagai pusat untuk dipukul."

        kg "Bonang dalam set gamelan memiliki beberapa jenis, yaknii bonang penerus, barung, dan panembung."

        kg "Cara bermain boning adalah memukul bagian cekungan atau penutupnya dengan tongkat pemukul khusus."

        hide bonang with dissolve
        #image pop up: Saron
        show saron with dissolve

        kg "Saron atau biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan (wilahan) dari logam."

        kg "Saron memiliki 6 atau 7 (1 oktaf) bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator."

        kg "Cara memainkan alat musik saron adalah memukul bilahan logam menggunakan tabuhan tangan kanan dan menahan bilahan yang dipukul sebelumnya menggunakan tangan kiri agar menghilangkan suara dengungan yang tersisa. Cara ini biasa disebut dengan teknik memahat atau memencet."

        hide saron with dissolve
        #image pop up: Gong
        show gong with dissolve

        kg "Hampir serupa dengan bonang dan kenong, gong juga memiliki bentuk cembung di bagian atas dengan ukuran yang lebih besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."

        aang "Suara yang dihasilkan sama persis seperti namanya, {i}Gongggggg{/i}"

        kg "Menyerupai bentuk piringan besar, gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas. Cara memainkan alat musik ini dipukul bagian kecembungannya menggunakan tongkat khusus."

        hide gong with dissolve
        #image pop up: Kendhang
        show kendang with dissolve

        kg "Kendhang atau gendang adalah salah satu instrumen gamelan Jawa yang dapat mengatur irama musik gamelan."
        
        aang "{i}Tak dung, dung tak, gendhes{/i}"

        kg "Cara memainkan alat musik gendang adalah memukul dengan telapak tangan bagian pinggir kendhang yang terbuat dari kulit hewan."

        kg "Kendhang memiliki berbagai macam jenis dan ukuran, yakni ketipung gamelan berukuran kecil dan kendang ciblon atau kebar gamelan yang berukuran sedang."

        kg "Kendang Ketipung biasanya memiliki kendang pasangan, yakni kendang gedhe atau kendhang kalih."

        hide kendang with dissolve
        #image pop up: Gambang
        show gambang with dissolve

        kg "Gambang mirip dengan saron dan demung, namun bilahan alat musik ini terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik."

        mc "Saron dan demung tadi dari logam, yang ini dari kayu wow"

        kg "Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu. Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang."

        kg "Cara memainkan alat musik gambang adalah memukul tiap bilangnya menggunakan pemukul khusus yang disebut tabuh. Hampir serupa dengan saron dan demung, bilang perlu ditahan setelah dipukul agar tidak meninggalkan suara."
        hide gambang with dissolve
return

label gamelan2:
        #image pop up: Siter
        show siter with dissolve
        kg "Siter adalah salah satu instrumen gamelan yang memainkannya dengan cara dipetik seperti alat musik guzheng asal cina atau sitar asal India."

        kg "Alat musik ini sudah jarang ditemukan atau digunakan dalam set-set gamelan saat ini. Alat musik ini biasa juga disebut gitar Jawa yang memiliki suara yang khas."

        aang "Hmmm, mirip gitar sedikit sih"

        kg "Alat musik siter memiliki dua sisi dengan nada yang berbeda, yakni sisi pelog dan slendro. Siter dianggap sebagai alat musik yang mengadopsi alat musik India karena hampir sama dengan Sitar yang merupakan alat musik tradisional india."
        hide siter with dissolve
        #image pop up: Kenong
        show kenong with dissolve
        kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan. Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."

        mc "seperti Bonang kesepian, lucu sekali"

        kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh. Alat musik ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."

        kg "Cara memainkan kenong serupa dengan memainkan bonang dengan memukul menggunakan tongkat khusus di bagian cekungan atau benjolan kenong."
        hide kenong with dissolve
        #image pop up: Gender
        show gender with dissolve
        kg "Gender adalah instrumen gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya. Ada 10 sampai 14 bilah pada alat musik gender yang terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."

        mc "Waaah, yang ini mirip gambang dan slenthem tadi"

        kg "Cara memainkan alat musik ini adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa). Dalam satu set gamelan lengkap, ada tiga jenis gender yang digunakan, yakni  slendro, pelog pathet nem lan lima, dan pelog pathet barang."
        hide gender with dissolve
        #image pop up: Kempul
        show kempul with dissolve
        kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."

        aang "Haha kayak Gong mini kembar"

        kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus. Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."
        hide kempul with dissolve
return

label gamelan3:
        #image pop up: Demung
        show demung with dissolve
        kg "Sama halnya dengan saron, demung juga masuk dalam golongan balungan dalam instrumen gamelan. Biasanya ada dua demung jenis pelog dan slendro dalam gamelan."

        mc "Mirip sekali dengan saron bentuknya"

        kg  "Alat musik ini menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar."

        kg  "Cara bermain demung serupa dengan saron hanya saja tabuh demung memiliki ukuran yang lebih besar dan berat daripada tabuh saron."
        hide demung with dissolve
        #image pop up: Rebab
        show rebab with dissolve
        kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."

        aang "Wah, namanya seperti kebab, aku jadi lapar"

        kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas. Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."
        hide rebab with dissolve
return

label after_gamelan:
        show kg senyum
        with dissolve
        kg "Bagaimana? Gamelan beragam dan menarik bukan?"

        hide kg

        show mc senyum 2
        with dissolve
        mc "Menarik sekali pak, ternyata gamelan ada berbagai jenis juga"

        hide mc

        show aang netral
        with dissolve
        aang "Aduh, kepalaku agak sakit dengan overload informasi"

        hide aang

        show kg senyum
        with dissolve
        kg "Ahaha, bagaimana kalau kita menguji pengetahuanmu? Ayo bermain tebak tebakan bersamaku untuk mengasah ingatan kalian. Jangan sampai kalian kalah dengan otak pak tua ini."
        hide kg

        if pilihan == 1:
                call pertanyaan_gamelan_1
                jump hitung_skor_gamelan
        elif pilihan == 2:
                call pertanyaan_gamelan_1
                call pertanyaan_gamelan_2
                jump hitung_skor_gamelan
        elif pilihan == 3:
                call pertanyaan_gamelan_1
                call pertanyaan_gamelan_2
                call pertanyaan_gamelan_3
                jump hitung_skor_gamelan

label pertanyaan_gamelan_1:
        #pertanyaan 1
        #tampilin gambar bonang
        show bonang with dissolve

        kg "Gamelan ini berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak)." 

        kg "Gamelan ini termasuk pencon yaitu dari logam,"

        hide bonang
        menu:
                kg "apa nama dari gamelan ini?"
                "Bonang":
                    $ jawab_benar += 1
                    python:
                        jawaban_benar()
                "Gong":
                    python:
                        jawaban_salah()
                    show bonang with dissolve
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                    hide bonang with dissolve
                "Gambang":
                    python:
                        jawaban_salah()
                    show bonang with dissolve
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                    hide bonang with dissolve
                "Gender":
                    python:
                        jawaban_salah()
                    show bonang with dissolve
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                    hide bonang with dissolve
                "Saron":
                    python:
                        jawaban_salah()
                    show bonang with dissolve
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                    hide bonang with dissolve
        
        #pertanyaan 2
        kg "Gamelan ini biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator,"

        kg "manakah gamelan yang saya deskripsikan?"
            #opsi dalam bentuk gambar
        call screen opsi_gambar_saron()

        #pertanyaan 3
        #tampilin gambar gambang
        show gambang with dissolve
        kg "Bilahan gamelan ini terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik. Ada 18 bilah nada yang terletak di atas sebuah rak konektor berbentuk perahu."

        kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang,"

        hide gambang
        menu:
            kg "apa nama dari gamelan ini?"
            "Gambang":
                $ jawab_benar += 1
                python:
                    jawaban_benar()
            "Slenthem":
                python:
                    jawaban_salah()
                show gambang with dissolve
                kg "Gambang terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik. Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu."
                kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang"
                hide gambang with dissolve
            "Gong":
                python:
                    jawaban_salah()
                show gambang with dissolve
                kg "Gambang terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik. Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu."
                kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang"
                hide gambang with dissolve
            "Bonang":
                python:
                    jawaban_salah()
                show gambang with dissolve
                kg "Gambang terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik. Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu."
                kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang"
                hide gambang with dissolve
            "Saron":
                python:
                    jawaban_salah()
                show gambang with dissolve
                kg "Gambang terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik. Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu."
                kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang"
                hide gambang with dissolve

        #pertanyaan 4
        kg "Gamelan Jawa ini dapat mengatur irama musik gamelan."

        kg "Cara memainkan gamelan ini adalah dengan memukul dengan telapak tangan bagian pinggir gamelan yang terbuat dari kulit hewan,"

        kg "manakah gamelan yang saya deskripsikan?"

        call screen opsi_gambar_kendhang()

        #pertanyaan 5
        #tampilin gambar Gong
        show gong with dissolve
        kg "Gamelan ini memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."
        
        kg "Gamelan ini terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas."

        kg "Gamelan ini dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus,"

        hide gong
        menu:
            kg "apa nama dari gamelan ini?"
            "Saron":
                python:
                    jawaban_salah()
                show gong with dissolve
                kg "Gong memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."
                kg "Gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas." 
                kg "Gong dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus."
                hide gong with dissolve
            "Kendhang":
                python:
                    jawaban_salah()
                show gong with dissolve
                kg "Gong memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."
                kg "Gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas." 
                kg "Gong dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus."
                hide gong with dissolve
            "Slenthem":
                python:
                    jawaban_salah()
                show gong with dissolve
                kg "Gong memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."
                kg "Gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas." 
                kg "Gong dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus."
                hide gong with dissolve
            "Gong":
                $ jawab_benar += 1
                python:
                    jawaban_benar()
            "Bonang":
                python:
                    jawaban_salah()
                show gong with dissolve
                kg "Gong memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."
                kg "Gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas." 
                kg "Gong dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus."
                hide gong with dissolve

        #pertanyaan 6
        kg "Gamelan ini masuk dalam keluarga balungan.  Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain,"

        kg "manakah gamelan yang saya deskripsikan?"
        
        call screen opsi_gambar_slenthem()

        #pertanyaan 7
        #tampilin gambar Saron
        show saron with dissolve
        kg "Gamelan ini biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator,"
        hide saron

        menu:
            kg "apa nama dari gamelan ini?"
            "Bonang":
                python:
                    jawaban_salah()
                show saron with dissolve
                kg "Saron itu biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator"
                hide saron with dissolve
            "Saron":
                $ jawab_benar += 1
                python:
                    jawaban_benar()
            "Gambang":
                python:
                    jawaban_salah()
                show saron with dissolve
                kg "Saron itu biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator"
                hide saron with dissolve
            "Slenthem":
                python:
                    jawaban_salah()
                show saron with dissolve
                kg "Saron itu biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator"
                hide saron with dissolve
            "Gong":
                python:
                    jawaban_salah()
                show saron with dissolve
                kg "Saron itu biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator"
                hide saron with dissolve

        #pertanyaan 8
        kg "Gamelan ini memiliki bentuk cembung di bagian atas dengan ukuran yang besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."

        kg "Gamelan ini terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas."

        kg "Gamelan ini dimainkan dengan memukul bagian kecembungannya menggunakan tongkat khusus,"

        kg "manakah gamelan yang saya deskripsikan?"

        call screen opsi_gambar_gong()

        #pertanyaan 9
        #tampilin gambar Slenthem
        show slenthem with dissolve
        kg "Gamelan ini masuk dalam keluarga balungan.  Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain,"
        hide slenthem

        menu:
            kg "apa nama dari gamelan ini?"
            "Kendhang":
                python:
                    jawaban_salah()
                show slenthem with dissolve
                kg "Gamelan slenthem adalah salah satu instrumen gamelan yang masuk dalam keluarga balungan seperti saron dan demung."
                kg "Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain."
                hide slenthem with dissolve
            "Slenthem":
                $ jawab_benar += 1
                python:
                    jawaban_benar()
            "Saron":
                python:
                    jawaban_salah()
                show slenthem with dissolve
                kg "Gamelan slenthem adalah salah satu instrumen gamelan yang masuk dalam keluarga balungan seperti saron dan demung."
                kg "Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain."
                hide slenthem with dissolve
            "Gong":
                python:
                    jawaban_salah()
                show slenthem with dissolve
                kg "Gamelan slenthem adalah salah satu instrumen gamelan yang masuk dalam keluarga balungan seperti saron dan demung."
                kg "Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain."
                hide slenthem with dissolve
            "Bonang":
                python:
                    jawaban_salah()
                show slenthem with dissolve
                kg "Gamelan slenthem adalah salah satu instrumen gamelan yang masuk dalam keluarga balungan seperti saron dan demung."
                kg "Gamelan ini menghasilkan dengungan nada yang rendah atau menggema mengikuti nada instrumen alat musik balungan yang lain."
                hide slenthem with dissolve

        #pertanyaan 10
        kg "Gamelan ini berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak)."

        kg "Gamelan ini termasuk pencon yaitu dari logam,"

        kg "manakah gamelan yang saya deskripsikan?"

        call screen opsi_gambar_bonang()
return

label pertanyaan_gamelan_2:
    #pertanyaan 11
    #tampilin gambar Gender
    show gender with dissolve
    kg "Gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya yang terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."

    kg "Cara memainkan gamelan adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa),"
    hide gender

    menu:
        kg "apa nama dari gamelan ini?"
        "Gender":
            $ jawab_benar += 1
            python:
                jawaban_benar()
        "Kenong":
            python:
                jawaban_salah()
            show gender with dissolve
            kg "Gender adalah instrumen gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya."
            kg "Gender terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."
            kg "Cara memainkan alat musik ini adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa)."
            kg "Dalam satu set gamelan lengkap, ada tiga jenis gender yang digunakan, yakni  slendro, pelog pathet nem lan lima, dan pelog pathet barang."
            hide gender with dissolve
        "Kempul":
            python:
                jawaban_salah()
            show gender with dissolve
            kg "Gender adalah instrumen gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya."
            kg "Gender terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."
            kg "Cara memainkan alat musik ini adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa)."
            kg "Dalam satu set gamelan lengkap, ada tiga jenis gender yang digunakan, yakni  slendro, pelog pathet nem lan lima, dan pelog pathet barang."
            hide gender with dissolve
        "Rebab":
            python:
                jawaban_salah()
            show gender with dissolve
            kg "Gender adalah instrumen gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya."
            kg "Gender terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."
            kg "Cara memainkan alat musik ini adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa)."
            kg "Dalam satu set gamelan lengkap, ada tiga jenis gender yang digunakan, yakni  slendro, pelog pathet nem lan lima, dan pelog pathet barang."
            hide gender with dissolve
        "Gong":
            python:
                jawaban_salah()
            show gender with dissolve
            kg "Gender adalah instrumen gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya."
            kg "Gender terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."
            kg "Cara memainkan alat musik ini adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa)."
            kg "Dalam satu set gamelan lengkap, ada tiga jenis gender yang digunakan, yakni  slendro, pelog pathet nem lan lima, dan pelog pathet barang."
            hide gender with dissolve

    #pertanyaan 12
    kg "Gamelan ini memiliki bentuk cembung di bagian atas dengan ukuran yang sedang dan posisinya digantung, tidak diletakan pada lapisan tertentu."

    kg "Gamelan ini masuk dalam keluarga pencon, bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan,"

    kg "manakah gamelan yang saya deskripsikan?"

    call screen opsi_gambar_kempul()
    
    #pertanyaan 13
    #tampilin gambar Kenong
    show kenong with dissolve
    kg "Gamelan ini masuk dalam keluarga pencon dan memiliki bentuk fisik lebih gemuk dari gamelan pencon lainnya."

    kg "Gamelan ini diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran saat ditabuh."

    kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas,"
    hide kenong

    menu:
        kg "apa nama dari gamelan ini?"
        "Rebab":
            python:
                jawaban_salah()
            show kenong with dissolve
            kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan."
            kg "Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."
            kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh."
            kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."
            hide kenong with dissolve
        "Kenong":
            $ jawab_benar += 1
            python:
                jawaban_benar()
        "Kendhang":
            python:
                jawaban_salah()
            show kenong with dissolve
            kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan."
            kg "Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."
            kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh."
            kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."
            hide kenong with dissolve
        "Slenthem":
            python:
                jawaban_salah()
            show kenong with dissolve
            kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan."
            kg "Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."
            kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh."
            kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."
            hide kenong with dissolve
        "Saron":
            python:
                jawaban_salah()
            show kenong with dissolve
            kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan."
            kg "Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."
            kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh."
            kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."
            hide kenong with dissolve
    
    #pertanyaan 14
    kg "Gamelan ini penting untuk mengelaborasi dan menghiasi melodi dasar."

    kg "Cara memainkannya bisa dikreasikan secara bebas."

    kg "Gamelan ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka,"

    kg "manakah gamelan yang saya deskripsikan?"

    call screen opsi_gambar_rebab()

    #pertanyaan 15
    #tampilin gambar Kempul
    show kempul with dissolve
    kg "Gamelan ini memiliki bentuk cembung di bagian atas dengan ukuran yang sedang dan posisinya digantung, tidak diletakan pada lapisan tertentu."

    kg "Gamelan ini masuk dalam keluarga pencon, bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan,"
    hide kempul
    menu:
        kg "apa nama dari gamelan ini?"
        "Rebab":
            python:
                jawaban_salah()
            show kempul with dissolve
            kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."
            kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus."
            kg " Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."
            hide kempul with dissolve
        "Gong":
            python:
                jawaban_salah()
            show kempul with dissolve
            kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."
            kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus."
            kg " Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."
            hide kempul with dissolve
        "Kendhang":
            python:
                jawaban_salah()
            show kempul with dissolve
            kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."
            kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus."
            kg " Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."
            hide kempul with dissolve
        "Siter":
            python:
                jawaban_salah()
            show kempul with dissolve
            kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."
            kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus."
            kg " Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."
            hide kempul with dissolve
        "Kempul":
            $ jawab_benar += 1
            python:
                jawaban_benar()
return

label pertanyaan_gamelan_3:
    #pertanyaan 16
    kg "Gamelan ini biasa juga disebut gitar Jawa yang memiliki suara yang khas yang terbuat dari kayu jati."

    kg "Gamelan yang memainkannya dengan cara dipetik seperti alat musik guzheng asal cina atau sitar asal India,"

    kg "manakah gamelan yang saya deskripsikan?"

    call screen opsi_gambar_siter()

    #pertanyaan 17
    #tampilin gambar Demung
    show demung with dissolve
    kg "Gamelan ini masuk dalam golongan balungan dalam instrumen gamelan."

    kg "Gamelan ini dimainkan dengan cara ditabuh dan menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar,"
    hide demung
    menu:
        kg "apa nama dari gamelan ini?"
        "Gender":
            python:
                jawaban_salah()
            show demung with dissolve
            kg "Demung masuk dalam golongan balungan dalam instrumen gamelan."
            kg "Biasanya ada dua demung jenis pelog dan slendro dalam gamelan."
            kg "Alat musik ini menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar."
            kg "Cara bermain demung serupa dengan saron hanya saja tabuh demung memiliki ukuran yang lebih besar dan berat daripada tabuh saron."
            hide demung with dissolve
        "Demung":
            $ jawab_benar += 1
            python:
                jawaban_benar()
        "Bonang":
            python:
                jawaban_salah()
            show demung with dissolve
            kg "Demung masuk dalam golongan balungan dalam instrumen gamelan."
            kg "Biasanya ada dua demung jenis pelog dan slendro dalam gamelan."
            kg "Alat musik ini menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar."
            kg "Cara bermain demung serupa dengan saron hanya saja tabuh demung memiliki ukuran yang lebih besar dan berat daripada tabuh saron."
            hide demung with dissolve
        "Kenong":
            python:
                jawaban_salah()
            show demung with dissolve
            kg "Demung masuk dalam golongan balungan dalam instrumen gamelan."
            kg "Biasanya ada dua demung jenis pelog dan slendro dalam gamelan."
            kg "Alat musik ini menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar."
            kg "Cara bermain demung serupa dengan saron hanya saja tabuh demung memiliki ukuran yang lebih besar dan berat daripada tabuh saron."
            hide demung with dissolve
        "Gong":
            python:
                jawaban_salah()
            show demung with dissolve
            kg "Demung masuk dalam golongan balungan dalam instrumen gamelan."
            kg "Biasanya ada dua demung jenis pelog dan slendro dalam gamelan."
            kg "Alat musik ini menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar."
            kg "Cara bermain demung serupa dengan saron hanya saja tabuh demung memiliki ukuran yang lebih besar dan berat daripada tabuh saron."
            hide demung with dissolve

    #pertanyaan 18
    kg "Bilahan gamelan ini terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik."

    kg "Ada 18 bilah nada yang terletak di atas sebuah rak konektor berbentuk perahu."

    kg "Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang,"

    kg "manakah gamelan yang saya deskripsikan?"

    call screen opsi_gambar_gambang()

    #pertanyaan 19
    #tampilin gambar Rebab
    show rebab with dissolve
    kg "Gamelan ini penting untuk mengelaborasi dan menghiasi melodi dasar."

    kg "Cara memainkannya bisa dikreasikan secara bebas."

    kg "Gamelan ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka,"
    hide rebab
    menu:
        kg "apa nama dari gamelan ini?"
        "Slenthem":
            python:
                jawaban_salah()
            show rebab with dissolve
            kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."
            kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas."
            kg "Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."
            hide rebab with dissolve
        "Saron":
            python:
                jawaban_salah()
            show rebab with dissolve
            kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."
            kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas."
            kg "Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."
            hide rebab with dissolve
        "Rebab":
            $ jawab_benar += 1
            python:
                jawaban_benar()
        "Kenong":
            python:
                jawaban_salah()
            show rebab with dissolve
            kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."
            kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas."
            kg "Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."
            hide rebab with dissolve
        "Kendhang":
            python:
                jawaban_salah()
            show rebab with dissolve
            kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."
            kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas."
            kg "Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."
            hide rebab with dissolve
            
    #pertanyaan 20
    kg "Gamelan ini masuk dalam keluarga pencon dan memiliki bentuk fisik lebih gemuk dari gamelan pencon lainnya."

    kg "Gamelan ini diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran saat ditabuh."

    kg "Gamelan ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas,"

    kg "manakah gamelan yang saya deskripsikan?"

    call screen opsi_gambar_kenong()
return

label hitung_skor_gamelan:
    if jawab_benar == jumlah_soal:
        show kg senyum
        kg "Hahaha, kamu ini memang cocok sekali menjadi penerus bangsa, saya senang sekali melihat generasi muda seperti kalian sangat bersemangat mempelajari Gamelan."

        hide kg

        show mc senyum 2 
        mc "Terima kasih pak, senang sekali dapat mempelajari keragaman dan keunikan alat musik tradisional."

        hide mc

        show aang netral
        aang " Betul itu pak, saya orang Jogja aja baru tau ada Gamelan sebanyak itu"

        hide aang

        show kg netral
        kg "Sama-sama nak, senang bisa memberikan ilmu bermanfaat bagi kalian"

        kg "Melihat antusiasme kalian membuatku semakin semangat untuk acara malam ini"

        hide kg

        show aang netral
        aang "Memangnya malam ini ada apa pak?"

        hide aang

        show kg netral
        kg "Kalian belum tahu kah? Malam ini akan ada pertunjukan Gamelan"

        kg "Sebagai penghargaan, kalian akan ku berikan tiket untuk acara pertunjukannya"

        hide kg

        #image pop up 2 tiket & sound effect maybe?

    elif jawab_benar > jumlah_soal / 2:
        show kg senyum
        kg "Hebat sekali nak, saya senang sekali melihat generasi muda seperti kalian sangat bersemangat mempelajari Gamelan."

        hide kg

        show mc netral
        mc "Terima kasih pak, senang sekali dapat mempelajari keragaman dan keunikan alat musik tradisional."

        hide mc

        show aang netral
        aang "Betul itu pak, saya orang Jogja aja baru tau ada Gamelan sebanyak itu"

        hide aang

        show kg netral
        kg "Sama-sama nak, senang bisa memberikan ilmu bermanfaat bagi kalian"

        kg "Melihat antusiasme kalian membuatku semakin semangat untuk acara malam ini"

        hide kg

        show aang netral
        aang "Memangnya malam ini ada apa pak?"

        hide aang
        
        show kg netral
        kg "Kalian belum tahu kah? Malam ini akan ada pertunjukan Gamelan"

        kg "Sebagai penghargaan, kalian akan ku berikan tiket untuk acara pertunjukannya"

        hide kg

        #image pop up 2 tiket

    else:
        show mc flat
        mc "Aduh, banyak sekali jawabanku yang salah  tadi, sepertinya {color=#ff0000}aku harus lebih memperhatikan catatanku"

        hide mc

        show aang senyum
        aang "Haha tidak apa apa Tok, kamu juga orang luar, bahkan aku yang orang Jogja pun tidak tau bahwa gamelan ada sebanyak itu"

        hide aang

        show mc netral
        mc "Mulai sekarang aku akan semakin rajin mencari tahu tentang budaya dan alat tradisional, semua hal ini begitu menarik bagiku"

        hide mc

        show kg senyum
        kg "Wah, antusias sekali dirimu nak, melihat kalian membuatku semakin semangat untuk acara malam ini"

        hide kg

        show aang flat
        aang "Memangnya malam ini ada apa pak?"

        hide aang

        show kg netral
        kg "Kalian belum tahu kah? Malam ini akan ada pertunjukan Gamelan"

        kg "Sebagai penghargaan, kalian akan ku berikan tiket untuk acara pertunjukannya"

        hide kg

        #image pop up 2 tiket
    
    show mc senyum 2
    mc "Waaaah, tiket gratis, terima kasih banyak bapak, kita pasti akan datang malam ini."

    hide mc

    show aang senyum
    aang "Waw, sudah berapa tahun aku tidak melihat pertunjukan Gamelan"

    hide aang

    show kg senyum
    kg "Hahaha, jangan lupa menyemangati kakek tua ini di kursi paling depan, akan ku nantikan kehadiran kalian."

    hide kg

    show mc netral
    mc "Tentu saja pak, sekali lagi terima kasih, kita pamit dulu ya"

    hide mc

    show kg senyum
    kg "Sama-sama, hati-hati di jalan anak muda."

    kg "(melihat penerus bangsa yang begitu bersemangat meyakinkanku dengan masa depan)"

    hide kg

    show bg keraton yogya
    with fade
    
    show aang netral
    aang "Sepertinya tidak sia sia kita pergi ke Keraton, apalagi setelah bertemu bapak baik itu."

    hide aang

    show mc senyum 2
    mc "Wah, semua tempat ini sungguh luar biasa!"

    mc "Aku tidak bisa membayangkan betapa kaya akan sejarah dan budaya Jogja."

    mc "Aku sangat beruntung bisa melihatnya dengan mata kepala sendiri."

    hide mc

    show aang senyum
    aang "Aku senang kamu merasa seperti itu."

    aang "Hari sudah sore, Next stop, Alun-Alun skuy!"

label alun_alun:
    scene bg trotoar
    with fade

    show aang netral
    with dissolve
    aang "Alun-Alun yang akan kita kunjungi namanya alun-alun kidul Tok."

    show aang netral
    with dissolve
    aang "Perjalanannya sedikit jauh, tapi kita akan melewati banyak tempat bersejarah kok jadi perjalanannya tidak akan membosankan"

    hide aang

    show mc netral
    with dissolve
    mc "Baiklah Aang, waktu kita juga masih banyak, pertunjukan gamelannya mulai cukup malam."

    show mc kaget
    with dissolve
    mc "Wah, bangunan apa itu? Aang, lihat betapa megahnya bangunannya."

    hide mc

label benteng:
    scene bg vredeburg depan
    with fade

    show aang netral
    with dissolve
    aang "Oh itu, itu adalah Benteng Vredeburg!"

    aang    "Benteng ini memiliki peran penting dalam sejarah Yogyakarta. Selama masa penjajahan Belanda, Benteng Vredeburg menjadi pusat administrasi militer 
            dan politik di wilayah ini."

    hide aang

    show mc senyum 2
    with dissolve
    mc "Wah, benarkah? Jadi ini adalah salah satu peninggalan dari zaman kolonial Belanda?"

    hide mc

    show aang netral
    with dissolve
    aang "Benar Tok, Benteng ini memiliki sejarah yang sangat kaya."

    aang    "Benteng Vredeburg awalnya dibangun pada tahun 1760 atas perintah dari Sri Sultan Hamengku Buwono I dan pemerintah Belanda, 
            dipimpin oleh Nicholaas Harting. Awalnya, benteng ini didirikan dengan tujuan menjaga keamanan Keraton Yogyakarta, tetapi sebenarnya untuk 
            memudahkan pengawasan Belanda terhadap aktivitas keraton."

    aang    "Bangunan awalnya sederhana, terbuat dari tanah dan kayu pohon kelapa, dengan keempat sudutnya diberi nama tertentu: 
            Jaya Wisesa (sudut barat laut), Jaya Purusa (sudut timur laut), Jaya Prakosaningprang (sudut barat daya), dan Jaya Prayitna (sudut tenggara)."

    aang    "Pada tahun 1767, atas permintaan gubernur pantai Utara Jawa, Sri Sultan Hamengku Buwono I memperkuat benteng ini. Pada tahun 1787, 
            benteng ini selesai dibangun dan diberi nama Rustenburgh, kemudian diresmikan sebagai Benteng Vredeburg oleh Gubernur Johannes Sioeberg. 
            Setelah mengalami gempa pada tahun 1867, benteng ini direnovasi dan berganti nama menjadi Benteng Vredeburg, yang artinya \"perdamaian\""

    hide aang

    show mc kaget
    with dissolve
    mc "Wow, betapa menariknya. Terima kasih atas penjelasannya, Aang. Ternyata ada begitu banyak cerita di balik bangunan ini."

    hide mc

    show aang netral
    with dissolve
    aang "Ya, memang begitulah. Untung aku sudah pernah mengunjunginya, jadi aku tahu sejarahnya"

    aang "Lain kali akan ku bawa kamu kesana, aku khawatir waktu kita tidak akan cukup apabila kita kesana sekarang."

    hide aang

    show mc netral
    with dissolve
    mc "Janji ya Aang?"

    hide mc
    
    show aang senyum
    with dissolve
    aang "Hahaha, iya janji Tok."

    show aang netral
    with dissolve
    aang "Kita masih punya waktu banyak, apabila ada bangunan yang menarik bagimu bilang saja Tok. Kita bisa mampir sebentar kok."

    show mc netral
    with dissolve
    mc "Baiklah Aang, ayo kita lanjutkan perjalanan kita"

label jalanan_cuy:
    show bg jalanan   
    with fade

    show mc netral
    mc "Bangunan dan jalan di Jogja sangat berbeda dengan desaku, jadi begini rasanya tinggal di kota besar."

    hide mc

    show aang netral
    with dissolve
    aang "Jogja belum ada-apanya kalau dibandingkan dengan kota besar lainnya seperti Surabaya, Bali, dan Jakarta Tok. Kapan-kapan kamu harus kesana."

    hide aang

    show mc senyum 2
    with dissolve
    aang "Haha, tentu saja Aang, aku juga berencana mengunjungi berbagai kota setelah Jogja"

    hide mc
    
    show mc kaget
    with dissolve
    mc "Wah? Benarkah? Ayo kita segera kesana"

    hide mc

    show aang senyum
    with dissolve
    aang "Senang mendengarnya, jangan lupa kirim foto pemandangan ketika kamu bepergian ya"

    hide aang

    show mc netral
    with dissolve
    mc "Tentu saja Aang, akan aku belikan oleh-oleh juga."

    hide mc

    show aang senyum
    with dissolve
    aang "Hahaha"

    hide aang

    show mc kaget
    with dissolve
    mc "Wah apa itu Aang? Apakah itu masjid? Aku tidak dapat melihatnya secara jelas dari jarak sejauh ini."

    hide mc

    show aang senyum
    with dissolve
    aang "Oh itu. Apakah kau tertarik untuk mengunjunginya Tok?"

    hide aang

    show mc netral
    with dissolve
    mc "Sungguh menarik perhatian, apakah kita bisa kesana sebentar Aang?"

    hide mc

    show aang senyum
    with dissolve
    aang "shapp!!"
    
label masjid_gede_kauman:
    scene bg masjid gede kauman
    with fade

    show aang netral
    with dissolve
    mc "Ini dia Tok, Masjid Gedhe Kauman."

    hide aang

    show mc kaget
    with dissolve
    mc "Wah? Mengagumkan sekali, ini benar masjid kah?"

    hide mc

    show aang senyum
    with dissolve
    aang "Haha, arsitekturnya terlihat unik bukan?"

    aang "Ayo kita masuk, aku tadi melihat beberapa bule juga masuk ke dalam"

label dalam_masjid_gede_kauman:
    scene bg dalam masjid gede kauman
    with fade

    show mc netral
    with dissolve
    mc "Terima kasih sudah membawaku kesini Aang, di desaku masjid-masjid jauh lebih kecil dari sini"

    hide mc

    show aang netral
    with dissolve
    aang "Tidak masalah Tok, aku juga bersyukur bisa melihat masjid semegah ini setelah sekian lama"

    aang "Melihat masjid sebesar ini membuatku penasaran terhadap sejarahnya"

    hide aang

    show pu
    with dissolve
    pu "Maafkan aku tapi tadi aku mendengar masnya penasaran terhadap sejarah masjid ini. Apakah kau ingin mengetahui sejarah tempat ini nak?"

    hide pu

    show aang netral
    with dissolve
    aang "Oh, iya benar pak"

    hide aang

    show mc netral
    with dissolve
    mc "Apakah bapak familiar dengan masjid ini?"

    hide mc

    show pu
    with dissolve
    pu "Biar saya jelaskan, saya ini adalah panitia ramadhan untuk masjid gedhe kauman, jadi saya lumayan kenal sejarahnya."

    pu "Masjid Gedhe Kauman adalah salah satu peninggalan bersejarah yang tak terpisahkan dari Kasultanan Yogyakarta, diresmikan 18 tahun setelah Perjanjian Giyanti pada tahun 1755."

    pu "Terletak di Kampung Kauman, Yogyakarta, masjid ini menjadi lokasi bersejarah dengan gaya arsitektur yang kental, menarik minat wisatawan lokal dan internasional."

    pu "Sistem atap tumpang tiga dan material bangunan yang khas mencerminkan kesempurnaan hidup dalam tiga tahapan kehidupan manusia: Syariat, Makrifat, dan Hakekat."

    pu "Meskipun mengalami perubahan seiring berjalannya waktu, keunikan dan keanggunan Masjid Gedhe Kauman tetap terjaga, seperti pemasangan batu kali putih tanpa semen dan penggunaan kayu jati utuh yang berusia lebih dari 200 tahun."

    hide pu

    show mc netral
    with dissolve
    mc "Aku tidak pernah menyangka sebuah masjid memiliki sejarah yang begitu berarti"

    hide mc

    show aang netral
    with dissolve
    aang "Oh ya pak, tempat ini terlihat besar sekali, sepertinya tidak hanya untuk sholat ya?"

    hide aang

    show pu
    with dissolve
    pu "Benar sekali nak, terdapat banyak ruang di masjid ini."

    pu "Bangunan utama masjid dilengkapi dengan ruang inti, maksura, mimbar, dan berbagai ruangan fungsional lainnya seperti pawestren, yakihun, dan blumbang. 
        Kompleks Masjid Gedhe juga mencakup KUA, kantor Takmir, dan Pagongan, yang menjadi tempat penyimpanan gamelan Sekaten."

    pu "Regol atau gapura yang berbentuk Semar Tinandu adalah pintu gerbang utama kompleks masjid, memperkaya keberadaan serta keunikan tempat ibadah yang sarat akan nilai sejarah 
        dan budaya."

    hide pu

    show aang senyum
    with dissolve
    aang "Tidak hanya untuk ibadah, tetapi juga mengandung nilai sejarah dan budaya"

    aang "senang bisa mempelajari nilai sejarah tempat seperti ini, senang juga bisa mengetahui bahwa masjid ini masih bermanfaat untuk banyak orang."

    hide aang

    show mc netral
    with dissolve
    mc "Bapak tadi bilang bahwa bapak adalah panitia ramadhan bukan? Bagaimana kondisi masjid ini ketika ramadhan pak?"

    hide mc

    show pu
    with dissolve
    pu "Untuk menyambut bulan Ramadhan, Masjid Gedhe juga menyiapkan rangkaian acara dan takjilan buka bersama yang tiap harinya dikunjungi hingga 600 orang jamaah."

    pu "bahkan terdapat hari khusus dengan menu spesial. Setiap hari Kamis kami panitia khusus menyembelih kambing dan menyediakan Gulai Kambing sebagai menu buka puasa."

    hide pu

    show mc netral
    with dissolve
    mc "Masjid Gedhe Kauman ini memang merupakan wisata religi dari nilai sejarah serta kemegahan yang unik dari arsitektur masjid tertua di Jogja ya."

    hide mc

    show pu
    with dissolve
    pu "Haha benar sekali, sekarang saya izin pamit dulu, saya masih ada keperluan kepanitiaan, Assalamualaikum"

    ma "Waalaikumsalam pak, terima kasih informasi sejarah dan budaya masjid ini"

label alun_alun_kidul_sore:
    scene bg alun alun kidul sore
    with fade

    show aang netral
    with dissolve
    aang "Inilah Alun-alun kidul Tok, tempat ini ramai sekali pada malam hari"

    aang "Alun-Alun Kidul selalu menjadi tujuan favorit para wisatawan. Mari kita jelajahi dan nikmati suasana di sini."

    hide aang

    show mc senyum 1
    with dissolve
    mc "Waaah, mengagumkan sekali. Beringin kembar di tengah lapangan berdiri dengan megah"

    #disini image pop up beringin kembar

    show mc senyum 2
    with dissolve
    mc "Ada banyak sekali orang naik mobil sepeda juga, sungguh membuat tempat ini kelap kelip"

    #disini image pop up mobil sepeda kelap kelip

    hide mc

    show aang netral
    with dissolve
    aang "Banyak orang yang menyewa mobil sepeda itu untuk menikmati suasana di sekitar alun-alun"

    show aang senyum
    with dissolve
    aang "kalo kita sewa, kita harus menggowes pedal untuk menjalankan mobil sepeda jadi terasa seperti olahraga malam"

    hide aang

    show mc netral
    with dissolve
    mc "aku tertarik mencobanya tetapi tidak dulu deh"
    
    show mc senyum 1
    with dissolve
    mc "mengayuh pedal terlihat sangat melelahkan pada jam segini, haha"

    show mc netral
    with dissolve
    mc "Oh ya, banyak sekali orang yang mengelilingi kedua pohon beringin itu."

    show mc bingung
    with dissolve
    mc "Beberapa orang juga sedang berjalan sambil menutup matanya, mereka sedang apa ya?"

    hide mc

    show aang netral
    with dissolve
    aang "Oh ituu, salah satu aktivitas yang sangat terkenal di alun-alun ini adalah permainan masangin."

    aang "Memang sudah menjadi tradisi bahwa permainan ini menjadi daya tarik tersendiri dan banyak membuat para wisatawan yang tertarik untuk mencobanya."

    aang "permainan masangin ini cukup sederhana. Kamu hanya perlu menutup mata dengan kain penutup lalu berjalan lurus sekitar 20 meter dari Sasono Hinggil menuju ke bagian tengah kedua pohon beringin."

    show aang senyum
    with dissolve
    aang "Permainan ini terdengar mudah, tapi seperti yang bisa kau lihat, banyak orang yang melenceng dan berputar tidak jelas haha"

    show aang netral
    with dissolve
    aang "Banyak mitos yang beredar bahwa hanya orang yang berhati bersih dan lurus yang bisa melewati kedua pohon tersebut."

    aang "Ada mitos lain yang mengatakan bahwa harapanmu akan terkabulkan apabila kau dapat melewatinya."

    aang "kau terlihat bersih seperti orang yang berhati bersih dan lurus Tok, maukah kamu mencobanya?"

    hide aang

    show mc bingung
    with dissolve
    mc "Eh… Apa? Apakah tidak bahaya apabila aku berjalan sambil menutup mata?"

    hide mc

    show aang senyum
    with dissolve
    aang "Haha tidak apa apa, kau akan ku jaga agar tidak menabrak siapa siapa, tidak perlu khawatir."

    hide aang

    show mc flat
    with dissolve
    mc "Tidak ah, aku tidak percaya dengan mitos seperti itu"

    hide mc

    show aang netral
    with dissolve
    aang "kita tidak perlu mempercayai mitos, cukup mencobanya agar tau saja"

    "suara perut"

    hide aang

    show mc netral
    with dissolve
    mc "{i}uggrgrggrgrgrgrhhrghrghr{/i}"

    mc "Ahaha, tidak dulu Aang, aku sedikit lapar."

    hide mc

    show aang senyum
    with dissolve
    aang "Haha, baiklah, sepertinya kita harus pergi cari makan dulu."

    "time passes"

    hide aang

    show mc netral
    with dissolve
    mc "Sudah jam segini, ayo kita berangkat ke pertunjukan Gamelan."

    hide mc

    show aang senyum
    with dissolve
    aang "Masih jam segini Tok, santai aja dulu"

    hide aang

    show mc netral
    with dissolve
    mc "Aku ingin mengambil kursi depan agar aku bisa melihat bapak tadi."

    hide mc

    show aang netral
    with dissolve
    aang "Oh, benar juga, kita belum tahu nama bapak itu sampai sekarang"

    hide aang

    show mc bingung
    with dissolve
    mc "Benar juga, nanti harus kita tanyakan kepadanya"

    hide mc

    show aang netral
    with dissolve
    aang "Baiklah, ayo berangkat. Final stop for today, Pertunjukan Gamelan skuy!"

label tempat_duduk_pertunjukan_terang:
    scene bg tempat duduk pertunjukan terang
    with fade

    show mc netral
    with dissolve
    mc "Jadi ini tempat pertunjukannya, menarik juga"

    hide mc

    show aang senyum
    with dissolve
    aang "Hehe kursi depan masih kosong,ayo ambil tempat"

    "suara perangkat jatuh"

    "Aang dan Totok kaget mbakjegagikk..."

    show aang kaget
    with dissolve
    aang "ASSSS… taghfirullah aladzim, suara apa itu?"

    hide aang

    show mc kaget
    with dissolve
    mc "Suara itu terdengar dari panggung, sepertinya ada yang jatuh."

    hide mc

    show pb panik
    with dissolve
    pb "Aduuuh, bagaimana iniii, aku akan dipecat aku akan dipecat, ini baru tugas kedua ku dan aku sudah mengacaukannya"

    pb "Kalau aku tidak bisa memperbaikinya, acara ini akan kacau, atau lebih buruk… DIBATALKAN!"

    hide pb

    show aang kaget
    with dissolve
    aang "Apa??? Dibatalkan??? Tok, apakah kau mendengar ini? Ada kemungkinan bahwa pertunjukannya dibatalkan"

    hide aang

    show mc kaget
    with dissolve
    mc "Aku tidak bisa mempercayai ini, padahal aku sudah menantikan penampilan bapak gamelan."

    hide mc

    show aang marah
    with dissolve
    aang "Aku tidak ingin acara ini dibatalkan, mari kita cari tahu alasannya"

label panggung:
    scene bg panggung
    with fade

    show aang marah
    with dissolve
    aang "Permisi mas, saya tadi tidak sengaja mendengar bahwa ada acara ini akan dibatalkan, apakah benar?"

    hide aang

    show pb panik
    with dissolve
    pb "A-A-Apaa??? Gawat, beritanya sudah sampai pada publik, aku akan dipecat aku akan dipecat!!!"

    hide pb

    show mc flat
    with dissolve
    mc "T-tenang saja mas, baru kami saja yang mendengar, ada masalah apa dengan pertunjukannya? Mengapa akan dibatalkan?"

    hide mc

    show pb panik
    with dissolve
    pb " E-e-e….. Jadi begini…"

    pb "Aku adalah seorang intern di organisasi penyelenggara acara ini, aku baru mengikuti acara sebagai panitia sekali, jadi ini kedua kalinya untukku"

    pb "Aku seharusnya hanya menjadi panitia operasional perkap, yang berarti aku hanya perlu menyiapkan dan memindahkan alat"

    pb "Te-te-tetapi koordinator acara tiba-tiba sakit, dan aku ditunjuk menjadi koordinator pengganti"

    pb "Aku tidak meminta untuk menjadi koordinator, aku tidak ingin menjadi koordinator, sekarang semuanya akan kacau karena aku"

    pb "Aku akan dipecat, aku seharusnya tidak mendaftar menjadi panitia, aku bodoh sekali"

    hide pb

    show aang sedih
    with dissolve
    aang "Hey, hey, tenang saja mas… Permasalahannya di mana? Apa yang kacau?"

    hide aang

    show pb panik
    with dissolve
    pb "Aku tidak tahu tempat masing-masing gamelan di panggung, aku harus dapat mengatur masing-masing gamelan di posisinya yang tepat"

    hide pb

    show aang sedih
    with dissolve
    aang "Apakah… kamu bisa berusaha mengingatnya kembali?"

    hide aang

    show pb netral
    with dissolve
    pb "A-aku sedikit ingat, jenis suara apa berasal darimana, bentuk, dan nama dari beberapa gamelan, tapi aku tidak ingat semuanya."

    hide pb

    show aang flat
    with dissolve
    aang "Tok, kita baru saja mempelajari beberapa jenis gamelan tadi siang."

    aang "Bagaimana kalau kita membantu mas mas ini dalam persiapan acara?"

    aang "Apabila kita membantu persiapan, acara tidak jadi dibatalkan, aku juga merasa kasihan kepada mas ini"

    aang "Aku yakin bapak gamelan akan sangat senang apabila kita menggunakan ilmu yang sudah kita dapatkan untuk kebaikan"

    show aang senyum
    with dissolve
    aang "jadi bagaimana Tok? Mau kah kamu membantu perisapan acara?"

    jump bantu_persiapan_gamelan

label bantu_persiapan_gamelan:
        while click <= 4:
                if click == 0:
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show aang flat
                                        with dissolve
                                        aang "Apakah kamu yakin Tok? Kita sudah jauh jauh kesini untuk menyaksikan pertunjukan Gamelan"

                                        hide aang
                                        
                                        show mc flat
                                        with dissolve
                                        mc "(Aang benar, aku kesini untuk menyaksikan pertunjukan gamelan)"
                                        hide mc
                elif click == 1:
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show aang flat
                                        with dissolve
                                        aang "Kakek sudah memberi ilmu gamelan kepada kita, mas mas ini juga sedang sangat kebingungan, sebaiknya kita membantunya"

                                        hide aang

                                        show mc flat
                                        with dissolve
                                        mc "(Semua kebaikkan pasti akan dibalas, aku juga tidak ingin melihat penampilan bapak gamelan)"
                                        hide mc
                elif click == 2:
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show aang flat
                                        with dissolve
                                        aang "Apakah kamu yakin Tok? Aku yakin {color=#ff0000}pengalaman yang kita dapatkan akan berubah apabila kita tidak membantu"

                                        hide aang

                                        show mc flat
                                        with dissolve
                                        mc "Aku {color=#ff0000}sebaiknya membantu persiapan{/color}, pengalaman dan hasilnya pasti akan bermanfaat"
                                        hide mc
                elif click == 3:
                        show aang flat
                        with dissolve
                        aang "Baiklah Tok, lalu sekarang kita mau kemana?"
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show mc flat
                                        with dissolve
                                        mc "Aku {color=#ff0000}sebaiknya membantu persiapan{/color}, pengalaman dan hasilnya pasti akan bermanfaat"
                                "{color=#ff0000}Aku mengantuk, aku ingin istirahat":
                                    hide mc
                                    jump balik_hotel
                elif click == 4:
                    menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        show mc flat
                                        with dissolve
                                        mc "Aku {color=#ff0000}sebaiknya membantu persiapan{/color}, pengalaman dan hasilnya pasti akan bermanfaat"
                                "{color=#ff0000}Aku mengantuk, aku ingin istirahat":
                                        jump balik_hotel  

label bantu_gamelan:
    show aang senyum
    with dissolve
    aang "Hahaha, sudah kuduga kamu akan membantu Tok."

    aang "Jangan khawatir mas, kami akan membantumu, kami lumayan tahu juga tentang gamelan."

    hide aang

    show pb senyum
    with dissolve
    pb "Be-benarkah? Kalian akan membantuku?"

    hide pb

    show mc senyum 2
    with dissolve
    mc "Tentu saja kami akan membantumu mas, kami juga sangat bersemangat ingin menyaksikan pertunjukan gamelan."

    hide mc

    show pb senyum
    with dissolve
    pb "Terima kasih banyak, baiklah, ayo kita mulai."  

    #mini game: set the stage

    if pilihan == 1:
        $ ulang_pertanyaan = 0
        while ulang_pertanyaan <= 3:
            if ulang_pertanyaan == 0:
                pb "Bilahan gamelan ini terbuat dari kayu atau bambu dan memiliki banyak bilah yang terletak di atas sebuah rak yang berbentuk perahu."

                pb "Bilah-bilahnya dirsusun berurutan dari bentuk terpendek, sampai yang paling panjang,"

                menu:
                    pb "gamelan apa ini?"
                    "Gambang":
                        $ ulang_pertanyaan += 1
                    "Slenthem":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Bonang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
            
            elif ulang_pertanyaan == 1:
                pb "Gamelan ini digantung dan sangat besar, dan cara memainkannya dipukul,"

                menu:
                    pb "apa nama dari gamelan ini?"
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Kendhang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Slenthem":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gong":
                        $ ulang_pertanyaan += 1
                    "Bonang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."

            elif ulang_pertanyaan == 2:
                pb "Yang aku ingat hanya lah gamelan ini bernama Bonang,"

                menu:
                    pb "manakah gamelan yang merupakan Bonang?"
                    #opsi dalam bentuk gambar
                    "Bonang":
                        $ ulang_pertanyaan += 1
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gambang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Slenthem":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."

            elif ulang_pertanyaan == 3:
                pb "Gamelan ini mengatur irama musik gamelan."

                pb "Cara memainkan gamelan ini adalah dengan memukul dengan telapak tangan bagian pinggirnya,"

                menu:
                    pb "gamelan apa ini?"
                    "Slenthem":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Bonang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Kendhang":
                        $ ulang_pertanyaan += 1

    elif pilihan == 2:
        $ ulang_pertanyaan = 0
        while ulang_pertanyaan <= 2:
            if ulang_pertanyaan == 0:
                pb "Gamelan ini lebih gemuk dari gamelan lainnya. Gamelan ini diletakan pada kayu tetapi terbuat dari logam."

                pb "Gamelan ini menghasilkan suara yang rendah,"

                menu:
                    pb "gamelan apa ini?"
                    "Bonang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Kenong":
                        $ ulang_pertanyaan += 1
                    "Kendhang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Slenthem":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
            
            elif ulang_pertanyaan == 1:
                pb "Aku hanya tau bahwa gamelan ini bernama Rebab,"

                menu:
                    pb "yang mana gamelan rebab?"
                    "Slenthem":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Rebab":
                        $ ulang_pertanyaan += 1
                    "Kenong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Kendhang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."

            elif ulang_pertanyaan == 2:
                pb "Gamelan ini punya banyak bilahan logam yang ditumpangkan di atas bingkai kayu,"

                menu:
                    pb "apa nama dari gamelan ini?"
                    "Bonang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Saron":
                        $ ulang_pertanyaan += 1
                    "Gambang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Rebab":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."

    elif pilihan == 3:
        $ ulang_pertanyaan = 0
        while ulang_pertanyaan <= 1:
            if ulang_pertanyaan == 0:
                pb "Yang bisa kuingat hanya gamelan ini bernama Slenthem,"

                menu:
                    pb "apakah kau tau gamelan yang mana Slenthem?"
                    "Kendhang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Slenthem":
                        $ ulang_pertanyaan += 1
                    "Saron":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gender":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Bonang":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
            
            elif ulang_pertanyaan == 1:
                pb "Gamelan ini dari bahan logam yang dipukul setiap bilahnya yang terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."

                pb "Aku pernah melihat gamelan ini ditabuh menggunakan tabuh kayu (Bali) atau berlapis kain (Jawa),"

                menu:
                    pb "apa nama dari gamelan ini?"
                    "Gender":
                        $ ulang_pertanyaan += 1
                    "Kenong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Kempul":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Rebab":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."
                    "Gong":
                        hide pb
                        show aang flat
                        with dissolve
                        aang "Sepertinya bukan gamelan itu yang dideskripsikan, coba ingat ingat ajaran bapak gamelan."

    hide aang
    show pb senyum
    with dissolve
    pb "Dengan begini, pertunjukan dapat berjalan dengan lancar!"

    pb "Aku sungguh berterima kasih kepada kalian, tanpa kalian aku sudah kehilangan pekerjaanku"

    pb "Senang sekali dapat melihat panggung yang sempurna"

    hide pb

    show aang flat
    with dissolve
    aang "Hadeuh, melelahkan juga kerjaannya, tetapi aku senang kita bisa membantu"

    hide aang

    show mc flat
    with dissolve
    mc "Tidak masalah, kami senang bisa membantu."

    hide mc

    show pb senyum
    with dissolve
    pb "Aku belajar banyak hal baru hari ini, berkat bantuan kalian semuanya berjalan lancar"

    hide pb

    show aang flat
    with dissolve
    aang "Itu bagus sekali. Tetapi ingatlah bahwa belajar adalah proses yang terus menerus. Jadi jangan ragu untuk terus mencoba hal-hal baru dan terus berkembang."

    hide aang

    show mc senyum 1
    with dissolve
    mc "Haha, aku tidak menyangka kamu bisa memberi pencerahan seperti itu Aang."

    hide mc

    show aang senyum
    with dissolve
    aang "Hehe, sekali-kali gapapa lah Tok."

    hide aang

    show mc flat
    with dissolve
    mc "Semoga sukses untuk pertunjukan gamelan nanti. Jangan ragu untuk meminta bantuan jika kalian membutuhkannya lagi."

    hide mc

    show pb senyum
    with dissolve
    pb "Tentu saja, aku akan terus berlatih dan belajar! Terima kasih sekali lagi atas bantuan dan dorongan kalian. Selamat menikmati pertunjukan"

    hide pb

    show aang flat
    with dissolve
    aang "Ayo kita kembali ke kursi kita Tok, kita saksikan pertunjukan gamelan spesial ini"

label tempat_duduk_terang:
    scene bg tempat duduk pertunjukan terang
    with fade
    show mc flat
    with dissolve
    mc "Membantu pertunjukan tadi membuatku semakin semangat menonton pertunjukan"

    hide mc
    
    show aang netral
    with dissolve
    aang "Betul sekali, melihat hasil dari kerja keras dan jerih payah sendiri terasa jauh lebih memuaskan."

    hide aang

    show mc senyum 2
    with dissolve
    mc "Aang, lihat deh, penonton mulai berdatangan. Senang bisa melihat orang-orang antusias dengan pertunjukan gamelan ini seperti kita."

    hide mc

    show aang netral
    with dissolve
    aang "Iya, Tok. Gamelan memang punya daya tarik tersendiri. Suaranya bisa membuat orang merasa tenang dan damai."

    aang "Lihat Tok, panggung sudah mulai terpenuhi oleh wiyaga"

    show mc bingung
    with dissolve
    aang "Wiyaga? Apa itu Aang?"

    hide mc

    show aang netral
    with dissolve
    aang "Wiyaga itu orang-orang yang memainkan gamelan Tok."

    hide aang

    scene bg tempat duduk gelap
    with fade

    show aang netral
    with dissolve
    aang "Sepertinya pertunjukannya sudah akan dimulai."

    hide aang

    show mc netral
    with dissolve
    mc "Ayo, kita nikmati pertunjukan ini. Semoga malam ini menjadi pengalaman yang tidak terlupakan."
    hide mc

    show aang senyum
    with dissolve
    aang "Setuju, Totok. Gamelan memang jembatan budaya yang indah. Kita beruntung bisa menontonnya."
    hide aang

    #disini bgm pertunjukan dimulai

    show mc senyum 2
    with dissolve
    mc "Lihat, Aang. Ada anak-anak kecil yang juga menonton dengan antusias. Senang rasanya melihat generasi muda tertarik pada gamelan."
    hide mc

    show aang senyum
    with dissolve
    aang "Wah, ternyata banyak juga anak-anak yang tertarik pada gamelan. Penting untuk mengenalkan budaya tradisional pada mereka."
    hide aang

    show mc senyum 1
    with dissolve
    mc "Semoga mereka tumbuh dengan mencintai dan melestarikan gamelan. Mungkin suatu hari nanti, mereka yang akan duduk di sana, memainkan alat-alat ini dengan penuh semangat."

    mc "Mendengar suara iringan gamelan ini sangat membuatku semangat."
    hide mc

    show aang netral
    with dissolve
    aang "Tok, kamu tahu nggak, setiap nada dalam gamelan punya makna tersendiri? Misalnya, nada pelog dan slendro."
    hide aang

    show mc netral
    with dissolve
    mc "Aku sempat mendengar kata-kata itu ketika bapak menjelaskan gamelan tadi siang. Apa maknanya Aang?"
    hide mc

    show aang netral
    with dissolve
    aang "Slendro memiliki 5 nada per oktaf, biasanya digunakan dalam pertunjukan wayang."

    aang "Perbedaan intervalnya kecil jadi lebih terkesan ceria dan fleksibel, atau  lincah, gembira, dan bersemangat."

    aang "Sedangkan pelog memiliki 7 nada oktaf dan biasanya digunakan sebagai musik iringan tarian"

    aang "Perbedaan interval ketukannya besar, sehingga cenderung memberi kesan yang diberikan adalah lebih serius dan sedih, atau rasa ketenangan dan penuh hormat"

    aang "Kombinasi keduanya laras slendro dan pelog menciptakan suasana yang sangat kaya dan beragam dalam setiap pertunjukan."
    hide aang

    show mc senyum 2
    with dissolve
    mc "Penampilan para wiyaga benar-benar memukau. Setiap alat gamelan dimainkan dengan sempurna."

    mc "Lihat itu, pemain bonang sangat terampil. Aku bisa merasakan energi dan emosi dari setiap pukulan"
    hide mc

    show aang netral
    with dissolve
    aang "Iya Tok, aku tidak sabar mendengarkan mendengarkan keseluruhan pertunjukan."
    hide aang

    show aang senyum
    with dissolve
    aang "Coba lihat pemain bonang itu Totok. Itu bapak yang menjelaskan gamelan kepada kita tadi siang"
    hide aang

    show mc senyum 2
    with dissolve
    mc "Kau benar, Aang. Pantas saja performanya bagus."
    
    mc "Bapak itu memang orang yang luar biasa. Dia banyak mengajarkan kita tentang beragam gamelan, dan sekarang beliau tampil dengan handal."
    hide mc

    show aang netral
    with dissolve
    aang "Benar, bapak itu sudah memiliki bertahun-tahun pengalaman bermain gamelan. Oh, dan pemain gong juga tidak kalah hebat."

    aang "Aku suka sekali bagian ini, ketika suara gong besar mulai dimainkan. Rasanya sangat menggetarkan. Bagian gong itu penting untuk menjaga ritme."
    hide aang

    show mc netral
    with dissolve
    mc "Aku suka dengan pemain kendang. Pemain kendang itu seperti jantung dari gamelan, menjaga ritme dan energi."
    hide mc

    show aang netral
    with dissolve
    aang "Mereka memang luar biasa. Setiap pemain membawa sentuhan pribadi mereka, tapi tetap dalam harmoni yang sempurna."

    aang "Orkestrasi gamelan ini begitu harmonis. Setiap instrumen saling melengkapi dan menciptakan alunan yang sangat indah."

    aang "Ini yang membuat gamelan begitu istimewa. Tidak hanya soal suara, tetapi juga kebersamaan dan kerja sama tim yang luar biasa."
    hide aang

    show mc netral
    with dissolve
    mc "Aku jadi kagum dengan bagaimana mereka bisa menjaga tempo. Pasti butuh latihan yang luar biasa untuk mencapai keselarasan seperti ini."
    hide mc

    show aang netral
    with dissolve
    aang "Gamelan memang tentang kerja sama dan saling mendengarkan. Kalau mereka kompak, hasilnya pasti bagus."
    hide aang

    show aang senyum
    with dissolve
    aang "Ayo kita nikmati pertunjukan ini sampai akhir. Setiap detiknya sangat berharga."
    hide aang

    show mc senyum 2
    with dissolve
    mc "Pasti, Aang. Ini adalah momen yang tak terlupakan. Mari kita resapi setiap alunan musik yang mereka mainkan."

    mc "Malam ini kita menyaksikan pertunjukan yang tidak terlupakan. Untung bapak gamelan memberikan kita tiket pertunjukan"
    hide mc

    #disini bgm pertunjukan selesai

    scene bg tempat duduk pertunjukan terang
    with fade

    show aang senyum
    with dissolve
    aang "Wah, pertunjukan tadi sungguh luar biasa. Mereka benar-benar menghidupkan tradisi gamelan dengan indah."

    show mc senyum 2
    with dissolve
    mc "Iya, betul sekali! Aku juga merasa terinspirasi oleh penampilan mereka. Semoga suatu hari nanti kami juga bisa sehebat mereka."

    mc "Lihat itu, bapak gamelan sedang turun panggung, mari kita sambut"

label panggung2:
    scene bg panggung
    with fade
    show mc senyum 2
    with dissolve
    mc "Bapak, pertunjukan tadi sungguh luar biasa. Mereka benar-benar memainkan gamelan dengan begitu indah."

    hide mc

    show aang senyum
    with dissolve
    aang "Iya, benar sekali. Kami sangat menikmati pertunjukan tadi. Cara bapak memainkan gamelan tadi sangat indah!"

    hide aang

    show kg senyum
    with dissolve
    kg "Terima kasih, anak muda. Pak tua ini senang kalian menikmati pertunjukan kami. Kakek juga senang bisa berbagi seni tradisional dengan kalian."

    kg "Aku dengar kalian juga membantu persiapan pertunjukan ini tadi."

    hide kg

    show aang senyum
    with dissolve
    aang "benar pak, itu semua berkat ilmu gamelan yang sudah bapak berikan kepada kami tadi siang"

    hide aang

    show mc senyum 2
    with dissolve
    mc "Apakah kami boleh foto bersama bapak? Kami ingin mengenang momen ini."

    hide mc

    show kg senyum
    with dissolve
    kg "Haha, dengan senang hati!"

    hide kg

    #disini Image pop up: Foto Totok, Aang, dan Bapak Gamelan dengan background panggung penuh gamelan

    show kg senyum
    with dissolve
    kg "Jangan lupa kirimkan foto itu kepadaku juga ya nak. Senang bisa bertemu dengan pemuda antusias dan baik hati seperti kalian"

    hide kg

    show mc senyum 2
    with dissolve
    mc "Tentu saja pak, boleh minta nomor telepon dan nama bapak siapa ya kalau boleh tau?"

    hide mc

    show kg netral
    with dissolve
    kg "Oh ya kita belum saling mengenal, namaku ada Sutrisno Haji Tifa"

    hide kg

    show aang netral
    with dissolve
    aang "Salam kenal pak, saya Aang Idhang Saputra."

    aang "Oh aku juga belum tahu nama lengkapmu Tok, apa nama lengkapmu?"

    hide aang

    show mc senyum 1
    with dissolve
    mc "Haha, benar juga. Nama lengkapku Totok Hestamma."

    hide mc

    show kg netral
    with dissolve
    su "..."

    su "Hestamma… Totok Hestamma dan Aang Idhang Saputra ya."

    show kg senyum
    su "Nama-nama yang bagus sekali, semoga aku bisa bertemu lagi dengan kalian di masa depan."

    show mc senyum 2
    with dissolve
    mc "Terima kasih pak Sutrisno, kami tidak akan melupakan pengalaman ini."

    hide mc

    show kg senyum
    with dissolve
    su "Sampai jumpa anak muda. Semoga Allah memberkati jalan kalian."

    #disini totok dan aang pergi

    su "Hestamma… Rasanya aku pernah mendengar nama itu"

label tempat_duduk_pertunjukan_terang2:
    scene bg tempat duduk pertunjukan terang
    with fade
    show aang netral
    with dissolve
    aang "ngomong-ngomong sudah jam berapa ini? Ternyata sudah cukup larut. Mungkin sudah waktunya kamu kembali ke hotel untuk istirahat Tok"

    hide aang

    show mc netral
    with dissolve
    mc "Benar juga. Kita sudah melalui hari yang panjang, dan esok akan menjadi hari yang penuh kisah. Ayo kita pulang."

label Depan_hotel_malam:
    scene bg depan hotel malam
    with fade
    show aang senyum
    with dissolve
    aang "Aku senang sekali bisa menyaksikan pertunjukan gamelan tadi."

    aang "Untung saja kita membantu persiapannya!"

    aang "Hari ini penuh berbagai petualangan, bukan?"

    aang "Mulai dari awal pertemuan kita"

    show aang sedih
    with dissolve
    aang "Yang diawali HPku yang jatuh…"

    aang "Melihat pesona Tugu Jogja, pergi ke Keraton bersama untuk mempelajari sejarah Yogyakarta. Belajar gamelan dari pak Sutrisno."

    aang "Pergi melihat Benteng Vredeburg, Sholat di Masjid Gedhe Kauman, lalu bersenang-senang di alun-alun."

    aang "Sampai persiapan hingga menyaksikan pertunjukan tadi, semuanya begitu menyenangkan."

    aang "Terima kasih telah menjadi bagian dari semuanya Tok. Semoga besok kita dapat berpetualang dengan semangat yang sama."

    show aang senyum
    with dissolve
    aang "Masih ada banyak tempat yang ingin ku tunjukan padamu!"

    aang "Selamat malam Tok, sampai jumpa besok!"
return

label balik_hotel:
        show aang flat
        with dissolve
        aang "B-Baiklah Tok, apabila itu yang kau inginkan."

        aang "Baik mas, terima kasih informasinya. Karena pertunjukannya dibatalkan kami akan pulang sekarang."

        aang "Tetap sabar dan tabah, semoga mas dimudahkan Allah dalam menghadapi musibah ini."

        hide aang

        show pb panik
        with dissolve
        pb "Ba-baiklah, mohon maaf sebesar besarnya… aduuuh bagaimana ini….. tamatlah aku!!!!"

        hide pb

        #nanti disini show bg depan hotel tapi malam hari

        scene bg depan hotel malam
        with fade
        show aang flat
        aang "Padahal kau terlihat begitu bersemangat ketika mendapat tiket dari bapak tadi siang"

        aang "Aku khawatir dengan apa yang terjadi pada pertunjukannya, apakah mas mas panitia tadi berhasil menyelesaikan masalahnya?"

        aang " ngomong-ngomong sudah jam berapa ini? Ternyata sudah cukup larut. Mungkin memang benar keputusanmu untuk kembali ke hotel untuk beristirahat."

        aang "Masih ada banyak tempat yang ingin ku tunjukan padamu besok"

        show aang senyum
        aang "Selamat malam Tok, sampai jumpa besok!"
        #CHAPTER 1 END DI SINI JIKA MC MEMILIH BALIK KE HOTEL
return