# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Sebagai contoh
define z = Character("Zee", color="#c8ffc8")
define m = Character("Me", color="#FFBB70")

# Define Char buat project
define mc       = Character("Totok", color="#c8ffc8")
define aangs    = Character("???", color="#ffffff")
define aang     = Character("Aang", color="#FFBB70")
define penjual  = Character("Bapak Penjual", color="#7ABA78")
define kg       = Character("Kakek Gamelan", color="#7ABA78")
define pu       = Character("Pak Ustad", color="#7ABA78")
define ma       = Character("Totok & Aang", color="#7ABA78")
define pb       = Character("Panitia beginner", color="#7ABA78")
define su       = Character("Sutrisno", color="#7ABA78")

# Define Variables
$ pilihan = 0
$ click = 0
$ jawabbenar = 0

# Define methods
python:
    import random
    def jawaban_benar():
        randombenar = random.randint(1, 2)
        if randombenar == 1:
            renpy.say("kg", "Bagus sekali")
        elif randombenar == 2:
            renpy.say("kg", "Yap, betul sekali")

    def jawaban_salah():
        randomsalah = random.randint(1, 3)
        if randomsalah == 1:
            renpy.say("kg", "Tebakan yang bagus nak, tetapi")
        elif randomsalah == 2:
            renpy.say("kg", "Haha, bukan gamelan yang itu nak,")
        elif randomsalah == 3:
            renpy.say("kg", "Tidak apa apa, kesalahan adalah bagian dari perjalanan,")

#sound & music effect
define audio.bell = "sfx_bell.mp3"

# The game starts here.

label start:
    scene bg stasiun
    with fade

    "disuatu hari pada saat jam istirahat sekolah..."

    play audio bell volume 0.5
    stop audio fadeout 1.0

    show mc happy #gambar mc sedang senyum
    with dissolve

    mc "Wow, Jogja! Akhirnya aku sampai juga"

    mc "Jadi ini kota asal kakek, kakek pernah bercerita tentang pengalamannya di kota ini. 
        Sekarang giliran ku untuk merasakannya sendiri. 
        Baiklah, pertama-tama aku harus mencari tempat untuk tinggal dan kemudian mulai menjelajahi kota ini."

    #nanti kasih pop up image bg stasiun tugu ada silhouette

    show mc huh #gambar mc ekspresi flat
    with dissolve
    mc "Waduh, ramai sekali stasiun ini, ditambah kata kakek jumlah kendaraan di Jogja yang lumayan padat. 
        Mungkin ada informasi turis di sekitar sini."
    
    aangs "Aduh!!!"

    mc "Suara apa itu? Kedengarannya seperti orang yang jatuh, dalam keadaan seramai ini aku harus berhati-hati, 
        bisa saja ada barang bawaanku yang jatuh, atau lebih buruk…"

    show mc mbakjegagik #gambar mc kaget
    mc "DICULIK!!"
    
    show mc lega #gambar mc lega
    mc "Astaghfirullah Totok, nauzubillah min zalik semoga aku selalu dijaga Allah"

    #nanti kasih gambar pop-up disini

    show mc mbakjegagik #gambar mc kaget
    mc "Ya ampun, baru saja aku pikirkan, langsung kejadian, kira kira ini ponsel siapa ya? 
        APA? PONSEL INI SAMSUNG GALAXY Z FLIP? 
        Harganya pasti sangat mahal, sayang sekali apabila ada kehilangan."
    
    aangs "Aduh… HP ku dimanaaa, sial sekali aku hari ini"

    show mc
    mc "Ah, sepertinya ponsel ini milik orang itu, sebaiknya ku hampiri"

    #totok jalan off-screen

    show aangs mbakjegagik #gambar aang kaget
    aangs "Permisi mas, apakah anda melihat hp jatuh? Permisi mbak…."

    aangs "permisi mas, apakah mas melihat HP jatuh?"
    
    menu:
        "mengembalikkan ponsel":
            jump bagian2
        "menyimpan ponsel untuk dirimu":
            mc "Apa yang aku lakukan? Aku tidak boleh berbohong! Semua perbuatan pasti akan dibalas baik maupun buruk"
            mc "Aku sebaiknya mengembalikan ponselnya ke orang malang ini"
            jump bagian2
    return

label bagian2:
    show mc bingung
    with dissolve
    mc "Apakah ini ponselmu?"

    show aangs senyum
    with dissolve
    aangs "Iya! Ini ponselku, terima kasih banyak mas, sebaiknya kita menghindari keramaian dulu"

label stasiun_tugu:
    scene bg stasiun #ilangin silhouette
    with fade

    show aangs senyum
    with dissolve
    aangs "Terima kasih, atas bantuannya mas, Perkenalkan nama aku Aang."

    show aang senyum #udah ganti karakter aang tanpa shadow atau misterius
    with dissolve
    aang "Aku baru saja kembali ke Jogja dari liburanku, entah apa yang akan ku lakukan tanpa HP ku, kau lah penyelamatku. Nama mas siapa ya?"

    show mc senyum
    with dissolve
    mc "Perkenalkan namaku Totok, salam kenal Aang. Jadi apakah kamu penduduk Jogja Aang?"

    show aang senyum
    with dissolve
    aang "Jadi namamu Totok? Baiklah Salam kenal Totok."

    aang "Iya aku asli Jogja nih! Bagaimana denganmu Tok? Kau tidak terlihat seperti orang sini"

    show mc muka b aja
    with dissolve
    mc "Oh, iya mas, saya baru saja sampai di Jogja, saya dari desa kecil bernama X. Saya datang ke Jogja untuk melihat pemandangan dan mempelajari kulinernya."

    show aang senyum
    with dissolve
    aang "Haha, santai aja kali, panggil saja aku Aang"

    show aang muka b aja
    with dissolve
    aang    "Jadi kamu turis ya? Baiklah baiklah, sebagai ucapan terima kasihku, aku akan menjadi tour guide mu selama perjalananmu di Jogja! 
            Aku akan membawamu ke beberapa tempat monumental yang tak boleh dilewatkan"
    
    show mc senyum
    with dissolve
    mc "Be-benarkah mas? Apakah kau rela menjadi pemandu wisata untukku?"

    show aang muka b aja
    with dissolve
    aang    "Sudah ku bilang panggil saja aku Aang, tentu saja! Aku sendiri juga udah lama gak keliling Jogja, 
            ini akan menjadi perjalanan seru untuk kita berdua, bepergian lebih asik apabila bersama teman bukan?"

    show mc senyum
    with dissolve
    mc "Terima kasih banyak mas, maksudku Aang. Semoga beberapa hari kedepan perjalanan di Jogja ini akan menjadi pengalaman tak terlupakan"

    show aang muka b aja
    with dissolve
    aang "Akhhh kece Tok, jadi mau kemana kamu sekarang?"

    show mc bingung
    with dissolve
    mc "aku sendiri belum tau tempat yang ingin ku kunjungi, apakah kamu ada saran tempat Aang?"

    show aang senyum
    with dissolve
    aang "Akkhhhh aku menyarankan Tugu Jogja, Keraton, Alun-Alun, Malioboro, Candi Borobudur, Monjali…."

    aang "Oh ya, tadi kau bilang ingin mempelajari kuliner Jogja?"

    aang "aku juga tau tempat Gudeg yang enak banget, harganya juga terjangkau, kalau mau berguru, aku saranin dari dia"

    show mc muka b aja
    with dissolve
    mc "Banyak juga tempat kunjungan di Jogja, tetapi sepertinya aku akan mengunjungi beberapa saja, tempat yang benar benar berbau Jogja serta kulinernya"

    show aang senyum
    with dissolve
    aang "Haha siap boss, mau langsung gas ke Tugu?"

    show mc senyum
    with dissolve
    mc " Haha, aku suka semangatmu Aang, tapi sebaiknya aku mencari tempat penginapan dulu untuk menaruh barang bawaanku."

    show aang muka b aja
    with dissolve
    aang "Baiklah, mari ikut denganku, akan ku boncengi kamu."

label luar_stasiun_tugu:
    scene bg stasiun tugu luar
    #kasih sound effect kendaraan bermotor

    show aang muka b aja
    with dissolve
    aang "Ini motorku, naiklah Tok."

    show mc mbakjegagik
    with dissolve
    mc "Wah, aku tidak pernah melihat motor dan mobil sebanyak ini dalam satu tempat. Beragam sekali kendaraan bermotor yang digunakan orang orang"

    show mc muka b aja
    with dissolve
    mc "Plat mobil itu berawalan B, mobil yang itu berawalan D,dan Motor yang itu berawalan BD, aku hanya pernah melihat motor berplat AB."

    #gambar pop up Berbagai plat di kendaraan berbeda beserta eksposisi Aang yang menjelaskan
    show aang muka b aja
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

    #Gambar pop up: Gambar end
    show mc muka b aja
    with dissolve
    mc "Ohhhh begitu Aang, kamu tau banyak juga ya, tidak sia-sia aku bertemu kamu"

    show aang senyum
    with dissolve
    aang "Haha, bersyukurlah kamu menemukan hpku"

    aang "Ayo berangkat menuju hotel"

label depan_hotel:
    scene bg depan hotel
    with fade

    show mc bingung
    with dissolve
    mc "Berdasarkan hasil google search, rekomendasi orang orang adalah Malioboro, Kraton, dan Tugu."

    show aang senyum
    with dissolve
    aang    "Hehe, biarkan aku memasak sebagai tour guide mu, saranku adalah kita hari ini ke tugu untuk melihat monumen khas Jogja, 
            lalu ke Keraton untuk melihat sejarah dan adat Jogjakarta"
    
    aang    "setelah itu kita akan ke Alun-Alun Selatan untuk melihat monumen seperti Masjid Gedhe Kauman dan Benteng Vredeburg"

    aang    "besoknya kita akan mengunjungi rumah makan spesialis Gudeg agar kamu dapat mempelajari kuliner kami"

    aang    "Lalu beberapa hari setelah itu kita akan ke Pusat Jogja yaitu Malioboro untuk membeli souvenir."

    show mc senyum
    with dissolve
    mc "Waaaah! Kau sudah familiar sekali dengan Jogja. Aku tidak sabar keliling Jogja bersamamu Aang"

    show aang senyum
    with dissolve
    aang "hehe, kan aku emang orang asli sini"

    aang "Ayo kita mulai perjalanan kita!"

label tugu_jogja:
    scene bg tugu yogja
    with fade

    show mc senyum
    with dissolve
    mc "Wow, Tugu Jogja benar-benar mengesankan ya!"

    #disini munculin image pop up tugu jogja

    show aang muka b aja
    with dissolve
    aang "Woiyadong, sejarah Tugu Jogja ini…"

    aang "Sejarahnya ini…."

    show mc muka b aja
    with dissolve
    mc "apa Aang sejarahnya?"

    show aang senyum
    with dissolve
    aang "Jujur aku sendiri sedikit lupa hehe, biar aku google sebentar"

    show mc senyum
    with dissolve
    mc "Hahaha, bisa saja kamu Aang."

    show aang muka b aja
    with dissolve
    aang "oh ini dia sudah ketemu"

    aang    "Tugu Jogja, dibangun pada 1755 oleh Sri Sultan Hamengku Buwono I, memiliki nilai simbolis sebagai titik magis yang menghubungkan Laut Selatan, 
            Keraton Yogyakarta, dan Gunung Merapi, mencerminkan semangat persatuan rakyat dan penguasa dalam melawan penjajah."

    aang    "Dikenal sebagai Tugu Golong-Gilig, tugu awalnya berbentuk silinder dengan puncak bulat, mencapai tinggi 25 meter. 
            Namun, setelah gempa besar pada 10 Juni 1867, tugu mengalami perubahan signifikan dan dikenal sebagai De White Paal, 
            dengan bentuk persegi dan tingginya yang berkurang sebanyak 10 meter menjadi 15 meter."

    aang    "Renovasi oleh pemerintah Belanda bertujuan mengikis persatuan, namun perjuangan rakyat dan raja membuktikan sebaliknya. 
            Tugu memiliki empat bentuk fisik, dengan bagian atas berbentuk kerucut ulir."

    show mc mbakjegagik
    with dissolve
    mc "Wah, mengagumkan sekali, bangunan ini masih tegak setelah bertahun-tahun. Dan bentuknya yang unik, 
        seperti menara yang menjulang tinggi, benar-benar mencuri perhatian."

    show aang muka b aja
    with dissolve
    aang    "Di malam hari, Tugu Jogja juga menjadi salah satu tempat favorit warga Jogja untuk 
            berkumpul dan menikmati keindahan lampu-lampu yang menghiasi sekitarnya."
    
    show mc muka b aja
    with dissolve
    mc "Terima kasih telah membawaku ke sini, Aang. Sangat mengesankan!"

    show aang muka b aja
    with dissolve
    aang "Next stop, Keraton Jogja skuy"

label keraton_yogya:
    scene bg keraton yogya
    with fade

    show aang muka b aja
    with dissolve
    mc "Sudah sampai Tok, inilah Keraton Yogyakarta"

    show mc kagum
    with dissolve
    mc "Waaaaah!! Jadi ini yang mereka sebut kerajaan Keraton."

    #munculin pop up gambar keraton yogya

    show aang muka b aja
    with dissolve
    aang "Betul Tok, sekarang Keraton ini dibuka untuk umum, terdapat museum untuk melihat berbagai macam koleksi barang dan peninggalan"

    show penjual
    with dissolve
    penjual "Betul itu mas! Ada banyak sekali hal menarik dalam Keraton"

    show aang mbakjegagik
    with dissolve
    aang "Astaghfirullah kaget!"

    show mc muka b aja
    with dissolve
    mc "Wah benar begitu kah pak?"

    show penjual senyum
    with dissolve
    penjual "Woooooh ya bener lah, kalo mau tau toh mas, saya ceritakan sedikit nih"

    show mc muka b aja
    with dissolve
    mc "Oh, boleh pak, saya sendiri juga penasaran"

    show bapak penjual senyum
    with dissolve
    penjual "Siap mas, bapak saya dulu jadi tour guide disini jadi saya juga tau banyak."

    #disini munculin image pop up (kek presentasi): Sejarah Keraton Yogyakarta

    show penjual
    with dissolve
    penjual "Kesultanan Yogyakarta, bersama dengan Kesultanan Surakarta, adalah dua wilayah yang merupakan pecahan dari Kesultanan Mataram pada abad ke-18. 
            Pemecahan ini terjadi setelah terjadinya Perang Suksesi Jawa antara para pewaris tahta Kesultanan Mataram."

    penjual "Perjanjian Giyanti yang ditandatangani pada tanggal 13 Februari 1755  ini menyatakan bahwa Kerajaan Mataram dibagi menjadi dua yaitu 
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

    show aang muka b aja
    with dissolve
    aang "Wah bapak ini emang agak lain… Seluruh sejarahnya dijelaskan, bagaimana menurutmu Aang?"

    show mc senyum
    with dissolve
    mc "Wah, bapak wawasannya banyak sekali, aku semakin tertarik memasuki Keraton"

    show penjual senyum
    with dissolve
    penjual "Hahaha, senang sekali aku melihat orang sepertimu mas, boleh tuh ke Keraton, beli tiketnya disana mas."

    show aang muka b aja
    with dissolve
    aang "Bapak ini tau banyak sekali, sebagian besar informasi sudah kami dapatkan"

    show penjual
    with dissolve
    penjual "Tetap saja mas, kalau mau pengalaman spesial dan informasi lebih lengkap boleh banget masuk ke Keratonnya"

    penjual "Seperti yang mas sebutkan tadi, Keraton ini memang ada museumnya"

    penjual "Beberapa hal yang bisa dilihat adalah sejumlah koleksi peninggalan Sri Sultan HB IX, seperti foto-foto, piagam, medali, tanda jasa, 
            surat keputusan presiden, baju-baju bersejarah beliau, koleksi mobil-mobilan beliau sewaktu kecil , peralatan memasak, kamera 
            yang sering dipergunakan beliau, dan berbagai benda lainnya."

    penjual "Lalu juga ada museum Batik yang menyimpan berbagai macam koleksi kain batik, patung, lukisan, topeng batik,peralatan membatik,serta sepeda tua 
            sebagai pengangkut batik serta museum Kristal menyimpan berbagai koleksi kristal milik Keraton mas"

    penjual "Wajib banget dicek itu, udah jauh-jauh ke Keraton masak iya gak mau masuk"

    show mc senyum
    with dissolve
    mc "Ayo Aang kita masuk, aku tidak sabar melihat semua koleksi Keraton"

    show aang muka b aja
    with dissolve
    aang "Baik Tok ayo, terima kasih ya pak"

    #disini Char Totok dan Aang otw jalan off screen

    show penjual kaget
    with dissolve
    penjual "Sebentar mas!!! hampir lupa…"

    #disini Char Totok dan Aang berhenti jalan terus nengok ke arah penjual

    show aang muka b aja
    with dissolve
    aang "Ada apa pak?"

    show penjual senyum
    with dissolve
    penjual "Sebelum masuk Keraton, beli minum dulu biar gak haus, ayo larisin dagangan saya"

    show aang muka b aja
    with dissolve
    aang "Yaelah pak…."

    show mc senyum
    with dissolve
    mc "Haha baiklah pak, aku juga kehausan dari tadi"

    show aang muka b aja
    with dissolve
    aang "Baiklah Totok, akan ku traktir kamu, mau minum apa kamu?"
    
    show mc kebingungan
    menu:
        mc "Aku mau minum apa?"
        
        "Air Dingin":
            show penjual senyum
            penjual "Terima kasih banyak mas, selamat bersenang-senang di Keraton nggih."
            jump joglo_keraton
        "Soft Drink":
            show penjual senyum
            penjual "Terima kasih banyak mas, selamat bersenang-senang di Keraton nggih."
            jump joglo_keraton        
        "Jamu{b}(?){/b}":
            show mc kebingungan
            mc "Jamu? Ini apa ya pak? Kok warnanya ada yang kuning dan coklat begini?"

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
            
            show mc senyum
            mc "Wahhhh, boleh deh pak saya coba satu, Aang, kalo boleh Jamu 1 ya"

            show aang flat
            aang "Korban marketing dan iklan kamu ini Tok... Bapak ini emang jiwa pedagangnya mahir."

            show aang senyum
            aang "Baiklah kalau begitu, Jamu nya 2 ya pak, saya sendiri juga mau nyoba."

            show penjual senyum
            penjual "Siap mas e. Saya bungkus plastik nih khusus buat mas e."

            penjual "Terima kasih banyak mas, selamat bersenang-senang di Keraton nggih."
            
            jump joglo_keraton
return
        
label joglo_keraton:
    scene bg joglo keraton yogya
    with fade

    show mc senyum
    with dissolve
    mc "Luar biasa sekali. Bangunan-bangunan dan koleksi barang di sini memiliki sejarah yang begitu kaya"

    show aang muka b aja
    with dissolve
    aang "iya tuh, Kraton Yogyakarta merupakan pusat kebudayaan dan kekuasaan di masa lalu. Banyak cerita menarik yang tersembunyi di balik temboknya."

    show mc muka b aja
    with dissolve
    mc "Benar-benar menarik. Senang bisa melihat dan mempelajari sejarah dan budaya."

    show aang muka b aja
    with dissolve
    aang "Aku tinggal ke toilet dulu ya Tok, jangan pergi jauh-jauh."

    show mc muka b aja
    with dissolve
    mc "Baiklah, aku akan menunggu mu."

    #disini Char Aang lari off screen

    show mc muka b aja
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

    show kg
    with dissolve
    kg "Hai anak muda, apakah kamu tertarik dengan gamelan?"

    show mc bingung
    with dissolve
    mc "Gamelan? Apa itu pak? Apakah semacam tarian?"

    show kg
    with dissolve
    kg "Hahaha, instrumen yang di depanmu ini disebut Gamelan, jenisnya memang bervariasi sekali"

    show mc senyum
    with dissolve
    mc "Wah, jadi ini alat musik dari Yogyakarta…"

    show kg
    with dissolve
    kg "Benar sekali, sebenarnya gamelan ini berasal dari Jawa dan Bali, Gamelan ini sering digunakan untuk musik karawitan. 
        Oh kau mungkin tidak tau arti karawitan."
    
    kg "Karawitan adalah seni gamelan dan seni suara yang bertangga nada slendro dan pelog. Karawitan berasal dari bahasa Jawa yaitu kata \"rawit\" yang berarti
        halus dan lembut Jadi karawitan ini berarti kelembutan perasaan yang terkandung dalam seni gamelan."

    #disini Char Aang jalan on screen

    show aang
    with dissolve
    aang "Hai Totok, aku kembali, sedang apa kamu?"

    aang "Oh, apakah gamelan gamelan ini menarik perhatianmu?"

    show mc
    with dissolve
    mc "Iya Aang, bapak ini baru saja menjelaskan kepadaku apa itu Gamelan."

    show aang senyum
    with dissolve
    aang "Hahaha, sugeng enjing pak, temanku dari luar Jogja nih. Tolong jelasin semua tentang gamelan"

    show kg senyum
    with dissolve
    kg "Ahahaha, dengan senang hati anak muda."

    kg "Apakah kau ingin dijelaskan secara jelas?"

    menu:
        "{color=#ff0000}Pilihanmu dapat berpengaruh dalam pengalamanmu*"

        "Penjelasan Singkat, aku hanya ingin tahu sedikit":
                $ pilihan = 1
                show kg senyum
                kg "Baik, akan ku mulai penjelasannya, perhatikan ya."
                jump gamelan1
                jump after_gamelan
        "Penjelasan sedang, ilmu ini pasti akan berguna bagiku":
                $ pilihan = 2
                show kg senyum
                kg "Baik, akan ku mulai penjelasannya, perhatikan ya."
                jump gamelan1
                jump gamelan2
                jump after_gamelan
        "Penjelasan Lengkap, beri tahu aku semua gamelan": 
                $ pilihan = 3
                show kg senyum
                kg "Baik, akan ku mulai penjelasannya, perhatikan ya." 
                jump gamelan1
                jump gamelan2
                jump gamelan3
                jump after_gamelan

return

label gamelan1:
    #image pop up: Bonang

        kg "Bonang adalah instrumen gamelan berbentuk ceret atau pot yang diletakan di atas string (tali) dalam bingkai kayu (rancak)."

        kg "Bonang termasuk dalam pencon yang merupakan alat musik dari logam dan berbentuk cekungan di bawahnya dengan poros cembung untuk dipukul"

        aang "Bentuknya mirip mangkuk kek"

        kg "Masing-masing pot kemudian memiliki poros cembung (pencon) di bagian atas sebagai pusat untuk dipukul."

        kg "Bonang dalam set gamelan memiliki beberapa jenis, yaknii bonang penerus, barung, dan panembung."

        kg "Cara bermain boning adalah memukul bagian cekungan atau penutupnya dengan tongkat pemukul khusus."

        #image pop up: Saron

        kg "Saron atau biasa dikenal juga dengan ricik adalah salah satu instrumen gamelan yang masuk dalam golongan balungan atau alat musik jenis bilahan (wilahan) dari logam."

        kg "Saron memiliki 6 atau 7 (1 oktaf) bilahan logam yang ditumpangkan di atas bingkai kayu yang berfungsi sebagai resonator."

        kg "Cara memainkan alat musik saron adalah memukul bilahan logam menggunakan tabuhan tangan kanan dan menahan bilahan yang dipukul sebelumnya menggunakan tangan kiri agar menghilangkan suara dengungan yang tersisa. Cara ini biasa disebut dengan teknik memahat atau memencet."

        #image pop up: Gong

        kg "Hampir serupa dengan bonang dan kenong, gong juga memiliki bentuk cembung di bagian atas dengan ukuran yang lebih besar dan posisinya digantung, tidak diletakan pada lapisan tertentu."

        aang "Suara yang dihasilkan sama persis seperti namanya, {i}Gongggggg{/i}"

        kg "Menyerupai bentuk piringan besar, gong terbuat dari leburan logam seperti perunggu dan tembaga untuk menghasilkan suara yang khas. Cara memainkan alat musik ini dipukul bagian kecembungannya menggunakan tongkat khusus."

        #image pop up: Kendhang

        kg "Kendhang atau gendang adalah salah satu instrumen gamelan Jawa yang dapat mengatur irama musik gamelan."
        
        aang "{i}Tak dung, dung tak, gendhes{/i}"

        kg "Cara memainkan alat musik gendang adalah memukul dengan telapak tangan bagian pinggir kendhang yang terbuat dari kulit hewan."

        kg "Kendhang memiliki berbagai macam jenis dan ukuran, yakni ketipung gamelan berukuran kecil dan kendang ciblon atau kebar gamelan yang berukuran sedang."

        kg "Kendang Ketipung biasanya memiliki kendang pasangan, yakni kendang gedhe atau kendhang kalih."

        #image pop up: Gambang

        kg "Gambang mirip dengan saron dan demung, namun bilahan alat musik ini terbuat dari kayu atau bambu untuk menghasilkan suara yang khas dan unik."

        mc "Saron dan demung tadi dari logam, yang ini dari kayu wow"

        kg "Ada 18 bilah nada pada gambang yang terletak di atas sebuah rak konektor berbentuk perahu. Bilah-bilah tersebut tersusun berurutan dari bentuk bilah terkecil sampai yang paling panjang."

        kg "Cara memainkan alat musik gambang adalah memukul tiap bilangnya menggunakan pemukul khusus yang disebut tabuh. Hampir serupa dengan saron dan demung, bilang perlu ditahan setelah dipukul agar tidak meninggalkan suara."

label gamelan2:
        #image pop up: Siter

        kg "Siter adalah salah satu instrumen gamelan yang memainkannya dengan cara dipetik seperti alat musik guzheng asal cina atau sitar asal India."

        kg "Alat musik ini sudah jarang ditemukan atau digunakan dalam set-set gamelan saat ini. Alat musik ini biasa juga disebut gitar Jawa yang memiliki suara yang khas."

        aang "Hmmm, mirip gitar sedikit sih"

        kg "Alat musik siter memiliki dua sisi dengan nada yang berbeda, yakni sisi pelog dan slendro. Siter dianggap sebagai alat musik yang mengadopsi alat musik India karena hampir sama dengan Sitar yang merupakan alat musik tradisional india."

        #image pop up: Kenong

        kg "Kenong juga masuk dalam keluarga pencon seperti bonang dalam instrumen gamelan. Perbedaan Nya, kenong memiliki bentuk fisik lebih gemuk dari alat musik pencon lainnya."

        mc "seperti Bonang kesepian, lucu sekali"

        kg "Kenong kemudian diletakan pada pangkon dari kayu yang beralas tali agar tidak menghambat getaran kenong saat ditabuh. Alat musik ini menghasilkan suara yang rendah namun tetap nyaring dengan timbre yang khas."

        kg "Cara memainkan kenong serupa dengan memainkan bonang dengan memukul menggunakan tongkat khusus di bagian cekungan atau benjolan kenong."

        #image pop up: Gender

        kg "Gender adalah instrumen gamelan Jawa dan Bali dari bahan logam yang dipukul setiap bilahnya. Ada 10 sampai 14 bilah pada alat musik gender yang terbuat dari kuningan yang kemudian digantung pada berkas diatas resonator bambu atau seng."

        mc "Waaah, yang ini mirip gambang dan slenthem tadi"

        kg "Cara memainkan alat musik ini adalah memukul tiap bilahnya dengan alat pemukul khusus yakni tabuh kayu (Bali) atau berlapis kain (Jawa). Dalam satu set gamelan lengkap, ada tiga jenis gender yang digunakan, yakni  slendro, pelog pathet nem lan lima, dan pelog pathet barang."

        #image pop up: Kempul

        kg "Kempul adalah instrumen gamelan yang ditabuh yang hampir serupa dengan gong tetapi memiliki ukuran yang lebih kecil."

        aang "Haha kayak Gong mini kembar"

        kg "Cara bermainnya pun sama dengan gong yakni dipukul dengan tongkat khusus. Meskipun kempul masuk dalam keluarga alat musik pencon, namun kempul bisa dimainkan dengan nada seperti musik balungan dan bisa juga mendahului nada balungan."


label gamelan3:
        #image pop up: Demung

        kg "Sama halnya dengan saron, demung juga masuk dalam golongan balungan dalam instrumen gamelan. Biasanya ada dua demung jenis pelog dan slendro dalam gamelan."

        mc "Mirip sekali dengan saron bentuknya"

        kg  "Alat musik ini menghasilkan nada oktaf paling rendah dari golongan alat musik balungan lainnya meskipun ukuran fisiknya yang paling besar."

        kg  "Cara bermain demung serupa dengan saron hanya saja tabuh demung memiliki ukuran yang lebih besar dan berat daripada tabuh saron."

        #image pop up: Rebab

        kg "Rebab adalah instrumen gamelan yang penting untuk mengelaborasi dan menghiasi melodi dasar."

        aang "Wah, namanya seperti kebab, aku jadi lapar"

        kg "Cara memainkannya tidak harus sesuai dengan skala instrumen alat musik lain, alias bisa dikreasikan secara bebas. Alat musik ini juga merupakan bagian dari ansambel yang dimainkan secara terbuka."

        #image pop up: Suling

        kg "Suling adalah salah satu instrumen gamelan yang cara mainnya dengan ditiup dan terbuat dari bamboo."

        aang "Seruling saktiiii"

        kg "Suara yang lembut memberikan ciri khas pada pada kepaduan musik gamelan. Alat musik ini dianggap bersala dari Jawa barat atau Sunda."

label after_gamelan:
        show kg senyum
        kg "Bagaimana? Gamelan beragam dan menarik bukan?"

        show mc senyum
        mc "Menarik sekali pak, ternyata gamelan ada berbagai jenis juga"

        show aang bingung
        aang "Aduh, kepalaku agak sakit dengan overload informasi"

        show kg tertawa
        kg "Ahaha, bagaimana kalau kita menguji pengetahuanmu? Ayo bermain tebak tebakan bersamaku untuk mengasah ingatan kalian. Jangan sampai kalian kalah dengan otak pak tua ini."

        if pilihan == 1:
                jump pertanyaan_gamelan_1:
        elif pilihan == 2:
                "ini nanti 15 soal"
        elif pilihan == 3:
                "ini nanti 20 soal"

label pertanyaan_gamelan_1:
        #tampilin gambar bonang
        kg "Gamelan ini berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak)." 

        kg "Gamelan ini termasuk pencon yaitu dari logam,"

        menu:
                kg "apa nama dari gamelan ini?"
                "Bonang":
                    $ jawabbenar += 1
                    jawaban_benar():
                "Gong":
                    jawaban_salah():
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                "Gambang":
                    jawaban_salah():
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                "Gender":
                    jawaban_salah():
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."
                "Saron":
                    jawaban_salah():
                    kg "Bonang itu berbentuk ceret atau pot yang diletakkan di atas string (tali) dalam bingkai kayu (rancak). Bonang termasuk pencon yaitu dari logam."

label alun_alun:
    scene bg jalanan
    with fade

    show aang
    with dissolve
    aang "Alun-Alun yang akan kita kunjungi namanya alun-alun kidul Tok."

    show aang
    with dissolve
    aang "Perjalanannya sedikit jauh, tapi kita akan melewati banyak tempat bersejarah kok jadi perjalanannya tidak akan membosankan"

    show mc
    with dissolve
    mc "Baiklah Aang, waktu kita juga masih banyak, pertunjukan gamelannya mulai cukup malam."

    show mc mbakjegagik
    with dissolve
    mc "Wah, bangunan apa itu? Aang, lihat betapa megahnya bangunannya."
    
    #disini image pop up Benteng Vredeburg

    show aang
    with dissolve
    aang "Oh itu, itu adalah Benteng Vredeburg!"

    show aang
    with dissolve
    aang    "Benteng ini memiliki peran penting dalam sejarah Yogyakarta. Selama masa penjajahan Belanda, Benteng Vredeburg menjadi pusat administrasi militer 
            dan politik di wilayah ini."

    show mc senyum
    with dissolve
    mc "Wah, benarkah? Jadi ini adalah salah satu peninggalan dari zaman kolonial Belanda?"

    show aang
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

    show mc kaget
    with dissolve
    mc "Wow, betapa menariknya. Terima kasih atas penjelasannya, Aang. Ternyata ada begitu banyak cerita di balik bangunan ini."

    show aang
    with dissolve
    aang "Ya, memang begitulah. Untung aku sudah pernah mengunjunginya, jadi aku tahu sejarahnya"

    aang "Lain kali akan ku bawa kamu kesana, aku khawatir waktu kita tidak akan cukup apabila kita kesana sekarang."

    show mc
    with dissolve
    mc "Janji ya Aang?"
    
    show aang senyum
    with dissolve
    aang "Hahaha, iya janji Tok."

    show aang
    with dissolve
    aang "Oh iya, sudah jam berapa ini? Aku belum sholat dhuhur…"

    show mc kaget
    with dissolve
    mc "Waduh, aku juga belum sholat! Sebentar aku cek ponselku."

    show mc kaget
    with dissolve
    mc "Masya Allah! Sudah hampir masuk jam Asar."

    show aang kaget
    with dissolve
    aang "Astaghfirullah, jangan khawatir Tok"

    show aang senyum
    with dissolve
    aang "aku tahu masjid di dekat sini. Masjid ini juga memiliki nilai sejarah"
    
    show mc kaget
    with dissolve
    mc "Wah? Benarkah? Ayo kita segera kesana"

    show aang
    with dissolve
    aang "shapp!"

    aang "Ini dia Tok, Masjid Gedhe Kauman."

    #disini Image pop up: Masjid Gedhe Kauman

    show mc kaget
    with dissolve
    mc "Wah? Mengagumkan sekali, ini benar masjid kah?"

    show aang senyum
    with dissolve
    aang "Haha, arsitekturnya terlihat unik bukan?"

    aang "Ayo sholat dulu, waktu dhuhur sudah mau habis, kita sekalian sholat Ashar juga"

    #Char Totok dan Aang otw jalan off screen
    
label masjid_gede:
    scene bg masjid gede
    with fade

    show mc
    with dissolve
    mc "Terima kasih sudah membawaku kesini Aang, di desaku masjid-masjid jauh lebih kecil dari sini"

    show aang
    with dissolve
    aang "Tidak masalah Tok, aku juga bersyukur bisa melihat masjid semegah ini setelah sekian lama"

    aang "Melihat masjid sebesar ini membuatku penasaran terhadap sejarahnya"

    show pu
    with dissolve
    pu "Maafkan aku tapi tadi aku mendengar masnya penasaran terhadap sejarah masjid ini. Apakah kau ingin mengetahui sejarah tempat ini nak?"

    show aang
    with dissolve
    aang "Oh, iya benar pak"

    show mc
    with dissolve
    mc "Apakah bapak familiar dengan masjid ini?"

    show pu
    with dissolve
    pu "Biar saya jelaskan, saya ini adalah panitia ramadhan untuk masjid gedhe kauman, jadi saya lumayan kenal sejarahnya."

    pu "Masjid Gedhe Kauman adalah salah satu peninggalan bersejarah yang tak terpisahkan dari Kasultanan Yogyakarta, diresmikan 18 tahun setelah Perjanjian Giyanti pada tahun 1755."

    pu "Terletak di Kampung Kauman, Yogyakarta, masjid ini menjadi lokasi bersejarah dengan gaya arsitektur yang kental, menarik minat wisatawan lokal dan internasional."

    pu "Sistem atap tumpang tiga dan material bangunan yang khas mencerminkan kesempurnaan hidup dalam tiga tahapan kehidupan manusia: Syariat, Makrifat, dan Hakekat."

    pu "Meskipun mengalami perubahan seiring berjalannya waktu, keunikan dan keanggunan Masjid Gedhe Kauman tetap terjaga, seperti pemasangan batu kali putih tanpa semen dan penggunaan kayu jati utuh yang berusia lebih dari 200 tahun."

    show mc
    with dissolve
    mc "Aku tidak pernah menyangka sebuah masjid memiliki sejarah yang begitu berarti"

    show aang
    with dissolve
    aang "Oh ya pak, tempat ini terlihat besar sekali, sepertinya tidak hanya untuk sholat ya?"

    show pu
    with dissolve
    pu "Benar sekali nak, terdapat banyak ruang di masjid ini."

    pu "Bangunan utama masjid dilengkapi dengan ruang inti, maksura, mimbar, dan berbagai ruangan fungsional lainnya seperti pawestren, yakihun, dan blumbang. 
        Kompleks Masjid Gedhe juga mencakup KUA, kantor Takmir, dan Pagongan, yang menjadi tempat penyimpanan gamelan Sekaten."

    pu "Regol atau gapura yang berbentuk Semar Tinandu adalah pintu gerbang utama kompleks masjid, memperkaya keberadaan serta keunikan tempat ibadah yang sarat akan nilai sejarah 
        dan budaya."

    show aang
    with dissolve
    aang "Tidak hanya untuk ibadah, tetapi juga mengandung nilai sejarah dan budaya"

    aang "senang bisa mempelajari nilai sejarah tempat seperti ini, senang juga bisa mengetahui bahwa masjid ini masih bermanfaat untuk banyak orang."

    show mc
    with dissolve
    mc "Bapak tadi bilang bahwa bapak adalah panitia ramadhan bukan? Bagaimana kondisi masjid ini ketika ramadhan pak?"

    show pu
    with dissolve
    pu "Untuk menyambut bulan Ramadhan, Masjid Gedhe juga menyiapkan rangkaian acara dan takjilan buka bersama yang tiap harinya dikunjungi hingga 600 orang jamaah."

    pu "bahkan terdapat hari khusus dengan menu spesial. Setiap hari Kamis kami panitia khusus menyembelih kambing dan menyediakan Gulai Kambing sebagai menu buka puasa."

    show mc
    with dissolve
    mc "Masjid Gedhe Kauman ini memang merupakan wisata religi dari nilai sejarah serta kemegahan yang unik dari arsitektur masjid tertua di Jogja ya."

    show pu
    with dissolve
    pu "Haha benar sekali, sekarang saya izin pamit dulu, saya masih ada keperluan kepanitiaan, Assalamualaikum"

    ma "Waalaikumsalam pak, terima kasih informasi sejarah dan budaya masjid ini"

label alun_alun_kidul_sore:
    scene bg alun alun kidul sore
    with fade

    show aang
    with dissolve
    aang "Inilah Alun-alun kidul Tok, tempat ini ramai sekali pada malam hari"

    aang "Alun-Alun Kidul selalu menjadi tujuan favorit para wisatawan. Mari kita jelajahi dan nikmati suasana di sini."

    show mc senyum
    with dissolve
    mc "Waaah, mengagumkan sekali. Beringin kembar di tengah lapangan berdiri dengan megah"

    #disini image pop up beringin kembar

    show mc senyum
    with dissolve
    mc "Ada banyak sekali orang naik mobil sepeda juga, sungguh membuat tempat ini kelap kelip"

    #disini image pop up mobil sepeda kelap kelip

    show aang
    with dissolve
    aang "Banyak orang yang menyewa mobil sepeda itu untuk menikmati suasana di sekitar alun-alun"

    show aang senyum
    with dissolve
    aang "kalo kita sewa, kita harus menggowes pedal untuk menjalankan mobil sepeda jadi terasa seperti olahraga malam"

    show mc
    with dissolve
    mc "aku tertarik mencobanya tetapi tidak dulu deh"
    
    show mc senyum
    with dissolve
    mc "mengayuh pedal terlihat sangat melelahkan pada jam segini, haha"

    show mc
    with dissolve
    mc "Oh ya, banyak sekali orang yang mengelilingi kedua pohon beringin itu."

    show mc kebingungan
    with dissolve
    mc "Beberapa orang juga sedang berjalan sambil menutup matanya, mereka sedang apa ya?"

    show aang
    with dissolve
    aang "Oh ituu, salah satu aktivitas yang sangat terkenal di alun-alun ini adalah permainan masangin."

    aang "Memang sudah menjadi tradisi bahwa permainan ini menjadi daya tarik tersendiri dan banyak membuat para wisatawan yang tertarik untuk mencobanya."

    aang "permainan masangin ini cukup sederhana. Kamu hanya perlu menutup mata dengan kain penutup lalu berjalan lurus sekitar 20 meter dari Sasono Hinggil menuju ke bagian tengah kedua pohon beringin."

    show aang senyum
    with dissolve
    aang "Permainan ini terdengar mudah, tapi seperti yang bisa kau lihat, banyak orang yang melenceng dan berputar tidak jelas haha"

    show aang
    with dissolve
    aang "Banyak mitos yang beredar bahwa hanya orang yang berhati bersih dan lurus yang bisa melewati kedua pohon tersebut."

    aang "Ada mitos lain yang mengatakan bahwa harapanmu akan terkabulkan apabila kau dapat melewatinya."

    aang "kau terlihat bersih seperti orang yang berhati bersih dan lurus Tok, maukah kamu mencobanya?"

    show mc kebingungan
    with dissolve
    mc "Eh… Apa? Apakah tidak bahaya apabila aku berjalan sambil menutup mata?" 

    show aang senyum
    with dissolve
    aang "Haha tidak apa apa, kau akan ku jaga agar tidak menabrak siapa siapa, tidak perlu khawatir."

    show mc
    with dissolve
    mc "Tidak ah, aku tidak percaya dengan mitos seperti itu"

    show aang
    with dissolve
    aang "kita tidak perlu mempercayai mitos, cukup mencobanya agar tau saja"

    #ngga tau mau diisi apa, kur masi ngga jelas (hal 23 script). tapi aku mau lanjut dialog selanjutnya

    "suara perut"

    show mc
    with dissolve
    mc "{i}uggrgrggrgrgrgrhhrghrghr{/i}"

    mc "Ahaha, tidak dulu Aang, aku sedikit lapar."

    show aang
    with dissolve
    aang "Haha, baiklah, sepertinya kita harus pergi cari makan dulu."

    "time passes"

    show mc
    with dissolve
    mc "Sudah jam segini, ayo kita berangkat ke pertunjukan Gamelan."

    show aang senyum
    with dissolve
    aang "Masih jam segini Tok, santai aja dulu"

    show mc
    with dissolve
    mc "Aku ingin mengambil kursi depan agar aku bisa melihat bapak tadi."

    show aang
    with dissolve
    aang "Oh, benar juga, kita belum tahu nama bapak itu sampai sekarang" 

    show mc bingung
    with dissolve
    mc "Benar juga, nanti harus kita tanyakan kepadanya"

    show aang
    with dissolve
    aang "Baiklah, ayo berangkat. Final stop for today, Pertunjukan Gamelan skuy!"

label tempat_duduk_pertunjukan_terang:
    scene bg tempat duduk pertunjukan terang
    with fade

    show mc
    with dissolve
    mc "Jadi ini tempat pertunjukannya, menarik juga"

    show aang
    with dissolve
    aang "Hehe kursi depan masih kosong,ayo ambil tempat"

    "suara perangkat jatuh"

    "Aang dan Totok kaget mbakjegagikk..."

    show aang kaget
    with dissolve
    aang "ASSSS… taghfirullah aladzim, suara apa itu?"

    show mc kaget
    with dissolve
    mc "Suara itu terdengar dari panggung, sepertinya ada yang jatuh."

    show pb kaget
    with dissolve
    pb "Aduuuh, bagaimana iniii, aku akan dipecat aku akan dipecat, ini baru tugas kedua ku dan aku sudah mengacaukannya"

    pb "Kalau aku tidak bisa memperbaikinya, acara ini akan kacau, atau lebih buruk… DIBATALKAN!"

    show aang kaget
    with dissolve
    aang "Apa??? Dibatalkan??? Tok, apakah kau mendengar ini? Ada kemungkinan bahwa pertunjukannya dibatalkan"

    show mc kaget
    with dissolve
    mc "Aku tidak bisa mempercayai ini, padahal aku sudah menantikan penampilan bapak gamelan."

    show aang
    with dissolve
    aang "Aku tidak ingin acara ini dibatalkan, mari kita cari tahu alasannya"

    #disini Char Totok dan Aang otw jalan off screen

label panggung:
    scene bg panggung
    with fade

    show aang marah
    with dissolve
    aang "Permisi mas, saya tadi tidak sengaja mendengar bahwa ada acara ini akan dibatalkan, apakah benar?"

    show pb panik
    with dissolve
    pb "A-A-Apaa??? Gawat, beritanya sudah sampai pada publik, aku akan dipecat aku akan dipecat!!!"

    show mc
    with dissolve
    mc "T-tenang saja mas, baru kami saja yang mendengar, ada masalah apa dengan pertunjukannya? Mengapa akan dibatalkan?"

    show pb panik
    with dissolve
    pb " E-e-e….. Jadi begini…"

    pb "Aku adalah seorang intern di organisasi penyelenggara acara ini, aku baru mengikuti acara sebagai panitia sekali, jadi ini kedua kalinya untukku"

    pb "Aku seharusnya hanya menjadi panitia operasional perkap, yang berarti aku hanya perlu menyiapkan dan memindahkan alat"

    pb "Te-te-tetapi koordinator acara tiba-tiba sakit, dan aku ditunjuk menjadi koordinator pengganti"

    pb "Aku tidak meminta untuk menjadi koordinator, aku tidak ingin menjadi koordinator, sekarang semuanya akan kacau karena aku"

    pb "Aku akan dipecat, aku seharusnya tidak mendaftar menjadi panitia, aku bodoh sekali"

    show aang sedih
    with dissolve
    aang "Hey, hey, tenang saja mas… Permasalahannya di mana? Apa yang kacau?"

    show pb sedih
    with dissolve
    pb "Aku tidak tahu tempat masing-masing gamelan di panggung, aku harus dapat mengatur masing-masing gamelan di posisinya yang tepat"

    show aang sedih
    with dissolve
    aang "Apakah… kamu bisa berusaha mengingatnya kembali?"

    show pb sedih
    with dissolve
    pb "A-aku sedikit ingat, jenis suara apa berasal darimana, bentuk, dan nama dari beberapa gamelan, tapi aku tidak ingat semuanya."

    show aang
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
        while click <= 3:
                if click == 0:
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show aang flat
                                        aang "Apakah kamu yakin Tok? Kita sudah jauh jauh kesini untuk menyaksikan pertunjukan Gamelan"
                                        
                                        show mc
                                        mc "(Aang benar, aku kesini untuk menyaksikan pertunjukan gamelan)"
                elif click == 1:
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show aang flat
                                        aang "Kakek sudah memberi ilmu gamelan kepada kita, mas mas ini juga sedang sangat kebingungan, sebaiknya kita membantunya"

                                        show mc
                                        mc "(Semua kebaikkan pasti akan dibalas, aku juga tidak ingin melihat penampilan bapak gamelan)"
                elif click == 2:
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        $ click += 1
                                        show aang flat
                                        aang "Apakah kamu yakin Tok? Aku yakin {color=#ff0000}pengalaman yang kita dapatkan akan berubah apabila kita tidak membantu"

                                        show mc
                                        mc "Aku {color=#ff0000}sebaiknya membantu persiapan{/color}, pengalaman dan hasilnya pasti akan bermanfaat"
                elif click == 3:
                        show aang flat
                        aang "Baiklah Tok, lalu sekarang kita mau kemana?"
                        menu:
                                "Kamu Memilih untuk:"
                                "Membantu Persiapan Gamelan":
                                        jump bantu_gamelan
                                "Akhhh Malassss":
                                        jump bantu_persiapan_gamelan
                                "{color=#ff0000}Aku mengantuk, aku ingin istirahat":
                                        jump balik_hotel
        return

label bantu_gamelan:
    show aang senyum
    aang "Hahaha, sudah kuduga kamu akan membantu Tok."

    aang "Jangan khawatir mas, kami akan membantumu, kami lumayan tahu juga tentang gamelan."

    show pb senyum_lebar
    pb "Be-benarkah? Kalian akan membantuku?"

    show mc
    mc "Tentu saja kami akan membantumu mas, kami juga sangat bersemangat ingin menyaksikan pertunjukan gamelan."

    show pb senyum_lebar
    pb "Terima kasih banyak, baiklah, ayo kita mulai."    

    #nanti cerita lanjut disini, yang balik_hotel itu ending dari chapter 1

    #mini game: set the stage
    show pb senyum lebar
    with dissolve
    pb "Dengan begini, pertunjukan dapat berjalan dengan lancar!"

    pb "Aku sungguh berterima kasih kepada kalian, tanpa kalian aku sudah kehilangan pekerjaanku"

    pb "Senang sekali dapat melihat panggung yang sempurna"

    show aang flat
    with dissolve
    aang "Hadeuh, melelahkan juga kerjaannya, tetapi aku senang kita bisa membantu"

    show mc flat
    with dissolve
    mc "Tidak masalah, kami senang bisa membantu."

    show pb senyum lebar
    with dissolve
    pb "Aku belajar banyak hal baru hari ini, berkat bantuan kalian semuanya berjalan lancar"

    show aang flat
    with dissolve
    aang "Itu bagus sekali. Tetapi ingatlah bahwa belajar adalah proses yang terus menerus. Jadi jangan ragu untuk terus mencoba hal-hal baru dan terus berkembang."

    show mc senyum
    with dissolve
    mc "Haha, aku tidak menyangka kamu bisa memberi pencerahan seperti itu Aang."

    show aang senyum
    with dissolve
    aang "Hehe, sekali-kali gapapa lah Tok."

    show mc flat
    with dissolve
    mc "Semoga sukses untuk pertunjukan gamelan nanti. Jangan ragu untuk meminta bantuan jika kalian membutuhkannya lagi."

    show pb senyum lebar
    with dissolve
    pb "Tentu saja, aku akan terus berlatih dan belajar! Terima kasih sekali lagi atas bantuan dan dorongan kalian. Selamat menikmati pertunjukan"

    show aang flat
    with dissolve
    aang "Ayo kita kembali ke kursi kita Tok, kita saksikan pertunjukan gamelan spesial ini"

label tempat_duduk_gelap:
    show mc flat
    with dissolve
    mc "Membantu pertunjukan tadi membuatku semakin semangat menonton pertunjukan"
    
    show aang
    with dissolve
    aang "Betul sekali, melihat hasil dari kerja keras dan jerih payah sendiri terasa jauh lebih memuaskan."

    show mc kaget
    with dissolve
    mc "Oh, aku melihat bapak tadi siang di panggung, dia memainkan bonang"

    show aang
    with dissolve
    aang "Aku melihatnya, sepertinya pertunjukannya sudah akan dimulai"

    #disini (pertunjukan mulai, terserah mau suara tok ata full cutscene orang main gamelan)

    show aang senyum
    with dissolve
    aang "Wah, pertunjukan tadi sungguh luar biasa. Mereka benar-benar menghidupkan tradisi gamelan dengan indah."

    show mc senyum
    with dissolve
    mc "Iya, betul sekali! Aku juga merasa terinspirasi oleh penampilan mereka. Semoga suatu hari nanti kami juga bisa sehebat mereka."

    show mc senyum
    with dissolve
    mc "Lihat itu, bapak gamelan sedang turun panggung, mari kita sambut"

label panggung:
    show mc senyum
    with dissolve
    mc "Bapak, pertunjukan tadi sungguh luar biasa. Mereka benar-benar memainkan gamelan dengan begitu indah."

    show aang senyum
    with dissolve
    aang "Iya, benar sekali. Kami sangat menikmati pertunjukan tadi. Cara bapak memainkan gamelan tadi sangat indah!"

    show kg senyum
    with dissolve
    kg "Terima kasih, anak muda. Pak tua ini senang kalian menikmati pertunjukan kami. Kakek juga senang bisa berbagi seni tradisional dengan kalian."

    kg "Aku dengar kalian juga membantu persiapan pertunjukan ini tadi."

    show aang senyum
    with dissolve
    aang "benar pak, itu semua berkat ilmu gamelan yang sudah bapak berikan kepada kami tadi siang"

    show mc
    with dissolve
    mc "Apakah kami boleh foto bersama bapak? Kami ingin mengenang momen ini."

    show kg senyum
    with dissolve
    kg "Haha, dengan senang hati!"

    #disini Image pop up: Foto Totok, Aang, dan Bapak Gamelan dengan background panggung penuh gamelan

    show kg
    with dissolve
    kg "Jangan lupa kirimkan foto itu kepadaku juga ya nak. Senang bisa bertemu dengan pemuda antusias dan baik hati seperti kalian"

    show mc
    with dissolve
    mc "Tentu saja pak, boleh minta nomor telepon dan nama bapak siapa ya kalau boleh tau?"

    show kg
    with dissolve
    kg "Oh ya kita belum saling mengenal, namaku ada Sutrisno Haji Tifa"

    show aang
    with dissolve
    aang "Salam kenal pak, saya Aang Idhang Saputra."

    aang "Oh aku juga belum tahu nama lengkapmu Tok, apa nama lengkapmu?"

    show mc
    with dissolve
    mc "Haha, benar juga. Nama lengkapku Totok Hestamma."

    show su
    with dissolve
    su "..."

    su "Hestamma… Totok Hestamma dan Aang Idhang Saputra ya."

    show su senyum
    su "Nama-nama yang bagus sekali, semoga aku bisa bertemu lagi dengan kalian di masa depan."

    show mc
    with dissolve
    mc "Terima kasih pak Sutrisno, kami tidak akan melupakan pengalaman ini."

    show su
    with dissolve
    su "Sampai jumpa anak muda. Semoga Allah memberkati jalan kalian."

    #disini totok dan aang pergi

    su "Hestamma… Rasanya aku pernah mendengar nama itu"

label tempat_duduk_pertunjukan_terang:
    show aang
    with dissolve
    aang "ngomong-ngomong sudah jam berapa ini? Ternyata sudah cukup larut. Mungkin sudah waktunya kamu kembali ke hotel untuk istirahat Tok"

    show mc
    with dissolve
    mc "Benar juga. Kita sudah melalui hari yang panjang, dan esok akan menjadi hari yang penuh kisah. Ayo kita pulang."

label Depan_hotel_malam:
    show aang
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

label balik_hotel:
        show aang flat
        aang "B-Baiklah Tok, apabila itu yang kau inginkan."

        aang "Baik mas, terima kasih informasinya. Karena pertunjukannya dibatalkan kami akan pulang sekarang."

        aang "Tetap sabar dan tabah, semoga mas dimudahkan Allah dalam menghadapi musibah ini."

        show pb panik
        pb "Ba-baiklah, mohon maaf sebesar besarnya… aduuuh bagaimana ini….. tamatlah aku!!!!"

        #nanti disini show bg depan hotel tapi malam hari

        scene bg depan hotel
        with fade
        show aang flat
        aang "Padahal kau terlihat begitu bersemangat ketika mendapat tiket dari bapak tadi siang"

        aang "Aku khawatir dengan apa yang terjadi pada pertunjukannya, apakah mas mas panitia tadi berhasil menyelesaikan masalahnya?"

        aang " ngomong-ngomong sudah jam berapa ini? Ternyata sudah cukup larut. Mungkin memang benar keputusanmu untuk kembali ke hotel untuk beristirahat."

        aang "Masih ada banyak tempat yang ingin ku tunjukan padamu besok"

        show aang senyum
        aang "Selamat malam Tok, sampai jumpa besok!"

        #CHAPTER 1 END DI SINI JIKA MC MEMILIH BALIK KE HOTEL