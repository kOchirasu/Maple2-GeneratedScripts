using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004320: Dunba
/// </summary>
public class _11004320 : NpcScript {
    internal _11004320(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011623$ 
                // - This place is super weird...
                return true;
            case 20:
                // $script:1010140307011449$ 
                // - This place is super weird...
                return true;
            case 10:
                // $script:1102172107011624$ 
                // - I don't like this place... It's new and scary...
                return true;
            case 30:
                // $script:1010140307011450$ 
                // - Ahh! You scared me!
                switch (selection) {
                    // $script:1010140307011451$
                    // - What's gotten into you?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011452$ 
                // - Oh... It's only you. Phew.
                // $script:1010140307011453$ 
                // - This place has me on edge. Everything's so different.
                // $script:1010140307011454$ 
                // - It seems like I'm the only one having any trouble fitting in. $npcName:11004322[gender:0]$ is so absorbed in his search for new ingredients. And it seems like $npcName:11004321[gender:1]$ has run out of all patience for me... Sniff.
                // $script:1010140307011455$ 
                // - I want to be of help tracking down traces of the dragons, but I'm just so anxious. I should've just stayed home.
                switch (selection) {
                    // $script:1010140307011456$
                    // - That's crazy! I'm sure your friends are glad to have you here.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1010140307011457$ 
                // - You really think so? Thanks... That means a lot. I'm sure I can muster up the courage to keep going.
                return true;
            default:
                return true;
        }
    }
}
