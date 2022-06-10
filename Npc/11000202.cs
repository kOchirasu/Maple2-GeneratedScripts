using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000202: Jason
/// </summary>
public class _11000202 : NpcScript {
    internal _11000202(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000880$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000883$ 
                // - My arms are killing me! Why is it always me who gets punished?
                return true;
            default:
                return true;
        }
    }
}
