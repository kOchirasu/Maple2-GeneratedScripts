using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000870: Marlowe
/// </summary>
public class _11000870 : NpcScript {
    internal _11000870(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003145$ 
                // - Huh? 
                return true;
            case 20:
                // $script:0831180407003147$ 
                // - Isn't this incredible? Frozen in time... 
                return true;
            default:
                return true;
        }
    }
}
