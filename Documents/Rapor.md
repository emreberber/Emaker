#### Problem Tanımı

- Kullanıcıların derslere ait soru ekleyip, bu sorular üzerinden belirleyeceği koşullara bağlı olarak pdf formatında test oluşturabileceği web tabanlı bir platformun geliştirilmesidir.

#### Genel Akış Şeması

![FlowChart](https://github.com/zyavuz610/exam-maker-and-assesment/blob/master/Documents/ExamMaker_FlowChart.png)

####  İş Paylaşımı

 - Kişiye özel herhangi bir iş paylaşımı yapılamadı.Proje, Github üzerinden ortaklaşa gerçekleştirilecektir. 

####  Literatür Araştırması ve Benzer Projeler 

 - [Test Maker](http://www.testmaker.net/), Ercan Yazılım firmasının geliştirmiş olduğu ücretli bir masaüstü test otomasyon yazılımıdır. Projemizde ana referans kaynağı Test Maker uygulamasıdır. Amacımız bu uygulamadaki eksiklerin giderilecek web platformuna taşınmasıdır. 
 - [Online Test Maker](https://www.typeform.com/tests/)
 - [Easy Test Maker](https://www.easytestmaker.com/)
 - [iSpring Quizmaker](https://www.ispringsolutions.com/ispring-quizmaker)
 - [Go Conqr](https://www.goconqr.com/)
 - [Class Marker](https://www.classmarker.com/)
 - [Quiz Works](https://www.quizworksinternational.com/)
 - [Help Teaching](https://www.helpteaching.com/)
 - [Pro Profs](https://www.proprofs.com/)
 - [Poll Maker](https://www.poll-maker.com/)
 - [School House Technologies](https://www.schoolhousetech.com/)
 - [Articulate Studio](https://articulate.com/360/studio)

####  Proje Planı

- Github üzerinde django projesinin oluşturulması.
- Projeye ait model yapısının belirlenmesi.
- Admin arayüzünün gerçekleştirilmesi.
- Admin arayüzüne Login, Register, Logout işlemlerinin gerçekleştirilmesi.
- Genel akış şemasında verilen tüm işlevlerin Admin paneli üzerinden gerçekleştirilmesi.
- Oluşturulan sınav formatının pdf ortamına akatarılması.

####  Yol Haritası
	
- Örnek projerin araştırılması.
- Projeye ait örnek senaryonun belirlenmesi.
- Django web çatısının verdiği imkanların araştırılıp, ögrenilmesi.
- Veritabanı Tablolarının oluşturulup, verilerinin belirlenmesi.
- Veritabanı ilişkilerinin kurulması.
- Genel akış şemasının belirlenmesi.
- Genel akış şemasında belirlenen metodların gerçekleştirilmesi.
- Yazılımın test edilmesi.

#### Projeyi Gerçekleştirmek İçin Kullanacağımız Yöntem

- Proje için kullancağımız en güçlü yöntemimiz planlı bir şekilde hareket etmek olacaktır.
Bu bize ilerleyen zamanlarda karşılaşacağımız problem sayısının daha aza indirgenmesinde rol oynayacaktır.
Ayrıca bu projeye benzer projeler bizim için en önemli yol haritasıdır.Bu sayede o projelerde
gördüğümüz eksik veya geliştirilmesi gereken noktaları biz bu projede uygulayacağız.
- Bir önemli detay ise zaman.Projeyi en sağlıklı şekilde yürütebilmemiz için zamanı olabildiğince en verimli
şekilde kullanmamız gerektiğinin farkındayız.Django'nun bize sağladığı admin paneli ve PDF çıktı alma tarafında
kullanacağımız PyFPDF python kütüphanesi, zaman konusunda bizlere pozitif yönde katkı sağlayacaktır.
- Sonuç olarak toparlamak gerekirse, Python diline ait Django Framework'un içinde bizlere sunulan admin panelini
kendi projemize dahil edeceğiz.Bu paneli admin kullancısı dışında diğer kullanıcıların da kullanabileceği bir
panel şekilde yapılandıracağız.Böylece ayrı bir önyüz işlemine takılmadan bu panel üzerinden tüm işlemlerimizi 
gerçekeştirebileceğiz.Proje için öncelikli hedefimiz kullanıcının oluşturduğu sınavı pdf ortamına çıktısını 
sağlayabilmek.Bunu PyFPDF kütüphanesini kullanarak gerçekleştireceğiz.Projemizde üzerinde en çok duracağımız 
noktaların başında bu gelmekte.

#### B Planı

- Yöntemimizin admin panelinden kaynaklı olarak başarısız olabilir.Bu panelin kullancılara göre esnetilememesi 
durumunda b planı aktif rol oynayacaktır.Bu plana göre de, django admin paneli yerine kullanıcılar için farklı bir 
arayüz tasarlanmasıdır.
- PDF çıktı alma tarafında problem yaşayacak olursak da, alternatif olarak hazırda beklettiğimiz diğer kütüphanelere 
müracaat edilecektir.

#### Başarılı Olma Kriterleri

- Projede %100 başarı söz konusu ise projenin son hali, oluşturulan sınavların pdf çıktısını ve bunun yanında
şıkların koordinatlarını da ayrı bir json formatında verebilmelidir.Projenin henüz başlangıç aşamasında bulunduğumuz bu
zaman diliminde öncelikli hedefimiz sınavların istenildiği gibi pdf ortamına aktarılabilmesidir.Bu adımdan sonra eklenecek
olan özellikler projenin daha farklı bir boyuta taşınmasında etkili olacaktır.

#### Ekler

- 01 : ExamMaker_FlowChart.png
- 02 : ExamMaker_FlowChart.xml
- 03 : gantchart.xlsx 

#### Hazırlayanlar

- Yunus Emre BERBER
- Emre AKTÜRK
- Ahmet İlgin
