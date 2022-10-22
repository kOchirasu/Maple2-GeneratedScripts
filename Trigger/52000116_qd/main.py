""" trigger/52000116_qd/main.xml """
from common import *
import state


class idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2001], questIds=[60100001], questStates=[1]):
            return ready()
        if quest_user_detected(boxIds=[2001], questIds=[60100001], questStates=[2]):
            return fadeout()
        if quest_user_detected(boxIds=[2001], questIds=[60100001], questStates=[3]):
            return fadeout()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003163, illustId='Nelf_normal', msg='$52000116_QD__MAIN__0$', duration=4000, align='Right') # 11003163: 넬프
        set_scene_skip(state=fadeout, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return jordyspawn()


class jordyspawn(state.State):
    def on_enter(self):
        move_user(mapId=52000116, portalId=2)
        set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')
        create_monster(spawnIds=[102], arg2=True) # 102:조디
        select_camera_path(pathIds=[4003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return jordyhelp()


class jordyhelp(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/Sound/Eff_Object_Castle_Door_Open_01.xml')
        set_conversation(type=2, spawnId=11001838, script='$52000116_QD__MAIN__1$', arg4=1, arg5=0) # 조디 계단 올라가며 하는 대사
        move_npc(spawnId=102, patrolName='MS2PatrolData_3002')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return wowspawn()


class wowspawn(state.State):
    def on_enter(self):
        create_monster(spawnIds=[103], arg2=True) # 103:연출용 강아지
        set_conversation(type=1, spawnId=102, script='$52000116_QD__MAIN__2$', arg4=2, arg5=0) # 조디 뒤로 돌아서 하는 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return camera()


class camera(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wow()


class wow(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=103, sequenceName='Attack_01_A')
        set_conversation(type=2, spawnId=11003179, script='$52000116_QD__MAIN__3$', arg4=2, arg5=0) # 강아지 짖는 대사

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return save()


class save(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_npc_emotion_loop(spawnId=102, sequenceName='Sit_Down_A', duration=400000)
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return battleready()


class battleready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104], arg2=True, arg3=500) # 멍멍이 몬스터

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return battle()


class battle(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=104, sequenceName='Attack_Idle_A', duration=10000)
        reset_camera(interpolationTime=0.5)
        move_user_path(patrolName='MS2PatrolData_3003')
        set_conversation(type=1, spawnId=102, script='$52000116_QD__MAIN__4$', arg4=2, arg5=0) # 조디 말풍선
        set_conversation(type=1, spawnId=101, script='$52000116_QD__MAIN__5$', arg4=2, arg5=0) # 넬프 말풍선
        set_conversation(type=1, spawnId=102, script='$52000116_QD__MAIN__6$', arg4=2, arg5=3) # 조디 말풍선

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return camera_A()


class camera_A(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        move_npc(spawnId=104, patrolName='MS2PatrolData_3005')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Motion()


class Motion(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return lol()


class lol(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='Damg_A')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return run()


class run(state.State):
    def on_enter(self):
        move_npc(spawnId=104, patrolName='MS2PatrolData_3004')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return fadeout()


class fadeout(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102,103,104])
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        create_monster(spawnIds=[105], arg2=True) # 조디

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return fadein()


class fadein(state.State):
    def on_enter(self):
        move_user(mapId=52000116, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return thank()


class thank(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=105, sequenceName='Talk_A')
        select_camera_path(pathIds=[4002], returnView=False) # 조디 얼굴로 클로즈업
        add_cinematic_talk(npcId=11003164, msg='$52000116_QD__MAIN__7$', duration=2000)
        set_scene_skip(state=end, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return endready()


class endready(state.State):
    def on_enter(self):
        show_caption(scale=2.3, type='NameCaption', title='$52000116_QD__MAIN__8$', desc='$52000116_QD__MAIN__9$', align='centerLeft', offsetRateX=-0.15, duration=4000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return end()


class end(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='jordy')
        reset_camera(interpolationTime=0.5)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


