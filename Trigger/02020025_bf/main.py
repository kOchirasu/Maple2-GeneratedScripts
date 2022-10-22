""" trigger/02020025_bf/main.xml """
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
        destroy_monster(spawnIds=[-1])
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_user_value(triggerId=99990004, key='Timer', value=0) # <일반 5분 타이머>
        set_user_value(triggerId=99990006, key='SpecialTimer', value=0) # <3분내 클리어 특별 타이머>
        set_user_value(triggerId=99990002, key='battlesetting', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 카메라_시작()


class 카메라_시작(state.State):
    def on_enter(self):
        set_scene_skip(state=카메라_종료, arg2='exit')
        move_user(mapId=2020025, portalId=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_캡션()


class 카메라_캡션(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[5001,5002], returnView=True)
        show_caption(type='VerticalCaption', title='$02020025_BF__main__3$', desc='$02020025_BF__main__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 유저연출()


class 유저연출(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202])
        set_conversation(type=1, spawnId=0, script='$02020025_BF__main__5$', arg4=5, arg5=0)
        select_camera(triggerId=503, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_콘대르설명1()


class 카메라_콘대르설명1(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=202, sequenceName='Talk_B', duration=18430)
        add_cinematic_talk(npcId=24110001, msg='$02020025_BF__main__0$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 유저연출_2()


class 유저연출_2(state.State):
    def on_enter(self):
        set_conversation(type=1, spawnId=0, script='$02020025_BF__main__6$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 유저연출_3()


class 유저연출_3(state.State):
    def on_enter(self):
        select_camera(triggerId=504, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 카메라_콘대르설명2()


class 카메라_콘대르설명2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24110001, illustId='Conder_normal', msg='$02020025_BF__main__1$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_콘대르설명3()


class 카메라_콘대르설명3(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24110001, illustId='Conder_normal', msg='$02020025_BF__main__2$', duration=4000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 카메라_콘대르설명4()


class 카메라_콘대르설명4(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=24110001, illustId='Conder_normal', msg='$02020025_BF__main__7$', duration=4000, align='left')
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

    def on_tick(self) -> state.State:
        if true():
            return 준비()


class 준비(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201], arg2=False, arg3=3000)

    def on_tick(self) -> state.State:
        if all_of():
            return 전투_진행()


class 전투_진행(state.State):
    def on_enter(self):
        set_agent(triggerIds=[9001], visible=False)
        set_agent(triggerIds=[9002], visible=False)
        set_agent(triggerIds=[9003], visible=False)
        set_agent(triggerIds=[9004], visible=False)
        set_agent(triggerIds=[9005], visible=False)
        set_agent(triggerIds=[9006], visible=False)
        set_agent(triggerIds=[9007], visible=False)
        set_agent(triggerIds=[9008], visible=False)
        set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990004" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990006" key="SpecialTimer" value="1"/>

    def on_tick(self) -> state.State:
        if user_value(key='End', value=1):
            return 랭크체크대사()


class 랭크체크대사(state.State):
    def on_tick(self) -> state.State:
        if dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            side_npc_talk(npcId=24110001, illust='Conder_normal', duration=5000, script='$02020025_BF__main__8$', voice='ko/Npc/00002146')
            return 던전종료_A랭크이상()
        if dungeon_first_user_mission_score(score=1500, operator='Less'):
            side_npc_talk(npcId=24110001, illust='Conder_smile', duration=5000, script='$02020025_BF__main__9$', voice='ko/Npc/00002145')
            return 던전종료_A랭크미만()


class 던전종료_A랭크이상(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        dungeon_clear()


class 던전종료_A랭크미만(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[201])
        dungeon_fail()


