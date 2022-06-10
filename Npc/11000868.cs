using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000868: Tess
/// </summary>
public class _11000868 : NpcScript {
    internal _11000868(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003139$ 
                // - Oh? 
                return true;
            case 20:
                // $script:0831180407003141$ 
                // - Are they doing this to me because I'm an intern? I didn't become a researcher to run errands! 
                return true;
            default:
                return true;
        }
    }
}
