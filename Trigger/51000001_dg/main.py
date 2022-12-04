""" trigger/51000001_dg/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[100]):
            self.add_buff(boxIds=[199], skillId=49179101, level=1, isSkillSet=False)
            return 인트로(self.ctx)


class 인트로(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5000,5001,5002,5003], isVisible=False)
        self.set_cube(triggerIds=[5101,5102,5103,5104,5105], isVisible=False)
        self.set_cube(triggerIds=[5201,5202,5203,5204,5205,5206,5207,5208,5209], isVisible=False)
        self.set_cube(triggerIds=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311], isVisible=False)
        self.set_cube(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410,5411,5412,5413,5414], isVisible=False)
        self.set_cube(triggerIds=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512], isVisible=False)
        self.set_cube(triggerIds=[5601,5602,5603,5604,5605,5606,5607,5608,5609,5610,5611,5612,5613,5614,5615,5616,5617,5618,5619,5620,5621], isVisible=False)
        self.set_cube(triggerIds=[5701,5702,5703,5704,5705,5706,5707,5708,5709,5710,5711,5712,5713,5714,5715,5716,5717,5718,5719,5720,5721], isVisible=False)
        self.set_cube(triggerIds=[5801,5802,5803,5804,5805,5806,5807,5808,5809,5810,5811,5812,5813,5814,5815,5816,5817,5818,5819,5820,5821,5822], isVisible=False)
        self.set_cube(triggerIds=[5901,5902,5903,5904,5905,5906,5907,5908,5909,5910,5911,5912,5913,5914,5915], isVisible=False)
        self.set_cube(triggerIds=[51001,51002,51003,51004,51005,51006,51007,51008,51009,51010,51011,51012,51013,51014,51015,51016,51017,51018,51019,51020,51021,51022,51023,51024], isVisible=False)
        self.select_camera(triggerId=300, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3, script='$51000001_DG__MAIN__0$')
        self.set_skip(state=튜토리얼시작)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 튜토리얼시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5000,5001,5002,5003], randomCount=4, isVisible=True)
        self.show_guide_summary(entityId=25100101, textId=25100101, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 튜토리얼02(self.ctx)
        if self.user_detected(boxIds=[101]):
            return 라운드카메라1(self.ctx)


class 튜토리얼02(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100102, textId=25100102, duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 튜토리얼03(self.ctx)
        if self.user_detected(boxIds=[101]):
            return 라운드카메라1(self.ctx)


class 튜토리얼03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100103, textId=25100103, duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 튜토리얼04(self.ctx)
        if self.user_detected(boxIds=[101]):
            return 라운드카메라1(self.ctx)


class 튜토리얼04(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=25100104, textId=25100104, duration=2500)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 튜토리얼시작(self.ctx)
        if self.user_detected(boxIds=[101]):
            return 라운드카메라1(self.ctx)


# 각 라운드별로 카메라 이동 시간 만큼 대기 시간을 가짐
class 라운드카메라1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기1(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기1(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_start')
        self.set_achievement(triggerId=199, type='trigger', achieve='arcade_startcheck')
        self.hide_guide_summary(entityId=25100101)
        self.hide_guide_summary(entityId=25100102)
        self.hide_guide_summary(entityId=25100103)
        self.hide_guide_summary(entityId=25100104) # randomCount : 웨폰 오브젝트를 몇 개나 배치할지 결정
        self.set_cube(triggerIds=[5101,5102,5103,5104,5105], randomCount=3, isVisible=True) # lifeCount : 최대 사망 횟수
        self.arcade_spring_farm(type='StartGame', lifeCount=3) # SetInteractScore : 반응 오브젝트를 반응했을 때 score
        self.arcade_spring_farm(type='SetInteractScore', id=19000022, score=50)
        self.arcade_spring_farm(type='SetInteractScore', id=11000013, score=10000)
        self.arcade_spring_farm(type='SetInteractScore', id=11000014, score=10000)
        self.arcade_spring_farm(type='SetInteractScore', id=11000015, score=10000)
        self.arcade_spring_farm(type='SetInteractScore', id=11000016, score=10000)
        self.arcade_spring_farm(type='SetInteractScore', id=11000017, score=10000) # SpawnMonster : 웨폰 오브젝트로 몬스터를 공격시 획득하는 score
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1001,1002,1003], score=5000) # uiDuration : 라운드 UI 노출 시간
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=1, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_timer(timerId='100001', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.set_event_ui(type=0, arg2='1,5,1', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작1(self.ctx)


class 라운드시작1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100001'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1001,1002,1003]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료1(self.ctx)


class 라운드종료1(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_1round')
        self.arcade_spring_farm(type='ClearRound', round=1)
        self.reset_timer(timerId='100001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=2, boxId=101)
            return 라운드유저위치2(self.ctx)


class 라운드유저위치2(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=2, boxId=101)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[102]):
            return 라운드카메라2(self.ctx)


class 라운드카메라2(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=302, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기2(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='100002', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.set_cube(triggerIds=[5201,5202,5203,5204,5205,5206,5207,5208,5209], randomCount=5, isVisible=True)
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1101,1102,1103,1104], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=2, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='2,5,1', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작2(self.ctx)


class 라운드시작2(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100002'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1101,1102,1103,1104]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료2(self.ctx)


class 라운드종료2(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_2round')
        self.arcade_spring_farm(type='ClearRound', round=2)
        self.reset_timer(timerId='100002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=3, boxId=102)
            return 라운드유저위치3(self.ctx)


class 라운드유저위치3(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=3, boxId=102)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[103]):
            return 라운드카메라3(self.ctx)


class 라운드카메라3(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=303, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기3(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기3(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='100003', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.set_cube(triggerIds=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311], randomCount=6, isVisible=True)
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1201,1202,1203,1204,1205,1206,1207], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=3, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='3,5,1', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작3(self.ctx)


class 라운드시작3(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100003'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1201,1202,1203,1204,1205,1206,1207]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료3(self.ctx)


class 라운드종료3(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_3round')
        self.arcade_spring_farm(type='ClearRound', round=3)
        self.reset_timer(timerId='100003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=4, boxId=103)
            return 라운드유저위치4(self.ctx)


class 라운드유저위치4(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=4, boxId=103)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[104]):
            return 라운드카메라4(self.ctx)


class 라운드카메라4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=304, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기4(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기4(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410,5411,5412,5413,5414], randomCount=7, isVisible=True)
        self.set_timer(timerId='100004', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1301,1302,1303,1304,1305,1306,1307,1308], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=4, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='4,5,1', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작4(self.ctx)


class 라운드시작4(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100004'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1301,1302,1303,1304,1305,1306,1307,1308]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료4(self.ctx)


class 라운드종료4(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_4round')
        self.arcade_spring_farm(type='ClearRound', round=4)
        self.reset_timer(timerId='100004')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=5, boxId=104)
            return 라운드유저위치5(self.ctx)


class 라운드유저위치5(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=5, boxId=104)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[105]):
            return 라운드카메라5(self.ctx)


class 라운드카메라5(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=305, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기5(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기5(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512], randomCount=6, isVisible=True)
        self.set_timer(timerId='100005', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1401,1402,1403,1404,1405], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=5, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='5,5,1', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작5(self.ctx)


class 라운드시작5(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100005'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1401,1402,1403,1404,1405]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료5(self.ctx)


class 라운드종료5(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_5round')
        self.arcade_spring_farm(type='ClearRound', round=5)
        self.reset_timer(timerId='100005')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=6, boxId=105)
            return 라운드유저위치6(self.ctx)


class 라운드유저위치6(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=6, boxId=105)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[106]):
            return 라운드카메라6(self.ctx)


class 라운드카메라6(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=306, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기6(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기6(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5601,5602,5603,5604,5605,5606,5607,5608,5609,5610,5611,5612,5613,5614,5615,5616,5617,5618,5619,5620,5621], randomCount=10, isVisible=True)
        self.set_timer(timerId='100006', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=6, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='6,10,6', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작6(self.ctx)


class 라운드시작6(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100006'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1501,1502,1503,1504,1505,1506,1507,1508,1509,1510]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료6(self.ctx)


class 라운드종료6(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_6round')
        self.arcade_spring_farm(type='ClearRound', round=6)
        self.reset_timer(timerId='100006')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=7, boxId=106)
            return 라운드유저위치7(self.ctx)


class 라운드유저위치7(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=7, boxId=106)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[107]):
            return 라운드카메라7(self.ctx)


class 라운드카메라7(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=307, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기7(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기7(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5701,5702,5703,5704,5705,5706,5707,5708,5709,5710,5711,5712,5713,5714,5715,5716,5717,5718,5719,5720,5721], randomCount=12, isVisible=True)
        self.set_timer(timerId='100007', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=7, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='7,10,6', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작7(self.ctx)


class 라운드시작7(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100007'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1601,1602,1603,1604,1605,1606,1607,1608,1609,1610]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료7(self.ctx)


class 라운드종료7(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_7round')
        self.reset_timer(timerId='100007')
        self.arcade_spring_farm(type='ClearRound', round=7)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=8, boxId=107)
            return 라운드유저위치8(self.ctx)


class 라운드유저위치8(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=8, boxId=107)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[108]):
            return 라운드카메라8(self.ctx)


class 라운드카메라8(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=308, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기8(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기8(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5801,5802,5803,5804,5805,5806,5807,5808,5809,5810,5811,5812,5813,5814,5815,5816,5817,5818,5819,5820,5821,5822], randomCount=12, isVisible=True)
        self.set_timer(timerId='100008', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=8, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='8,10,6', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작8(self.ctx)


class 라운드시작8(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100008'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1701,1702,1703,1704,1705,1706,1707,1708,1709,1710,1711]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료8(self.ctx)


class 라운드종료8(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_8round')
        self.arcade_spring_farm(type='ClearRound', round=8)
        self.reset_timer(timerId='100008')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=9, boxId=108)
            return 라운드유저위치9(self.ctx)


class 라운드유저위치9(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=9, boxId=108)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[109]):
            return 라운드카메라9(self.ctx)


class 라운드카메라9(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=309, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기9(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기9(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[5901,5902,5903,5904,5905,5906,5907,5908,5909,5910,5911,5912,5913,5914,5915], randomCount=8, isVisible=True)
        self.set_timer(timerId='100009', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=9, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='9,10,6', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작9(self.ctx)


class 라운드시작9(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100009'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[1901,1902,1903,1904,1905,1906,1907,1908,1909,1910,1911,1912,1913,1914,1915]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료9(self.ctx)


class 라운드종료9(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_9round')
        self.arcade_spring_farm(type='ClearRound', round=9)
        self.reset_timer(timerId='100009')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=10, boxId=109)
            return 라운드유저위치10(self.ctx)


class 라운드유저위치10(trigger_api.Trigger):
    def on_enter(self):
        self.move_user(mapId=51000001, portalId=10, boxId=109)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[110]):
            return 라운드카메라10(self.ctx)


class 라운드카메라10(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=310, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 라운드대기10(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class 라운드대기10(trigger_api.Trigger):
    def on_enter(self):
        self.set_cube(triggerIds=[51001,51002,51003,51004,51005,51006,51007,51008,51009,51010,51011,51012,51013,51014,51015,51016,51017,51018,51019,51020,51021,51022,51023,51024], randomCount=6, isVisible=True)
        self.set_timer(timerId='100010', seconds=120, startDelay=1, interval=1, vOffset=-30, type='TR')
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[2001], score=10000)
        self.arcade_spring_farm(type='SpawnMonster', spawnIds=[2002,2003,2004,2005], score=5000)
        self.arcade_spring_farm(type='StartRound', uiDuration=3000, round=10, timeScoreType='remain', timeScoreRate='500', roundDuration='120000')
        self.set_event_ui(type=0, arg2='10,10,6', arg4='120')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 라운드시작10(self.ctx)


class 라운드시작10(trigger_api.Trigger):
    def on_enter(self):
        self.remove_buff(boxId=199, skillId=70000091)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='100010'):
            return 종료(self.ctx)
        if self.monster_dead(boxIds=[2001,2002,2003,2004,2005]):
            self.add_buff(boxIds=[199], skillId=70000091, level=1, isSkillSet=False)
            return 라운드종료10(self.ctx)


class 라운드종료10(trigger_api.Trigger):
    def on_enter(self):
        self.set_achievement(triggerId=199, type='trigger', achieve='springfarm_clear')
        self.arcade_spring_farm(type='ClearRound', round=10)
        self.reset_timer(timerId='100010')
        self.set_event_ui(type=7, arg3='2000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            self.move_user(mapId=51000001, portalId=44, boxId=110)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_Ending_Popup_01')
        self.arcade_spring_farm(type='EndGame')
        self.move_user(mapId=51000001, portalId=44, boxId=110)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 진짜끝(self.ctx)


class 진짜끝(trigger_api.Trigger):
    pass


initial_state = 대기
