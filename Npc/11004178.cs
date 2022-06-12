using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004178: Katvan
/// </summary>
public class _11004178 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010618$
    // - Do you need something?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010619$
                // - If we want to win the next match, the two of you need to be more pragmatic.
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
