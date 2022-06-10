using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000021: Santiago
/// </summary>
public class _11000021 : NpcScript {
    internal _11000021(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000106$ 
                // - How may I help you? 
                return true;
            case 10:
                // $script:0831180407000107$ 
                // - My grandson is so rebellious that he's going to give me a heart attack. I miss the days when he would just listen. 
                return true;
            case 40:
                // $script:0831180407000110$ 
                // - $npcName:11000054[gender:0]$ is as stubborn as a mule. Please find him before he leaves $map:63000001$. 
                return true;
            default:
                return true;
        }
    }
}
