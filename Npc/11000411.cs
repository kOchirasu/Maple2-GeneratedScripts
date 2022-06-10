using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000411: Meminem
/// </summary>
public class _11000411 : NpcScript {
    internal _11000411(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001734$ 
                // - Yo!
                return true;
            case 20:
                // $script:0831180407001736$ 
                // - You ask me, tagging is just as much art as sick beats and hot moves. Some people say I'm just some punk, but they don't know what they're talking about.
                return true;
            default:
                return true;
        }
    }
}
