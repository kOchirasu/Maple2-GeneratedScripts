using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000100: Dede
/// </summary>
public class _11000100 : NpcScript {
    internal _11000100(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000393$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000395$ 
                // - Can't touch this! Na na na... Um, is that one still popular?
                return true;
            default:
                return true;
        }
    }
}
