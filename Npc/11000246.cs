using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000246: Beans
/// </summary>
public class _11000246 : NpcScript {
    internal _11000246(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001046$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407001048$ 
                // - My dream is to live in a bigger and nicer house with $npcName:11000401[gender:0]$. 
                return true;
            default:
                return true;
        }
    }
}
