""" trigger/52000118_qd/main.xml """
from common import *
import state


#  넬프의 집 : 60100015  
class ready(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100015], questStates=[2]):
            return fadeout()
        if quest_user_detected(boxIds=[2001], questIds=[60100015], questStates=[3]):
            return fadeout_a()


class fadeout(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 수상한 가면: 11003167
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        visible_my_pc(isVisible=False) # 유저 투명 처리
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        set_scene_skip(state=fadeout_a, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return suspiciousmask()


class suspiciousmask(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001,4002,4003], returnView=False)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__0$', duration=3000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return dooropen()


class dooropen(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        create_monster(spawnIds=[102], arg2=True) # 조디: 11003186

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return jordyspawn()


class jordyspawn(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__1$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return jordyin()


class jordyin(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__2$', duration=3000)
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__3$', duration=3000, illustId='Jordy_normal', align='Left')
        move_npc(spawnId=102, patrolName='MS2PatrolData_3001') # 조디 올라감

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return jordyhello()


class jordyhello(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__4$', duration=1000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return huk()


class huk(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=1000)
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__5$', duration=1000, align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return suspiciousmaskmove()


class suspiciousmaskmove(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3002') # 수상한 가면 뒤 돌아봄

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return talk_01()


class talk_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=10000)
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_02()


class talk_02(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__7$', duration=3000, illustId='Jordy_normal', align='Left')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__8$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return talk_03()


class talk_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__9$', duration=3000, illustId='Jordy_normal', align='Left')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__10$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return talk_04()


class talk_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__11$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return killyou()


class killyou(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_B')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_05()


class talk_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__13$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_06()


class talk_06(state.State):
    def on_enter(self):
        set_sound(triggerId=7001, arg2=True)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return camera_01()


class camera_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return camera_02()


class camera_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return talk_07()


class talk_07(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__15$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return talk_08()


class talk_08(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__16$', duration=3000, illustId='Jordy_normal', align='Left')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return talk_09()


class talk_09(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__18$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_10()


class talk_10(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__19$', duration=3000, illustId='Jordy_normal', align='Left')
        add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__20$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return talk_11()


class talk_11(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_12()


class talk_12(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        move_npc(spawnId=101, patrolName='MS2PatrolData_3005') # 수상한 가면 내려감
        move_npc(spawnId=102, patrolName='MS2PatrolData_3003') # 조디 비켜줌
        add_balloon_talk(spawnId=102, msg='$52000118_QD__MAIN__22$', duration=4000)
        add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__23$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return fadeout_a()


class fadeout_a(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)
        visible_my_pc(isVisible=True) # 유저 투명 처리 해제
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[104], arg2=True) # 조디
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return fadein_a()


class fadein_a(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$52000118_QD__MAIN__24$', arg3='3000', arg4='0')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


