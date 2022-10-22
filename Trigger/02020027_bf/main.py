""" trigger/02020027_bf/main.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8001], visible=True)
        set_agent(triggerIds=[8002], visible=True)
        set_agent(triggerIds=[8003], visible=True)
        set_agent(triggerIds=[8004], visible=True)
        set_agent(triggerIds=[8005], visible=True)
        set_agent(triggerIds=[8006], visible=True)
        set_agent(triggerIds=[8007], visible=True)
        set_agent(triggerIds=[8008], visible=True)
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_user_value(triggerId=99990003, key='Timer', value=0)
        set_user_value(triggerId=99990011, key='SpecialTimer', value=0)
        set_user_value(triggerId=99990002, key='battlesetting', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1001]):
            return 카메라_시작()


class 카메라_시작(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        move_user(mapId=2020027, portalId=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_캡션()


class 카메라_캡션(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[5001,5002], returnView=False)
        show_caption(type='VerticalCaption', title='$02020027_BF__main__2$', desc='$02020027_BF__main__3$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 유저연출()


class 유저연출(state.State):
    def on_enter(self):
        select_camera(triggerId=5003, enable=True)
        set_conversation(type=1, spawnId=0, script='$02020027_BF__main__4$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 카메라_메이슨설명1()


class 카메라_메이슨설명1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 유저연출_2()


class 유저연출_2(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=202, sequenceName='Talk_B', duration=18430)
        set_conversation(type=1, spawnId=0, script='$02020027_BF__main__5$', arg4=3, arg5=0)
        add_cinematic_talk(npcId=24120006, illustId='Mason_normal', msg='$02020027_BF__main__0$', duration=4000, align='left')
        remove_buff(boxId=901, skillId=51200001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_메이슨설명2()


class 카메라_메이슨설명2(state.State):
    def on_enter(self):
        select_camera(triggerId=5004, enable=True)
        add_cinematic_talk(npcId=24120006, illustId='Mason_normal', msg='$02020027_BF__main__1$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_메이슨설명3()


class 카메라_메이슨설명3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24120006, illustId='Mason_normal', msg='$02020027_BF__main__6$', duration=4000, align='left')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.1)
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if all_of():
            return 전투_진행()


class 전투_진행(state.State):
    def on_enter(self):
        set_agent(triggerIds=[8001], visible=False)
        set_agent(triggerIds=[8002], visible=False)
        set_agent(triggerIds=[8003], visible=False)
        set_agent(triggerIds=[8004], visible=False)
        set_agent(triggerIds=[8005], visible=False)
        set_agent(triggerIds=[8006], visible=False)
        set_agent(triggerIds=[8007], visible=False)
        set_agent(triggerIds=[8008], visible=False)
        set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990003" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990011" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return 랭크체크대사()


class 랭크체크대사(state.State):
    def on_tick(self) -> state.State:
        if dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            side_npc_talk(npcId=24120006, illust='Mason_normal', duration=6089, script='$02020027_BF__main__7$', voice='ko/Npc/00002100')
            return 던전종료_A랭크이상()
        if dungeon_first_user_mission_score(score=1500, operator='Less'):
            side_npc_talk(npcId=24120006, illust='Mason_closeEye', duration=5000, script='$02020027_BF__main__8$', voice='ko/Npc/00002099')
            return 던전종료_A랭크미만()


class 던전종료_A랭크이상(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        dungeon_clear()


class 던전종료_A랭크미만(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[-1])
        dungeon_fail()


