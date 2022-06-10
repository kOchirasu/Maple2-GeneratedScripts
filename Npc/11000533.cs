using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000533: Camton
/// </summary>
public class _11000533 : NpcScript {
    internal _11000533(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002298$ 
                // - What seems to be the problem? 
                return true;
            case 30:
                // $script:0831180407002300$ 
                // - Unless you've worked a day here, you can't truly appreciate what we're doing. 
                return true;
            default:
                return true;
        }
    }
}
