using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000368: Miyo
/// </summary>
public class _11000368 : NpcScript {
    internal _11000368(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001517$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407001519$ 
                // - $MyPCName$, you of all people should help protect the forest! 
                return true;
            default:
                return true;
        }
    }
}
