using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003446: Dark Wind Agent
/// </summary>
public class _11003446 : NpcScript {
    internal _11003446(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008694$ 
                // - $male:Sir,female:Ma'am$! 
                return true;
            case 10:
                // $script:0721142007008712$ 
                // - You mess with Dark Wind, you mess with me. 
                return true;
            default:
                return true;
        }
    }
}
