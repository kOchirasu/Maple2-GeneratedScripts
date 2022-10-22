""" trigger/52020010_qd/main_b.xml """
from common import *
import state


class Idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2006], questIds=[60200055], questStates=[1]):
            return Object_Check()


class Object_Check(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001276], arg2=0):
            return Ready()


class Ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Move_6001()


class Move_6001(state.State):
    def on_enter(self):
        move_user(mapId=52020010, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Event_01()


class Event_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_sequence(sequenceNames=['Object_React_H'])
        add_cinematic_talk(npcId=0, msg='왜 아무일도 일어나지 않는거지?', duration=2800)
        set_scene_skip(state=Next, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return Event_02()


class Event_02(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Object_React_G'])
        add_cinematic_talk(npcId=0, msg='두들겨 볼까?', duration=2800)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_03()


class Event_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003610, msg='으으으.... 시끄럽구나!', duration=2800) # 11003610: 틱택톡
        add_balloon_talk(spawnId=0, msg='!!!', duration=2000, delayTick=1000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_04()


class Event_04(state.State):
    def on_enter(self):
        create_monster(spawnIds=[501], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return Event_05()


class Event_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003610, msg='네 놈이냐! 내 잠을 깨운 녀석이!', duration=2800) # 11003610: 틱택톡

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_06()


class Event_06(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003610, msg='감히 내 시간을 방해하다니 가만두지 않겠다!', duration=2800) # 11003610: 틱택톡

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Next()


class Next(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[501])
        create_monster(spawnIds=[601], arg2=True)

    def on_tick(self) -> state.State:
        if true():
            return Battle()


class Battle(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601]):
            return Mission_Clear()


class Mission_Clear(state.State):
    def on_enter(self):
        set_achievement(type='trigger', achieve='ClockDevil')

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[2006], questIds=[60200050], questStates=[1]):
            return Mission_Clear()
        if quest_user_detected(boxIds=[2006], questIds=[60200055], questStates=[2]):
            return Event_07()


class Event_07(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=11003603, illustId='0', msg='인간! 파편이 돌아왔다! 어서 이리 와라!', duration=2800, align='Left') # 11003603: 틱토그

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Event_End()


class Event_End(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


