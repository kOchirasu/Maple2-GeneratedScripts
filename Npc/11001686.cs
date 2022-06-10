using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001686: Zabeth
/// </summary>
public class _11001686 : NpcScript {
    internal _11001686(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006484$ 
                // - What're you staring at? You want a piece of me?
                return true;
            case 30:
                // $script:0629000607006487$ 
                // - You need something, go bother $npcName:11001545[gender:0]$ instead. He likes to hear himself talk, and I got real work to do.
                switch (selection) {
                    // $script:0706173707006645$
                    // - What's your rank in Blackstar?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0706173707006646$ 
                // - I'm a henchman, plain and simple. $npcName:11001678[gender:0]$ has big ideas about moving up in the organization, but I don't care what they call me as long as I get to bash heads in.
                // $script:0706173707006647$ 
                // - Boss. Lackey. It doesn't matter. All that matters is how strong you are. $npcName:11001678[gender:0]$ can try to rise as much as he wants, but he's got a glass jaw. A weakling like him just ain't officer material.
                return true;
            default:
                return true;
        }
    }
}
