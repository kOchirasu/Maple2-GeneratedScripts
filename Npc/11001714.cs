using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001714: Tinchai
/// </summary>
public class _11001714 : NpcScript {
    internal _11001714(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0728022507006966$ 
                // - Hello there.
                return true;
            case 30:
                // $script:0805021607007090$ 
                // - None of us are okay right now. All the more reason to stay strong.
                switch (selection) {
                    // $script:0805021607007091$
                    // - (Nod your head.)
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0805021607007092$ 
                // - You know, I... Oh, never mind.
                //   <font color="#909090">($npcName:11001714[gender:1]$ looks you in the eye, but stops herself from saying more.)</font>
                return true;
            default:
                return true;
        }
    }
}
