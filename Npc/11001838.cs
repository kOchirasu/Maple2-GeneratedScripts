using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001838: Joddy
/// </summary>
public class _11001838 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1111015907007375$
    // - Ah... What should I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1111015907007378$
                // - I thought everything'd work out if I could just get into the army. Now I'm not sure I'm cut out for this...
                switch (selection) {
                    // $script:1111015907007379$
                    // - I believe in you.
                    case 0:
                        return 31;
                    // $script:1111015907007380$
                    // - Stop slacking and train harder!
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:1111015907007381$
                // - Th-thank you! I'll do my best. 
                return -1;
            case (32, 0):
                // $script:1111015907007382$
                // - T-train harder... Yeah, that'll help...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
