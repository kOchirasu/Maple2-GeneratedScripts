""" trigger/02020021_bf/main.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=True)
        set_agent(triggerIds=[9002], visible=True)
        set_agent(triggerIds=[9003], visible=True)
        set_agent(triggerIds=[9004], visible=True)
        set_agent(triggerIds=[9005], visible=True)
        set_agent(triggerIds=[9006], visible=True)
        set_agent(triggerIds=[9007], visible=True)
        set_agent(triggerIds=[9008], visible=True)
        set_user_value(triggerId=99990002, key='battlesetting', value=0)
        set_user_value(triggerId=99990003, key='Timer', value=0)
        set_user_value(triggerId=99990004, key='SpecialTimer', value=0)
        set_user_value(triggerId=99990002, key='SpecialTimer', value=0)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 카메라_시작()


class 카메라_시작(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        create_monster(spawnIds=[202], arg2=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_캡션()


class 카메라_캡션(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[501,502], returnView=False)
        show_caption(type='VerticalCaption', title='$02020021_BF__main__3$', desc='$02020021_BF__main__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_샤텐대사1()


class 카메라_샤텐대사1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[503,504], returnView=False)
        add_cinematic_talk(npcId=23200085, illustId='Schatten_normal', msg='$02020021_BF__main__0$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_샤텐대사2()


class 카메라_샤텐대사2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=23200085, illustId='Schatten_normal', msg='$02020021_BF__main__1$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_샤텐대사3()


class 카메라_샤텐대사3(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[505,506], returnView=False)
        add_cinematic_talk(npcId=23200085, illustId='Schatten_normal', msg='$02020021_BF__main__2$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_샤텐대사4()


class 카메라_샤텐대사4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[507,508], returnView=False)
        add_cinematic_talk(npcId=23200085, illustId='Schatten_normal', msg='$02020021_BF__main__5$', duration=4000, align='left')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[202])
        create_monster(spawnIds=[201], arg2=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.1)

    def on_tick(self) -> state.State:
        if all_of():
            return 전투시작()


class 전투시작(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_agent(triggerIds=[9008], visible=False)
        set_ai_extra_data(key='Start', value=1)
        side_npc_talk(npcId=23200085, illust='Schatten_smile', duration=5000, script='$02020021_BF__main__6$', voice='ko/Npc/00002248')
        set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990003" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990004" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return 랭크체크대사()


class 랭크체크대사(state.State):
    def on_tick(self) -> state.State:
        if dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            side_npc_talk(npcId=23200085, illust='Schatten_smile', duration=5000, script='$02020021_BF__main__7$', voice='ko/Npc/00002082')
            return 던전종료_A랭크이상()
        if dungeon_first_user_mission_score(score=1500, operator='Less'):
            side_npc_talk(npcId=23200085, illust='Schatten_serious', duration=5000, script='$02020021_BF__main__8$', voice='ko/Npc/00002081')
            return 던전종료_A랭크미만()


class 던전종료_A랭크이상(state.State):
    def on_enter(self):
        dungeon_clear()


class 던전종료_A랭크미만(state.State):
    def on_enter(self):
        dungeon_fail()


