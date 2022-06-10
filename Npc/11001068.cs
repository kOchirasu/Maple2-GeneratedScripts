using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001068: Gaden
/// </summary>
public class _11001068 : NpcScript {
    internal _11001068(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003639$ 
                // - Hello. 
                return true;
            case 30:
                // $script:0831180407003642$ 
                // - Did you come to enjoy Oil and Water's concert? Head up to the front of the stage if you did. 
                return true;
            default:
                return true;
        }
    }
}
