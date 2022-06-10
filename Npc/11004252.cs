using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004252: Arte
/// </summary>
public class _11004252 : NpcScript {
    internal _11004252(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0829171107010964$ 
                // - Looks like another day with no luck. Hm? Who are you?
                return true;
            case 10:
                // $script:0829171107010965$ 
                // - Looks like another day with no luck. Hm? Who are you?
                switch (selection) {
                    // $script:0831123907010999$
                    // - No one important. I'm just passing through.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0831123907011000$ 
                // - You're either brave or real dumb, to come all the way out here. Anyway, my name's $npcName:11004252[gender:1]$. I'm here observing.
                switch (selection) {
                    // $script:0831123907011001$
                    // - Observing what?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0831123907011002$ 
                // - Observing the movements of $npcName:11001813[gender:0]$'s army. He's one of the Seven Commanders, you know, and I have it on good authority that he often sends his troops through $map:03000115$ and $map:03000118$.
                switch (selection) {
                    // $script:0831123907011003$
                    // - Are you sure that's wise?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0831123907011004$ 
                // - Pfft, I'm not scared. I have family in Maple World, and I'll do anything I can to keep them safe, including marching right up to $npcName:11001813[gender:0]$ and stopping him right here and now.
                switch (selection) {
                    // $script:0831143807011039$
                    // - Thanks.
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:0831143807011040$ 
                // - No need to thank me. I'm happy if my family is happy. You should keep it up, too.
                return true;
            default:
                return true;
        }
    }
}
