const AboutItems = {
  konsep : {
    content : "Ide utama dari sistem temu balik informasi adalah mengubah search query menjadi ruang vektor. Setiap dokumen maupun query dinyatakan sebagai vektor w = (w1, w2,..., wn) di dalam Rn, dimana nilai wi dapat menyatakan jumlah kemunculan kata tersebut dalam dokumen (term frequency). Penentuan dokumen mana yang relevan dengan search query dipandang sebagai pengukuran kesamaan (similarity measure) antara query dengan dokumen. Semakin sama suatu vektor dokumen dengan vektor query, semakin relevan dokumen tersebut dengan query. Kesamaan tersebut dapat diukur dengan cosine similarity dengan rumus:"
  },
  penggunaan : {
    content : "Program ini digunakan untuk mencari dokumen yang sesuai dengan pencarian pengguna. Terdapat 2 hal yang dapat dilakukan pengguna yaitu:",
    list1 : "1. Mengunggah dokumen ke dalam web browser",
    list2 : "2. Melakukan pencarian dokumen yang paling mirip dengan input pengguna di search bar"
  }
}

export default AboutItems