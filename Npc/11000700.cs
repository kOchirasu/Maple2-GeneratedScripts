using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000700: Tabatha
/// </summary>
public class _11000700 : NpcScript {
    internal _11000700(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000851$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000852$ 
                // - Helping each other out is always so rewarding!
                return true;
            default:
                return true;
        }
    }
}
