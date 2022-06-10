using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004234: Lanemone
/// </summary>
public class _11004234 : NpcScript {
    internal _11004234(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010919$ 
                // - You're really amazing, you know that? 
                return true;
            case 10:
                // $script:0809223207010920$ 
                // - You're really amazing, you know that? 
                // $script:0809223207010921$ 
                // - I hate tedious matters, but I suppose I can help if you're the one asking. 
                // $script:0809223207010922$ 
                // - But if you happen to find anything interesting, you'd better bring it to me instead of $npcName:11004103[gender:1]$! Promise. 
                return true;
            default:
                return true;
        }
    }
}
