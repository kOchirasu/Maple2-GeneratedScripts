using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004097: Beatrice
/// </summary>
public class _11004097 : NpcScript {
    internal _11004097(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0622171707010341$ 
                // - Welcome, my other half.
                return true;
            case 20:
                // $script:0622171707010342$ 
                // - My kin... you've come.
                return true;
            case 30:
                // $script:0622171707010343$ 
                // - Prove that I made the right decision, $MyPCName$.
                return true;
            default:
                return true;
        }
    }
}
