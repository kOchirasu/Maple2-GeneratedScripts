using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004149: Terry
/// </summary>
public class _11004149 : NpcScript {
    internal _11004149(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010569$ 
                // - Hm hm hmmm, hm! Those marching songs always get stuck in my head. 
                return true;
            case 10:
                // $script:0806025707010570$ 
                // - I've loved $npcName:11000444[gender:0]$'s books and the sea ever since I was a boy—probably a side-effect of growing up by the ocean. And now I'm on a voyage of my own, alongside my childhood friends. 
                return true;
            default:
                return true;
        }
    }
}
