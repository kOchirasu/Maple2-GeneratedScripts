""" trigger/02020019_bf/02020019_main.xml """
from common import *
import state


class 입장(state.State):
    def on_enter(self):
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        move_user(mapId=2020019, portalId=1)
        set_user_value(triggerId=99990002, key='battlesetting', value=0)
        set_user_value(triggerId=99990004, key='Timer', value=0)
        set_user_value(triggerId=99990005, key='SpecialTimer', value=0)
        set_user_value(triggerId=99990002, key='SpecialTimer', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 카메라_시작()


class 카메라_시작(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        move_user(mapId=2020019, portalId=1)
        create_monster(spawnIds=[101,102,103], arg2=False) # <네이린과 대포 스폰(아군)>
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_캡션()


class 카메라_캡션(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[501,502], returnView=False)
        show_caption(type='VerticalCaption', title='$02020019_BF__02020019_main__3$', desc='$02020019_BF__02020019_main__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_네이린설명1()


class 카메라_네이린설명1(state.State):
    def on_enter(self):
        select_camera(triggerId=503, enable=True)
        add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020019_BF__02020019_main__0$', duration=4000, align='left')
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6300)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_네이린설명2()


class 카메라_네이린설명2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020019_BF__02020019_main__1$', duration=4000, align='left') # action name="AddCinematicTalk" npcID="24100001" illustID="Neirin_normal" msg="$02020019_BF__02020019_main__2$" duration="4000" align="left" /

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_네이린설명3()


class 카메라_네이린설명3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020019_BF__02020019_main__5$', duration=4000, align='left')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_종료()


class 카메라_종료(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0.1)

    def on_tick(self) -> state.State:
        if true():
            return 전투_대기()


class 전투_대기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 전투_진행()


class 전투_진행(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990004" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990005" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return 랭크체크대사()


class 랭크체크대사(state.State):
    def on_tick(self) -> state.State:
        if dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            side_npc_talk(npcId=24100001, illust='Neirin_surprise', duration=5000, script='$02020019_BF__02020019_main__6$', voice='ko/Npc/00002125')
            return 던전종료_A랭크이상()
        if dungeon_first_user_mission_score(score=1500, operator='Less'):
            side_npc_talk(npcId=24100001, illust='Neirin_smile', duration=5000, script='$02020019_BF__02020019_main__7$', voice='ko/Npc/00002124')
            return 던전종료_A랭크미만()


class 던전종료_A랭크이상(state.State):
    def on_enter(self):
        dungeon_clear()


class 던전종료_A랭크미만(state.State):
    def on_enter(self):
        dungeon_fail()


