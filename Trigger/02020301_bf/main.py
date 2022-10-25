""" trigger/02020301_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=300002, key='Phase_1', value=0) # 페이즈별 트리거 실행 대기
        self.set_user_value(triggerId=300003, key='Phase_2', value=0)
        self.set_user_value(triggerId=300004, key='Phase_3', value=0)
        self.set_user_value(triggerId=300005, key='Phase_4', value=0)
        self.set_user_value(triggerId=300006, key='Phase_5', value=0)
        self.set_mesh(triggerIds=[5241,5242,5243,5244], visible=True) # 4페이즈 상하좌우 엘리베이터 길막 닫음
        self.set_mesh(triggerIds=[5641,5642,5643,5644], visible=True) # 5페이즈 상하좌우 엘리베이터 길막 닫음
        self.set_breakable(triggerIds=[5171,5172,5173,5174,5175,5176,5177,5178,5179,5180,5181,5182,5183,5184], enable=False) # 좌우 이동 엘리베이터 동작 대기
        self.set_breakable(triggerIds=[5151,5152,5153,5154,5155,5156,5157,5158,5159,5160,5161,5162,5163,5164], enable=False)
        self.set_breakable(triggerIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], enable=False) # 4페이즈 상하 엘리베이터 동작 대기
        self.set_breakable(triggerIds=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120], enable=False)
        self.set_breakable(triggerIds=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130], enable=False)
        self.set_breakable(triggerIds=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140], enable=False)
        self.set_breakable(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], enable=False) # 5페이즈 상하 엘리베이터 동작 대기
        self.set_breakable(triggerIds=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], enable=False)
        self.set_breakable(triggerIds=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], enable=False)
        self.set_breakable(triggerIds=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], enable=False)
        self.set_visible_breakable_object(triggerIds=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364], visible=False) # 좌우 이동 엘리베이터 숨기기
        self.set_visible_breakable_object(triggerIds=[5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384], visible=False)
        self.set_visible_breakable_object(triggerIds=[5351,5352,5353,5354,5355,5356,5357,5358,5359,5360,5361,5362,5363,5364,5371,5372,5373,5374,5375,5376,5377,5378,5379,5380,5381,5382,5383,5384], visible=False) # 3페이즈 좌우 엘리베이터 숨기기
        self.set_visible_breakable_object(triggerIds=[5301,5302,5303,5304,5305,5306,5307,5308,5309,5310,5311,5312,5313,5314,5315,5316,5317,5318,5319,5320,5321,5322,5323,5324,5325,5326,5327,5328,5329,5330,5331,5332,5333,5334,5335,5336,5337,5338,5339,5340], visible=False) # 4페이즈 상하 엘리베이터(정지) 숨기기
        self.set_visible_breakable_object(triggerIds=[5101,5102,5103,5104,5105,5106,5107,5108,5109,5110], visible=False) # 4페이즈 상하 엘리베이터 숨기기
        self.set_visible_breakable_object(triggerIds=[5111,5112,5113,5114,5115,5116,5117,5118,5119,5120], visible=False)
        self.set_visible_breakable_object(triggerIds=[5121,5122,5123,5124,5125,5126,5127,5128,5129,5130], visible=False)
        self.set_visible_breakable_object(triggerIds=[5131,5132,5133,5134,5135,5136,5137,5138,5139,5140], visible=False)
        self.set_visible_breakable_object(triggerIds=[5401,5402,5403,5404,5405,5406,5407,5408,5409,5410], visible=False) # 5페이즈 상하 엘리베이터 동작 숨기기
        self.set_visible_breakable_object(triggerIds=[5411,5412,5413,5414,5415,5416,5417,5418,5419,5420], visible=False)
        self.set_visible_breakable_object(triggerIds=[5421,5422,5423,5424,5425,5426,5427,5428,5429,5430], visible=False)
        self.set_visible_breakable_object(triggerIds=[5431,5432,5433,5434,5435,5436,5437,5438,5439,5440], visible=False)
        self.set_visible_breakable_object(triggerIds=[5501,5502,5503,5504,5505,5506,5507,5508,5509,5510,5511,5512,5513,5514,5515,5516,5517,5518,5519,5520,5521,5522,5523,5524,5525,5526,5527,5528,5529,5530,5531,5532,5533,5534,5535,5536,5537,5538,5539,5540], visible=False) # 5페이즈 상하 엘리베이터 숨기기
        self.set_interact_object(triggerIds=[10003131], state=2) # 2페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(triggerIds=[10003121], state=2) # 3페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(triggerIds=[10003122], state=2)
        self.set_interact_object(triggerIds=[10003111], state=2) # 4페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(triggerIds=[10003112], state=2)
        self.set_interact_object(triggerIds=[10003113], state=2)
        self.set_interact_object(triggerIds=[10003114], state=2)
        self.set_interact_object(triggerIds=[10003101], state=2) # 5페이즈 인터렉트 오브젝트 대기
        self.set_interact_object(triggerIds=[10003102], state=2)
        self.set_interact_object(triggerIds=[10003103], state=2)
        self.set_interact_object(triggerIds=[10003104], state=2)
        self.set_agent(triggerIds=[1800000,1800001,1800002,1800003,1800004,1800005,1800006,1800007,1800008,1800009,1800010,1800011], visible=True)
        self.set_agent(triggerIds=[1810000,1810001,1810002,1810003,1810004,1810005,1810006,1810007,1810008,1810009,1810010,1810011], visible=True)
        self.add_buff(boxIds=[1003], skillId=62100168, level=1) # 포탑 기절 이뮨
        self.set_portal(portalId=13, visible=False, enable=False, minimapVisible=False) # 페이즈 시작전에 올라오지 엘리베이터에 플레이어가 도달할 경우, 전투 지역으로 돌려보냄
        self.set_portal(portalId=14, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=15, visible=False, enable=False, minimapVisible=False)
        self.set_portal(portalId=16, visible=False, enable=False, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[1001]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[5241,5242,5243,5244], visible=True)
        self.side_npc_talk(type='talk', npcId=23503003, illust='ArcheonBlack_Normal', script='$02020301_BF__MAIN__0$', duration=5684)
        self.create_monster(spawnIds=[101], animationEffect=False) # 아르케온 등장
        self.create_monster(spawnIds=[112], animationEffect=True) # 아르케온 한방기 폭발 ai 엘리베이터
        self.create_monster(spawnIds=[113], animationEffect=True)
        self.create_monster(spawnIds=[114], animationEffect=True)
        self.create_monster(spawnIds=[115], animationEffect=True)
        self.create_monster(spawnIds=[121], animationEffect=True) # 아르케온 페이즈4 일직선 폭발 ai
        self.create_monster(spawnIds=[122], animationEffect=True)
        self.create_monster(spawnIds=[123], animationEffect=True)
        self.create_monster(spawnIds=[124], animationEffect=True)
        self.set_portal(portalId=13, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=14, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=15, visible=False, enable=True, minimapVisible=False)
        self.set_portal(portalId=16, visible=False, enable=True, minimapVisible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return 조건추가(self.ctx)


class 조건추가(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.all_of():
            return 보스전_성공(self.ctx)
        """
        <condition name="DungeonCheckPlayTime" playSeconds="420" operator="Equal" > 
            <transition state="보스전_타임어택실패"/>
        </condition>
        """


class 보스전_성공(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[1003], skillId=62100169, level=1)
        self.dungeon_mission_complete(missionId=23039005) # 포탑 기절 이뮨 제거
        self.dungeon_set_end_time()
        self.side_npc_talk(type='talk', npcId=23503003, illust='ArcheonBlack_Die', script='$02020301_BF__MAIN__1$', duration=3176)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 추가대화(self.ctx)


class 추가대화(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11004205, illust='ArcaneBlader_normal', script='$02020301_BF__MAIN__2$', duration=3176)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[-1])
        self.dungeon_clear()
        self.set_portal(portalId=4, visible=True, enable=True, minimapVisible=True)
        self.set_portal(portalId=7, visible=True, enable=True, minimapVisible=True)


initial_state = 대기
