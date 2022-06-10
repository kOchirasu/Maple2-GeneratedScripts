using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003252: Merin
/// </summary>
public class _11003252 : NpcScript {
    internal _11003252(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404104807008251$ 
                // - $MyPCName$! 
                return true;
            case 30:
                // $script:0404104807008252$ 
                // - I'm gonna be just as awesome as you when I grow up! 
                return true;
            default:
                return true;
        }
    }
}
