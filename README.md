# 🤖 Kedytagger Bot

Telegram gruplarında ve kanallarında üyeleri toplu veya tekli olarak (isimle, emojiyle veya özel etiketlerle) kolayca etiketlemenizi sağlayan gelişmiş bir tagger botudur.

## ✨ Özellikler

- 👥 **`/utag`**: Üyeleri klasik formatta etiketler.
- ✨ **`/itag`**: Üyeleri özel güzel isimlerle etiketler.
- 🎨 **`/etag`**: Üyeleri eğlenceli emojilerle etiketler.
- 👤 **`/tektag`**: Üyeleri tek tek etiketler.
- ❌ **`/cancel`**: Devam eden etiketleme işlemini anında durdurur.
- 👮 **Güvenlik:** Komutlar yalnızca grup yöneticileri tarafından kullanılabilir.

---

## 🛠️ Kurulum ve Değişkenler (Environment Variables)

Botun çalışabilmesi için aşağıdaki çevre değişkenlerini (Secrets) tanımlamanız gerekir:

- `APP_ID` : Telegram API ID'niz (my.telegram.org adresinden alınır)
- `API_HASH` : Telegram API Hash'iniz
- `TOKEN` : BotFather'дан aldığınız Telegram Bot Token'ı

---

## 🚀 Komut Listesi

| Komut | Açıklama |
| :--- | :--- |
| `/start` | Botun çalışıp çalışmadığını ve menüyü gösterir. |
| `/bilgi` | Yardım menüsünü açar. |
| `/utag <mesaj>` | Gruptakileri etiketleyerek mesaj gönderir. |
| `/itag <mesaj>` | Gruptakileri güzel isimler ekleyerek etiketler. |
| `/etag <mesaj>` | Gruptakileri emojilerle etiketler. |
| `/tektag <mesaj>`| Üyeleri tekli olarak etiketler. |
| `/cancel` | Etiketleme döngüsünü iptal eder. |

---
> Geliştirici: [@SakirBey1](https://t.me/SakirBey1)
> 
