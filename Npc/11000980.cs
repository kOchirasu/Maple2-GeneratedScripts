using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000980: Beefy
/// </summary>
public class _11000980 : NpcScript {
    internal _11000980(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003387$ 
                // - Nice to meet you.
                return true;
            case 30:
                // $script:0831180407003390$ 
                // - Got a spare umbrella?
                return true;
            default:
                return true;
        }
    }
}
