# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama


def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0
    assert kargo_ucreti(0) == 50
    assert kargo_ucreti(500) == 0
    assert kargo_ucreti(350) == 50
    with pytest.raises(ValueError):
        kargo_ucreti(-100) 
    
def test_bilet_fiyatı():
    assert bilet_fiyati(0) == 0
    assert bilet_fiyati(4) == 0
    assert bilet_fiyati(6) == 0
    assert bilet_fiyati(7) == 50
    assert bilet_fiyati(17) ==50
    assert bilet_fiyati(14) == 50
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(61) == 100
    assert bilet_fiyati(64) == 100
    assert bilet_fiyati(65) == 60
    assert bilet_fiyati(68) == 60
    with pytest.raises(ValueError):
         bilet_fiyati(-5) 

def test_ortama_kontrol():
    with pytest.raises(ValueError):
     ortalama([])     
    assert ortalama([70,70]) == 70
    assert ortalama([33,66,99]) == 66
    assert ortalama([39,42]) == 40.5
    assert ortalama([20.5,31.7]) == 26.1