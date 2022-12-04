""" trigger/52000149_qd/main.xml """
import trigger_api


class start(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101,102,111,112])
        self.set_effect(triggerIds=[6001,6002], visible=True)
        self.set_npc_emotion_loop(spawnId=111, sequenceName='Sit_Down_A', duration=100000000) # 아시모프
        self.set_npc_emotion_loop(spawnId=112, sequenceName='Event_02_Idle', duration=100000000) # 아노스
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return 퀘스트조건체크(self.ctx)


class 퀘스트조건체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001633], questStates=[2]):
            return 빈집(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001633], questStates=[1]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[2]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[1]):
            return 전경_연출준비(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001631], questStates=[3]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001631], questStates=[2]):
            return 기본상태(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[50001631], questStates=[1]):
            return 기본상태(self.ctx)


class 기본상태(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[50001632], questStates=[1]):
            return 전경_연출준비(self.ctx)


class 전경_연출준비(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000149, portalId=10)
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return 전경_연출시작(self.ctx)


class 전경_연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8000,8010], returnView=False)
        self.move_user_path(patrolName='MS2PatrolData_pc')
        self.set_scene_skip(state=아노스아파_스킵완료, action='nextState') # setsceneskip 1 set

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라_아노스줌인(self.ctx)


class 카메라_아노스줌인(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8001], returnView=False)
        self.add_cinematic_talk(npcId=11003436, msg='$52000149_QD__MAIN__0$', duration=3000)
        self.set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라_아노스줌인01(self.ctx)


class 카메라_아노스줌인01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_케이틀린01(self.ctx)


class 카메라_케이틀린01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8002,8004], returnView=False)
        self.add_cinematic_talk(npcId=11003436, msg='$52000149_QD__MAIN__1$', duration=3000)
        self.set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 카메라_케이틀린0102(self.ctx)


class 카메라_케이틀린0102(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_케이틀린02(self.ctx)


class 카메라_케이틀린02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Idle_A', duration=3000)
        self.add_cinematic_talk(npcId=11003436, msg='$52000149_QD__MAIN__2$', duration=3000)
        self.add_balloon_talk(spawnId=102, msg='$52000149_QD__MAIN__3$', duration=3000, delayTick=0)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_katelyn')
        self.set_skip(state=아노스아파_스킵완료)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 호르헤이동(self.ctx)


class 호르헤이동(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[8003], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Jorge')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 빈집(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[111,112])
        self.set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=100):
            return 연출종료(self.ctx)


class 아노스아파_스킵완료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=4)
        self.move_user(mapId=52000149, portalId=11)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_Jorge')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.reset_camera(interpolationTime=3)
        self.set_achievement(triggerId=9000, type='trigger', achieve='AnosReturns')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = start
