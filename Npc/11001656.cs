using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001656: Tinchai
/// </summary>
public class _11001656 : NpcScript {
    internal _11001656(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617105607006366$ 
                // - Halo Mountain...
                return true;
            case 30:
                // $script:0727223007006860$ 
                // - We need to focus... focus...
                switch (selection) {
                    // $script:0727223007006861$
                    // - Is the master really gone?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006862$ 
                // - <font color="#909090">($npcName:11001656[gender:1]$ chokes back a tear.)</font>
                //   The master is fine. He... he has to be...
                return true;
            default:
                return true;
        }
    }
}
