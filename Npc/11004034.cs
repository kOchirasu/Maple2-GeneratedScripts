using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004034: Lanemone
/// </summary>
public class _11004034 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0614185307010053$
    // - Sigh... How did I end up with that one again? We have unfinished business.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0614185307010054$
                // - Sigh... This one is useless without me. That's why I'm always busy cleaning up the mess. Can't really say whether or not I like it at this point.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
