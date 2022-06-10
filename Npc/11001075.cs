using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001075: Mojiran
/// </summary>
public class _11001075 : NpcScript {
    internal _11001075(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003667$ 
                // - Wah! You startled me.
                return true;
            case 30:
                // $script:0831180407003670$ 
                // - Ah, I came here on a tour...
                return true;
            default:
                return true;
        }
    }
}
