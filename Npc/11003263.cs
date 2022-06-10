using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003263: Jorge
/// </summary>
public class _11003263 : NpcScript {
    internal _11003263(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008206$ 
                // - $MyPCName$... You did everything you could.
                return true;
            case 30:
                // $script:0403155707008207$ 
                // - The path to Ellinel is still blocked, but we'll find a way back.
                return true;
            default:
                return true;
        }
    }
}
