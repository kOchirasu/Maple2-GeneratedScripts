using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001238: Merkaz
/// </summary>
public class _11001238 : NpcScript {
    internal _11001238(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123154807004427$ 
                // - Hm...
                return true;
            case 30:
                // $script:1123154807004430$ 
                // - Come, come, tell me what you need. You won't be leaving empty-handed, heh heh heh...
                switch (selection) {
                    // $script:1123154807004431$
                    // - I bet you get lots of customers.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1123154807004432$
                    // - Why the creep—er, cheery smile?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1123154807004433$
                    // - I bet you have all kinds of weird stories.
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:1123154807004434$ 
                // - Of course, of course! I do not know why they come here, but I do so enjoy watching them skitter here and there.
                return true;
            case 32:
                // $script:1123154807004435$ 
                // - Don't worry your little soul about that. You'll learn soon enough... even if you don't want to.
                return true;
            case 33:
                // $script:1123154807004436$ 
                // - Enough to spend all night in the telling, and then some! So, what would you like to hear? The tale of a young monster slayer and his buxom mage companion? The story of how I've kept my youthful looks? Or... something else? 
                switch (selection) {
                    // $script:1123154807004437$
                    // - Something else! Please, something else.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1123154807004438$ 
                // - Ahhh, yes... I know just the tale for a squirmy adventurer like you. Listen close, dearie...
                // $script:1123154807004439$ 
                // - Legend has it that when the Shadow Seed takes root, a new son will be born unto the Demon King and darkness shall swallow the world. A lovely little tale, don't you think?
                switch (selection) {
                    // $script:1123154807004440$
                    // - You and I have different definitions of 'lovely.'
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:1123154807004441$ 
                // - Blind little child! Lovely is in the eye of the beholder.
                return true;
            case 40:
                // $script:1125183507007502$ 
                // - Even when it is too dark to see, keep your eyes wide open. You'll find your way... eventually.
                switch (selection) {
                    // $script:1125183507007503$
                    // - Okay. Sure. <i>That</i> makes sense.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1125183507007504$ 
                // - What I am <i>trying</i> to say is that you shouldn't be here right now. I will send you to where you should be.
                switch (selection) {
                    // $script:1125183507007505$
                    // - Please send me there again.
                    case 0:
                        Id = 0; // TODO: 42 | 43
                        return false;
                }
                return true;
            case 42:
                // $script:1125183507007506$ functionID=1 
                // - I've created a portal for you down there. It will take you to $map:52000076$. Next time, use the portal instead of bothering me, all right?
                return true;
            case 43:
                // $script:1125185807007507$ 
                // - You've come here empty-handed. What are you talking about?
                return true;
            case 50:
                // $script:1214150707007552$ 
                // - Do you not realize that you should be somewhere else?
                switch (selection) {
                    // $script:1214150707007553$
                    // - Yes. Send me to $map:63000050$.
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1214150707007554$ functionID=2 
                // - Heh heh heh... Off with you!
                return true;
            case 52:
                // $script:1214150707007555$ 
                // - Why are you still empty-handed?
                return true;
            case 60:
                // $script:1214150707007556$ 
                // - Come, come, tell me what you need. You won't be leaving empty-handed, heh heh heh...
                switch (selection) {
                    // $script:1214150707007557$
                    // - I bet you get lots of customers.
                    case 0:
                        Id = 61;
                        return false;
                    // $script:1214150707007558$
                    // - Why the creep—er, cheery smile?
                    case 1:
                        Id = 62;
                        return false;
                    // $script:1214150707007559$
                    // - I bet you have all kinds of weird stories.
                    case 2:
                        Id = 63;
                        return false;
                }
                return true;
            case 61:
                // $script:1214150707007560$ 
                // - Of course, of course! I do not know why they come here, but I do so enjoy watching them skitter here and there.
                return true;
            case 62:
                // $script:1214150707007561$ 
                // - Don't worry your little soul about that. You'll learn soon enough... even if you don't want to.
                return true;
            case 63:
                // $script:1214150707007562$ 
                // - Enough to spend all night in the telling, and then some! So, what would you like to hear? The tale of a young monster slayer and his buxom mage companion? The story of how I've kept my youthful looks? Or... something else? 
                switch (selection) {
                    // $script:1214150707007563$
                    // - Something else! Please, something else.
                    case 0:
                        Id = 64;
                        return false;
                }
                return true;
            case 64:
                // $script:1214150707007564$ 
                // - Ahhh, yes... I know just the tale for a squirmy adventurer like you. Listen close, dearie...
                // $script:1214150707007565$ 
                // - Legend has it that when the Shadow Seed takes root, a new son will be born unto the Demon King and darkness shall swallow the world. A lovely little tale, don't you think?
                switch (selection) {
                    // $script:1214150707007566$
                    // - You and I have different definitions of 'lovely.'
                    case 0:
                        Id = 65;
                        return false;
                }
                return true;
            case 65:
                // $script:1214150707007567$ 
                // - Blind little child! Lovely is in the eye of the beholder.
                return true;
            default:
                return true;
        }
    }
}
