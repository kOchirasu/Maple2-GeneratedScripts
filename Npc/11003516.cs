using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003516: Jahari
/// </summary>
public class _11003516 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008840$
    // - What?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008843$
                // - What?
                switch (selection) {
                    // $script:0817044507008844$
                    // - Tell me about the five auras.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008845$
                // - Lycaos live in the wastelands to the southwest. You can capture them to get their Enduring Health.
                switch (selection) {
                    // $script:0817044507008846$
                    // - Tell me about lycaos.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0817044507008847$
                // - They're not easy to capture. If you don't tie them up or stun them, they'll slip away.
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
