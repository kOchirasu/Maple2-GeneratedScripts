using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000640: Prisoner 150122
/// </summary>
public class _11000640 : NpcScript {
    internal _11000640(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002608$ 
                // - Get me out of here... 
                return true;
            case 40:
                // $script:0831180407002612$ 
                // - Argh, this place is a sty! I hate prison! 
                return true;
            default:
                return true;
        }
    }
}
