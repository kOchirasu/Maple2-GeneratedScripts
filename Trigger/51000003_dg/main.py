""" trigger/51000003_dg/main.xml """
from common import *
import state


#  여기서 부터 시작 
class Idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7999], visible=False) # 카메라 사운드
        set_portal(portalId=8, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[6001,6002,6003,6004,6005,6006,6007,6008,6009,6010,6011,6012,6013,6014,6015,6016,6017,6018,6019,6020,6021,6022,6023,6024,6025,6026,6027,6028,6029,6030,6031,6032,6033,6034,6035,6036,6037,6038,6039,6040,6041,6042,6043,6044,6045,6046,6047,6048,6049,6050,6051,6052,6053,6054,6055,6056,6057,6058,6059,6060,6061,6062,6063,6064,6065,6066,6067,6068,6069,6070,6071,6072,6073,6074,6075,6076,6077,6078,6079,6080,6081,6082,6083,6084,6085,6086,6087,6088,6089,6090,6091,6092,6093,6094,6095,6096,6097,6098,6099,6100], visible=False, arg3=0, arg4=0, arg5=0) # 일반 존 투명 블록
        set_mesh(triggerIds=[6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211,6212,6213,6214,6215,6216,6217,6218,6219,6220,6221,6222,6223,6224,6225,6226,6227,6228,6229,6230,6231,6232,6233,6234,6235,6236,6237,6238,6239,6240,6241,6242,6243,6244,6245,6246,6247,6248,6249,6250,6251,6252,6253,6254,6255,6256,6257,6258,6259,6260,6261,6262,6263,6264,6265,6266,6267,6268,6269,6270,6271,6272,6273,6274,6275,6276,6277,6278,6279,6280,6281,6282,6283,6284,6285,6286,6287,6288,6289,6290,6291,6292,6293,6294,6295,6296,6297,6298,6299,6300], visible=False, arg3=0, arg4=0, arg5=0) # 히든 존 투명 블록

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return Tutorial()

    def on_exit(self):
        create_monster(spawnIds=[501,502,503,504,505,506,507,508,509], arg2=True, arg3=0)


class Tutorial(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7998], visible=True) # 컷신 사운드 AMB
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[8100,8101,8104,8106,8103,8105,8107,8108], returnView=False) # 카메라 뒤로 당김

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return Tutorial_01()


class Tutorial_01(state.State):
    def on_enter(self):
        set_skip(state=Tutorial_02)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9500):
            return Tutorial_02()


class Tutorial_02(state.State):
    def on_enter(self):
        move_user(mapId=51000003, portalId=1, boxId=701)
        set_effect(triggerIds=[7998], visible=False) # 컷신 사운드 AMB OFF
        select_camera_path(pathIds=[8005,8001,8002], returnView=False) # 카메라 뒤로 당김
        set_user_value(triggerId=991109, key='Tutorial', value=0) # 튜토리얼 동안 무적 버프
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7) # 라이프 카운트 정의
        arcade_boom_boom_ocean(type='StartGame', lifeCount=20)
        show_count_ui(text='$51000003_DG__MAIN__0$', stage=0, count=5)
        set_user_value(triggerId=991103, key='Fail', value=1) # Fail Event on
        add_buff(boxIds=[701], skillId=70000087, level=1, arg5=False) # 아케이드 포커스

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return Start()

    def on_exit(self):
        destroy_monster(spawnIds=[501,502,503,504,505,506,507,508,509])


class Start(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Monkey_01') # [02100226] System_Monkey_01 ~ 06 (원숭이 간헐적으로 우키키, 우카카)
        set_achievement(triggerId=701, type='trigger', achieve='boomocean_start') # 붐붐오션 시작하기 (트로피)
        set_achievement(triggerId=701, type='trigger', achieve='arcade_startcheck') # 아케이드 참여 일괄 체크용
        set_mesh(triggerIds=[6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,6112,6113,6114,6115,6116,6117,6118,6119,6120,6121,6122,6123,6124,6125,6126,6127,6128,6129,6130,6131,6132,6133,6134,6135,6136,6137,6138,6139,6140,6141,6142,6143,6144,6145,6146,6147,6148,6149,6150,6151,6152,6153,6154,6155,6156,6157,6158,6159,6160,6161,6162,6163,6164,6165,6166,6167,6168,6169,6170,6171,6172,6173,6174,6175,6176,6177,6178,6179,6180,6181,6182,6183,6184,6185,6186,6187,6188,6189,6190,6191,6192,6193,6194,6195,6196,6197,6198,6199,6200], visible=False, arg3=0, arg4=0, arg5=0) # 벽 설정
        remove_buff(boxId=49179004, skillId=0) # 발사체 피격 감점 점수 정의
        arcade_boom_boom_ocean(type='SetSkillScore', id=49210001, score=-500) # 일반 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49210011, score=-500) # 일반 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49210021, score=-500) # 일반 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49210031, score=-500) # 일반 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49200021, score=-500) # 파도 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49200001, score=-500) # 튜브 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49190012, score=-500) # 대포 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=49190022, score=-500) # 대포 발사체
        arcade_boom_boom_ocean(type='SetSkillScore', id=70000080, score=1000)
        arcade_boom_boom_ocean(type='SetSkillScore', id=70000081, score=1000)
        arcade_boom_boom_ocean(type='SetSkillScore', id=70000082, score=1000)
        arcade_boom_boom_ocean(type='SetSkillScore', id=70000083, score=1000)
        arcade_boom_boom_ocean(type='SetSkillScore', id=70000085, score=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Step_01()


class Step_01(state.State):
    def on_enter(self):
        set_user_value(triggerId=991107, key='Round_01', value=1) # normal LV1
        arcade_boom_boom_ocean(type='StartRound', round=1, roundDuration=1500, timeScoreRate=1033) # 20초
        play_system_sound_in_box(sound='System_Fruit_Throw_Loop_01') # [02100216] System_Fruit_Throw_Loop_01 (과일 날라 다니는 효과음, 루핑)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_02()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_02(state.State):
    def on_enter(self):
        set_user_value(triggerId=991107, key='Round_02', value=1) # normal LV2
        arcade_boom_boom_ocean(type='ClearRound', round=1)
        arcade_boom_boom_ocean(type='StartRound', round=2, roundDuration=20000, timeScoreRate=1033)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_03()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_03(state.State):
    def on_enter(self):
        set_user_value(triggerId=991111, key='Round_01', value=1) # item_01
        set_user_value(triggerId=991107, key='Round_03', value=1) # normal LV3
        arcade_boom_boom_ocean(type='ClearRound', round=2)
        arcade_boom_boom_ocean(type='StartRound', round=3, roundDuration=20000, timeScoreRate=1033)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_04()
        if count_users(boxId=705, boxId=1):
            return End()

    def on_exit(self):
        set_achievement(triggerId=701, type='trigger', achieve='boomocean_1min') # 붐붐오션 1분 버티기 트로피


class Step_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8002,8003], returnView=False) # 카메라 뒤로 당김
        set_effect(triggerIds=[7999], visible=True) # 카메라 사운드
        set_user_value(triggerId=991120, key='Round_01', value=1) # wave3 LV1
        set_user_value(triggerId=991107, key='Round_04', value=1) # normal LV4
        arcade_boom_boom_ocean(type='ClearRound', round=3)
        arcade_boom_boom_ocean(type='StartRound', round=4, roundDuration=20000, timeScoreRate=1550)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_05()
        if count_users(boxId=705, boxId=1):
            return End()

    def on_exit(self):
        set_effect(triggerIds=[7999], visible=False) # 카메라 사운드


class Step_05(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=4)
        arcade_boom_boom_ocean(type='StartRound', round=5, roundDuration=20000, timeScoreRate=1550)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="5,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991104, key='Round_01', value=1) # wave LV1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_06()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_06(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=5)
        arcade_boom_boom_ocean(type='StartRound', round=6, roundDuration=20000, timeScoreRate=1550)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="6,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_07()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_07(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=6)
        arcade_boom_boom_ocean(type='StartRound', round=7, roundDuration=20000, timeScoreRate=2067)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="7,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991105, key='Round_00', value=1) # wave2 LV0
        set_user_value(triggerId=991102, key='Treasure_box', value=1) # 보물상자 스폰 스위치 ON

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_08()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_08(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=7)
        arcade_boom_boom_ocean(type='StartRound', round=8, roundDuration=20000, timeScoreRate=2067)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="8,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991121, key='Round_01', value=1) # wave4 LV1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_09()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_09(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=8)
        arcade_boom_boom_ocean(type='StartRound', round=9, roundDuration=20000, timeScoreRate=2067)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="9,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991122, key='Round_01', value=1) # wave5 LV1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_10()
        if count_users(boxId=705, boxId=1):
            return End()

    def on_exit(self):
        set_achievement(triggerId=701, type='trigger', achieve='boomocean_3min') # 붐붐오션 3분 버티기 트로피


class Step_10(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=9)
        arcade_boom_boom_ocean(type='StartRound', round=10, roundDuration=20000, timeScoreRate=2583)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="10,25" arg3="0" arg4="0" />
        set_effect(triggerIds=[7999], visible=True) # 카메라 사운드
        select_camera_path(pathIds=[8003,8004], returnView=False) # 카메라 뒤로 당김
        set_user_value(triggerId=991106, key='Round_01', value=1) # cannon LV 1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_11()


class Step_11(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=10)
        arcade_boom_boom_ocean(type='StartRound', round=11, roundDuration=20000, timeScoreRate=2583)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="11,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991106, key='Round_02', value=1) # cannon LV 2

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_12()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_12(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=11)
        arcade_boom_boom_ocean(type='StartRound', round=12, roundDuration=20000, timeScoreRate=2583)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="12,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991106, key='Round_03', value=1) # cannon LV 3

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_13()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_13(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=12)
        arcade_boom_boom_ocean(type='StartRound', round=13, roundDuration=20000, timeScoreRate=3100)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="13,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991106, key='Round_04', value=1) # cannon LV 4
        set_user_value(triggerId=991105, key='Round_01', value=1) # wave2 LV1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_14()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_14(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=13)
        arcade_boom_boom_ocean(type='StartRound', round=14, roundDuration=20000, timeScoreRate=3100)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="14,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991123, key='Round_01', value=1) # normal2 LV1
        set_user_value(triggerId=991108, key='Round_03', value=1) # fog

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_15()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_15(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=14)
        arcade_boom_boom_ocean(type='StartRound', round=15, roundDuration=20000, timeScoreRate=3100)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="15,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_16()
        if count_users(boxId=705, boxId=1):
            return End()

    def on_exit(self):
        set_achievement(triggerId=701, type='trigger', achieve='boomocean_5min') # 붐붐오션 5분 버티기 트로피


class Step_16(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=15)
        arcade_boom_boom_ocean(type='StartRound', round=16, roundDuration=20000, timeScoreRate=1350)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="16,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991123, key='Round_02', value=1) # normal2 LV2
        set_user_value(triggerId=991105, key='Round_02', value=1) # wave2 LV2

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_17()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_17(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=16)
        arcade_boom_boom_ocean(type='StartRound', round=17, roundDuration=20000, timeScoreRate=1350)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="17,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991106, key='Round_05', value=1) # cannon LV 5

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_18()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_18(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=17)
        arcade_boom_boom_ocean(type='StartRound', round=18, roundDuration=20000, timeScoreRate=1350)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="18,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991123, key='Round_03', value=1) # normal2 LV3
        set_user_value(triggerId=991122, key='Round_02', value=1) # wave5 LV1

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_19()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_19(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=18)
        arcade_boom_boom_ocean(type='StartRound', round=19, roundDuration=20000, timeScoreRate=1125)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="18,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991107, key='Round_06', value=1) # normal LV4

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_20()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_20(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=19)
        arcade_boom_boom_ocean(type='StartRound', round=20, roundDuration=20000, timeScoreRate=1125)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="20,25" arg3="0" arg4="0" />
        set_user_value(triggerId=991123, key='Round_04', value=1) # normal2 LV4

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_21()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_21(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=20)
        arcade_boom_boom_ocean(type='StartRound', round=21, roundDuration=20000, timeScoreRate=1125)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="21,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_22()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_22(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=21)
        arcade_boom_boom_ocean(type='StartRound', round=22, roundDuration=20000, timeScoreRate=900)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="22,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_23()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_23(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=22)
        arcade_boom_boom_ocean(type='StartRound', round=23, roundDuration=20000, timeScoreRate=900)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="23,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_24()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_24(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=23)
        arcade_boom_boom_ocean(type='StartRound', round=24, roundDuration=20000, timeScoreRate=900)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="24,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return Step_25()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_25(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='ClearRound', round=24)
        arcade_boom_boom_ocean(type='StartRound', round=25, roundDuration=20000, timeScoreRate=562)
        # <action name="이벤트UI를설정한다" arg1="0" arg2="25,25" arg3="0" arg4="0" />

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=120000):
            return Step_26()
        if count_users(boxId=705, boxId=1):
            return End()


class Step_26(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='EndGame')
        set_achievement(triggerId=701, type='trigger', achieve='boomocean_10min') # 붐붐오션 10분 버티기 트로피

    def on_tick(self) -> state.State:
        if count_users(boxId=705, boxId=1):
            return End()


class End(state.State):
    def on_enter(self):
        arcade_boom_boom_ocean(type='EndGame')


