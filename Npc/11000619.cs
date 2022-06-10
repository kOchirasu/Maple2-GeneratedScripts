using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000619: Janne
/// </summary>
public class _11000619 : NpcScript {
    internal _11000619(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002525$ 
                // - Try to think positively.
                return true;
            case 10:
                // $script:0831180407002526$ 
                // - It's nice to be outside sometimes.
                return true;
            default:
                return true;
        }
    }
}
