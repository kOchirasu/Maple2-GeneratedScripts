""" trigger/63000024_cs/wakeup01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=False) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # 목표 바닥 지점01 NPC
        self.set_effect(triggerIds=[5102], visible=False) # 목표 바닥 지점03 포탈
        self.set_effect(triggerIds=[5200], visible=False) # 화살표01 NPC
        self.set_effect(triggerIds=[5300], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5301], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5302], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5303], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5304], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5500], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5501], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5502], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5503], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5504], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5505], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5506], visible=False) # 경로 안내
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001674
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001714
        self.set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001675
        self.create_monster(spawnIds=[101], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return PlayMovie01(self.ctx)


class PlayMovie01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[1]):
            # 두 번째 퀘스트 수락한 상태
            return QuestOnGoing04(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[3]):
            # 첫 번째 퀘스트 완료 상태
            return QuestOnGoing03(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[2]):
            # 첫 번째 퀘스트 완료 가능 상태
            return QuestOnGoing02(self.ctx)
        if self.quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[1]):
            # 첫 번째 퀘스트 수락한 상태
            return QuestOnGoing01(self.ctx)
        if self.wait_tick(waitTick=2000):
            return LodingDelay01(self.ctx)


# 첫 번째 퀘스트 수락한 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000024, portalId=10, boxId=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return None # Missing State: MoveToGetWeapon01


# 첫 번째 퀘스트 완료 가능 상태
class QuestOnGoing02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000024, portalId=10, boxId=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestStart02(self.ctx)


# 첫 번째 퀘스트 완료 상태
class QuestOnGoing03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000024, portalId=10, boxId=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return QuestStart03(self.ctx)


# 두 번째 퀘스트 수락한 상태
class QuestOnGoing04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000024, portalId=10, boxId=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.set_portal(portalId=1, visible=True, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TimeToLeave01(self.ctx)


# 최초 입장
class LodingDelay01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=500, enable=True)
        self.set_scene_skip(state=TinChaiTalk04_CSkip, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCDownIdle01(self.ctx)


class PCDownIdle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Down_Idle_D', duration=9000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCDownIdle02(self.ctx)


class PCDownIdle02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return LookAround01(self.ctx)


class LookAround01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[501,502], returnView=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return LookAround02(self.ctx)


class LookAround02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_loop(sequenceName='Sit_Ground_Idle_A', duration=18000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround03(self.ctx)


class LookAround03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround04(self.ctx)


class LookAround04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=510, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_105')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return LookAround05(self.ctx)


class LookAround05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LookAround06(self.ctx)


class LookAround06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=511, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return LookAround07(self.ctx)


class LookAround07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=600, enable=True)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return TinChaiTalk01(self.ctx)


class TinChaiTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001674
        self.set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__0$', arg4=7) # Voice 00001674
        self.set_skip(state=TinChaiTalk02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return TinChaiTalk02(self.ctx)


class TinChaiTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TinChaiTalk03(self.ctx)


class TinChaiTalk03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001714
        self.set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__1$', arg4=5) # Voice 00001714
        self.set_skip(state=TinChaiTalk04)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TinChaiTalk04(self.ctx)


class TinChaiTalk04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_user(mapId=63000024, portalId=10, boxId=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=600, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 키타입설정안내01(self.ctx)


class TinChaiTalk04_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_102')
        self.move_user(mapId=63000024, portalId=10, boxId=9900)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=600, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 키타입설정안내01(self.ctx)


class 키타입설정안내01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.guide_event(eventId=10030005) # 트리거 To가이드 : 키타입설정

    def on_tick(self) -> trigger_api.Trigger:
        if self.widget_condition(type='Guide', name='IsTriggerEvent', condition='10030009'):
            return MeetTinChai01(self.ctx)


class MeetTinChai01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=True) # 목표 바닥 지점01 NPC
        self.set_effect(triggerIds=[5200], visible=True) # 화살표01 NPC
        self.set_effect(triggerIds=[5300], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5301], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5302], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5303], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5304], visible=True) # 경로 안내
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entityId=10030010, textId=10030010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9001]):
            return MeetTinChai02(self.ctx)


class MeetTinChai02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5001], visible=False) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # 목표 바닥 지점01 NPC
        self.set_effect(triggerIds=[5200], visible=False) # 화살표01 NPC
        self.set_effect(triggerIds=[5300], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5301], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5302], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5303], visible=False) # 경로 안내
        self.set_effect(triggerIds=[5304], visible=False) # 경로 안내
        self.hide_guide_summary(entityId=10030010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return TinChaiTalk10(self.ctx)


class TinChaiTalk10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return TinChaiTalk11(self.ctx)


class TinChaiTalk11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001675
        self.set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__2$', arg4=6) # Voice 00001675
        self.set_skip(state=TinChaiTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return TinChaiTalk12(self.ctx)


class TinChaiTalk12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return TinChaiTalk13(self.ctx)


class TinChaiTalk13(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=2, spawnId=11001708, script='$63000024_CS__WAKEUP01__3$', arg4=5)
        self.set_skip(state=TinChaiTalk14)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TinChaiTalk14(self.ctx)


class TinChaiTalk14(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 틴차이에게 다가가 스페이스키로 대화하기
        self.show_guide_summary(entityId=10030020, textId=10030020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[1]):
            # 90000443 신비로운 보옥 수락한 상태
            return QuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=10030020)


# 오브젝트 반응, 아이템 줍기, 무기 장착, 일반 공격 가이드
class QuestStart01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[2]):
            # 90000443 신비로운 보옥 완료 가능
            return QuestStart02(self.ctx)


class QuestStart02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000443], questStates=[3]):
            # 90000443 신비로운 보옥 완료
            return QuestStart03(self.ctx)


# 약초 장착 가이드
class QuestStart03(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000444], questStates=[1]):
            # 90000444 가이던스의 대제자 수락
            return QuestStart04(self.ctx)


class QuestStart04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=True, enable=False, minimapVisible=False)
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_103')
        self.set_conversation(type=1, spawnId=103, script='$63000024_CS__WAKEUP01__4$', arg4=4, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return GuideNextMap01(self.ctx)


class GuideNextMap01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 방향키를 이용해 화살표가 가리키는 곳으로 이동하기
        self.show_guide_summary(entityId=10030010, textId=10030010)
        self.set_effect(triggerIds=[5001], visible=True) # 화살표 안내 사운드 이펙트
        self.set_effect(triggerIds=[5102], visible=True) # 목표 바닥 지점03 포탈
        self.set_effect(triggerIds=[5500], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5501], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5502], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5503], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5504], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5505], visible=True) # 경로 안내
        self.set_effect(triggerIds=[5506], visible=True) # 경로 안내

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9003]):
            return GuideNextMap02(self.ctx)


class GuideNextMap02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_104')
        self.hide_guide_summary(entityId=10030010)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.set_effect(triggerIds=[5002], visible=True) # 미션 완료 사운드 이펙트
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=1060, textId=1060) # 가이드 : 포털 위치에서 스페이스 키 누르기

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return GuideNextMap03(self.ctx)


class GuideNextMap03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.hide_guide_summary(entityId=1060)


initial_state = Wait
