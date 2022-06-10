using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003352: Ralph's Lackey
/// </summary>
public class _11003352 : NpcScript {
    internal _11003352(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008503$ 
                // - Get away!
                return true;
            case 20:
                // $script:0517164307008505$ 
                // - This time, the big guy'll mop the floor with you! No way he'll lose twice.
                return true;
            default:
                return true;
        }
    }
}
