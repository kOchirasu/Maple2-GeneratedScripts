using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004226: Elizabeth
/// </summary>
public class _11004226 : NpcScript {
    internal _11004226(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010802$ 
                // - Meow. 
                return true;
            case 10:
                // $script:0806222707010803$ 
                // - Meoow! 
                return true;
            default:
                return true;
        }
    }
}
