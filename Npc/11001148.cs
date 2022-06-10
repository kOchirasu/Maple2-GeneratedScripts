using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001148: Danpa
/// </summary>
public class _11001148 : NpcScript {
    internal _11001148(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0915221607003971$ 
                // - What? If it's not urgent, come back later. 
                return true;
            case 30:
                // $script:0915221607003974$ 
                // - See the fortress over there? It's got to be full of all kinds of amazing stuff worth collecting. Say, would you be interested in checking it out? 
                switch (selection) {
                    // $script:0915221607003975$
                    // - I don't think there's much of value left in that abandoned fortress.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0915221607003976$
                    // - I'm a little more worried about the monsters guarding it.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0915221607003977$ 
                // - <font color="#909090">(He chuckles.)</font>
Well I do! It's gotta be chock full of treasure. I can tell, just by the look of it. I guess we'll see which of us is right. 
                return true;
            case 32:
                // $script:0915221607003978$ 
                // - No kidding. Why do you think I haven't gone inside? I wish someone would take care of them for me... 
                return true;
            default:
                return true;
        }
    }
}
