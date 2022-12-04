""" trigger/02020027_bf/main.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8001], visible=True)
        self.set_agent(triggerIds=[8002], visible=True)
        self.set_agent(triggerIds=[8003], visible=True)
        self.set_agent(triggerIds=[8004], visible=True)
        self.set_agent(triggerIds=[8005], visible=True)
        self.set_agent(triggerIds=[8006], visible=True)
        self.set_agent(triggerIds=[8007], visible=True)
        self.set_agent(triggerIds=[8008], visible=True)
        self.destroy_monster(spawnIds=[-1])
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_user_value(triggerId=99990003, key='Timer', value=0)
        self.set_user_value(triggerId=99990011, key='SpecialTimer', value=0)
        self.set_user_value(triggerId=99990002, key='battlesetting', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 카메라_시작(self.ctx)


class 카메라_시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_scene_skip(state=카메라_종료, action='exit')
        self.move_user(mapId=2020027, portalId=1)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 카메라_캡션(self.ctx)


class 카메라_캡션(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[5001,5002], returnView=False)
        self.show_caption(type='VerticalCaption', title='$02020027_BF__main__2$', desc='$02020027_BF__main__3$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=4000, scale=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 유저연출(self.ctx)


class 유저연출(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=5003, enable=True)
        self.set_conversation(type=1, spawnId=0, script='$02020027_BF__main__4$', arg4=3, arg5=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 카메라_메이슨설명1(self.ctx)


class 카메라_메이슨설명1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[202])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 유저연출_2(self.ctx)


class 유저연출_2(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=202, sequenceName='Talk_B', duration=18430)
        self.set_conversation(type=1, spawnId=0, script='$02020027_BF__main__5$', arg4=3, arg5=0)
        self.add_cinematic_talk(npcId=24120006, illustId='Mason_normal', msg='$02020027_BF__main__0$', duration=4000, align='left')
        self.remove_buff(boxId=901, skillId=51200001)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_메이슨설명2(self.ctx)


class 카메라_메이슨설명2(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=5004, enable=True)
        self.add_cinematic_talk(npcId=24120006, illustId='Mason_normal', msg='$02020027_BF__main__1$', duration=4000, align='left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_메이슨설명3(self.ctx)


class 카메라_메이슨설명3(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=24120006, illustId='Mason_normal', msg='$02020027_BF__main__6$', duration=4000, align='left')
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 카메라_종료(self.ctx)


class 카메라_종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0.1)
        self.destroy_monster(spawnIds=[202])
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.all_of():
            return 전투_진행(self.ctx)


class 전투_진행(trigger_api.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[8001], visible=False)
        self.set_agent(triggerIds=[8002], visible=False)
        self.set_agent(triggerIds=[8003], visible=False)
        self.set_agent(triggerIds=[8004], visible=False)
        self.set_agent(triggerIds=[8005], visible=False)
        self.set_agent(triggerIds=[8006], visible=False)
        self.set_agent(triggerIds=[8007], visible=False)
        self.set_agent(triggerIds=[8008], visible=False)
        self.set_user_value(triggerId=99990002, key='battlesetting', value=1)
        # <action name="SetUserValue" triggerID="99990003" key="Timer" value="1"/>
        # <action name="SetUserValue" triggerID="99990011" key="SpecialTimer" value="1"/>
        # <action name="SetUserValue" triggerID="99990002" key="SpecialTimer" value="1"/>

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='End', value=1):
            return 랭크체크대사(self.ctx)


class 랭크체크대사(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.dungeon_first_user_mission_score(score=1500, operator='GreaterEqual'):
            self.side_npc_talk(npcId=24120006, illust='Mason_normal', duration=6089, script='$02020027_BF__main__7$', voice='ko/Npc/00002100')
            return 던전종료_A랭크이상(self.ctx)
        if self.dungeon_first_user_mission_score(score=1500, operator='Less'):
            self.side_npc_talk(npcId=24120006, illust='Mason_closeEye', duration=5000, script='$02020027_BF__main__8$', voice='ko/Npc/00002099')
            return 던전종료_A랭크미만(self.ctx)


class 던전종료_A랭크이상(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.dungeon_clear()


class 던전종료_A랭크미만(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.dungeon_fail()


initial_state = 입장
