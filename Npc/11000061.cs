using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000061: Samantha
/// </summary>
public class _11000061 : NpcScript {
    internal _11000061(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000279$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000282$ 
                // - If you came to see $npcName:11000016[gender:0]$, you can find him in $map:63000003$. The chief called him to talk about the ship for the court. 
                return true;
            default:
                return true;
        }
    }
}
