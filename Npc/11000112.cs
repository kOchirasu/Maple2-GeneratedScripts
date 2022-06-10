using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000112: Burfy
/// </summary>
public class _11000112 : NpcScript {
    internal _11000112(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000463$ 
                // - What's up?
                return true;
            case 10:
                // $script:0831180407000464$ 
                // - Look at this. Terrible, isn't it? Geez, I've never seen such a big fissure.
                return true;
            default:
                return true;
        }
    }
}
