""" trigger/52000068_qd/tria_seige_movie.xml """
from common import *
import state


class start(state.State):
    def on_tick(self) -> state.State:
        if user_value(key='tria_seige', value=1):
            return LoadingDelayB0()


#  챕터5 에필로그 [10002105 엇갈리는 마음]완료 시 연출맵으로 이동
class LoadingDelayB0(state.State):
    def on_enter(self):
        set_scene_skip(state=NPC이동, arg2='nextState')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skill(triggerIds=[701], isEnable=True)
        set_actor(triggerId=11010, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=11010, visible=True, initialSequence='Dead_A')
        set_actor(triggerId=16000, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=16001, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=16002, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16003, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16004, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16005, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16006, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16007, visible=True, initialSequence='Stun_A')
        set_actor(triggerId=16008, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16009, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16010, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16011, visible=True, initialSequence='Idle_A')
        set_actor(triggerId=16012, visible=True, initialSequence='Stun_A')
        create_monster(spawnIds=[10000,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013,10014,10015,10016,10017,10018,10019,10020,10021,10022,10023], arg2=False)
        create_monster(spawnIds=[10024,10025,10026,10027,10028,10029,10030,10031,10032,10033,10034], arg2=False)
        set_visible_breakable_object(triggerIds=[5000,5002,5003,5004,5005,5006,5007,5008,5009,5010,5011,5012], arg2=False)
        create_monster(spawnIds=[11000,11001,11002,11003,11004,11005,11006,11007], arg2=False)
        create_monster(spawnIds=[11009], arg2=False)
        set_sound(triggerId=90000, arg2=True) # TriaAttack

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LoadingDelayB1()


class LoadingDelayB1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 원경카메라01()


class 원경카메라01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[12000,12001], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 원경카메라02()


class 원경카메라02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[12002,12003], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 원경카메라03()


class 원경카메라03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[12004,12005], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 프레이대사()


class 프레이대사(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11000064, illustId='Lennon_closeEye', msg='$52000068_QD__TRIA_SEIGE_MOVIE__0$', duration=5000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 알론대사()


class 알론대사(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000076, script='$52000068_QD__TRIA_SEIGE_MOVIE__1$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 근위대원등장()


class 근위대원등장(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=2)
        create_monster(spawnIds=[11008], arg2=False)
        move_npc(spawnId=11008, patrolName='MS2PatrolData_soldier') # 에레브 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 근위대대사01()


class 근위대대사01(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001968, script='$52000068_QD__TRIA_SEIGE_MOVIE__2$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 근위대대사02()


class 근위대대사02(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001968, script='$52000068_QD__TRIA_SEIGE_MOVIE__3$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 근위대대사03()


class 근위대대사03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11000601, script='$52000068_QD__TRIA_SEIGE_MOVIE__4$', arg4=5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 근위대대사04()


class 근위대대사04(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return NPC이동()


class NPC이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeOut.xml')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.5)
        move_npc(spawnId=11000, patrolName='MS2PatrolData_GoToJody_ereb') # 에레브 이동
        move_npc(spawnId=11001, patrolName='MS2PatrolData_GoToJody_karl') # 칼 이동
        move_npc(spawnId=11002, patrolName='MS2PatrolData_GoToJody_luana') # 루아나 이동
        move_npc(spawnId=11003, patrolName='MS2PatrolData_GoToJody_BlackEye') # 블랙아이 이동
        move_npc(spawnId=11004, patrolName='MS2PatrolData_GoToJody_lennon') # 레논 이동
        move_npc(spawnId=11005, patrolName='MS2PatrolData_GoToJody_eve') # 이브 이동
        move_npc(spawnId=11006, patrolName='MS2PatrolData_GoToJody_alon') # 알론 이동
        move_npc(spawnId=11007, patrolName='MS2PatrolData_GoToJody_pray') # 프레이 이동

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=20000):
            return None # Missing State: 지원군등장


