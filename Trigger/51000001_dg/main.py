""" trigger/51000001_dg/main.xml """
from common import *
import state


class 대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[100]):
            add_buff(boxIds=[199], skillId=49179101, level=1, arg5=False)
            return 인트로()


class 인트로(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5000,5001,5002,5003], isVisible=False)
        set_cube(triggerIds=[5101,5102,5103,5104,5105], isVisible=False)
        set_cube(triggerIds=[5201,5202,5203,5204,5205,5206,5207,5208,5209], isVisible=False)
        set_cube(triggerIds=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311], isVisible=False)
        set_cube(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410,5411,5412,5413,5414], isVisible=False)
        set_cube(triggerIds=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512], isVisible=False)
        set_cube(triggerIds=[5601,5602,5603,5604,5605,5606,5607,5608,5609,5610,5611,5612,5613,5614,5615,5616,5617,5618,5619,5620,5621], isVisible=False)
        set_cube(triggerIds=[5701,5702,5703,5704,5705,5706,5707,5708,5709,5710,5711,5712,5713,5714,5715,5716,5717,5718,5719,5720,5721], isVisible=False)
        set_cube(triggerIds=[5801,5802,5803,5804,5805,5806,5807,5808,5809,5810,5811,5812,5813,5814,5815,5816,5817,5818,5819,5820,5821,5822], isVisible=False)
        set_cube(triggerIds=[5901,5902,5903,5904,5905,5906,5907,5908,5909,5910,5911,5912,5913,5914,5915], isVisible=False)
        set_cube(triggerIds=[51001,51002,51003,51004,51005,51006,51007,51008,51009,51010,51011,51012,51013,51014,51015,51016,51017,51018,51019,51020,51021,51022,51023,51024], isVisible=False)
        select_camera(triggerId=300, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3, script='$51000001_DG__MAIN__0$')
        set_skip(state=튜토리얼시작)

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 튜토리얼시작(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5000,5001,5002,5003], randomCount=4, isVisible=True)
        show_guide_summary(entityId=25100101, textId=25100101, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 튜토리얼02()
        if user_detected(boxIds=[101]):
            return 라운드카메라1()


class 튜토리얼02(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100102, textId=25100102, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 튜토리얼03()
        if user_detected(boxIds=[101]):
            return 라운드카메라1()


class 튜토리얼03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100103, textId=25100103, duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 튜토리얼04()
        if user_detected(boxIds=[101]):
            return 라운드카메라1()


class 튜토리얼04(state.State):
    def on_enter(self):
        show_guide_summary(entityId=25100104, textId=25100104, duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 튜토리얼시작()
        if user_detected(boxIds=[101]):
            return 라운드카메라1()


# 각 라운드별로 카메라 이동 시간 만큼 대기 시간을 가짐
class 라운드카메라1(state.State):
    def on_enter(self):
        select_camera(triggerId=301, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기1()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기1(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_start')
        set_achievement(triggerId=199, type='trigger', achieve='arcade_startcheck')
        hide_guide_summary(entityId=25100101)
        hide_guide_summary(entityId=25100102)
        hide_guide_summary(entityId=25100103)
        hide_guide_summary(entityId=25100104) # randomCount : 웨폰 오브젝트를 몇 개나 배치할지 결정
        set_cube(triggerIds=[5101,5102,5103,5104,5105], randomCount=3, isVisible=True) # lifeCount : 최대 사망 횟수
        arcade_spring_farm(type='StartGame', lifeCount=3) # SetInteractScore : 반응 오브젝트를 반응했을 때 score
        arcade_spring_farm(type='SetInteractScore', id=19000022, score=50)
        arcade_spring_farm(type='SetInteractScore', id=11000013, score=10000)
        arcade_spring_farm(type='SetInteractScore', id=11000014, score=10000)
        arcade_spring_farm(type='SetInteractScore', id=11000015, score=10000)
        arcade_spring_farm(type='SetInteractScore', id=11000016, score=10000)
        arcade_spring_farm(type='SetInteractScore', id=11000017, score=10000) # SpawnMonster : 웨폰 오브젝트로 몬스터를 공격시 획득하는 score
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1001,1002,1003], score=5000) # uiDuration : 라운드 UI 노출 시간
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=1, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_timer(timerId='100001', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        set_event_ui(type=0, arg2='1,5,1', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작1()


class 라운드시작1(state.State):
    def on_tick(self) -> state.State:
        if time_expired(timerId='100001'):
            return 종료()
        if monster_dead(boxIds=[1001,1002,1003]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료1()


class 라운드종료1(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_1round')
        arcade_spring_farm(type='ClearRound', round=1)
        reset_timer(timerId='100001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=2, boxId=101)
            return 라운드유저위치2()


class 라운드유저위치2(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=2, boxId=101)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[102]):
            return 라운드카메라2()


class 라운드카메라2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=302, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기2()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기2(state.State):
    def on_enter(self):
        set_timer(timerId='100002', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        set_cube(triggerIds=[5201,5202,5203,5204,5205,5206,5207,5208,5209], randomCount=5, isVisible=True)
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1101,1102,1103,1104], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=2, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='2,5,1', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작2()


class 라운드시작2(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100002'):
            return 종료()
        if monster_dead(boxIds=[1101,1102,1103,1104]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료2()


class 라운드종료2(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_2round')
        arcade_spring_farm(type='ClearRound', round=2)
        reset_timer(timerId='100002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=3, boxId=102)
            return 라운드유저위치3()


class 라운드유저위치3(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=3, boxId=102)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[103]):
            return 라운드카메라3()


class 라운드카메라3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=303, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기3()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기3(state.State):
    def on_enter(self):
        set_timer(timerId='100003', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        set_cube(triggerIds=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311], randomCount=6, isVisible=True)
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1201,1202,1203,1204,1205,1206,1207], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=3, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='3,5,1', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작3()


class 라운드시작3(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100003'):
            return 종료()
        if monster_dead(boxIds=[1201,1202,1203,1204,1205,1206,1207]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료3()


class 라운드종료3(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_3round')
        arcade_spring_farm(type='ClearRound', round=3)
        reset_timer(timerId='100003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=4, boxId=103)
            return 라운드유저위치4()


class 라운드유저위치4(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=4, boxId=103)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[104]):
            return 라운드카메라4()


class 라운드카메라4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=304, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기4()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기4(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410,5411,5412,5413,5414], randomCount=7, isVisible=True)
        set_timer(timerId='100004', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1301,1302,1303,1304,1305,1306,1307,1308], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=4, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='4,5,1', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작4()


class 라운드시작4(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100004'):
            return 종료()
        if monster_dead(boxIds=[1301,1302,1303,1304,1305,1306,1307,1308]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료4()


class 라운드종료4(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_4round')
        arcade_spring_farm(type='ClearRound', round=4)
        reset_timer(timerId='100004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=5, boxId=104)
            return 라운드유저위치5()


class 라운드유저위치5(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=5, boxId=104)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[105]):
            return 라운드카메라5()


class 라운드카메라5(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=305, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기5()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기5(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512], randomCount=6, isVisible=True)
        set_timer(timerId='100005', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1401,1402,1403,1404,1405], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=5, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='5,5,1', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작5()


class 라운드시작5(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100005'):
            return 종료()
        if monster_dead(boxIds=[1401,1402,1403,1404,1405]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료5()


class 라운드종료5(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_5round')
        arcade_spring_farm(type='ClearRound', round=5)
        reset_timer(timerId='100005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=6, boxId=105)
            return 라운드유저위치6()


class 라운드유저위치6(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=6, boxId=105)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[106]):
            return 라운드카메라6()


class 라운드카메라6(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=306, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기6()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기6(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5601,5602,5603,5604,5605,5606,5607,5608,5609,5610,5611,5612,5613,5614,5615,5616,5617,5618,5619,5620,5621], randomCount=10, isVisible=True)
        set_timer(timerId='100006', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=6, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='6,10,6', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작6()


class 라운드시작6(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100006'):
            return 종료()
        if monster_dead(boxIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료6()


class 라운드종료6(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_6round')
        arcade_spring_farm(type='ClearRound', round=6)
        reset_timer(timerId='100006')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=7, boxId=106)
            return 라운드유저위치7()


class 라운드유저위치7(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=7, boxId=106)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[107]):
            return 라운드카메라7()


class 라운드카메라7(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=307, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기7()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기7(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5701,5702,5703,5704,5705,5706,5707,5708,5709,5710,5711,5712,5713,5714,5715,5716,5717,5718,5719,5720,5721], randomCount=12, isVisible=True)
        set_timer(timerId='100007', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=7, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='7,10,6', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작7()


class 라운드시작7(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100007'):
            return 종료()
        if monster_dead(boxIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료7()


class 라운드종료7(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_7round')
        reset_timer(timerId='100007')
        arcade_spring_farm(type='ClearRound', round=7)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=8, boxId=107)
            return 라운드유저위치8()


class 라운드유저위치8(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=8, boxId=107)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[108]):
            return 라운드카메라8()


class 라운드카메라8(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=308, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기8()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기8(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5801,5802,5803,5804,5805,5806,5807,5808,5809,5810,5811,5812,5813,5814,5815,5816,5817,5818,5819,5820,5821,5822], randomCount=12, isVisible=True)
        set_timer(timerId='100008', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=8, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='8,10,6', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작8()


class 라운드시작8(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100008'):
            return 종료()
        if monster_dead(boxIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료8()


class 라운드종료8(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_8round')
        arcade_spring_farm(type='ClearRound', round=8)
        reset_timer(timerId='100008')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=9, boxId=108)
            return 라운드유저위치9()


class 라운드유저위치9(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=9, boxId=108)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[109]):
            return 라운드카메라9()


class 라운드카메라9(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=309, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기9()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기9(state.State):
    def on_enter(self):
        set_cube(triggerIds=[5901,5902,5903,5904,5905,5906,5907,5908,5909,5910,5911,5912,5913,5914,5915], randomCount=8, isVisible=True)
        set_timer(timerId='100009', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=9, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='9,10,6', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작9()


class 라운드시작9(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100009'):
            return 종료()
        if monster_dead(boxIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료9()


class 라운드종료9(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_9round')
        arcade_spring_farm(type='ClearRound', round=9)
        reset_timer(timerId='100009')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=10, boxId=109)
            return 라운드유저위치10()


class 라운드유저위치10(state.State):
    def on_enter(self):
        move_user(mapId=51000001, portalId=10, boxId=109)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[110]):
            return 라운드카메라10()


class 라운드카메라10(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=310, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 라운드대기10()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class 라운드대기10(state.State):
    def on_enter(self):
        set_cube(triggerIds=[51001,51002,51003,51004,51005,51006,51007,51008,51009,51010,51011,51012,51013,51014,51015,51016,51017,51018,51019,51020,51021,51022,51023,51024], randomCount=6, isVisible=True)
        set_timer(timerId='100010', seconds=120, clearAtZero=True, display=True, arg5=-30, arg6='TR')
        arcade_spring_farm(type='SpawnMonster', spawnIds=[2001], score=10000)
        arcade_spring_farm(type='SpawnMonster', spawnIds=[2002,2003,2004,2005], score=5000)
        arcade_spring_farm(type='StartRound', uiDuration=3000, round=10, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        set_event_ui(type=0, arg2='10,10,6', arg4='120')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 라운드시작10()


class 라운드시작10(state.State):
    def on_enter(self):
        remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> state.State:
        if time_expired(timerId='100010'):
            return 종료()
        if monster_dead(boxIds=[2001,2002,2003,2004,2005]):
            add_buff(boxIds=[199], skillId=70000091, level=1, arg5=False)
            return 라운드종료10()


class 라운드종료10(state.State):
    def on_enter(self):
        set_achievement(triggerId=199, type='trigger', achieve='springfarm_clear')
        arcade_spring_farm(type='ClearRound', round=10)
        reset_timer(timerId='100010')
        set_event_ui(type=7, arg3='2000', arg4='0')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            move_user(mapId=51000001, portalId=44, boxId=110)
            return 종료()


class 종료(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Ending_Popup_01')
        arcade_spring_farm(type='EndGame')
        move_user(mapId=51000001, portalId=44, boxId=110)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 진짜끝()


class 진짜끝(state.State):
    pass


