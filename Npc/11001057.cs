using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001057: Stark
/// </summary>
public class _11001057 : NpcScript {
    internal _11001057(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003608$ 
                // - Oh, no...  
                return true;
            case 30:
                // $script:0831180407003611$ 
                // - I look older than $npcName:11001028[gender:0]$. Well, thanks, I guess. 
                // $script:0831180407003612$ 
                // - $npcName:11001028[gender:0]$ looks young because he's bald, but he's the same age I am. Maybe I should shave my head, too.  
                return true;
            default:
                return true;
        }
    }
}
