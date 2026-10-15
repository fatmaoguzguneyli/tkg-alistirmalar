# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("abvcgfd") == "zayıf"
    assert sifre_gucu("abcfgsha") == "orta"
    assert sifre_gucu("adcvbhdgefa") == "orta"
    assert sifre_gucu("acvgbhjnmklr") == "güçlü"
    assert sifre_gucu("hjgsfdacvsfgehsa") == "güçlü"
    with pytest.raises (ValueError):
        sifre_gucu("") 

def test_otopark_ucret():
    with pytest . raises(ValueError):
        otopark_ucreti(-3)
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(10) == 0
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(30) == 20
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(90) == 40
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(200) == 60

def test_yuzde_degisim():
    with pytest . raises(ValueError):
        assert yuzde_degisim(0,0)
    with pytest . raises(ValueError):
            assert yuzde_degisim(0,20)
    assert yuzde_degisim(20,60) == 200

    



    

