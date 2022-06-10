using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000168: Kay
/// </summary>
public class _11000168 : NpcScript {
    internal _11000168(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1103095507004409$ 
                // - Welcome to the Maple OX Quiz!
                return true;
            case 30:
                // $script:1103095507004412$ 
                // - How'd you like the quiz? Pretty tricky, right? Come back next time, because there's more where that came from!
                switch (selection) {
                    // $script:1103095507004413$
                    // - I lost. I <i>lost</i>. I <i>never</i> lose!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1103095507004414$
                    // - So... what are the questions for the next quiz?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:1103095507004415$
                    // - Congratulations on being the host.
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:1103095507004416$ 
                // - Don't lose heart. You can always come back and try again next time. I'll be rooting for you, $MyPCName$!
                return true;
            case 32:
                // $script:1103095507004417$ 
                // - You want me to help you cheat? No. No way. I can't believe you'd ask me that...
                return true;
            case 33:
                // $script:1103095507004418$ 
                // - Thank you! It's a dream come true, to be honest. A dream come true...
                //   <font color="#909090">(He starts weeping.)</font>
                switch (selection) {
                    // $script:1103095507004419$
                    // - Don't cry, little raccoon guy.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1103095507004420$ 
                // - I-I won't! Sorry. I just wasn't expecting anyone to congratulate me. I'll do my best not to let you down as a host, $MyPCName$!
                return true;
            default:
                return true;
        }
    }
}
