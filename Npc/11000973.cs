using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000973: Hamantha
/// </summary>
public class _11000973 : NpcScript {
    internal _11000973(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003367$ 
                // - Oh, no. You aren't getting my digits. Now shoo!
                return true;
            case 20:
                // $script:0831180407003369$ 
                // - Sniff... Name's $npcName:11000973[gender:1]$, and I'm the prettiest little thing you're going to find in $map:02000186$.
                return true;
            default:
                return true;
        }
    }
}
