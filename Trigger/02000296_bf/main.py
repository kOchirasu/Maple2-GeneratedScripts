""" trigger/02000296_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[110], visible=False, animationEffect=False) # Enter
        set_ladder(triggerIds=[111], visible=False, animationEffect=False) # Enter
        set_ladder(triggerIds=[112], visible=False, animationEffect=False) # Enter
        set_ladder(triggerIds=[113], visible=False, animationEffect=False) # Enter
        destroy_monster(spawnIds=[5001]) # Mob
        destroy_monster(spawnIds=[5002]) # Mob
        destroy_monster(spawnIds=[5003]) # Mob
        destroy_monster(spawnIds=[5004]) # Mob
        destroy_monster(spawnIds=[5100]) # Boss
        destroy_monster(spawnIds=[5005]) # Blackeye_Actor01
        destroy_monster(spawnIds=[5006]) # Blackeye_Battle
        destroy_monster(spawnIds=[5007]) # Lennon_Battle
        destroy_monster(spawnIds=[5012]) # Blackeye_Actor02
        destroy_monster(spawnIds=[5013]) # Lennon_Actor
        set_effect(triggerIds=[1000], visible=True)
        set_effect(triggerIds=[4000], visible=False) # Intro_Chord
        set_mesh(triggerIds=[1001], visible=False, arg3=0, arg4=0, arg5=0) # SoulBead
        set_mesh(triggerIds=[1100], visible=True, arg3=0, arg4=0, arg5=0) # SoulBeadBarrier_AlwaysOn
        set_mesh(triggerIds=[1101], visible=True, arg3=0, arg4=0, arg5=0) # EnterBarrier
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=True, arg3=0, arg4=100, arg5=5) # ExitBridge
        set_portal(portalId=2, visible=True, enabled=False, minimapVisible=True)
        set_agent(triggerIds=[1300], visible=True)
        set_agent(triggerIds=[1301], visible=True)

    def on_tick(self) -> state.State:
        if check_user():
            return LoadingDelay01()


class LoadingDelay01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5007], arg2=False) # Lennon_Battle
        create_monster(spawnIds=[5005], arg2=False) # Blackeye_Actor01
        create_monster(spawnIds=[5001], arg2=False)
        create_monster(spawnIds=[5002], arg2=False)
        create_monster(spawnIds=[5003], arg2=False)
        create_monster(spawnIds=[5004], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LoadingDelay02()


class LoadingDelay02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=1, spawnId=5005, script='$02000296_BF__MAIN__0$', arg4=3, arg5=0)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LoadingDelay03()


class LoadingDelay03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_conversation(type=1, spawnId=5005, script='$02000296_BF__MAIN__1$', arg4=2, arg5=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return MeetLennon01()


#  레논 전투 중 
class MeetLennon01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return MeetLennon02()


class MeetLennon02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[5005]) # Blackeye_Actor01
        create_monster(spawnIds=[5012], arg2=False) # Blackeye_Actor02
        set_conversation(type=1, spawnId=5007, script='$02000296_BF__MAIN__2$', arg4=3, arg5=0) # Lennon_Battle
        set_conversation(type=1, spawnId=5007, script='$02000296_BF__MAIN__3$', arg4=3, arg5=3) # Lennon_Battle

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return MeetLennon03()


class MeetLennon03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=600, enable=False)
        select_camera(triggerId=601, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonLeave01()


class LennonLeave01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_npc(spawnId=5012, patrolName='MS2PatrolData_5012')
        set_conversation(type=1, spawnId=5012, script='$02000296_BF__MAIN__4$', arg4=3, arg5=1) # Blackeye_Battle

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return LennonLeave02()


class LennonLeave02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_agent(triggerIds=[1300], visible=False)
        set_agent(triggerIds=[1301], visible=False)
        change_monster(removeSpawnId=5012, addSpawnId=5006) # Blackeye_Battle
        change_monster(removeSpawnId=5007, addSpawnId=5013) # Lennon_Actor
        remove_balloon_talk(spawnId=5012)
        remove_balloon_talk(spawnId=5007)
        set_conversation(type=1, spawnId=5013, script='$02000296_BF__MAIN__5$', arg4=4, arg5=1) # Lennon_Actor
        move_npc(spawnId=5013, patrolName='MS2PatrolData_5009')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return LennonLeave03()


class Skip_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5005]) # Blackeye_Actor01
        create_monster(spawnIds=[5012], arg2=False) # Blackeye_Actor02
        change_monster(removeSpawnId=5012, addSpawnId=5006) # Blackeye_Battle
        change_monster(removeSpawnId=5007, addSpawnId=5013) # Lennon_Actor

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return LennonLeave03()


class LennonLeave03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        select_camera(triggerId=601, enable=False)
        destroy_monster(spawnIds=[5013]) # Lennon_Actor
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=False, arg3=500, arg4=100, arg5=5) # ExitBridge
        set_mesh(triggerIds=[1101], visible=False, arg3=0, arg4=0, arg5=0) # EnterBarrier
        set_ladder(triggerIds=[110], visible=True, animationEffect=True, animationDelay=0) # Enter
        set_ladder(triggerIds=[111], visible=True, animationEffect=True, animationDelay=0) # Enter
        set_ladder(triggerIds=[112], visible=True, animationEffect=True, animationDelay=0) # Enter
        set_ladder(triggerIds=[113], visible=True, animationEffect=True, animationDelay=0) # Enter

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReactSoulBead01()


class ReactSoulBead01(state.State):
    def on_enter(self):
        set_agent(triggerIds=[1300], visible=True)
        set_agent(triggerIds=[1301], visible=True)
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002961, textId=20002961) # 영혼의 구슬에 속박된 주민들을 구해주세요
        set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__6$', arg4=4, arg5=0) # Blackeye_Battle

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ReactSoulBead02()


class ReactSoulBead02(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=20002961)
        set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__7$', arg4=4, arg5=0) # Blackeye_Battle

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10000500,10000501,10000502,10000503], arg2=0):
            return BossBattle01()


class BossBattle01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[4000], visible=True) # Intro_Chord
        set_mesh(triggerIds=[1001], visible=True, arg3=0, arg4=0, arg5=2)
        set_effect(triggerIds=[1000], visible=False)
        set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__8$', arg4=3, arg5=0) # Blackeye_Battle

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return BossBattle02()


class BossBattle02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[5100], arg2=True) # Boss

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return BossBattle03()


class BossBattle03(state.State):
    def on_enter(self):
        play_system_sound_in_box(boxIds=[9001], sound='System_ShowGuideSummary_01')
        show_guide_summary(entityId=20002963, textId=20002963, duration=5000) # 악령술사 디툰을 처치하세요

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[5100]):
            return ReadyToMove01()


class ReadyToMove01(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5100,5001,5002,5003,5004])
        set_mesh(triggerIds=[1200,1201,1202,1203,1204,1205,1206,1207,1208,1209], visible=True, arg3=0, arg4=100, arg5=5) # ExitBridge
        set_agent(triggerIds=[1300], visible=False)
        set_agent(triggerIds=[1301], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ReadyToMove02()


class ReadyToMove02(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
        move_npc(spawnId=5006, patrolName='MS2PatrolData_5009')
        set_conversation(type=1, spawnId=5006, script='$02000296_BF__MAIN__9$', arg4=4, arg5=0) # Blackeye_Battle

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ReadyToMove03()


class ReadyToMove03(state.State):
    def on_enter(self):
        show_guide_summary(entityId=20002962, textId=20002962, duration=6000) # 다음 층으로 이동

    def on_tick(self) -> state.State:
        if npc_detected(boxId=9002, spawnIds=[5006]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[5006])


