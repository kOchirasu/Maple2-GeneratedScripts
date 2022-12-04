""" trigger/80000016_bonus/prize.xml """
import trigger_api


class 입장(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154], visible=True)
        self.create_monster(spawnIds=[199], animationEffect=False)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[301]):
            return 시작(self.ctx)


class 시작(trigger_api.Trigger):
    def on_enter(self):
        self.create_item(spawnIds=[201])
        self.create_item(spawnIds=[202])
        self.create_item(spawnIds=[203])
        self.create_item(spawnIds=[204])
        self.create_item(spawnIds=[205])
        self.create_item(spawnIds=[206])
        self.create_item(spawnIds=[207])
        self.create_item(spawnIds=[208])
        self.create_item(spawnIds=[209])
        self.create_item(spawnIds=[210])
        self.create_item(spawnIds=[211])
        self.create_item(spawnIds=[212])
        self.create_item(spawnIds=[213])
        self.create_item(spawnIds=[216])
        self.create_item(spawnIds=[217])
        self.create_item(spawnIds=[218])
        self.create_item(spawnIds=[219])
        self.create_item(spawnIds=[220])
        self.create_item(spawnIds=[221])
        self.create_item(spawnIds=[222])
        self.create_item(spawnIds=[226])
        self.create_item(spawnIds=[227])
        self.create_item(spawnIds=[228])
        self.create_item(spawnIds=[229])
        self.create_item(spawnIds=[230])
        self.create_item(spawnIds=[231])
        self.create_item(spawnIds=[232])
        self.create_item(spawnIds=[233])
        self.create_item(spawnIds=[234])
        self.create_item(spawnIds=[235])
        self.create_item(spawnIds=[243])
        self.create_item(spawnIds=[244])
        self.create_item(spawnIds=[245])
        self.create_item(spawnIds=[246])
        self.create_item(spawnIds=[247])
        self.create_item(spawnIds=[248])
        self.create_item(spawnIds=[250])
        self.create_item(spawnIds=[251])
        self.create_item(spawnIds=[255])
        self.create_item(spawnIds=[256])
        self.create_item(spawnIds=[257])
        self.create_item(spawnIds=[258])
        self.create_item(spawnIds=[259])
        self.create_item(spawnIds=[260])
        self.create_item(spawnIds=[261])
        self.create_item(spawnIds=[262])
        self.create_item(spawnIds=[263])
        self.create_item(spawnIds=[264])
        self.create_item(spawnIds=[265])
        self.create_item(spawnIds=[266])
        self.create_item(spawnIds=[267])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 몬스터체크(self.ctx)


class 몬스터체크(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[199]):
            return 포탈생성(self.ctx)


class 포탈생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 완료(self.ctx)


class 완료(trigger_api.Trigger):
    pass


initial_state = 입장
