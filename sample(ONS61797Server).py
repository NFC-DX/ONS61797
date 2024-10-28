"""
Copyright (c) 2024 NF Corporation

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of 
the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS 
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN 
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import time
import labrad


def main():
    try:
        cxn = labrad.connect(username="", password="pass")

        # 1. ONS61797オブジェクトを初期化
        # 1.1 USBを使用する場合
        port = "COM3"  # 適切なポート番号に置き換えてください
        instrument = cxn.ons61797_server
        instrument.connect(port, "")  # シリアルポートを指定してデバイスに接続

        # 1.2 LANを使用する場合
        # ip_address = "192.168.1.3"  # 適切なIPアドレスに置き換えてください
        # instrument = cxn.ons61797_server
        # instrument.connect("", ip_address)  # IPアドレスを指定してデバイスに接続

        # 2. デバイス情報の取得
        # デバイスに固有のIDなどを取得し、接続確認を行う
        device_info = instrument.get_device_information()
        print(f"Device Information: {device_info}")
        ip_address = instrument.get_ip_address()
        print(f"IP Address: {ip_address}")
        default_gateway = instrument.get_default_gateway()
        print(f"Default Gateway: {default_gateway}")
        subnet_mask = instrument.get_subnet_mask()
        print(f"Subnet Mask: {subnet_mask}")

        # 3. 出力チャンネル1をオンにして電圧を設定
        # チャンネル1をオンにし、5.0Vを設定
        channel = 1
        voltage = 5
        instrument.on(channel)
        print(f"Channel {channel} is now ON.")
        instrument.set_voltage(channel, voltage)
        print(f"Channel {channel} Voltage Set to {voltage} V")

        # 4. 電圧の確認
        # 現在のチャンネル1の電圧を確認
        current_voltage = instrument.get_voltage(channel)
        print(f"Current Voltage of Channel 1: {current_voltage} V")

        # 5. 出力状態の確認
        # チャンネル1がオンかオフかを確認
        output_state = instrument.get_output_state(channel)
        state_str = "ON" if output_state == 1 else "OFF"
        print(f"Channel {channel} is currently {state_str}.")

        # 6. 少し待機してから、チャンネル1をオフにする
        time.sleep(5)
        instrument.off(channel)
        print(f"Channel {channel} is now OFF.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # 7. 接続を閉じる
        # プログラム終了前に必ずシリアル接続を閉じる
        instrument.close()
        print("Connection closed.")


if __name__ == "__main__":
    main()
