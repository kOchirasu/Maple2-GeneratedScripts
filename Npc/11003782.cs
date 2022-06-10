using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003782: Kaitlyn
/// </summary>
public class _11003782 : NpcScript {
    internal _11003782(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009634$ 
                // - What?
                return true;
            case 10:
                // $script:1213192607009635$ 
                // - What is it?
                return true;
            default:
                return true;
        }
    }
}
