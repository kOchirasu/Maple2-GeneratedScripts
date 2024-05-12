""" trigger/63000015_cs/intro01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_sound(triggerId=10000, enable=False)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_effect(triggerIds=[5100], visible=False) # 목표지점 바닥
        self.set_effect(triggerIds=[5101], visible=False) # 목표지점 화살표
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 목료 완료 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5204], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5205], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5206], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5207], visible=False) # 경로 안내
        self.set_effect(triggerIds=[6000], visible=False) # VoiceGangster
        self.set_effect(triggerIds=[8000], visible=False) # WeiHong 00001390
        self.set_effect(triggerIds=[8001], visible=False) # WeiHong 00001391
        self.set_effect(triggerIds=[8002], visible=False) # WeiHong 00001392
        self.set_effect(triggerIds=[8003], visible=False) # WeiHong 00001393
        self.set_effect(triggerIds=[8004], visible=False) # WeiHong 00001394
        self.set_effect(triggerIds=[8005], visible=False) # WeiHong 00000480
        self.create_monster(spawnIds=[101,201,202,203,204,205,206], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return PlayOpeningMovie01(self.ctx)


# 퀘스트 진행 중 상태, 완료 가능 상태
class StandAside10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=10000, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return StandAside11(self.ctx)


class StandAside11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_206')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return WeiHongQuest03(self.ctx)


# 퀘스트 진행 완료 상태
class StandAside20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=10000, enable=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return StandAside21(self.ctx)


class StandAside21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_206')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return GuideNextMap01(self.ctx)


# 최초 입장
class PlayOpeningMovie01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[2]):
            # 퀘스트 완료 가능 상태
            return StandAside10(self.ctx)
        if self.quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[3]):
            # 퀘스트 완료 상태
            return StandAside20(self.ctx)
        if self.wait_tick(waitTick=2000):
            return PlayOpeningMovie02(self.ctx)


class PlayOpeningMovie02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='common\\Common_Opening.usm', movieId=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='2'):
            return PlayMovie01(self.ctx)
        if self.wait_tick(waitTick=190000):
            return PlayMovie01(self.ctx)


class PlayMovie01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return PlayMovie02(self.ctx)


class PlayMovie02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='SceneMovie')
        self.widget_action(type='SceneMovie', func='Clear')
        self.play_scene_movie(fileName='Cut_Blackstar_Crash.swf', movieId=1) # 임시

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return WeiHongTalk01(self.ctx)
        if self.wait_tick(waitTick=66000):
            return WeiHongTalk01(self.ctx)


class WeiHongTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=10000, enable=True)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)
        self.set_effect(triggerIds=[6000], visible=True) # VoiceGangster

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return WeiHongTalk02(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(triggerIds=[6000], visible=False)
        # VoiceGangster


class WeiHongTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)
        self.set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__0$', arg4=6) # Voice 00001390
        self.set_effect(triggerIds=[8000], visible=True) # WeiHong 00001390
        self.set_skip(state=WeiHongTalk03)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return WeiHongTalk03(self.ctx)


class WeiHongTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_effect(triggerIds=[8000], visible=False) # WeiHong 00001390

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return WeiHongTalk04(self.ctx)


class WeiHongTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__1$', arg4=6) # Voice 00001391
        self.set_effect(triggerIds=[8001], visible=True) # WeiHong 00001391
        self.set_skip(state=WeiHongTalk05)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return WeiHongTalk05(self.ctx)


class WeiHongTalk05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_effect(triggerIds=[8001], visible=False) # WeiHong 00001391

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return WeiHongTalk06(self.ctx)


class WeiHongTalk06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__2$', arg4=5) # Voice 00001392
        self.set_effect(triggerIds=[8002], visible=True) # WeiHong 00001392
        self.set_skip(state=WeiHongTalk07)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return WeiHongTalk07(self.ctx)


class WeiHongTalk07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_effect(triggerIds=[8002], visible=False) # WeiHong 00001392
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=601, enable=False)
        self.set_mesh(triggerIds=[3001,3002,3003,3004], visible=False, arg3=0, delay=0, scale=0) # barrier

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return StandAside01(self.ctx)


class StandAside01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_201')
        self.move_npc(spawnId=202, patrolName='MS2PatrolData_202')
        self.move_npc(spawnId=204, patrolName='MS2PatrolData_204')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return StandAside02(self.ctx)


class StandAside02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_203')
        self.move_npc(spawnId=205, patrolName='MS2PatrolData_205')
        self.move_npc(spawnId=206, patrolName='MS2PatrolData_206')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return StandAside03(self.ctx)


class StandAside03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return KeytypeSelect01(self.ctx)


class KeytypeSelect01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(eventId=10020005)

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='Guide', name='IsTriggerEvent', condition='10020009'):
            return MeetWeiHong01(self.ctx)


class MeetWeiHong01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=True) # 목표지점 바닥
        self.set_effect(triggerIds=[5101], visible=True) # 목표지점 화살표
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entityId=10020010, textId=10020010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return MeetWeiHong02(self.ctx)


class MeetWeiHong02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # 목표지점 바닥
        self.set_effect(triggerIds=[5101], visible=False) # 목표지점 화살표
        self.hide_guide_summary(entityId=10020010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return WeiHongTalk10(self.ctx)


class WeiHongTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=602, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WeiHongTalk11(self.ctx)


class WeiHongTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__3$', arg4=5) # Voice 00000480
        self.set_effect(triggerIds=[8005], visible=True) # WeiHong 00000480
        self.set_skip(state=WeiHongTalk12)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return WeiHongTalk12(self.ctx)


class WeiHongTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_effect(triggerIds=[8005], visible=False) # WeiHong 00000480
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return WeiHongTalk13(self.ctx)


class WeiHongTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__4$', arg4=5) # Voice 00001393
        self.set_effect(triggerIds=[8003], visible=True) # WeiHong 00001393
        self.set_skip(state=WeiHongTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return WeiHongTalk14(self.ctx)


class WeiHongTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_effect(triggerIds=[8003], visible=False) # WeiHong 00001393
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return MafiaTalk10(self.ctx)


class MafiaTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6000], visible=True) # VoiceGangster
        self.set_conversation(type=1, spawnId=201, script='$63000015_CS__INTRO01__5$', arg4=3, arg5=0)
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MafiaTalk11(self.ctx)


class MafiaTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=201, sequenceName='Idle_A')
        self.set_conversation(type=1, spawnId=202, script='$63000015_CS__INTRO01__6$', arg4=3, arg5=0)
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MafiaTalk12(self.ctx)


class MafiaTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=202, sequenceName='Idle_A')
        self.set_conversation(type=1, spawnId=206, script='$63000015_CS__INTRO01__7$', arg4=3, arg5=0)
        self.set_npc_emotion_sequence(spawnId=206, sequenceName='Talk_A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return WeiHongTalk20(self.ctx)

    def on_exit(self) -> None:
        self.set_effect(triggerIds=[6000], visible=False)
        # VoiceGangster


class WeiHongTalk20(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=206, sequenceName='Idle_A')
        self.set_conversation(type=2, spawnId=11000251, script='$63000015_CS__INTRO01__8$', arg4=6) # Voice 00001394
        self.set_effect(triggerIds=[8004], visible=True) # WeiHong 00001394
        self.set_skip(state=WeiHongQuest01)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return WeiHongQuest01(self.ctx)


class WeiHongQuest01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_effect(triggerIds=[8004], visible=False) # WeiHong 00001394
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=602, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return WeiHongQuest02(self.ctx)


class WeiHongQuest02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10020020, textId=10020020) # 가이드 : 스페이스키로 대화하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[2]):
            # 퀘스트 진행 중 상태
            return WeiHongQuest03(self.ctx)


class WeiHongQuest03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=10020020)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10020021, textId=10020021) # 가이드 : 웨이 홍과 대화하기

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9100], questIds=[90000430], questStates=[3]):
            # 퀘스트 완료 상태
            return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=10020021)
        self.set_portal(portalId=1, visible=True, enable=False, minimapVisible=True)
        self.set_effect(triggerIds=[5200], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5201], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5202], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5203], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5204], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5205], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5206], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5207], visible=True) # 경로 안내
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entityId=10020012, textId=10020012)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9002]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=10020012)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.show_guide_summary(entityId=10020011, textId=10020011) # 가이드 : 포털 위치에서 스페이스 키 누르기
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9100]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=10020011)
        self.set_effect(triggerIds=[5200], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5201], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5202], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5203], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5204], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5205], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5206], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5207], visible=False) # 경로 안내


initial_state = Wait
