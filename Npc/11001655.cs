using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001655: Tinchai
/// </summary>
public class _11001655 : NpcScript {
    internal _11001655(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617105607006365$ 
                // - Where did $npcName:11001557[gender:0]$ get off to...?
                return true;
            case 30:
                // $script:0727223007006855$ 
                // - Did you see that shadow? I wonder if that was $npcName:11001557[gender:0]$ skulking around.
                switch (selection) {
                    // $script:0727223007006856$
                    // - I didn't see anything.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006857$ 
                // - Well, I know I saw something! And he has to be around here somewhere.
                return true;
            default:
                return true;
        }
    }
}
