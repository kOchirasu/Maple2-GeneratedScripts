using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001045: Rauter
/// </summary>
public class _11001045 : NpcScript {
    internal _11001045(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003569$ 
                // - What just passed by? It was shining. 
                return true;
            case 30:
                // $script:0831180407003572$ 
                // - Experience really is the best teacher. I've worked at this research center for so long that now I know scientific terms better than slang. 
                return true;
            default:
                return true;
        }
    }
}
