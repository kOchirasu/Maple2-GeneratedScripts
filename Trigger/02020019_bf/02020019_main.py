""" trigger/02020019_bf/02020019_main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.move_user(mapId=2020019, portalId=1)
        self.set_user_value(triggerId=99990002, key='battlesetting', value=0)
        self.set_user_value(triggerId=99990004, key='Timer', value=0)
        self.set_user_value(triggerId=99990005, key='SpecialTimer', value=0)
        self.set_user_value(triggerId=99990002, key='SpecialTimer', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(mapId=2020019, portalId=1)
        self.create_monster(spawnIds=[101,102,103], animationEffect=False) # <네이린과 대포 스폰(아군)>
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[501,502], returnView=False)
        self.show_caption(type='VerticalCaption', title='$02020019_BF__02020019_main__3$', desc='$02020019_BF__02020019_main__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_네이린설명1(self.ctx)


class 카메라_네이린설명1(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=503, enable=True)
        self.add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020019_BF__02020019_main__0$', duration=4000, align='left')
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=6300)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_네이린설명2(self.ctx)


class 카메라_네이린설명2(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020019_BF__02020019_main__1$', duration=4000, align='left')
        # action name="AddCinematicTalk" npcID="24100001" illustID="Neirin_normal" msg="$02020019_BF__02020019_main__2$" duration="4000" align="left" /

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_네이린설명3(self.ctx)


class 카메라_네이린설명3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=24100001, illustId='Neirin_normal', msg='$02020019_BF__02020019_main__5$', duration=4000, align='left')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.true():
            return 전투_대기(self.ctx)


class 전투_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 전투_진행(self.ctx)


class 전투_진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990004" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990005" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End', value=1):
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            self.side_npc_talk(npcId=24100001, illust='Neirin_surprise', duration=5000, script='$02020019_BF__02020019_main__6$', voice='ko/Npc/00002125')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score(score=1500, operator='Less'):
            self.side_npc_talk(npcId=24100001, illust='Neirin_smile', duration=5000, script='$02020019_BF__02020019_main__7$', voice='ko/Npc/00002124')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self):
        self.dungeon_fail()


initial_state = 입장
