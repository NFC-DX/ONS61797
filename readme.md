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
- **str**: デバイス情報。

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

# ONS61797Server

ONS61797をLabRADサーバーを通じて制御するためのPythonプログラムです。本サーバーを利用することで、LabRADクライアントからの操作が可能になります。

## 概要

このサーバーは、シリアル通信またはソケット通信で接続される**ONS61797**をLabRADサーバー経由で制御します。各種のコマンドでデバイスの状態を取得・設定し、LabRADネットワーク上で利用することが可能です。

## クラス: `ONS61797Server`

### 機能概要

- **LabradServerクラス**を継承して実装されたクラスで、LabRADプロトコルに従いONS61797デバイスを制御します。
- **属性**
  - `device`：`ONS61797`オブジェクトまたは`None`（Noneの場合、機器一覧から選択する必要があります）
- **メソッド**：デバイスの接続、設定、取得、出力制御などの機能を提供します。

### 設定関数一覧

#### 1. 接続・切断
- **`connect(c, port, ip_address)`**  
  デバイスに接続する。
  - **引数**：
    - `port`: シリアルポート名
    - `ip_address`: デバイスのIPアドレス
- **`close(c)`**  
  デバイスからの接続を切断し、`device`を`None`に設定。

#### 2. 出力制御
- **`on(c, channel)`**  
  指定されたチャンネルの出力をオンにする。
  - **引数**：
    - `channel`: 制御するチャンネル番号
- **`off(c, channel)`**  
  指定されたチャンネルの出力をオフにする。
  - **引数**：
    - `channel`: 制御するチャンネル番号
- **`get_output_state(c, channel)`**  
  チャンネルの出力状態（オン/オフ）を取得。

#### 3. 電圧設定と取得
- **`set_voltage(c, channel, voltage)`**  
  チャンネルに電圧を設定する。
  - **引数**：
    - `channel`: チャンネル番号
    - `voltage`: 設定する電圧値
- **`get_voltage(c, channel)`**  
  チャンネルの現在の電圧を取得。

#### 4. デバイス情報
- **`get_device_information(c)`**  
  デバイス情報（IDや型番など）を取得。

#### 5. リセット機能
- **`reset(c)`**  
  デバイスをリセットする。

#### 6. ネットワーク設定
- **`set_ip_address(c, ip_address)`**  
  デバイスのIPアドレスを設定。
- **`get_ip_address(c)`**  
  デバイスの現在のIPアドレスを取得。
- **`set_subnet_mask(c, subnet_mask)`**  
  サブネットマスクを設定。
- **`get_subnet_mask(c)`**  
  サブネットマスクの取得。
- **`set_default_gateway(c, default_gateway)`**  
  デフォルトゲートウェイを設定。
- **`get_default_gateway(c)`**  
  デフォルトゲートウェイの取得。

## 使用方法

1. **サーバー起動**：
   ```bash
   python ons61797_server.py
   ```
   `__main__`ブロックで`util.runServer(__server__)`を呼び出し、サーバーを起動。

2. **LabRADクライアント**から各メソッドを呼び出し、デバイス制御が可能。

# 著作権及びライセンス
Copyright (c) 2024 NF Corporation  
Released under the MIT license  
https://opensource.org/licenses/mit-license.php
