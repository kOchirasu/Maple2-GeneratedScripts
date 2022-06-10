using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004330: Kaitlyn
/// </summary>
public class _11004330 : NpcScript {
    internal _11004330(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011631$ 
                // - Sigh... 
                return true;
            case 20:
                // $script:1010140307011542$ 
                // - Sigh... 
                return true;
            case 10:
                // $script:1102172107011632$ 
                // - Will he be okay without me? Maybe I should go back... 
                return true;
            case 30:
                // $script:1010140307011543$ 
                // - Sigh... 
                switch (selection) {
                    // $script:1010140307011544$
                    // - Why the long face?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011545$ 
                // - $MyPCName$? It seems like I can't go anywhere without bumping into you. 
                // $script:1010140307011546$ 
                // - When I heard about the discovery of a new continent from somewhere else, I rushed over in order to study their unique magical practices. But I'm afraid I haven't learned much. 
                // $script:1010140307011547$ 
                // - It seems $npcName:11004329[gender:0]$ is, to the contrary, already deep into his research. 
                // $script:1010140307011548$ 
                // - I was hoping to find something that would improve Professor $npcName:11000032[gender:0]$'s condition. 
                switch (selection) {
                    // $script:1010140307011549$
                    // - I believe in you.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1010140307011550$ 
                // - Ahem! W-well I'm not going to make any progress sitting around talking to you! Excuse me. 
                return true;
            default:
                return true;
        }
    }
}
