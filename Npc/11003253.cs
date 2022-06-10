using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003253: Lian
/// </summary>
public class _11003253 : NpcScript {
    internal _11003253(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404104807008253$ 
                // - $MyPCName$, you're amazing! 
                return true;
            case 30:
                // $script:0404104807008254$ 
                // - I'm gonna be just as awesome as you when I grow up! 
                return true;
            default:
                return true;
        }
    }
}
