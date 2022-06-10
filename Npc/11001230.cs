using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001230: Landevian
/// </summary>
public class _11001230 : NpcScript {
    internal _11001230(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1125194807004469$ 
                // - We've got nothing but problems here. 
                return true;
            case 30:
                // $script:1125194807004472$ 
                // - This is all that old coot Arazaad's fault. He's giving me work to do from beyond the grave! 
                switch (selection) {
                    // $script:1205185107004717$
                    // - Was there bad blood between you and Arazard?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1205185107004718$ 
                // - More like resentment. He was always bossing me around. "Practice your rune magic. Practice with your blade. Behave like a leader and set an example for the other Runeblades. Blah blah blah!" Even when $npcName:11001246[gender:0]$ and $npcName:11001231[gender:0]$ were there, the old man always singled me out. 
                switch (selection) {
                    // $script:1205185107004719$
                    // - Sounds like you were Arazaad's most trusted student.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1205185107004720$ 
                // - W-what? No way. He was just a mean old man looking for an easy mark to pick on. Trust me, his favorite student was that jerk $npcName:11001231[gender:0]$, and boy did that one come back to bite him. 
                return true;
            default:
                return true;
        }
    }
}
