""" trigger/02010052_bf/boss.xml """
from common import *
import state


class Idle(state.State):
    def on_enter(self):
        set_portal(portalId=4, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[6801,6802,6803,6804,6805,6806,6807,6808,6809,6810,6811,6812,6813,6814,6815,6816,6817,6818,6819,6820,6821,6822,6823,6824,6825,6826,6827,6828,6829,6830,6831,6832,6833,6834,6835,6836,6837,6838,6839,6840,6841,6842,6843,6844,6845,6846,6847,6848,6849,6850,6851,6852,6853,6854,6855,6856,6857,6858,6859,6860,6861,6862,6863,6864,6865,6866,6867,6868,6869,6870,6871,6872,6873,6874,6875,6876,6877,6878,6879,6880,6881,6882,6883,6884,6885,6886,6887,6888,6889,6890,6891,6892,6893,6894,6895,6896,6897,6898,6899,6900], visible=False, arg3=0, arg4=0, arg5=0) # 블록 없음
        set_effect(triggerIds=[7031], visible=False) # 횃불에 불이 붙는 이펙트
        set_effect(triggerIds=[7032], visible=False) # 횃불에 불이 붙는 이펙트
        set_effect(triggerIds=[7033], visible=False) # 횃불에 불이 붙는 이펙트
        set_effect(triggerIds=[7034], visible=False) # 횃불에 불이 붙는 이펙트
        set_effect(triggerIds=[7035], visible=False) # 횃불에 불이 붙는 이펙트
        set_effect(triggerIds=[7999], visible=False) # 인트로 사운드
        set_effect(triggerIds=[7910], visible=False) # 카나 텔레포트
        set_effect(triggerIds=[7911], visible=False) # 카나 텔레포트
        set_effect(triggerIds=[7912], visible=False) # 카나 텔레포트
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if count_users(boxId=750, boxId=1):
            return Echo()

    def on_exit(self):
        set_portal(portalId=5, visible=True, enabled=True, minimapVisible=True)


class Echo(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7800], visible=True) # 카나 메아리

    def on_tick(self) -> state.State:
        if count_users(boxId=720, boxId=1):
            return Boss_01()


class Boss_01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7531], visible=True) # 얼어붙는 소리
        set_mesh(triggerIds=[6801,6802,6803,6804,6805,6806,6807,6808,6809,6810], visible=True, arg3=80, arg4=70, arg5=8) # 얼음!
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_01b()


class Boss_01b(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7910], visible=True) # 카나 텔레포트
        create_monster(spawnIds=[995], arg2=False) # 카나 (995)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_01c()


class Boss_01c(state.State):
    def on_enter(self):
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        set_conversation(type=1, spawnId=995, script='$02010052_BF__BOSS__0$', arg4=3, arg5=0) # 카나 말풍선 대사
        create_monster(spawnIds=[120], arg2=False) # 화로 (107)
        create_monster(spawnIds=[621,622,623,624,625], arg2=True) # 몬스터 웨이브

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[120]):
            return burn_state_01()


class burn_state_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_effect(triggerIds=[7507], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6801,6802,6803,6804,6805,6806,6807,6808,6809,6810], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_mesh(triggerIds=[600003], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_effect(triggerIds=[7910], visible=True) # 카나 텔레포트
        destroy_monster(spawnIds=[995]) # 카나 사라짐 (995)
        set_event_ui(type=1, arg2='$02010052_BF__BOSS__1$', arg3='3000')
        set_effect(triggerIds=[7031], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_02_idle()


class Boss_02_idle(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=721, boxId=1):
            return Boss_02()


class Boss_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7532], visible=True) # 얼어붙는 소리
        set_mesh(triggerIds=[6821,6822,6823,6824,6825,6826,6827,6828,6829,6830], visible=True, arg3=80, arg4=70, arg5=8) # 얼음!
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_02b()


class Boss_02b(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7911], visible=True) # 카나 텔레포트
        create_monster(spawnIds=[996], arg2=False) # 카나 (995)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_02c()


class Boss_02c(state.State):
    def on_enter(self):
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        set_conversation(type=1, spawnId=996, script='$02010052_BF__BOSS__2$', arg4=3, arg5=0) # 카나 말풍선 대사
        create_monster(spawnIds=[121], arg2=False) # 화로 (107)
        create_monster(spawnIds=[631,632,633,634,635], arg2=True) # 몬스터 웨이브

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121]):
            return burn_state_02()


class burn_state_02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_effect(triggerIds=[7508], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6821,6822,6823,6824,6825,6826,6827,6828,6829,6830], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_mesh(triggerIds=[600004], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_effect(triggerIds=[7911], visible=True) # 카나 텔레포트
        destroy_monster(spawnIds=[996]) # 카나 사라짐 (995)
        set_event_ui(type=1, arg2='$02010052_BF__BOSS__3$', arg3='3000')
        set_effect(triggerIds=[7032], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_03_idle()


class Boss_03_idle(state.State):
    def on_tick(self) -> state.State:
        if count_users(boxId=722, boxId=1):
            return Boss_03()


class Boss_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7533], visible=True) # 얼어붙는 소리
        set_mesh(triggerIds=[6830,6831,6832,6833,6834,6835,6836,6837,6838,6839,6840], visible=True, arg3=80, arg4=70, arg5=8) # 얼음!
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_03b()


class Boss_03b(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7912], visible=True) # 카나 텔레포트
        create_monster(spawnIds=[997], arg2=False) # 카나 (995)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return Boss_03c()


class Boss_03c(state.State):
    def on_enter(self):
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요
        set_conversation(type=1, spawnId=997, script='$02010052_BF__BOSS__4$', arg4=3, arg5=0) # 카나 말풍선 대사
        create_monster(spawnIds=[641,642,643,644,645], arg2=True) # 몬스터 웨이브
        create_monster(spawnIds=[122], arg2=False) # 화로 (107)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[122]):
            return burn_state_03()


class burn_state_03(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_effect(triggerIds=[7509], visible=True) # 얼음 녹는 소리
        set_mesh(triggerIds=[6830,6831,6832,6833,6834,6835,6836,6837,6838,6839,6840], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_mesh(triggerIds=[600005], visible=False, arg3=800, arg4=100, arg5=0) # 벽 해제
        set_effect(triggerIds=[7912], visible=True) # 카나 텔레포트
        destroy_monster(spawnIds=[997]) # 카나 사라짐 (995)
        set_event_ui(type=1, arg2='$02010052_BF__BOSS__5$', arg3='3000')
        set_effect(triggerIds=[7033], visible=True) # 횃불에 불이 붙는 이펙트
        set_timer(timerId='1', seconds=1, display=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=724, boxId=1):
            return Boss_04_idle()
        """
        <condition name="시간이경과했으면" arg1="1">
        <transition state="Boss_04_idle"/> 
        </condition>
        """

    def on_exit(self):
        create_monster(spawnIds=[123,124], arg2=False) # 마지막 두 화로


class Boss_04_idle(state.State):
    def on_enter(self):
        show_guide_summary(entityId=200, textId=20105201) # 화로를 공격하여 불을 붙이세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[123]):
            return Boss_04_idle_A()
        if monster_dead(boxIds=[124]):
            return Boss_04_idle_B()


class Boss_04_idle_A(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7034], visible=True) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[124]):
            return burn_state_04()

    def on_exit(self):
        set_effect(triggerIds=[7035], visible=True) # 횃불에 불이 붙는 이펙트


class Boss_04_idle_B(state.State):
    def on_enter(self):
        set_effect(triggerIds=[7035], visible=True) # 횃불에 불이 붙는 이펙트

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[123]):
            return burn_state_04()

    def on_exit(self):
        set_effect(triggerIds=[7034], visible=True) # 횃불에 불이 붙는 이펙트


class burn_state_04(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=200)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[7999], visible=True) # 컷인 사운드
        set_conversation(type=2, spawnId=21800073, script='$02010052_BF__BOSS__6$', arg4=5) # 카나 대사
        # Missing State: Boss_Battle
        set_skip()
        set_mesh(triggerIds=[6201,6202,6203,6204,6205,6206,6207,6208,6209,6210,6211,6212,6213,6214,6215,6216,6217,6218,6219,6220,6221,6222,6223,6224,6225,6226,6227,6228,6229,6230,6231,6232,6233,6234,6235,6236,6237,6238,6239,6240,6241,6242,6243,6244,6245,6246,6247,6248,6249,6250,6251,6252,6253,6254,6255,6256,6257,6258,6259,6260,6261,6262,6263,6264,6265,6266,6267,6268,6269,6270,6271,6272,6273,6274,6275,6276,6277,6278,6279,6280,6281,6282,6283,6284,6285,6286,6287,6288,6289,6290,6291,6292,6293,6294,6295,6296,6297,6298,6299,6300,6301,6302,6303,6304,6305,6306,6307,6308,6309,6310,6311,6312,6313,6314,6315,6316,6317,6318,6319,6320,6321,6322,6323,6324,6325,6326,6327,6328,6329,6330,6331,6332,6333,6334,6335,6336,6337,6338,6339,6340,6341,6342,6343,6344,6345,6346,6347,6348,6349,6350,6351,6352,6353,6354,6355,6356,6357,6358,6359,6360,6361,6362,6363,6364,6365,6366,6367,6368,6369,6370,6371,6372,6373,6374,6375,6376,6377,6378,6379,6380,6381,6382,6383,6384,6385,6386,6387,6388,6389,6390,6391,6392,6393,6394,6395,6396,6397,6398,6399,6400,6401,6402,6403,6404,6405,6406,6407,6408,6409,6410,6411,6412,6413,6414,6415,6416,6417,6418,6419,6420,6421,6422,6423,6424,6425,6426,6427,6428,6429,6430,6431,6432,6433,6434,6435,6436,6437,6438,6439,6440,6441,6442,6443,6444,6445,6446,6447,6448,6449,6450,6451,6452,6453,6454,6455,6456,6457,6458,6459,6460,6461,6462,6463,6464,6465,6466,6467,6468,6469,6470,6471,6472,6473,6474,6475,6476,6477,6478,6479,6480,6481,6482,6483,6484,6485,6486,6487,6488,6489,6490,6491,6492,6493,6494,6495,6496,6497,6498,6499,6500,6501,6502,6503,6504,6505,6506,6507,6508,6509,6510,6511,6512,6513,6514,6515,6516,6517,6518,6519,6520,6521,6522,6523,6524,6525,6526,6527,6528,6529,6530,6531,6532,6533,6534,6535,6536,6537,6538,6539,6540,6541,6542,6543,6544,6545,6546,6547,6548,6549,6550,6551,6552,6553,6554,6555,6556,6557,6558,6559,6560,6561,6562,6563,6564,6565,6566,6567,6568,6569,6570,6571,6572,6573,6574,6575,6576,6577,6578,6579,6580,6581,6582,6583,6584,6585,6586,6587,6588,6589,6590,6591,6592,6593,6594,6595,6596,6597,6598,6599,6600,6601,6602,6603,6604,6605,6606,6607,6608,6609,6610,6611,6612,6613,6614,6615,6616,6617,6618,6619,6620,6621,6622,6623,6624,6625,6626,6627,6628,6629,6630,6631,6632,6633,6634,6635,6636,6637,6638,6639,6640,6641,6642,6643,6644,6645,6646,6647,6648,6649,6650,6651,6652,6653,6654,6655,6656,6657,6658,6659,6660,6661,6662,6663,6664,6665,6666,6667,6668,6669,6670,6671,6672,6673,6674,6675,6676,6677,6678,6679,6680,6681,6682,6683,6684,6685,6686,6687,6688,6689,6690,6691,6692,6693,6694,6695,6696,6697,6698,6699], visible=False, arg3=80, arg4=10, arg5=0) # 벽 해제
        select_camera_path(pathIds=[80004,80005], returnView=True) # 연출 카메라
        set_timer(timerId='6', seconds=6, ara3='1', display=False)
        create_monster(spawnIds=[998], arg2=False) # 기본 배치 될 몬스터 등장
        move_npc(spawnId=998, patrolName='MS2PatrolData_1008') # 카나의 분신 991 (이동)

    def on_tick(self) -> state.State:
        if time_expired(timerId='6'):
            return Boss_battle_01()

    def on_exit(self):
        set_mesh(triggerIds=[6890,6891,6892,6893,6894,6895], visible=True, arg3=50, arg4=70, arg5=0) # 벽 생성
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class Boss_battle_01(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6701,6702,6703,6704,6705,6706,6707,6708,6709,6710,6711,6712,6713,6714,6715,6716,6717,6718,6719,6720,6721,6722,6723,6724,6725,6726,6727,6728,6729,6730,6731,6732,6733,6734,6735,6736,6737,6738,6739,6740,6741,6742,6743,6744,6745,6746,6747,6748,6749,6750,6751,6752,6753,6754,6755,6756,6757,6758,6759,6760,6761,6762,6763,6764,6765,6766,6767,6768,6769,6770,6771,6772,6773,6774,6775,6776,6777,6778,6779,6780,6781,6782,6783,6784,6785,6786,6787,6788,6789,6790,6791,6792,6793,6794,6795,6796,6797,6798,6799], visible=False, arg3=80, arg4=50, arg5=0) # 벽 해제
        set_event_ui(type=1, arg2='$02010052_BF__BOSS__7$', arg3='3000')

    def on_tick(self) -> state.State:
        if count_users(boxId=723, boxId=1):
            return Boss_Spawn_01()


class Boss_Spawn_01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[998]) # 카나 사라짐 (998)
        create_monster(spawnIds=[999], arg2=False) # 보스 카나 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[999]):
            return Clear_01()


class Clear_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=80006, enable=True)
        create_monster(spawnIds=[9998], arg2=False) # 카나 등장
        set_effect(triggerIds=[7998], visible=True) # 텔레포트
        move_npc(spawnId=9998, patrolName='MS2PatrolData_1009') # 카나의 분신 991 (이동)
        set_conversation(type=2, spawnId=21800073, script='$02010052_BF__BOSS__8$', arg4=4) # 카나 대사
        set_timer(timerId='5', seconds=5, ara3='1', display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='5'):
            return Clear()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)
        set_effect(triggerIds=[7998], visible=True) # 텔레포트
        destroy_monster(spawnIds=[9998]) # 카나 사라짐 (998)
        select_camera(triggerId=80006, enable=False)


class Clear(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return end()


class end(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[6890,6891,6892,6893,6894,6895], visible=False, arg3=80, arg4=10, arg5=0) # 벽 해제
        set_portal(portalId=4, visible=True, enabled=True, minimapVisible=True)
        dungeon_clear()


