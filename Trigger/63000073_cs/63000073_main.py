""" trigger/63000073_cs/63000073_main.xml """
from common import *
import state


class 준비(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        create_monster(spawnIds=[101], arg2=True)
        create_monster(spawnIds=[102], arg2=True)
        create_monster(spawnIds=[103], arg2=True)
        create_monster(spawnIds=[104], arg2=True)
        create_monster(spawnIds=[105], arg2=True)
        create_monster(spawnIds=[106], arg2=True)
        create_monster(spawnIds=[107], arg2=True)
        create_monster(spawnIds=[108], arg2=True)
        create_monster(spawnIds=[109], arg2=True)
        create_monster(spawnIds=[110], arg2=True)
        create_monster(spawnIds=[111], arg2=True)
        create_monster(spawnIds=[112], arg2=True)
        create_monster(spawnIds=[113], arg2=True)
        create_monster(spawnIds=[114], arg2=True)
        create_monster(spawnIds=[115], arg2=True)
        create_monster(spawnIds=[116], arg2=True)
        create_monster(spawnIds=[117], arg2=True)
        set_ladder(triggerIds=[6001], visible=False, animationEffect=False)
        set_ladder(triggerIds=[6002], visible=False, animationEffect=False)
        set_ladder(triggerIds=[6003], visible=False, animationEffect=False)
        set_ladder(triggerIds=[6004], visible=False, animationEffect=False)
        set_mesh(triggerIds=[4001], visible=True)
        set_mesh(triggerIds=[4002], visible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[701], questIds=[30000372], questStates=[3]):
            return 전투만()
        if quest_user_detected(boxIds=[701], questIds=[30000372], questStates=[2]):
            return 퀘완료가능재입장()
        if quest_user_detected(boxIds=[701], questIds=[30000372], questStates=[1]):
            return 잠시대기_01()
        if user_detected(boxIds=[701]):
            return 전투만()


class 전투만(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[115]):
            return 종료()

    def on_exit(self):
        set_ladder(triggerIds=[6001], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6002], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6003], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6004], visible=True, animationEffect=True)


class 잠시대기_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[121], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 잠시대기_02()


class 잠시대기_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스퇴장_01()


class 보보스퇴장_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=보보스퇴장_03, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스퇴장_02()


class 보보스퇴장_02(state.State):
    def on_enter(self):
        move_npc(spawnId=121, patrolName='MS2PatrolData_2001')
        add_balloon_talk(spawnId=121, msg='$63000073_CS__63000073_MAIN__0$', duration=2500, delayTick=1000) # 책 틈에서 지내게 해줬으니, 소원 들어준 거야…

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 보보스퇴장_03()


class 보보스퇴장_03(state.State):
    def on_enter(self):
        set_scene_skip()
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 보보스퇴장_04()

    def on_exit(self):
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[121])


class 보보스퇴장_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        show_guide_summary(entityId=26300731, textId=26300731)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[115]):
            return 사다리등장_01()


class 사다리등장_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=26300731)
        set_ladder(triggerIds=[6001], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6002], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6003], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6004], visible=True, animationEffect=True)
        show_guide_summary(entityId=26300733, textId=26300733)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001385], arg2=0):
            return 트렁크오픈_01()


class 트렁크오픈_01(state.State):
    def on_enter(self):
        hide_guide_summary(entityId=26300733)
        create_monster(spawnIds=[122], arg2=False)
        set_mesh(triggerIds=[4001], visible=False)
        set_mesh(triggerIds=[4002], visible=True)
        show_guide_summary(entityId=26300732, textId=26300732)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[702], questIds=[30000372], questStates=[2]):
            return 트렁크오픈_02()


class 퀘완료가능재입장(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        create_monster(spawnIds=[122], arg2=False)
        set_mesh(triggerIds=[4001], visible=False)
        set_mesh(triggerIds=[4002], visible=True)
        set_ladder(triggerIds=[6001], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6002], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6003], visible=True, animationEffect=True)
        set_ladder(triggerIds=[6004], visible=True, animationEffect=True)
        move_user(mapId=63000073, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 트렁크오픈_02()


class 트렁크오픈_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        hide_guide_summary(entityId=26300732)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 트렁크오픈_03()


class 트렁크오픈_03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_2002')
        select_camera_path(pathIds=[8002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 트렁크오픈_04()


class 트렁크오픈_04(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_halfsec.xml')
        set_scene_skip(state=에이든퇴장_01, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에이든대화_01()


class 에이든대화_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)
        set_npc_emotion_sequence(spawnId=122, sequenceName='Idle_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에이든대화_02()


class 에이든대화_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11004359, msg='$63000073_CS__63000073_MAIN__1$', duration=2500, align='right', illustId='0') # 아… 머리야.\n이게 어떻게 된 일이지

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에이든대화_03()


class 에이든대화_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8004], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에이든대화_04()


class 에이든대화_04(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=2500)
        add_cinematic_talk(npcId=0, msg='$63000073_CS__63000073_MAIN__2$', duration=2500, align='right') # $npcName:11004359$이지?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 에이든대화_05()


class 에이든대화_05(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Talk_A', duration=2500)
        add_cinematic_talk(npcId=0, msg='$63000073_CS__63000073_MAIN__3$', duration=4500, align='right') # 네 동생, $npcName:11004354$$pp:가,이$ 마을에서 널 기다리고 있어.\n마을에서 같이 부모님을 찾아보자고 하는데.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에이든대화_06()


class 에이든대화_06(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[8003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에이든대화_07()


class 에이든대화_07(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=3500)
        add_cinematic_talk(npcId=11004359, msg='$63000073_CS__63000073_MAIN__4$', duration=3500, align='right', illustId='0') # …뭐라고?\n그럼… 나만 당한 게 아닌 건가?

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 에이든대화_08()


class 에이든대화_08(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=122, sequenceName='Talk_A', duration=4500)
        add_cinematic_talk(npcId=11004359, msg='$63000073_CS__63000073_MAIN__5$', duration=4500, align='right', illustId='0') # 어서 $npcName:11004354$$pp:를,을$ 만나봐야겠군.\n먼저 출발할게, 마을에서 보자.

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 에이든퇴장_01()


class 에이든퇴장_01(state.State):
    def on_enter(self):
        set_scene_skip()
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        destroy_monster(spawnIds=[122])

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


