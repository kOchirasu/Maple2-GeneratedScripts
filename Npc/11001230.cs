using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001230: Landevian
/// </summary>
public class _11001230 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1125194807004469$
    // - We've got nothing but problems here.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1125194807004472$
                // - This is all that old coot Arazaad's fault. He's giving me work to do from beyond the grave!
                switch (selection) {
                    // $script:1205185107004717$
                    // - Was there bad blood between you and Arazard?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1205185107004718$
                // - More like resentment. He was always bossing me around. "Practice your rune magic. Practice with your blade. Behave like a leader and set an example for the other Runeblades. Blah blah blah!" Even when $npcName:11001246[gender:0]$ and $npcName:11001231[gender:0]$ were there, the old man always singled me out.
                switch (selection) {
                    // $script:1205185107004719$
                    // - Sounds like you were Arazaad's most trusted student.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1205185107004720$
                // - W-what? No way. He was just a mean old man looking for an easy mark to pick on. Trust me, his favorite student was that jerk $npcName:11001231[gender:0]$, and boy did that one come back to bite him.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
