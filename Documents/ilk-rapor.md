# projenin amacı
* amaç test maker benzeri web tabanlı soru oluşturma, soru saklama, test oluşturma ve pdf olarak basma yapabilen bir sistem geliştirmek
* bunu yaparken farklı grup testler oluşturabilmeli
* soruların türlerini desteklemeli (çoktan seçmeli, evet/hayır, açık uçlu)
* sorularda ve/veya seçeneklerde şekil olabilmeli (mümkün olabiliyorsa şekli kendimiz çizelimi olamıyorsa Ctrl+V ile yapıştırma ya da sürükle bırak ile yüklenebilmeli, o da olamıyorsa upload ile yükleyebilmeliyiz)
* soruları basarken kitapçık, a4, a3 formatları olabilmeli
* cevap anahtarı oluşturabilmeli,
* a4 kağıdı için çıkların koordinatlarını ayrı bir json formatında verebilmeli (json formatını düşüneceğiz)

## örnek senaryo
* kullanıcılar olacak, her kullanıcı bir hoca
* hoca girip bir ders ekleyecek, o dersin altına soru ekleyebilecek
* örn. 200 soru oluştu. bu soruları daha sonra düzenleyebilecek
* hoca bir sınav oluştur diyebilecek, o sınava soru ekleyip çıkarabilecek.
* sınav kağıdı bas seçeneği olacak, a,b gibi farklı gruplarda soru basabilecek
* soruları basarken kağıtta beyaz boşluk olmayacak, soruların şekli varsa hizalama akullı olacak
* soruların basıldığı koordinatlara göre seçeneklerin koordinatları bir json dosyasında çıktı olacak verilecek. (bir çeşit cevap anahtarı)
