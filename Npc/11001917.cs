using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001917: Guard
/// </summary>
public class _11001917 : NpcScript {
    internal _11001917(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1116181807007420$ 
                // - Oh no...
                return true;
            case 20:
                // $script:1116181807007422$ 
                // - Tria is under attack!
                return true;
            default:
                return true;
        }
    }
}
