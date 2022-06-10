using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003162: Pudge
/// </summary>
public class _11003162 : NpcScript {
    internal _11003162(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008070$ 
                // - What is it?
                return true;
            case 30:
                // $script:0306155707008073$ 
                // - Everyone likes flowers because they're pretty. I don't care about that, because I use them to make supplements, scented candles, and potions.
                return true;
            default:
                return true;
        }
    }
}
