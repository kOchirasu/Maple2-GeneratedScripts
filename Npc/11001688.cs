using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001688: Zabeth
/// </summary>
public class _11001688 : NpcScript {
    internal _11001688(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006492$ 
                // - What're you staring at? You want a piece of me?
                return true;
            case 30:
                // $script:0629000607006495$ 
                // - You need something, go bother $npcName:11001545[gender:0]$ instead. He likes to hear himself talk, and I got real work to do.
                switch (selection) {
                    // $script:0706173707006650$
                    // - What was that clone in the video?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0706173707006651$ 
                // - I don't know if it was a clone or just someone who really looks like $npcName:11001680[gender:0]$. And I don't want to know. Now stop making me think about it.
                return true;
            default:
                return true;
        }
    }
}
