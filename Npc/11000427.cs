using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000427: Kakomani
/// </summary>
public class _11000427 : NpcScript {
    internal _11000427(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001779$ 
                // - What're you doing here?
                return true;
            case 20:
                // $script:0831180407001781$ 
                // - Mature $npcName:11000423$s are almost impossible to train. The best time to train them is right after they're born. If only $npcName:23000019[gender:0]$ didn't keep interfering, I could train up a new group of chicks... 
                return true;
            default:
                return true;
        }
    }
}
