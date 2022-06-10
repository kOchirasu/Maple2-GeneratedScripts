using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000641: Prisoner 150123
/// </summary>
public class _11000641 : NpcScript {
    internal _11000641(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002613$ 
                // - Get me out of here... 
                return true;
            case 30:
                // $script:0831180407002616$ 
                // - Bah, I'm just going to sleep...
                return true;
            default:
                return true;
        }
    }
}
