""" trigger/02020023_bf/main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='battlesetting', value=0)
        self.set_user_value(triggerId=99990003, key='Timer', value=0)
        self.set_user_value(triggerId=99990004, key='SpecialTimer', value=0)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_agent(triggerIds=[9001], visible=True)
        self.set_agent(triggerIds=[9002], visible=True)
        self.set_agent(triggerIds=[9003], visible=True)
        self.set_agent(triggerIds=[9004], visible=True)
        self.set_agent(triggerIds=[9005], visible=True)
        self.set_agent(triggerIds=[9006], visible=True)
        self.set_agent(triggerIds=[9007], visible=True)
        self.set_agent(triggerIds=[9008], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[901]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[501,502], returnView=True)
        self.show_caption(type='VerticalCaption', title='$02020023_BF__main__3$', desc='$02020023_BF__main__4$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_줌인(self.ctx)


class 카메라_줌인(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[503,504], returnView=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_블리체등장(self.ctx)


class 카메라_블리체등장(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=505, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_블리체뒤돌기(self.ctx)


class 카메라_블리체뒤돌기(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_rotation(spawnId=102, rotation=180)
        self.add_cinematic_talk(npcId=23200083, illustId='Bliche_normal', msg='$02020023_BF__main__1$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_블리체대사1(self.ctx)


class 카메라_블리체대사1(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=23200083, illustId='Bliche_normal', msg='$02020023_BF__main__0$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 블리체_전투시작대사(self.ctx)


class 블리체_전투시작대사(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=23200083, illustId='Bliche_normal', msg='$02020023_BF__main__5$', duration=4000, align='left')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.1)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 전투시작(self.ctx)


class 전투시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[9001], visible=False)
        self.set_agent(triggerIds=[9002], visible=False)
        self.set_agent(triggerIds=[9003], visible=False)
        self.set_agent(triggerIds=[9004], visible=False)
        self.set_agent(triggerIds=[9005], visible=False)
        self.set_agent(triggerIds=[9006], visible=False)
        self.set_agent(triggerIds=[9007], visible=False)
        self.set_agent(triggerIds=[9008], visible=False)
        self.set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990003" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End', value=1):
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            self.side_npc_talk(npcId=23200083, illust='Bliche_smile', duration=5050, script='$02020023_BF__main__7$', voice='ko/Npc/00002064')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score(score=1500, operator='Less'):
            self.side_npc_talk(npcId=23200083, illust='Bliche_nomal', duration=6158, script='$02020023_BF__main__8$', voice='ko/Npc/00002063')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.dungeon_fail()


initial_state = 입장
