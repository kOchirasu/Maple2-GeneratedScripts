using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000701: Oska
/// </summary>
public class _11000701 : NpcScript {
    internal _11000701(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002827$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:0831180407002828$ 
                // - We don't have time for this. I'll take $npcName:11000119[gender:0]$ to HQ.
                //   $MyPCName$, please follow $npc:11000057[gender:1]$. 
                return true;
            default:
                return true;
        }
    }
}
