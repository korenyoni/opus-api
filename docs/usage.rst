Usage
=====

Find your languages:

.. code:: console

    $ opus_api langs

    [
    ...
      {
        "description": "en (English)", 
        "id": 69, 
        "name": "en"
      },
      ...
      {
        "description": "ru (Russian)", 
        "id": 198, 
        "name": "ru"
      }...
    ]

Find corpora:

.. code:: console

    $ opus_api get en ru --maximum 300 --minimum 3

    {
      "corpora": [
        {
          "id": 1, 
          "name": "OpenSubtitles2016", 
          "src_tokens": "157.5M", 
          "trg_tokens": "133.6M", 
          "url": "http://opus.lingfil.uu.se/download.php?f=OpenSubtitles2016%2Fen-ru.txt.zip"
        },
      ...
        {
          "id": 13, 
          "name": "KDE4", 
          "src_tokens": "1.8M", 
          "trg_tokens": "1.4M", 
          "url": "http://opus.lingfil.uu.se/download.php?f=KDE4%2Fen-ru.txt.zip"
        }
      ]
    }
