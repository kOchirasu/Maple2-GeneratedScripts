using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004328: Tina
/// </summary>
public class _11004328 : NpcScript {
    internal _11004328(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011526$ 
                // - I've never heard such a call... 
                return true;
            case 10:
                // $script:1010140307011527$ 
                // - I've never heard such a call... 
                // $script:1010140307011528$ 
                // - Hey! Fancy meeting you there. 
                // $script:1010140307011529$ 
                // - Quick question. You hear that noise? 
                switch (selection) {
                    // $script:1010140307011530$
                    // - What noise?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011531$ 
                // - So, you can't hear it, either. That figures. 
                // $script:1010140307011532$ 
                // - I keep hearing this crying sound. It's like a hurt animal... but it's no animal I've ever seen. 
                // $script:1010140307011533$ 
                // - $npcName:11004327[gender:0]$ and I are new to this land, but I'm sure the crying isn't from a monster. 
                // $script:1010140307011534$ 
                // - What could it be? There are so many secrets here. 
                return true;
            default:
                return true;
        }
    }
}
