#
# データ取得スレッド
#


# ================================= パスの取得 ================================ #
import os

path = os.getcwd().rsplit('\\', 1)[0]
server_address = '192.168.2.111'
port_num = {'1': {'presenter': 5001,
                'audience': 50001},
            '2': {'presenter': 5002,
                'audience': 50002},
            '3': {'presenter': 5003,
                'audience': 50003}}

# ============================ 変数宣言部 ============================== #
# 分析用データのラベル
process_columns = ['window_ID', 'timeStamp',
                   'acc_X', 'acc_Y', 'acc_Z',
                   'gyro_X', 'gyro_Y', 'gyro_Z']

analysis_columns = ['window_ID', 'timeStamp',
                    'acc_X', 'acc_Y', 'acc_Z',
                    'gyro_X', 'gyro_Y', 'gyro_Z',
                    'acc_xyz']

axis_columns = ['acc_X', 'acc_Y', 'acc_Z',
                'gyro_X', 'gyro_Y', 'gyro_Z',
                'acc_xyz']
acc_columns = ['acc_X', 'acc_Y', 'acc_Z', 'acc_xyz']
gyro_columns = ['gyro_X', 'gyro_Y', 'gyro_Z']


# 表情の文字列を記号に変換
def face_symbol(pred_face):
    face_dict = {
        'neutral': 'a',
        'happy': 'b',
        'surprise': 'c',
        'sad': 'd',
        'angry': 'e',
        'fear': 'f',
        'disgust': 'g',
        'null': 'z'
    }
    return face_dict[pred_face]


# ============================ ウィンドウ単位の処理用定数 ============================== #
T = 100  # サンプリング周期 [Hz]
N = 32  # ウィンドウサイズ(0.32秒)
OVERLAP = 50  # オーバーラップ率 [%]
threshold = 0.3  # ウィンドウラベル閾値

# ============================ 精度検証用定数 ============================== #
FOLD = 10  # 交差検証数

# ランダムフォレストパラメータ
max_depth = 30
n_estimators = 30
random_state = 42
