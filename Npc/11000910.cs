using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000910: Renji
/// </summary>
public class _11000910 : NpcScript {
    internal _11000910(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003272$ 
                // - There's nothing to life. Just let nature take its course.
                return true;
            case 20:
                // $script:0831180407003274$ 
                // - Stop bothering me. I don't have time for chitchat!
                return true;
            default:
                return true;
        }
    }
}
