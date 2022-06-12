using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001339: Potler
/// </summary>
public class _11001339 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005275$
    // - Skateboarding is harder than it looks.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005278$
                // - Why is this so hard?! I can <i>visualize</i> myself doing these tricks, so why can't I actually <i>do</i> them?!
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
