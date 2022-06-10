using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000128: Gary
/// </summary>
public class _11000128 : NpcScript {
    internal _11000128(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000549$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0831180407000551$ 
                // - I heard this path was dangerous. I didn't know it was this bad. You'd better be careful. 
                return true;
            default:
                return true;
        }
    }
}
