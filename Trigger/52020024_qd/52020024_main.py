""" trigger/52020024_qd/52020024_main.xml """
from common import *
import state


class 감지(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='TimerStart', value=0)
        set_user_value(triggerId=99990003, key='FinalPhase', value=0)
        set_effect(triggerIds=[5001], visible=False)
        set_actor(triggerId=10001, visible=True, initialSequence='ks_quest_movewall_A02_off')
        set_actor(triggerId=10002, visible=True, initialSequence='ks_quest_movewall_A02_off')
        set_actor(triggerId=10003, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
        set_mesh(triggerIds=[1001], visible=True)
        set_mesh(triggerIds=[2001], visible=True)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10002006], state=2)
        set_interact_object(triggerIds=[10002007], state=2)
        set_interact_object(triggerIds=[10002008], state=2)
        set_interact_object(triggerIds=[10002009], state=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 차전투감지1()


class 차전투감지1(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            return 차전투1()


class 차전투1(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='방 안을 수색하세요', arg3='5000', arg4='0')
        create_monster(spawnIds=[101,102,103], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103], arg2=False):
            return 번레버활성화1()


class 번레버활성화1(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002006], state=1)
        add_balloon_talk(spawnId=0, msg='파편 융합 장치 전원을 찾아야해', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002006], arg2=0):
            return 차전투감지2()


class 차전투감지2(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001], visible=False, arg3=500)
        set_actor(triggerId=10001, visible=True, initialSequence='ks_quest_movewall_A02_start')
        add_balloon_talk(spawnId=0, msg='헐... 대박...', duration=3000, delayTick=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 차전투2()


class 차전투2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[111,112], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,112], arg2=False):
            return 번레버활성화2()


class 번레버활성화2(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=0, msg='여기엔 없는것 같네', duration=3000, delayTick=0)
        set_interact_object(triggerIds=[10002007], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002007], arg2=0):
            return 차전투감지3()


class 차전투감지3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[2001], visible=False, arg3=500)
        set_actor(triggerId=10002, visible=True, initialSequence='ks_quest_movewall_A02_start')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[904]):
            return 차전투3()


class 차전투3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[121,122], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[121,122], arg2=False):
            return 번레버활성화3()


class 번레버활성화3(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002008], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002008], arg2=0):
            return 파편모으기()


class 파편모으기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002009], state=1)
        add_balloon_talk(spawnId=0, msg='중앙으로 가보자!', duration=3000, delayTick=0)
        set_event_ui(type=1, arg2='융합장치 전원 활성화.', arg3='5000', arg4='0')

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002009], arg2=0):
            return 파이널전투()


class 파이널전투(state.State):
    def on_enter(self):
        set_actor(triggerId=10003, visible=True, initialSequence='ks_quest_fusiondevice_A01_on')
        set_user_value(triggerId=99990002, key='TimerStart', value=1)
        set_user_value(triggerId=99990003, key='FinalPhase', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='TimerStart', value=2):
            return 파편합성완료()
        if user_value(key='FinalPhase', value=2):
            return 파편합성완료()


class 파편합성완료(state.State):
    def on_enter(self):
        set_actor(triggerId=10003, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
        destroy_monster(spawnIds=[-1])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_미카엘등장()


class 카메라_미카엘등장(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        move_user(mapId=52020024, portalId=2)
        create_monster(spawnIds=[201], arg2=False)
        move_npc(spawnId=201, patrolName='MS2PatrolData_Michael')
        select_camera(triggerId=501, enable=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_미카엘대사1()


class 카메라_미카엘대사1(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=201, script='아주 좋아!', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카메라_미카엘대사2()


class 카메라_미카엘대사2(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_conversation(type=1, spawnId=201, script='파편이 어쩌구~ 저쩌구~', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 카메라_지진사태()


class 카메라_지진사태(state.State):
    def on_enter(self):
        select_camera(triggerId=503, enable=True)
        set_conversation(type=1, spawnId=0, script='왜...왜 이러지?', arg4=4)
        set_onetime_effect(id=1, enable=True, path='BG\Common\Eff_Com_Vibrate_Lowamp.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_바닥부서짐()


class 카메라_바닥부서짐(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='으아아악!!!', arg4=2)
        select_camera(triggerId=504, enable=True)
        set_skill(triggerIds=[1], isEnable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        move_user(mapId=52020025, portalId=1)


