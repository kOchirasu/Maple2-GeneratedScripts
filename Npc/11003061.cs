using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003061: Frozen Tree
/// </summary>
public class _11003061 : NpcScript {
    internal _11003061(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007643$ 
                // - <font color="#909090">(A chilling wind blows through the gap in the ice wall behind the frozen tree.)</font> 
                return true;
            case 30:
                // $script:0102155907007644$ 
                // - <font color="#909090">(Something must be hidden behind this tree.)</font> 
                return true;
            default:
                return true;
        }
    }
}
