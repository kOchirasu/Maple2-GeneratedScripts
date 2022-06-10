using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001133: Hujo
/// </summary>
public class _11001133 : NpcScript {
    internal _11001133(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003875$ 
                // - Do you have business with me? 
                return true;
            case 30:
                // $script:0911192907003878$ 
                // - I'm trapped here! There are monsters everywhere. I knew this place was dangerous, but... 
                switch (selection) {
                    // $script:0911192907003879$
                    // - Then why did you come here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0911192907003880$ 
                // - I have my reasons. 
                return true;
            default:
                return true;
        }
    }
}
