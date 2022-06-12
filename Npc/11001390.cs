using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001390: Yul
/// </summary>
public class _11001390 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217193307005390$
    // - Sigh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1223165107005568$
                // - My daughter, $npcName:11001396[gender:1]$, is always lost in thought. What could keep her so preoccupied all day long?
                switch (selection) {
                    // $script:1226235907005589$
                    // - Tell me about her.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1223165107005569$
                // - She used to be such a clever girl. Even the people in $map:02010002$ heard about her genius.
                return 31;
            case (31, 1):
                // $script:1223165107005570$
                // - But instead of going out and making something of herself, she came back to this small town. I'm happy to have her here, but I can't help but feel that she's wasting her talent...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
