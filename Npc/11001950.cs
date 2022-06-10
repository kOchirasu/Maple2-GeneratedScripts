using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001950: Mareda
/// </summary>
public class _11001950 : NpcScript {
    internal _11001950(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007496$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1208184307007548$ 
                // - First, I'll learn how to play the harp. Then I'll let my hair down, and wear a flowing white gown, and spend all day plucking on the strings. I'll look so pretty!
                return true;
            default:
                return true;
        }
    }
}
