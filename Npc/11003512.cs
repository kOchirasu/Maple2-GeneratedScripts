using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003512: Babatundey
/// </summary>
public class _11003512 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008802$
    // - Need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008803$
                // - The boss's word is good. What more do you need?
                switch (selection) {
                    // $script:0817044507008804$
                    // - Tell me about the exam.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008805$
                // - Humans can't do anything alone. If you can't figure it out, ask someone to help you.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
