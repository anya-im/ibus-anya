# ibus-anya
This project join Input Method IBus and kanakanji converter Anya.<br>
Caution: State is sample. Do not production use.

# Requirement
* IBus
* [[anya-grpc](https://github.com/anya-im/anya-grpc)]
* autotools
* python3

# Install
## build
    run command below.
    1. autoreconf
    2. ./configure --datadir=<<data dir>>
    3. make
    4. sudo make install
    * <<data dir>> ibus and glib-2.0 parent path. In openSUSE it is /usr/share. Default is /usr/local/share.

## Use
Restart ibus. and add [[Anya](https://github.com/anya-im/anya-grpc)] in [[設定](https://github.com/anya-im/anya-grpc)] - [入力メソッド] - [追加] - [日本語].<br>
Then [日本語 - [Anya](https://github.com/anya-im/anya-grpc)] is shown in list of IBus. Select it.<br>

## Convert
Select [Input mode] - [Hiragana].<br>
Input any key and press [SPACE].

