""" trigger/02000296_bf/main.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_ladder(triggerIds=[110], visible=False, animationEffect=False) # Enter
        self.set_ladder(triggerIds=[111], visible=False, animationEffect=False) # Enter
        self.set_ladder(triggerIds=[112], visible=False, animationEffect=False) # Enter
        self.set_ladder(triggerIds=[113], visible=False, animationEffect=False) # Enter
        self.destroy_monster(spawnIds=[5001]) # Mob
        self.destroy_monster(spawnIds=[5002]) # Mob
        self.destroy_monster(spawnIds=[5003]) # Mob
        self.destroy_monster(spawnIds=[5004]) # Mob
        self.destroy_monster(spawnIds=[5100]) # Boss
        self.destroy_monster(spawnIds=[5005]) # Blackeye_Actor01
        self.destroy_monster(spawnIds=[5006]) # Blackeye_Battle
        self.destroy_monster(spawnIds=[5007]) # Lennon_Battle
        self.destroy_monster(spawnIds=[5012]) # Blackeye_Actor02
        self.destroy_monster(spawnIds=[5013]) # Lennon_Actor
        self.set_effect(triggerIds=[1000], visible=True)
        self.set_effect(triggerIds=[4000], visible=False) # Intro_Chord
        self.set_mesh(triggerIds=[1001], visible=False, arg3=0, delay=0, scale=0) # SoulBead
        self.set_mesh(triggerIds=[1100], visible=True, arg3=0, delay=0, scale=0) # SoulBeadBarrier_AlwaysOn
        self.set_mesh(triggerIds=[1101], visible=True, arg3=0, delay=0, scale=0) # EnterBarrier
        self.set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=True, arg3=0, delay=100, scale=5) # ExitBridge
        self.set_portal(portalId=2, visible=True, enable=False, minimapVisible=True)
        self.set_agent(triggerIds=[1300], visible=True)
        self.set_agent(triggerIds=[1301], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.check_user():
            return LoadingDelay01(self.ctx)


class LoadingDelay01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[5007], animationEffect=False) # Lennon_Battle
        self.create_monster(spawnIds=[5005], animationEffect=False) # Blackeye_Actor01
        self.create_monster(spawnIds=[5001], animationEffect=False)
        self.create_monster(spawnIds=[5002], animationEffect=False)
        self.create_monster(spawnIds=[5003], animationEffect=False)
        self.create_monster(spawnIds=[5004], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LoadingDelay02(self.ctx)


class LoadingDelay02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=1, spawnId=5005, script='$02000296_BF__MAIN__0$', arg4=3, arg5=0)
        self.set_scene_skip(state=Skip_1, action='nextState')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return LoadingDelay03(self.ctx)


class LoadingDelay03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_conversation(type=1, spawnId=5005, script='$02000296_BF__MAIN__1$', arg4=2, arg5=1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return MeetLennon01(self.ctx)


# 레논 전투 중
class MeetLennon01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return MeetLennon02(self.ctx)


class MeetLennon02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.destroy_monster(spawnIds=[5005]) # Blackeye_Actor01
        self.create_monster(spawnIds=[5012], animationEffect=False) # Blackeye_Actor02
        self.set_conversation(type=1, spawnId=5007, script='$02000296_BF__MAIN__2$', arg4=3, arg5=0) # Lennon_Battle
        self.set_conversation(type=1, spawnId=5007, script='$02000296_BF__MAIN__3$', arg4=3, arg5=3) # Lennon_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return MeetLennon03(self.ctx)


class MeetLennon03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=600, enable=False)
        self.select_camera(triggerId=601, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonLeave01(self.ctx)


class LennonLeave01(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_npc(spawnId=5012, patrolName='MS2PatrolData_5012')
        self.set_conversation(type=1, spawnId=5012, script='$02000296_BF__MAIN__4$', arg4=3, arg5=1) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return LennonLeave02(self.ctx)


class LennonLeave02(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_agent(triggerIds=[1300], visible=False)
        self.set_agent(triggerIds=[1301], visible=False)
        self.change_monster(removeSpawnId=5012, addSpawnId=5006) # Blackeye_Battle
        self.change_monster(removeSpawnId=5007, addSpawnId=5013) # Lennon_Actor
        self.remove_balloon_talk(spawnId=5012)
        self.remove_balloon_talk(spawnId=5007)
        self.set_conversation(type=1, spawnId=5013, script='$02000296_BF__MAIN__5$', arg4=4, arg5=1) # Lennon_Actor
        self.move_npc(spawnId=5013, patrolName='MS2PatrolData_5009')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7000):
            return LennonLeave03(self.ctx)


class Skip_1(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5005]) # Blackeye_Actor01
        self.create_monster(spawnIds=[5012], animationEffect=False) # Blackeye_Actor02
        self.change_monster(removeSpawnId=5012, addSpawnId=5006) # Blackeye_Battle
        self.change_monster(removeSpawnId=5007, addSpawnId=5013) # Lennon_Actor

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return LennonLeave03(self.ctx)


class LennonLeave03(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.select_camera(triggerId=601, enable=False)
        self.destroy_monster(spawnIds=[5013]) # Lennon_Actor
        self.set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=False, arg3=500, delay=100, scale=5) # ExitBridge
        self.set_mesh(triggerIds=[1101], visible=False, arg3=0, delay=0, scale=0) # EnterBarrier
        self.set_ladder(triggerIds=[110], visible=True, animationEffect=True, animationDelay=0) # Enter
        self.set_ladder(triggerIds=[111], visible=True, animationEffect=True, animationDelay=0) # Enter
        self.set_ladder(triggerIds=[112], visible=True, animationEffect=True, animationDelay=0) # Enter
        self.set_ladder(triggerIds=[113], visible=True, animationEffect=True, animationDelay=0) # Enter

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReactSoulBead01(self.ctx)


class ReactSoulBead01(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[1300], visible=True)
        self.set_agent(triggerIds=[1301], visible=True)
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002961, textId=20002961) # 영혼의 구슬에 속박된 주민들을 구해주세요
        self.set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__6$', arg4=4, arg5=0) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return ReactSoulBead02(self.ctx)


class ReactSoulBead02(trigger_api.Trigger):
    def on_enter(self):
        self.hide_guide_summary(entityId=20002961)
        self.set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__7$', arg4=4, arg5=0) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.object_interacted(interactIds=[10000500,10000501,10000502,10000503], stateValue=0):
            return BossBattle01(self.ctx)


class BossBattle01(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[4000], visible=True) # Intro_Chord
        self.set_mesh(triggerIds=[1001], visible=True, arg3=0, delay=0, scale=2)
        self.set_effect(triggerIds=[1000], visible=False)
        self.set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__8$', arg4=3, arg5=0) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return BossBattle02(self.ctx)


class BossBattle02(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[5100], animationEffect=True) # Boss

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return BossBattle03(self.ctx)


class BossBattle03(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        self.show_guide_summary(entityId=20002963, textId=20002963, duration=5000) # 악령술사 디툰을 처치하세요

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[5100]):
            return ReadyToMove01(self.ctx)


class ReadyToMove01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5100,5001,5002,5003,5004])
        self.set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=True, arg3=0, delay=100, scale=5) # ExitBridge
        self.set_agent(triggerIds=[1300], visible=False)
        self.set_agent(triggerIds=[1301], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return ReadyToMove02(self.ctx)


class ReadyToMove02(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)
        self.move_npc(spawnId=5006, patrolName='MS2PatrolData_5009')
        self.set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__9$', arg4=4, arg5=0) # Blackeye_Battle

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return ReadyToMove03(self.ctx)


class ReadyToMove03(trigger_api.Trigger):
    def on_enter(self):
        self.show_guide_summary(entityId=20002962, textId=20002962, duration=6000) # 다음 층으로 이동

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=9002, spawnIds=[5006]):
            return Quit(self.ctx)


class Quit(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[5006])


initial_state = 대기
