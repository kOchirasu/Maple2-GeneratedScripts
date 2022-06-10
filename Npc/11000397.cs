using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000397: Adrienne
/// </summary>
public class _11000397 : NpcScript {
    internal _11000397(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001610$ 
                // - May I help you? 
                return true;
            case 20:
                // $script:0831180407001612$ 
                // - It may not look it, but my house is the most expensive in the neighborhood. There's nothing quite like living up so high. I hope my daughter appreciates how hard it was for me to get this place for us. 
                return true;
            default:
                return true;
        }
    }
}
