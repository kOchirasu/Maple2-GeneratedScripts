using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003883: Beatrice
/// </summary>
public class _11003883 : NpcScript {
    internal _11003883(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0515102507009915$ 
                // - Welcome, my other half. 
                return true;
            case 20:
                // $script:0515102507009916$ 
                // - My kin... you've come. 
                return true;
            case 30:
                // $script:0515102507009917$ 
                // - Prove that I made the right decision, $MyPCName$. 
                return true;
            default:
                return true;
        }
    }
}
