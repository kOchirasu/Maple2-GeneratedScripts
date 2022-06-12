using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004078: Scribbles under the Bridge
/// </summary>
public class _11004078 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010226$
    // - <font color="#909090">(A teeny-tiny scribble written so small, it almost appears to be shy.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010227$
                // - <font color="#909090">(A teeny-tiny scribble written so small, it almost appears to be shy.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010228$
                // - <i>$npcName:11000015[gender:1]$'s secret, exposed! She actually has a boyfriend! We've been betrayed!</i>
                return 10;
            case (10, 2):
                // $script:0619202207010229$
                // - <font color="#909090">(Is the person who wrote this... angry? $npcName:11000015[gender:1]$'s fans can be scary sometimes...)</font>
                return 10;
            case (10, 3):
                // $script:0619202207010230$
                // - <font color="#909090">(Wait. There's another note written here!)</font>
                return 10;
            case (10, 4):
                // $script:0619202207010231$
                // - <i>Interesting rumor. If you happen to meet my boyfriend, bring him to me. I want to know what he looks like.
                //   - $npcName:11000015[gender:1]$</i>
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
            (10, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
