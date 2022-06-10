using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000292: Kanto
/// </summary>
public class _11000292 : NpcScript {
    internal _11000292(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001163$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0831180407001166$ 
                // - If only she loved me... I would do anything for her... 
                return true;
            default:
                return true;
        }
    }
}
