using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000046: Jenna
/// </summary>
public class _11000046 : NpcScript {
    protected override int First() {
        // TODO: Job 1
        // TODO: RandomPick 10;20;30;40;50;60;70;80;90;100;110;120
    }

    // Select 0:
    // $script:0831180610000234$
    // - Do you have something to say to me?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (1, 0):
                // $script:0831180610000235$
                // - Everyone's so on edge right now, but not me... In fact, I can't wait to show the rest of the world what I can do! How about we forget about everything and go blow some stuff up? I'll even help you pick out your own cannon.
                return 1;
            case (1, 1):
                // functionID=1 
                // $script:0831180610000236$
                // - I'm not afraid of anything as long as I've got my giant cannon with me. Unlike people, it'll never disappoint me. What do you say, want to become a Heavy Gunner?
                return -1;
            case (10, 0):
                // $script:0831180610000237$
                // - Everyone's so on edge right now, but not me... in fact, I can't wait to show the rest of the world what I can do!
                switch (selection) {
                    // $script:0831180610000238$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000239$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:0831180610000240$
                // - This is a cannon, and it's the greatest! It can tear things up from a zillion feet away. Here, wanna see?
                return 11;
            case (11, 1):
                // $script:0831180610000241$
                // - Hahaha! Did you think I was serious? If I spun up my cannon right now, I'd send this whole place crumbling down.
                return -1;
            case (12, 0):
                // $script:0831180610000242$
                // - Fun is in the eye of the beholder. If you want to live a happy life, then figure out what you really want to do, and do it for the rest of your life.
                return 12;
            case (12, 1):
                // $script:0831180610000243$
                // - Just keep trying new things until you get to something that sticks! Anything goes, as long as you don't hurt anybody. Well, it's okay if they deserve it.
                return 12;
            case (12, 2):
                // $script:0831180610000244$
                // - I became a mercenary because a boring traditional life wasn't for me. And now I get to lug this beauty everywhere I go and blow stuff up!
                return 12;
            case (12, 3):
                // $script:0831180610000245$
                // - I came here as some doctor's bodyguard. But I got tired of escorting him to all his stuffy events. I'm actually pretty excited about all the recent chaos. I know some people are grumpy about it, but it's an opportunity for me to take on adversaries tougher than I ever dreamed. I'm stoked!
                return -1;
            case (13, 0):
                // $script:0607163510001528$
                // - Look at my weapons, $MyPCName$. Heavy Gunners use firearms like these. Amazing, huh?
                switch (selection) {
                    // $script:0607163510001529$
                    // - True warriors rely on more than their weapons.
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:0607163510001530$
                // - You don't know what you're talking about. My cannon could blow you to pieces in a single second!
                switch (selection) {
                    // $script:0607163510001531$
                    // - And I could break your cannon in a tenth of a second!
                    case 0:
                        return 15;
                }
                return -1;
            case (15, 0):
                // $script:0607163510001532$
                // - That's ridiculous! You know what, you're just no fun. Get lost.
                switch (selection) {
                    // $script:0607181410001557$
                    // - Let's talk about something else.
                    case 0:
                        return 110;
                }
                return -1;
            case (16, 0):
                // $script:0806014810001640$
                // - Look at my weapons, $MyPCName$. Heavy Gunners use firearms like these. Amazing, huh?
                switch (selection) {
                    // $script:0806014810001641$
                    // - Take a look at $npcName:11000046[gender:1]$'s cannon.
                    case 0:
                        return 17;
                }
                return -1;
            case (17, 0):
                // $script:0806014810001642$
                // - Let me tell you about this cannon. It's specially forged in Taliskar...
                //   <font color="#909090">(You touch the cannon, and instantly feel cold and dizzy. Her voice sounds like it's miles away.)</font>
                return 17;
            case (17, 1):
                // $script:0806014810001643$
                // - Heh, I told them there was only person who could handle this cannon, and that person was standing right in front of them! Heh, heh. It was me, get it? Hey, I asked you a question! Are you even listening?
                return 17;
            case (17, 2):
                // $script:0806014810001644$
                // - Hey, what's going on? You look pale. And you're sweating like crazy. Ha, ha, is touching my cannon <i>that</i> exciting?
                return 17;
            case (17, 3):
                // $script:0806014810001645$
                // - Hey. What's happening to you?
                //   <font color="#909090">(Her cannon brings up images from the nightmare you used to have when you slept in Halo Mountain. You'd better leave.)</font>
                switch (selection) {
                    // $script:0806014810001646$
                    // - I want to leave.
                    case 0:
                        return 18;
                }
                return -1;
            case (18, 0):
                // $script:0806014810001647$
                // - Oh. Well, fine. I was going to show you the awesome things my cannon does, but I guess not. What's wrong with you, anyway? Been traumatized by cannons or something? Wouldn't surprise me, since they're so powerful. They should only be handled by the fearless, anyway.
                switch (selection) {
                    // $script:0806014810001648$
                    // - Change the subject.
                    case 0:
                        return 120;
                }
                return -1;
            case (20, 0):
                // $script:0831180610000246$
                // - It'll be much more fun to travel around the world, looking for worthy opponents, than protecting grouchy old dudes.
                switch (selection) {
                    // $script:0831180610000247$
                    // - What should I do now?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180610000250$
                // - If you want to take on tough serious, you need serious hardware. $npc:11000004[gender:0]$ can hook you up with some sweet Heavy Gunner equipment. Go gear up and introduce yourself to the world outside with a bang!
                return 21;
            case (21, 1):
                // $script:0831180610000251$
                // - Keep shooting stuff, and eventually you'll reach a new level. Then it'll be time to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
                return -1;
            case (22, 0):
                // $script:0831180610000252$
                // - When you're ready to <font color="#ffd200">upgrade a skill</font>, just press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
                return 22;
            case (22, 1):
                // $script:0831180610000253$
                // - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
                return -1;
            case (23, 0):
                // $script:0831180610000254$
                // - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>. 
                return 23;
            case (23, 1):
                // $script:0831180610000255$
                // - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
                return 23;
            case (23, 2):
                // $script:0831180610000256$
                // - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently.
                return 23;
            case (23, 3):
                // $script:0831180610000257$
                // - And as for $itemPlural:40100022$... Hah, that's way out of your league.
                return -1;
            case (30, 0):
                // $script:0831180610000258$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already a Knight. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000259$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000260$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (40, 0):
                // $script:0831180610000261$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already a Berserker. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000262$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000263$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (50, 0):
                // $script:0831180610000264$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already a Wizard. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000265$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000266$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (60, 0):
                // $script:0831180610000267$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already a Priest. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000268$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000269$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (70, 0):
                // $script:0831180610000270$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already an Archer. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000271$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000272$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (80, 0):
                // $script:0831180610000273$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already a Thief. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000274$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000275$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (90, 0):
                // $script:0831180610000276$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already an Assassin. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:0831180610000277$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0831180610000278$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (100, 0):
                // $script:1216124310001334$
                // - Wait, I can't teach you to be a Heavy Gunner... you're already a Runeblade. What a shame—you missed your opportunity to live a life of fun and explosions!
                switch (selection) {
                    // $script:1216124310001335$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:1216124310001336$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                }
                return -1;
            case (110, 0):
                // $script:0607163510001533$
                // - Hm, you're not a Heavy Gunner, $MyPCName$. You know what that means? You don't know how to have fun!
                switch (selection) {
                    // $script:0607163510001534$
                    // - Tell me about that weapon of yours.
                    case 0:
                        return 11;
                    // $script:0607163510001535$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                    // $script:0607163510001536$
                    // - I want to ask you about something else.
                    case 2:
                        return 13;
                }
                return -1;
            case (120, 0):
                // $script:0806014810001649$
                // - Hm, you're not a Heavy Gunner, $MyPCName$.
                //   You know what that means? You don't know how to <font color="#ffd200">have fun</font>!
                switch (selection) {
                    // $script:0806014810001650$
                    // - What's that weapon on your back?
                    case 0:
                        return 11;
                    // $script:0806014810001651$
                    // - What's there to do around here?
                    case 1:
                        return 12;
                    // $script:0806014810001652$
                    // - Talk to $npcName:11000046[gender:1]$ about a different subject.
                    case 2:
                        return 16;
                }
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Close,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Next,
            (12, 2) => NpcTalkButton.Next,
            (12, 3) => NpcTalkButton.Close,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.SelectableDistractor,
            (16, 0) => NpcTalkButton.SelectableDistractor,
            (17, 0) => NpcTalkButton.Next,
            (17, 1) => NpcTalkButton.Next,
            (17, 2) => NpcTalkButton.Next,
            (17, 3) => NpcTalkButton.SelectableDistractor,
            (18, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Next,
            (22, 1) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Next,
            (23, 1) => NpcTalkButton.Next,
            (23, 2) => NpcTalkButton.Next,
            (23, 3) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.SelectableDistractor,
            (80, 0) => NpcTalkButton.SelectableDistractor,
            (90, 0) => NpcTalkButton.SelectableDistractor,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (110, 0) => NpcTalkButton.SelectableDistractor,
            (120, 0) => NpcTalkButton.SelectableDistractor,
            (1, 0) => NpcTalkButton.Next,
            (1, 1) => NpcTalkButton.ChangeJob,
            _ => NpcTalkButton.None,
        };
    }
}
