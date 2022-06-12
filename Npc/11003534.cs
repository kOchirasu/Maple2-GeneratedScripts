using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003534: Condor
/// </summary>
public class _11003534 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1126150707011919$
    // - Back in my day, we knew a thing or two about duty!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1126150707011920$
                // - What's the matter? Don't have enough to do?
                switch (selection) {
                    // $script:1126150707011921$
                    // - Uh...
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1126150707011922$
                // - If you've got time for chit-chat, you've got time for a mission!
                return -1;
            case (40, 0):
                // $script:1126150707011923$
                // - If you think you've got what it takes to serve the Imperial Vanguard, then prove it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
