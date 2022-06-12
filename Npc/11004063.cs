using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004063: Hotottot Monument
/// </summary>
public class _11004063 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010099$
    // - <font color="#909090">(The lava is eerily silent, but the heat is blistering. There's an inscription on this statue.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010100$
                // - <font color="#909090">(The lava is eerily silent, but the heat is blistering. There's an inscription on this statue.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010101$
                // - <i>Fifteen hundred years ago, a great earthquake gave birth to this volcano. The nearby forests were destroyed, and in the hot springs gave rise to a new and exotic ecosystem.</i>
                return 10;
            case (10, 2):
                // $script:0619202207010102$
                // - <i>The basaltic lava from the volcano influenced the weapons and ceramics used by the local population. But there's more to the lava than precious metals...</i>
                return 10;
            case (10, 3):
                // $script:0619202207010103$
                // - <font color="#909090">(There's a story about the birth of the $npcName:22000005$ that lives within the mountain further down in the inscription...)</font>
                return 10;
            case (10, 4):
                // $script:0619202207010104$
                // - <i>Long ago, there was a lava eye named Round Eye. It was the runt of its clutch, and all the other lava eyes teased it for its size.</i>
                return 10;
            case (10, 5):
                // $script:0619202207010105$
                // - <i>One summer, it dived into the lava river under Hotottot Mountain to try to prove that it was strong, but it was swept away in the lava flow. Rather than help Round Eye out of the river, the other lava eyes mocked their stunted sibling.</i>
                return 10;
            case (10, 6):
                // $script:0619202207010106$
                // - <i>Round Eye couldn't take it anymore. It closed its eye and let the lava flow carry it away. "Nobody will miss me," it told itself...</i>
                return 10;
            case (10, 7):
                // $script:0619202207010107$
                // - <i>As it drifted away, it prayed that one day it would be reborn as a big, powerful lava eye someday...</i>
                return 10;
            case (10, 8):
                // $script:0619202207010108$
                // - <i>Round Eye wasn't seen for a long time after that. Soon, the other lava eyes began to realize that it was gone for good, and there was much fiery weeping at the $map:02000039$.</i> 
                return 10;
            case (10, 9):
                // $script:0619202207010109$
                // - <i>Then, one day, a gout of lava gushed forth from the mountain, followed by an earth-shattering roar.</i>
                return 10;
            case (10, 10):
                // $script:0619202207010110$
                // - <i>The $npcName:22000005$ emerged from the chasm, shocking the rest of the lava eyes. And yet, this monster seemed somehow familiar to them... It was Round Eye!</i>
                return 10;
            case (10, 11):
                // $script:0619202207010111$
                // - <i>Overjoyed, the other lava eyes asked it how it had survived. Hahoi, the guardian spirit of the $map:02000039$, had heard Round Eyes' prayer and shown pity.</i>
                return 10;
            case (10, 12):
                // $script:0619202207010112$
                // - <i>From that day forth, Round Eye and its fellow lava eyes lived happily on the $map:02000039$, working together to lift each other up.</i>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Next,
            (10, 4) => NpcTalkButton.Next,
            (10, 5) => NpcTalkButton.Next,
            (10, 6) => NpcTalkButton.Next,
            (10, 7) => NpcTalkButton.Next,
            (10, 8) => NpcTalkButton.Next,
            (10, 9) => NpcTalkButton.Next,
            (10, 10) => NpcTalkButton.Next,
            (10, 11) => NpcTalkButton.Next,
            (10, 12) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
