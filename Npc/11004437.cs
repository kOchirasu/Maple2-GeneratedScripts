using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004437: Nairin
/// </summary>
public class _11004437 : NpcScript {
    internal _11004437(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213154907011978$ 
                // - Would you like to take on a mission for Green Hoods?
                return true;
            case 10:
                // $script:1213154907011979$ 
                // - Where should I start? Local ecology? Demographics? There's so much data to collate!
                return true;
            default:
                return true;
        }
    }
}
