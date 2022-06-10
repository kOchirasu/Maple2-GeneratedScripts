using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001702: Tinchai
/// </summary>
public class _11001702 : NpcScript {
    internal _11001702(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0719003107006786$ 
                // - $MyPCName$, are you all right?
                return true;
            case 30:
                // $script:0727223007006911$ 
                // - If $npcName:11001557[gender:0]$ had gotten here a minute later...
                return true;
            default:
                return true;
        }
    }
}
