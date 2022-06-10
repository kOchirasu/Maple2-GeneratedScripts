using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003425: Sola
/// </summary>
public class _11003425 : NpcScript {
    internal _11003425(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008637$ 
                // - H-help me...
                return true;
            case 10:
                // $script:0706160807008638$ 
                // - H-help me...
                return true;
            default:
                return true;
        }
    }
}
