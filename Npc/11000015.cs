using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000015: Oska
/// </summary>
public class _11000015 : NpcScript {
    internal _11000015(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000074$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0831180407000077$ 
                // - What brings you to this place?
                switch (selection) {
                    // $script:0831180407000078$
                    // - I came to see you.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000079$
                    // - I came to $map:02000076$ to see the elder.
                    case 1:
                        Id = 41;
                        return false;
                    // $script:0831180407000080$
                    // - I have business here.
                    case 2:
                        Id = 51;
                        return false;
                    // $script:0831180407000081$
                    // - That's none of your business.
                    case 3:
                        Id = 61;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000082$ 
                // - Do you have a reason for coming to see me?
                switch (selection) {
                    // $script:0831180407000083$
                    // - I just thought I'd say hi.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0831180407000084$
                    // - Nope.
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407000085$ 
                // - Oh. Well. Hi.
                return true;
            case 33:
                // $script:0831180407000086$ 
                // - Well, you're just being ridiculous. I've no time for that. Excuse me. 
                return true;
            case 41:
                // $script:0831180407000087$ 
                // - $npcName:11000001[gender:0]$'s house is on the hill behind the clock tower in the center of the village. He's always there, keeping an eye on everyone.
                return true;
            case 51:
                // $script:0831180407000088$ 
                // - I see. All I'll say then is that if you need help, the militia is always here.
                return true;
            case 61:
                // $script:0831180407000089$ 
                // - I hope I didn't upset you. You certainly don't have to explain yourself. But if you do, the rest of the militia and I may be able to help.
                return true;
            default:
                return true;
        }
    }
}
