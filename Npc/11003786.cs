using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003786: Mason
/// </summary>
public class _11003786 : NpcScript {
    internal _11003786(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009642$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:1213192607009643$ 
                // - There's work to be done. 
                return true;
            default:
                return true;
        }
    }
}
