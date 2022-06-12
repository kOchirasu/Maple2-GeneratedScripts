using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001238: Merkaz
/// </summary>
public class _11001238 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50;60
    }

    // Select 0:
    // $script:1123154807004427$
    // - Hm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1123154807004430$
                // - Come, come, tell me what you need. You won't be leaving empty-handed, heh heh heh...
                switch (selection) {
                    // $script:1123154807004431$
                    // - I bet you get lots of customers.
                    case 0:
                        return 31;
                    // $script:1123154807004432$
                    // - Why the creep—er, cheery smile?
                    case 1:
                        return 32;
                    // $script:1123154807004433$
                    // - I bet you have all kinds of weird stories.
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1123154807004434$
                // - Of course, of course! I do not know why they come here, but I do so enjoy watching them skitter here and there.
                return -1;
            case (32, 0):
                // $script:1123154807004435$
                // - Don't worry your little soul about that. You'll learn soon enough... even if you don't want to.
                return -1;
            case (33, 0):
                // $script:1123154807004436$
                // - Enough to spend all night in the telling, and then some! So, what would you like to hear? The tale of a young monster slayer and his buxom mage companion? The story of how I've kept my youthful looks? Or... something else? 
                switch (selection) {
                    // $script:1123154807004437$
                    // - Something else! Please, something else.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1123154807004438$
                // - Ahhh, yes... I know just the tale for a squirmy adventurer like you. Listen close, dearie...
                return 34;
            case (34, 1):
                // $script:1123154807004439$
                // - Legend has it that when the Shadow Seed takes root, a new son will be born unto the Demon King and darkness shall swallow the world. A lovely little tale, don't you think?
                switch (selection) {
                    // $script:1123154807004440$
                    // - You and I have different definitions of 'lovely.'
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:1123154807004441$
                // - Blind little child! Lovely is in the eye of the beholder.
                return -1;
            case (40, 0):
                // $script:1125183507007502$
                // - Even when it is too dark to see, keep your eyes wide open. You'll find your way... eventually.
                switch (selection) {
                    // $script:1125183507007503$
                    // - Okay. Sure. <i>That</i> makes sense.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1125183507007504$
                // - What I am <i>trying</i> to say is that you shouldn't be here right now. I will send you to where you should be.
                switch (selection) {
                    // $script:1125183507007505$
                    // - Please send me there again.
                    case 0:
                        // TODO: goto 42
                        // TODO: gotoFail 43
                        return -1;
                }
                return -1;
            case (42, 0):
                // functionID=1 
                // $script:1125183507007506$
                // - I've created a portal for you down there. It will take you to $map:52000076$. Next time, use the portal instead of bothering me, all right?
                return -1;
            case (43, 0):
                // $script:1125185807007507$
                // - You've come here empty-handed. What are you talking about?
                return -1;
            case (50, 0):
                // $script:1214150707007552$
                // - Do you not realize that you should be somewhere else?
                switch (selection) {
                    // $script:1214150707007553$
                    // - Yes. Send me to $map:63000050$.
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // functionID=2 
                // $script:1214150707007554$
                // - Heh heh heh... Off with you!
                return -1;
            case (52, 0):
                // $script:1214150707007555$
                // - Why are you still empty-handed?
                return -1;
            case (60, 0):
                // $script:1214150707007556$
                // - Come, come, tell me what you need. You won't be leaving empty-handed, heh heh heh...
                switch (selection) {
                    // $script:1214150707007557$
                    // - I bet you get lots of customers.
                    case 0:
                        return 61;
                    // $script:1214150707007558$
                    // - Why the creep—er, cheery smile?
                    case 1:
                        return 62;
                    // $script:1214150707007559$
                    // - I bet you have all kinds of weird stories.
                    case 2:
                        return 63;
                }
                return -1;
            case (61, 0):
                // $script:1214150707007560$
                // - Of course, of course! I do not know why they come here, but I do so enjoy watching them skitter here and there.
                return -1;
            case (62, 0):
                // $script:1214150707007561$
                // - Don't worry your little soul about that. You'll learn soon enough... even if you don't want to.
                return -1;
            case (63, 0):
                // $script:1214150707007562$
                // - Enough to spend all night in the telling, and then some! So, what would you like to hear? The tale of a young monster slayer and his buxom mage companion? The story of how I've kept my youthful looks? Or... something else? 
                switch (selection) {
                    // $script:1214150707007563$
                    // - Something else! Please, something else.
                    case 0:
                        return 64;
                }
                return -1;
            case (64, 0):
                // $script:1214150707007564$
                // - Ahhh, yes... I know just the tale for a squirmy adventurer like you. Listen close, dearie...
                return 64;
            case (64, 1):
                // $script:1214150707007565$
                // - Legend has it that when the Shadow Seed takes root, a new son will be born unto the Demon King and darkness shall swallow the world. A lovely little tale, don't you think?
                switch (selection) {
                    // $script:1214150707007566$
                    // - You and I have different definitions of 'lovely.'
                    case 0:
                        return 65;
                }
                return -1;
            case (65, 0):
                // $script:1214150707007567$
                // - Blind little child! Lovely is in the eye of the beholder.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (43, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (61, 0) => NpcTalkButton.Close,
            (62, 0) => NpcTalkButton.Close,
            (63, 0) => NpcTalkButton.SelectableDistractor,
            (64, 0) => NpcTalkButton.Next,
            (64, 1) => NpcTalkButton.SelectableDistractor,
            (65, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
