using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004467: Lenni
/// </summary>
public class _11004467 : NpcScript {
    internal _11004467(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012103$ 
                // - I'm worried about $npcName:11004472[gender:0]$. He's got his heart set on joining the rebellion...
                return true;
            case 10:
                // $script:1227192907012104$ 
                // - I'm worried about $npcName:11004472[gender:0]$. He's got his heart set on joining the rebellion...
                switch (selection) {
                    // $script:1227192907012105$
                    // - What's his story?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012106$ 
                // - $npcName:11004472[gender:0]$'s family was expelled from Tairen during one of the purges, so they signed on with the freedom fighters. Then... they went missing.
                // $script:1227192907012107$ 
                // - Ever since then, he spends all his time exercising so that he can join the fight and save his family.
                switch (selection) {
                    // $script:1227192907012108$
                    // - That's so sad!
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012109$ 
                // - I hope he never has to see the battlefield. We told him he could be a freedom fighter if he trained hard enough, but it was really to keep him from running off and getting himself killed.
                // $script:1227192907012110$ 
                // - And now I have to spend my free time babysitting him... Hey, you look free. Mind watching him for an hour or two?
                switch (selection) {
                    // $script:1227192907012111$
                    // - I'm actually really busy!
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1227192907012112$ 
                // - Hmph. You don't look like it. Oh well! I'd probably get in trouble if I left him with a stranger, anyway.
                return true;
            default:
                return true;
        }
    }
}
