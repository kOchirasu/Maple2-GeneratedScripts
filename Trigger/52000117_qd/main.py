""" trigger/52000117_qd/main.xml """
from common import *
import state


#  트라이아 청사 : 60100015  
class ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=True) # 조디

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100015], questStates=[1]):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadein()

    def on_exit(self):
        move_user(mapId=52000117, portalId=6001)


class fadein(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return jordyidle()


class jordyidle(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__0$', duration=3000, illustId='Jordy_normal', align='Left')
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__1$', duration=3000)
        set_scene_skip(state=end, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return pcmove()


class pcmove(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_3002')
        set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__2$', duration=3000)
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return wow()


class wow(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])
        add_cinematic_talk(npcId=0, msg='$52000117_QD__MAIN__15$', duration=2000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=3000)
        set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=3000)
        add_balloon_talk(spawnId=101, msg='$52000117_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_01()


class scene_01(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=101, msg='$52000117_QD__MAIN__6$', duration=3000)
        move_npc(spawnId=101, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return scene_02()


class scene_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False) # 대화 모습
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__7$', duration=3000)
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        set_pc_emotion_loop(sequenceName='Emotion_Dance_S', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return pctalk()


class pctalk(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Talk_A','Talk_B'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return scene_03()


class scene_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__8$', duration=3000)
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__9$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return scene_04()


class scene_04(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__10$', duration=3000)
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return scene_05()


class scene_05(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__12$', duration=3000)
        add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return scene_06()


class scene_06(state.State):
    def on_enter(self):
        move_npc(spawnId=101, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_fadeout()


class scene_fadeout(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return jordydel()


class jordydel(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return scene_fadein()


class scene_fadein(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return end()


class end(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[101])
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_achievement(triggerId=2001, type='trigger', achieve='jordyhello')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return endmessage()


class endmessage(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        set_event_ui(type=1, arg2='$52000117_QD__MAIN__14$', arg3='3000', arg4='0')
        move_user(mapId=52000118, portalId=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return endmessage()


