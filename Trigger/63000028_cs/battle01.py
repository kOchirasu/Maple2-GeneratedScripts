""" trigger/63000028_cs/battle01.xml """
import trigger_api


class Wait(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_widget(type='Guide')
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5100], visible=False) # Sound_ShadowApp_Loop
        self.set_effect(triggerIds=[6000], visible=False) # Voice_Tinchai_00001684
        self.set_effect(triggerIds=[6001], visible=False) # Voice_Tinchai_00001685
        self.set_effect(triggerIds=[6002], visible=False) # Voice_Tinchai_00001686
        self.set_effect(triggerIds=[6003], visible=False) # Voice_Tinchai_00001717
        self.set_effect(triggerIds=[6004], visible=False) # Voice_Tinchai_00001687
        self.set_effect(triggerIds=[6100], visible=False) # Voice_Junta_00001773
        self.set_effect(triggerIds=[6101], visible=False) # Voice_Junta_00001774
        self.set_effect(triggerIds=[6102], visible=False) # Voice_Junta_00001775
        self.set_agent(triggerIds=[8000], visible=True)
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)
        self.set_agent(triggerIds=[8102], visible=False)
        self.set_agent(triggerIds=[8103], visible=False)
        self.set_agent(triggerIds=[8104], visible=False)
        self.set_agent(triggerIds=[8105], visible=False)
        self.set_agent(triggerIds=[8106], visible=False)
        self.set_agent(triggerIds=[8107], visible=False)
        self.set_agent(triggerIds=[8108], visible=False)
        self.set_agent(triggerIds=[8109], visible=False)
        self.set_agent(triggerIds=[8110], visible=False)
        self.set_agent(triggerIds=[8111], visible=False)
        self.set_agent(triggerIds=[8112], visible=False)
        self.set_agent(triggerIds=[8113], visible=False)
        self.set_agent(triggerIds=[8114], visible=False)
        self.set_agent(triggerIds=[8115], visible=False)
        self.set_skill(triggerIds=[7000], enable=False) # 올킬

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


class Enter01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000452], questStates=[1]):
            # 그림자의 파도 퀘스트 수락한 상태
            return QuestOnGoing21(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[3]):
            # 별, 수정, 그리고 퀘스트 완료 상태
            return QuestOnGoing11(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[2]):
            # 별, 수정, 그리고 퀘스트 완료 가능 상태
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[1]):
            # 별, 수정, 그리고 퀘스트 진행중 상태
            return PCWakeUp01(self.ctx)


# 별, 수정, 그리고 퀘스트 완료 가능 상태
class QuestOnGoing01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[103,202], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return FirstQuestEnd01(self.ctx)


# 별, 수정, 그리고 퀘스트 완료 상태
class QuestOnGoing11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[103,202], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return SecondQuestStart01(self.ctx)


# 그림자의 파도 퀘스트 수락한 상태
class QuestOnGoing21(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return QuestOnGoing22(self.ctx)


class QuestOnGoing22(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000028, portalId=11, boxId=9900)
        self.create_monster(spawnIds=[104,203], animationEffect=False)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=300):
            return QuestOnGoing23(self.ctx)


class QuestOnGoing23(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=400):
            return ShadowWaveAgain02(self.ctx)


# 최초 입장
class PCWakeUp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCWakeUp02(self.ctx)


class PCWakeUp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=500, enable=True)
        self.set_scene_skip(state=TinChaiTalk02_CSkip, action='nextState')
        self.create_monster(spawnIds=[101,900,901,902], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return PCWakeUp03(self.ctx)


class PCWakeUp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user_path(patrolName='MS2PatrolData_1000')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return PCWakeUp04(self.ctx)


class PCWakeUp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_pc_emotion_sequence(sequenceNames=['Bore_C'])
        self.set_conversation(type=1, spawnId=0, script='$63000028_CS__BATTLE01__0$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return PCWakeUp05(self.ctx)


class PCWakeUp05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=0, script='$63000028_CS__BATTLE01__1$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleING01(self.ctx)


class BattleING01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleING02(self.ctx)


class BattleING02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return TinChaiTalk01(self.ctx)


class TinChaiTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6000], visible=True) # Voice_Tinchai_00001684
        self.set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__2$', arg4=5) # 틴차이 00001684
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TinChaiTalk02(self.ctx)


class TinChaiTalk02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ReadyToBattle01(self.ctx)


class TinChaiTalk02_CSkip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ReadyToBattle01(self.ctx)


class ReadyToBattle01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_agent(triggerIds=[8000], visible=False)
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.select_camera(triggerId=501, enable=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return ReadyToBattle02(self.ctx)


# HP 가이드
class ReadyToBattle02(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BattleStart01(self.ctx)


class BattleStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : 틴차이를 도와 검은 그림자 처치하기
        self.show_guide_summary(entityId=10035010, textId=10035010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BattleStart02(self.ctx)


class BattleStart02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 트리거 To가이드 : HP가 0이 되면 비석에 깔리니 조심
        self.guide_event(eventId=10035020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[900,901,902]):
            return BattleEnd01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=10035010)


class BattleEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[900,901,902])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BattleEnd02(self.ctx)


class BattleEnd02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BattleEnd03(self.ctx)


class BattleEnd03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000028, portalId=10, boxId=9900)
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleEnd04(self.ctx)


class BattleEnd04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_scene_skip(state=MeetJunta05_Cskip, action='nextState')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return BattleEnd05(self.ctx)


class BattleEnd05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=102, script='$63000028_CS__BATTLE01__3$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return ShadowWave01(self.ctx)


class ShadowWave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(triggerIds=[8100], visible=True)
        self.set_agent(triggerIds=[8101], visible=True)
        self.set_agent(triggerIds=[8102], visible=True)
        self.set_agent(triggerIds=[8103], visible=True)
        self.set_agent(triggerIds=[8104], visible=True)
        self.set_agent(triggerIds=[8105], visible=True)
        self.set_agent(triggerIds=[8106], visible=True)
        self.set_agent(triggerIds=[8107], visible=True)
        self.set_agent(triggerIds=[8108], visible=True)
        self.set_agent(triggerIds=[8109], visible=True)
        self.set_agent(triggerIds=[8110], visible=True)
        self.set_agent(triggerIds=[8111], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowWave02(self.ctx)


class ShadowWave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=600, enable=True)
        self.set_effect(triggerIds=[5100], visible=True) # Sound_ShadowApp_Loop

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowWave03(self.ctx)


# 정면 1차 스폰 후 다리 패트롤 바로 시작
class ShadowWave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[910,911,912,913])
        self.move_npc(spawnId=910, patrolName='MS2PatrolData_910')
        self.move_npc(spawnId=911, patrolName='MS2PatrolData_911')
        self.move_npc(spawnId=912, patrolName='MS2PatrolData_912')
        self.move_npc(spawnId=913, patrolName='MS2PatrolData_913')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowWave04(self.ctx)


# 정면 2차 스폰 후 다리 패트롤 바로 시작
class ShadowWave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[920,921,922,923,924])
        self.move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        self.move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        self.move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        self.move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        self.move_npc(spawnId=924, patrolName='MS2PatrolData_924')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowWave05(self.ctx)


# 카메라 워크
class ShadowWave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_101')
        self.move_user_path(patrolName='MS2PatrolData_1002')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowWave06(self.ctx)


class ShadowWave06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[930,931,932,933,950,951,952,953])
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        self.move_npc(spawnId=932, patrolName='MS2PatrolData_932')
        self.move_npc(spawnId=933, patrolName='MS2PatrolData_933')
        self.move_npc(spawnId=950, patrolName='MS2PatrolData_950')
        self.move_npc(spawnId=951, patrolName='MS2PatrolData_951')
        self.move_npc(spawnId=952, patrolName='MS2PatrolData_952')
        self.move_npc(spawnId=953, patrolName='MS2PatrolData_953')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowWave07(self.ctx)


# 양측 2차 스폰
class ShadowWave07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_conversation(type=1, spawnId=102, script='$63000028_CS__BATTLE01__4$', arg4=3, arg5=0) # 틴차이
        self.create_monster(spawnIds=[940,941,942,943,944,945,960,961,962,963,964,965])
        self.move_npc(spawnId=940, patrolName='MS2PatrolData_940')
        self.move_npc(spawnId=941, patrolName='MS2PatrolData_941')
        self.move_npc(spawnId=942, patrolName='MS2PatrolData_942')
        self.move_npc(spawnId=943, patrolName='MS2PatrolData_943')
        self.move_npc(spawnId=944, patrolName='MS2PatrolData_944')
        self.move_npc(spawnId=945, patrolName='MS2PatrolData_945')
        self.move_npc(spawnId=960, patrolName='MS2PatrolData_960')
        self.move_npc(spawnId=961, patrolName='MS2PatrolData_961')
        self.move_npc(spawnId=962, patrolName='MS2PatrolData_962')
        self.move_npc(spawnId=963, patrolName='MS2PatrolData_963')
        self.move_npc(spawnId=964, patrolName='MS2PatrolData_964')
        self.move_npc(spawnId=965, patrolName='MS2PatrolData_965')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TinChaiDesperate01(self.ctx)


class TinChaiDesperate01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=602, enable=True)
        self.set_npc_emotion_loop(spawnId=102, sequenceName='Attack_Idle_A', duration=12000)
        self.set_pc_emotion_loop(sequenceName='Orb_Attack_Idle_A', duration=12000)
        self.set_effect(triggerIds=[6001], visible=True) # Voice_Tinchai_00001685
        self.set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__5$', arg4=5) # 틴차이 00001685
        self.set_skip(state=TinChaiDesperate02)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return TinChaiDesperate02(self.ctx)


class TinChaiDesperate02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return JuntaApp01(self.ctx)


class JuntaApp01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return JuntaApp02(self.ctx)


class JuntaApp02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=700, enable=True)
        self.destroy_monster(spawnIds=[910,911,912,913,920,921,922,923,924,930,931,932,933,940,941,942,943,944,945,950,951,952,953,960,961,962,963,964,965])
        self.create_monster(spawnIds=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return JuntaApp03(self.ctx)


class JuntaApp03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(triggerIds=[8100], visible=False)
        self.set_agent(triggerIds=[8101], visible=False)
        self.set_agent(triggerIds=[8102], visible=False)
        self.set_agent(triggerIds=[8103], visible=False)
        self.set_agent(triggerIds=[8104], visible=False)
        self.set_agent(triggerIds=[8105], visible=False)
        self.set_agent(triggerIds=[8106], visible=False)
        self.set_agent(triggerIds=[8107], visible=False)
        self.set_agent(triggerIds=[8108], visible=False)
        self.set_agent(triggerIds=[8109], visible=False)
        self.set_agent(triggerIds=[8110], visible=False)
        self.set_agent(triggerIds=[8111], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return JuntaApp04(self.ctx)


class JuntaApp04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        # 11001742_M_Junta 준타 Regen_A
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=900):
            return JuntaTalk01(self.ctx)

    def on_exit(self) -> None:
        self.set_skill(triggerIds=[7000], enable=True)
        # 올킬


class JuntaTalk01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5100], visible=False) # Sound_ShadowApp_Loop
        self.set_effect(triggerIds=[6100], visible=True) # Voice_Junta_00001773
        self.set_conversation(type=2, spawnId=11001557, script='$63000028_CS__BATTLE01__6$', arg4=4) # 준타 00001773

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return MeetJunta01(self.ctx)


class MeetJunta01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998])
        self.move_user_path(patrolName='MS2PatrolData_1003')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_102')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MeetJunta02(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class MeetJunta02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=701, enable=True)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.set_effect(triggerIds=[6002], visible=True) # Voice_Tinchai_00001686
        self.set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__7$', arg4=5) # 틴차이 00001686

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return MeetJunta03(self.ctx)


class MeetJunta03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Idle_A')
        self.remove_cinematic_talk()
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return MeetJunta04(self.ctx)


class MeetJunta04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6101], visible=True) # Voice_Junta_00001774
        self.set_conversation(type=2, spawnId=11001557, script='$63000028_CS__BATTLE01__8$', arg4=7) # 준타 00001774

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return MeetJunta05(self.ctx)


class MeetJunta05_Cskip(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=701, enable=True)
        self.set_effect(triggerIds=[5100], visible=False) # Sound_ShadowApp_Loop
        self.destroy_monster(spawnIds=[910,911,912,913,920,921,922,923,924,930,931,932,933,940,941,942,943,944,945,950,951,952,953,960,961,962,963,964,965])
        self.move_user_path(patrolName='MS2PatrolData_1003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return MeetJunta05_Cskip2(self.ctx)


class MeetJunta05_Cskip2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998])
        self.destroy_monster(spawnIds=[102,201])
        self.create_monster(spawnIds=[103,202], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetJunta06(self.ctx)

    def on_exit(self) -> None:
        self.remove_cinematic_talk()


class MeetJunta05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.remove_cinematic_talk()
        self.destroy_monster(spawnIds=[102,201])
        self.create_monster(spawnIds=[103,202], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return MeetJunta06(self.ctx)


class MeetJunta06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=701, enable=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=9900, type='trigger', achieve='complete_airstrikeofjunta')

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000451], questStates=[2]):
            # 별, 수정, 그리고 퀘스트 완료 가능 상태
            return FirstQuestEnd01(self.ctx)


class FirstQuestEnd01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questcomplete]] 준타와 대화하기
        self.show_guide_summary(entityId=10031010, textId=10031010)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000451], questStates=[3]):
            # 별, 수정, 그리고 퀘스트 완료 상태
            return SecondQuestStart01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=10031010)


class SecondQuestStart01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        # 가이드 : [[icon:questaccept]] 준타와 대화하기
        self.show_guide_summary(entityId=10031020, textId=10031020)

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000452], questStates=[1]):
            # 그림자의 파도 퀘스트 수락한 상태
            return Delay01(self.ctx)

    def on_exit(self) -> None:
        self.hide_guide_summary(entityId=10031020)


class Delay01(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return Delay02(self.ctx)


class Delay02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowWaveAgain01(self.ctx)


class ShadowWaveAgain01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user(mapId=63000028, portalId=12, boxId=9900)
        self.destroy_monster(spawnIds=[103,202])
        self.create_monster(spawnIds=[104,203], animationEffect=False)
        self.select_camera(triggerId=600, enable=True)
        self.set_scene_skip(state=TimeToLeave05, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return ShadowWaveAgain02(self.ctx)


# 정면 1차 스폰 후 다리 패트롤 바로 시작
class ShadowWaveAgain02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(triggerIds=[8100], visible=True)
        self.set_agent(triggerIds=[8101], visible=True)
        self.set_agent(triggerIds=[8102], visible=True)
        self.set_agent(triggerIds=[8103], visible=True)
        self.set_agent(triggerIds=[8106], visible=True)
        self.set_agent(triggerIds=[8107], visible=True)
        self.set_agent(triggerIds=[8108], visible=True)
        self.set_agent(triggerIds=[8109], visible=True)
        self.set_agent(triggerIds=[8110], visible=True)
        self.set_agent(triggerIds=[8111], visible=True)
        self.set_agent(triggerIds=[8112], visible=True)
        self.set_agent(triggerIds=[8113], visible=True)
        self.set_agent(triggerIds=[8114], visible=True)
        self.set_agent(triggerIds=[8115], visible=True)
        self.create_monster(spawnIds=[910,911,912,913])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowWaveAgain03(self.ctx)


# 정면 2차 스폰 후 다리 패트롤 바로 시작
class ShadowWaveAgain03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=601, enable=True)
        self.set_effect(triggerIds=[5100], visible=True) # Sound_ShadowApp_Loop
        self.set_effect(triggerIds=[6003], visible=True) # Voice_Tinchai_00001717
        self.set_conversation(type=1, spawnId=104, script='$63000028_CS__BATTLE01__9$', arg4=3, arg5=1) # 틴차이 00001717
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_103')
        self.move_user_path(patrolName='MS2PatrolData_1004')
        self.create_monster(spawnIds=[920,921,922,923,924])
        self.move_npc(spawnId=910, patrolName='MS2PatrolData_910')
        self.move_npc(spawnId=911, patrolName='MS2PatrolData_911')
        self.move_npc(spawnId=912, patrolName='MS2PatrolData_912')
        self.move_npc(spawnId=913, patrolName='MS2PatrolData_913')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowWaveAgain04(self.ctx)


# 카메라 워크
class ShadowWaveAgain04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=920, patrolName='MS2PatrolData_920')
        self.move_npc(spawnId=921, patrolName='MS2PatrolData_921')
        self.move_npc(spawnId=922, patrolName='MS2PatrolData_922')
        self.move_npc(spawnId=923, patrolName='MS2PatrolData_923')
        self.move_npc(spawnId=924, patrolName='MS2PatrolData_924')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ShadowWaveAgain05(self.ctx)


class ShadowWaveAgain05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[6102], visible=True) # Voice_Junta_00001775
        self.set_conversation(type=2, spawnId=11001557, script='$63000028_CS__BATTLE01__10$', arg4=4) # 준타 00001775
        self.create_monster(spawnIds=[930,931,932,933,950,951,952,953])
        self.move_npc(spawnId=930, patrolName='MS2PatrolData_930')
        self.move_npc(spawnId=931, patrolName='MS2PatrolData_931')
        self.move_npc(spawnId=932, patrolName='MS2PatrolData_932')
        self.move_npc(spawnId=933, patrolName='MS2PatrolData_933')
        self.move_npc(spawnId=950, patrolName='MS2PatrolData_950')
        self.move_npc(spawnId=951, patrolName='MS2PatrolData_951')
        self.move_npc(spawnId=952, patrolName='MS2PatrolData_952')
        self.move_npc(spawnId=953, patrolName='MS2PatrolData_953')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ShadowWaveAgain06(self.ctx)


# 양측 2차 스폰
class ShadowWaveAgain06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[940,941,942,943,944,945,960,961,962,963,964,965])
        self.move_npc(spawnId=940, patrolName='MS2PatrolData_940')
        self.move_npc(spawnId=941, patrolName='MS2PatrolData_941')
        self.move_npc(spawnId=942, patrolName='MS2PatrolData_942')
        self.move_npc(spawnId=943, patrolName='MS2PatrolData_943')
        self.move_npc(spawnId=944, patrolName='MS2PatrolData_944')
        self.move_npc(spawnId=945, patrolName='MS2PatrolData_945')
        self.move_npc(spawnId=960, patrolName='MS2PatrolData_960')
        self.move_npc(spawnId=961, patrolName='MS2PatrolData_961')
        self.move_npc(spawnId=962, patrolName='MS2PatrolData_962')
        self.move_npc(spawnId=963, patrolName='MS2PatrolData_963')
        self.move_npc(spawnId=964, patrolName='MS2PatrolData_964')
        self.move_npc(spawnId=965, patrolName='MS2PatrolData_965')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TimeToLeave01(self.ctx)


class TimeToLeave01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera(triggerId=602, enable=True)
        self.set_effect(triggerIds=[6004], visible=True) # Voice_Tinchai_00001687
        self.set_conversation(type=2, spawnId=11001708, script='$63000028_CS__BATTLE01__11$', arg4=4) # 틴차이 00001687
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=203, patrolName='MS2PatrolData_201')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=700):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=104, patrolName='MS2PatrolData_104')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return TimeToLeave04(self.ctx)


class TimeToLeave04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_user_path(patrolName='MS2PatrolData_1005')
        self.select_camera(triggerId=602, enable=False)
        self.remove_cinematic_talk()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return TimeToLeave05(self.ctx)


class TimeToLeave05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[104,203])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return PCTeleport01(self.ctx)


class PCTeleport01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.move_user(mapId=63000029, portalId=1, boxId=9900)

    def on_tick(self) -> trigger_api.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    pass


initial_state = Wait
