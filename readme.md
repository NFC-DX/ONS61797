# ONS61797
`ONS61797` クラスは、シリアルポートまたはソケット通信を介して ONS61797 デバイスとのインターフェースを提供するためのクラスです。このクラスは、デバイスに対する基本的な制御（出力のオン/オフや電圧設定など）および設定（IP アドレスやサブネットマスクの設定など）を行う機能を提供します。

## クラス概要
### Parameters
portかip_addressのどちらかを指定して下さい。

- **port** (`str`, optional): デバイス接続に使用するシリアルポート。デフォルトは `None`。
- **ip_address** (`str`, optional): デバイス接続に使用する IP アドレス。デフォルトは `None`。

### Attributes
- **instrument** (`serial.Serial` または `socket.socket`): デバイス接続のオブジェクト。
- **port** (`str`): 通信に使用されるシリアルポート。
- **baudrate** (`int`): シリアル通信のボーレート。デフォルトは `115200`。
- **ip_address** (`str`): ソケット通信のための IP アドレス。
- **line_feed_code** (`str`): 通信に使用する改行コード。
- **time_out** (`float`): 通信のタイムアウト。デフォルトは `10.0` 秒。
- **time_interval** (`float`): コマンド送信後の応答読み取りまでのインターバル。デフォルトは `0.1` 秒。

### Methods
#### `__init__(port: str = None, ip_address: str = None)`

インスタンスを初期化し、指定されたシリアルポートまたは IP アドレスでデバイスに接続します。

##### Parameters
- **port** (`str`, optional): デバイス接続に使用するシリアルポート。デフォルトは `None`。
- **ip_address** (`str`, optional): デバイス接続に使用する IP アドレス。デフォルトは `None`。

#### `connect(port: str = None, ip_address: str = None)`

デバイスへの接続を確立します。シリアルまたはソケット通信で接続を確立し、通信オブジェクトを生成します。

##### Parameters
- **port** (`str`, optional): デバイス接続に使用するシリアルポート。デフォルトは `None`。
- **ip_address** (`str`, optional): デバイス接続に使用する IP アドレス。デフォルトは `None`。

##### Raises
- **ValueError**: `port` または `ip_address` のどちらも指定されていない場合。
- **TypeError**: 両方の `port` および `ip_address` が指定された場合。

#### `close()`

デバイスへの接続を終了します。

#### `write(cmd: str)`

デバイスにコマンドを送信します。

##### Parameters
- **cmd** (`str`): デバイスに送信するコマンド文字列。

#### `read() -> str`

デバイスからの応答を読み取ります。

##### Returns
- **str**: デバイスからの応答文字列。

#### `query(cmd: str) -> str`

コマンドを送信し、デバイスからの応答を読み取って返します。

##### Parameters
- **cmd** (`str`): デバイスに送信するコマンド。

##### Returns
- **str**: デバイスからの応答文字列。

#### `on(channel: int)`

指定されたチャンネルをオンにします。

##### Parameters
- **channel** (`int`): オンにする出力チャンネルの番号。

#### `off(channel: int)`

指定されたチャンネルをオフにします。

##### Parameters
- **channel** (`int`): オフにする出力チャンネルの番号。

#### `get_output_state(channel: int) -> int`

指定されたチャンネルの出力状態を取得します。

##### Parameters
- **channel** (`int`): 出力状態を確認するチャンネルの番号。

##### Returns
- **int**: 出力チャンネルの状態。`0` はオフ、`1` はオン。

#### `set_voltage(channel: int, voltage: float)`

指定されたチャンネルに出力電圧を設定します。

##### Parameters
- **channel** (`int`): 出力電圧を設定するチャンネルの番号。
- **voltage** (`float`): 設定する電圧。

#### `get_voltage(channel: int) -> float`

指定されたチャンネルの出力電圧を取得します。

##### Parameters
- **channel** (`int`): 出力電圧を取得するチャンネルの番号。

##### Returns
- **float**: 出力電圧。

#### `get_device_information() -> str`

デバイス情報を取得します。

##### Returns
- **str**: デバイス情報文字列。

#### `reset()`

デバイスをリセットします。

#### `set_ip_address(ip_address: str)`

デバイスの IP アドレスを設定します。

##### Parameters
- **ip_address** (`str`): 設定する IP アドレス。

#### `get_ip_address() -> str`

現在のデバイスの IP アドレスを取得します。

##### Returns
- **str**: IP アドレス。

#### `set_subnet_mask(subnet_mask: str)`

デバイスのサブネットマスクを設定します。

##### Parameters
- **subnet_mask** (`str`): 設定するサブネットマスク。

#### `get_subnet_mask() -> str`

現在のデバイスのサブネットマスクを取得します。

##### Returns
- **str**: サブネットマスク。

#### `set_default_gateway(default_gateway: str)`

デバイスのデフォルトゲートウェイを設定します。

##### Parameters
- **default_gateway** (`str`): 設定するデフォルトゲートウェイ。

#### `get_default_gateway() -> str`

現在のデバイスのデフォルトゲートウェイを取得します。

##### Returns
- **str**: デフォルトゲートウェイ。

# ライセンス
Copyright (c) 2024 NF Corporation  
Released under the MIT license  
https://opensource.org/licenses/mit-license.php
