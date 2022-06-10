using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000478: Kodor
/// </summary>
public class _11000478 : NpcScript {
    internal _11000478(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002080$ 
                // - Can I help you?
                return true;
            case 50:
                // $script:0831180407002085$ 
                // - I have a friend not far from here, but being away from him is agony. I wonder how he's doing...
                switch (selection) {
                    // $script:0831180407002086$
                    // - Who is he?
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407002087$
                    // - I'm sure he's fine.
                    case 1:
                        Id = 52;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407002088$ 
                // - That's... Um... Sheesh, $MyPCName$! You wouldn't know even if I told you! Don't you miss someone like that?
                return true;
            case 52:
                // $script:0831180407002089$ 
                // - Do you think so? I think so, too...
                // $script:0831180407002090$ 
                // - I know he's doing well. He's strong enough to get through anything.
                // $script:0831180407002091$ 
                // - But sometimes bad things happen, and that's why I'm worried about him. $MyPCName$, could you pray for his well-being?
                switch (selection) {
                    // $script:0831180407002092$
                    // - Of course.
                    case 0:
                        Id = 53;
                        return false;
                    // $script:0831180407002093$
                    // - It's not my business.
                    case 1:
                        Id = 54;
                        return false;
                }
                return true;
            case 53:
                // $script:0831180407002094$ 
                // - You're very kind! I consider you a good friend, $MyPCName$. I'll be praying for you, too.
                return true;
            case 54:
                // $script:0831180407002095$ 
                // - Oh, $MyPCName$... You must not have many friends...
                return true;
            default:
                return true;
        }
    }
}
