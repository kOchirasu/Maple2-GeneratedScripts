using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004113: Junta
/// </summary>
public class _11004113 : NpcScript {
    internal _11004113(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010469$ 
                // - I am ready to leave at a moments notice. 
                return true;
            case 10:
                // $script:0720125407010470$ 
                // - Guidance has been retasked toward the recovery of Lapenshards. 
                return true;
            default:
                return true;
        }
    }
}
