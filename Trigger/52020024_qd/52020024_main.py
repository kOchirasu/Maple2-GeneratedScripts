""" trigger/52020024_qd/52020024_main.xml """
import trigger_api


class 감지(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_user_value(triggerId=99990002, key='TimerStart', value=0)
        self.set_user_value(triggerId=99990003, key='FinalPhase', value=0)
        self.set_effect(triggerIds=[5001], visible=False)
        self.set_actor(triggerId=10001, visible=True, initialSequence='ks_quest_movewall_A02_off')
        self.set_actor(triggerId=10002, visible=True, initialSequence='ks_quest_movewall_A02_off')
        self.set_actor(triggerId=10003, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
        self.set_mesh(triggerIds=[1001], visible=True)
        self.set_mesh(triggerIds=[2001], visible=True)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10002006], state=2)
        self.set_interact_object(triggerIds=[10002007], state=2)
        self.set_interact_object(triggerIds=[10002008], state=2)
        self.set_interact_object(triggerIds=[10002009], state=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 차전투감지1(self.ctx)


class 차전투감지1(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[902]):
            return 차전투1(self.ctx)


class 차전투1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='방 안을 수색하세요', arg3='5000', arg4='0')
        self.create_monster(spawnIds=[101,102,103], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102,103], arg2=False):
            return 번레버활성화1(self.ctx)


class 번레버활성화1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002006], state=1)
        self.add_balloon_talk(spawnId=0, msg='파편 융합 장치 전원을 찾아야해', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002006], stateValue=0):
            return 차전투감지2(self.ctx)


class 차전투감지2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[1001], visible=False, arg3=500)
        self.set_actor(triggerId=10001, visible=True, initialSequence='ks_quest_movewall_A02_start')
        self.add_balloon_talk(spawnId=0, msg='헐... 대박...', duration=3000, delayTick=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[903]):
            return 차전투2(self.ctx)


class 차전투2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[111,112], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,112], arg2=False):
            return 번레버활성화2(self.ctx)


class 번레버활성화2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_balloon_talk(spawnId=0, msg='여기엔 없는것 같네', duration=3000, delayTick=0)
        self.set_interact_object(triggerIds=[10002007], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002007], stateValue=0):
            return 차전투감지3(self.ctx)


class 차전투감지3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[2001], visible=False, arg3=500)
        self.set_actor(triggerId=10002, visible=True, initialSequence='ks_quest_movewall_A02_start')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[904]):
            return 차전투3(self.ctx)


class 차전투3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[121,122], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[121,122], arg2=False):
            return 번레버활성화3(self.ctx)


class 번레버활성화3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002008], state=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002008], stateValue=0):
            return 파편모으기(self.ctx)


class 파편모으기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_interact_object(triggerIds=[10002009], state=1)
        self.add_balloon_talk(spawnId=0, msg='중앙으로 가보자!', duration=3000, delayTick=0)
        self.set_event_ui(type=1, arg2='융합장치 전원 활성화.', arg3='5000', arg4='0')

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10002009], stateValue=0):
            return 파이널전투(self.ctx)


class 파이널전투(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=10003, visible=True, initialSequence='ks_quest_fusiondevice_A01_on')
        self.set_user_value(triggerId=99990002, key='TimerStart', value=1)
        self.set_user_value(triggerId=99990003, key='FinalPhase', value=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='TimerStart', value=2):
            return 파편합성완료(self.ctx)
        if self.user_value(key='FinalPhase', value=2):
            return 파편합성완료(self.ctx)


class 파편합성완료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_actor(triggerId=10003, visible=True, initialSequence='ks_quest_fusiondevice_A01_off')
        self.destroy_monster(spawnIds=[-1])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_미카엘등장(self.ctx)


class 카메라_미카엘등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(mapId=52020024, portalId=2)
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_Michael')
        self.select_camera(triggerId=501, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_미카엘대사1(self.ctx)


class 카메라_미카엘대사1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=201, script='아주 좋아!', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카메라_미카엘대사2(self.ctx)


class 카메라_미카엘대사2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=502, enable=True)
        self.set_conversation(type=1, spawnId=201, script='파편이 어쩌구~ 저쩌구~', arg4=5)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 카메라_지진사태(self.ctx)


class 카메라_지진사태(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=503, enable=True)
        self.set_conversation(type=1, spawnId=0, script='왜...왜 이러지?', arg4=4)
        self.set_onetime_effect(id=1, enable=True, path='BG\\Common\\Eff_Com_Vibrate_Lowamp.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_바닥부서짐(self.ctx)


class 카메라_바닥부서짐(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='으아아악!!!', arg4=2)
        self.select_camera(triggerId=504, enable=True)
        self.set_skill(triggerIds=[1], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=52020025, portalId=1)


initial_state = 감지
