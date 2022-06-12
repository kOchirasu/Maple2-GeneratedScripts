using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001899: MC Kay
/// </summary>
public class _11001899 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1109185407007370$
    // - Ladies and gentlemen! Are you ready for some action-packed racing?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1109185407007373$
                // - Are you joining today's race? Good luck!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
