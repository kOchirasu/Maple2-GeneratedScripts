using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000205: Lily
/// </summary>
public class _11000205 : NpcScript {
    internal _11000205(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000801$ 
                // - What is it?
                return true;
            case 10:
                // $script:1121222006000802$ 
                // - What is it?
                return true;
            default:
                return true;
        }
    }
}
