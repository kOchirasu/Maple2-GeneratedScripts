using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000387: May
/// </summary>
public class _11000387 : NpcScript {
    internal _11000387(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001574$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407001576$ 
                // - Have you seen $npcName:11000406[gender:0]$? He's right over there... and he's sooooooo handsome. Ah, I wish I could get close to him...
                return true;
            default:
                return true;
        }
    }
}
