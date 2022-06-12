using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004225: Riol
/// </summary>
public class _11004225 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806222707010799$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806222707010800$
                // - When I think back on that audition at $map:52000061$, I can't help but smile. That day changed my life.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
