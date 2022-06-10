using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001723: Vision
/// </summary>
public class _11001723 : NpcScript {
    internal _11001723(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006973$ 
                // - ... 
                return true;
            case 30:
                // $script:0728024507007025$ 
                // - I'm not telling you a thing. It's better that way. 
                return true;
            default:
                return true;
        }
    }
}
