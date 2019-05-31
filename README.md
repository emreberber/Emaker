<<<<<<< HEAD
### görüşmeler (emre^2,ahmet)
* 3 kasım'18 öncesi
  * django projesi oluşturuldu, blok şeması çizildi 
  * iş bölümü (ahmet?)
  * bir sonraki görüşme: 8 kasım,12:00,grafik lab
* 8 kasım'18
  * proje planı, iş bölümü neredeyse tamam
  * ilk prototip görmek istiyorum
  * model'i netleştirelim,
  * bir sonraki görüşme: 15 kasım,12:00,grafik lab

### exam-maker-and-assesment

sınav (test) oluşturma ve otomatik okuma

- Yunus Emre Berber
- Emre Aktürk
- Ahmet İlgin

------------
```
$ sudo apt-get install python3-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

```
(venv) $ pip install -r requirements.txt
(venv) $ django-admin startproject emaker .
(venv) $ python manage.py runserver
```

```
(venv) $ python manage.py startapp exam
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser
=======
# Emaker
web based exam preparation platform 
>>>>>>> 509ae2ac52210137cdcf611a233c0140dd503594
