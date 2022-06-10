using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001482: Dunba
/// </summary>
public class _11001482 : NpcScript {
    internal _11001482(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106111607005771$ 
                // - Ugh... 
                return true;
            case 30:
                // $script:0106111607005774$ 
                // - W-what do I do now? We finally got the Lumenstone back, but I dropped it into a pool of water. $npcName:11001292[gender:0]$ and $npcName:11001218[gender:1]$ are looking for it... but I can't swim... I feel useless. 
                switch (selection) {
                    // $script:0106111607005775$
                    // - You should calm down.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0106111607005776$ 
                // - If $npcName:23000068[gender:0]$ finds out we lost the Lumenstone, he'll come after us. Could you hold off $npcName:23000068[gender:0]$ until we get the Lumenstone back? 
                return true;
            default:
                return true;
        }
    }
}
