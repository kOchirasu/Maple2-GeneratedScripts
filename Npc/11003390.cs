using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003390: Wolf Heart
/// </summary>
public class _11003390 : NpcScript {
    internal _11003390(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008585$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008586$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
