using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000204: Lavenne
/// </summary>
public class _11000204 : NpcScript {
    internal _11000204(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000799$ 
                // - What is it?
                return true;
            case 10:
                // $script:1121222006000800$ 
                // - What is it?
                return true;
            default:
                return true;
        }
    }
}
